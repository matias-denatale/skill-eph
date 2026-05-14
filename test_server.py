"""
Smoke tests for eph-context MCP server.
Run: uv run pytest test_server.py -v
"""
import pytest
from server import (
    eph_setup,
    get_design_record,
    get_methodology,
    get_package_docs,
    get_classifiers,
    search_variable,
    _DESIGN,
    _METHODOLOGY,
    _PACKAGES,
)


# ── eph_setup ──────────────────────────────────────────────────────────────────

def test_eph_setup_structure():
    result = eph_setup()
    assert isinstance(result, dict)
    assert "mandatory_workflow" in result
    assert "critical_rules" in result
    assert "available_topics" in result


# ── get_design_record ──────────────────────────────────────────────────────────

@pytest.mark.parametrize("tipo", list(_DESIGN.keys()))
def test_design_record_returns_content(tipo):
    result = get_design_record(tipo)
    assert isinstance(result, str)
    assert len(result) > 500, f"get_design_record({tipo!r}) demasiado corto"


@pytest.mark.parametrize("tipo", list(_DESIGN.keys()))
def test_design_record_has_key_variables(tipo):
    result = get_design_record(tipo)
    assert "CODUSU" in result
    assert "PONDERA" in result
    assert "ESTADO" in result


def test_design_record_invalid_tipo():
    with pytest.raises(ValueError, match="Error"):
        get_design_record("no_existe")


def test_design_31_aglomerados_post_has_empleo_sector():
    result = get_design_record("31_aglomerados_post")
    assert "EMPLEO" in result
    assert "SECTOR" in result


def test_design_31_aglomerados_pre_no_empleo_sector():
    result = get_design_record("31_aglomerados_pre")
    # EMPLEO y SECTOR solo existen en POST 4T2023
    assert "EMPLEO" not in result
    assert "SECTOR" not in result


def test_design_total_urbano_post_trim_documented():
    result = get_design_record("total_urbano_post")
    assert "TRIM" in result
    assert "TRIMESTRE" in result


def test_design_total_urbano_post_no_pdf_toc_noise():
    result = get_design_record("total_urbano_post")
    # Verifica que el rewrite eliminó la tabla de contenidos del PDF
    assert "Diseño de registros de la base Hogar 5" not in result
    # Verifica que CODUSU no tiene la introducción entera metida en la celda
    codusu_line = next((l for l in result.splitlines() if "CODUSU" in l and "|" in l), "")
    assert len(codusu_line) < 500, "CODUSU sigue teniendo texto extra en la celda"


def test_design_total_urbano_has_provincia():
    for tipo in ["total_urbano_pre", "total_urbano_post"]:
        result = get_design_record(tipo)
        assert "PROVINCIA" in result, f"{tipo} debería tener PROVINCIA"


def test_design_continua_no_provincia():
    for tipo in ["31_aglomerados_pre", "31_aglomerados_post"]:
        result = get_design_record(tipo)
        assert "PROVINCIA" not in result, f"{tipo} no debería tener PROVINCIA"


# ── get_methodology ────────────────────────────────────────────────────────────

@pytest.mark.parametrize("tema", list(_METHODOLOGY.keys()))
def test_methodology_returns_content(tema):
    result = get_methodology(tema)
    assert isinstance(result, str)
    assert len(result) > 200, f"get_methodology({tema!r}) demasiado corto"


def test_methodology_invalid_tema():
    with pytest.raises(ValueError, match="Error"):
        get_methodology("no_existe")


def test_methodology_ponderadores_has_all_weights():
    result = get_methodology("ponderadores")
    assert "PONDERA" in result
    assert "PONDIH" in result
    assert "PONDIIO" in result


def test_methodology_informalidad_has_empleo_sector():
    result = get_methodology("informalidad_laboral")
    assert "EMPLEO" in result
    assert "SECTOR" in result


def test_methodology_quiebre_mentions_both_surveys():
    result = get_methodology("quiebre_serie_4t2023")
    # El quiebre afecta a ambas encuestas — debe decirlo explícitamente
    assert "Total Urbano" in result or "total urbano" in result.lower()


# ── get_package_docs ───────────────────────────────────────────────────────────

@pytest.mark.parametrize("lang", list(_PACKAGES.keys()))
def test_package_docs_returns_content(lang):
    result = get_package_docs(lang)
    assert isinstance(result, str)
    assert len(result) > 500


def test_package_docs_invalid_lang():
    with pytest.raises(ValueError, match="Error"):
        get_package_docs("julia")


def test_package_docs_r_has_organize_panels_gotcha():
    result = get_package_docs("r")
    assert "pivot_longer" in result
    assert "duplicad" in result.lower() or "GOTCHA" in result


# ── get_classifiers ────────────────────────────────────────────────────────────

def test_classifiers_returns_content():
    result = get_classifiers()
    assert isinstance(result, str)
    assert len(result) > 1000


def test_classifiers_filter():
    result = get_classifiers(filter="transporte")
    assert "transporte" in result.lower()


def test_classifiers_filter_no_match():
    result = get_classifiers(filter="XXXXXX_NO_EXISTE")
    assert "No matches" in result


# ── search_variable ────────────────────────────────────────────────────────────

def test_search_variable_finds_result():
    result = search_variable("PONDERA")
    assert isinstance(result, dict)
    assert any(len(v) > 0 for v in result.values())


def test_search_variable_no_result():
    result = search_variable("XXXXXX_NO_EXISTE")
    assert result == {"found": False, "query": "XXXXXX_NO_EXISTE"}


def test_search_variable_partial_match():
    result = search_variable("ingreso")
    assert isinstance(result, dict)
    assert len(result) > 0


def test_search_variable_all_designs():
    result = search_variable("CODUSU")
    assert set(result.keys()) == set(_DESIGN.keys())


# ── content versioning ─────────────────────────────────────────────────────────

def test_content_version_in_setup():
    result = eph_setup()
    assert "content_version" in result
    assert isinstance(result["content_version"], str)
    assert len(result["content_version"]) == 10  # YYYY-MM-DD
