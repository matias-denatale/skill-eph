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
    result = get_design_record("no_existe")
    assert "Error" in result


def test_design_continua_post_has_empleo_sector():
    result = get_design_record("continua_post")
    assert "EMPLEO" in result
    assert "SECTOR" in result


def test_design_continua_pre_no_empleo_sector():
    result = get_design_record("continua_pre")
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
    for tipo in ["continua_pre", "continua_post"]:
        result = get_design_record(tipo)
        assert "PROVINCIA" not in result, f"{tipo} no debería tener PROVINCIA"


# ── get_methodology ────────────────────────────────────────────────────────────

@pytest.mark.parametrize("tema", list(_METHODOLOGY.keys()))
def test_methodology_returns_content(tema):
    result = get_methodology(tema)
    assert isinstance(result, str)
    assert len(result) > 200, f"get_methodology({tema!r}) demasiado corto"


def test_methodology_invalid_tema():
    result = get_methodology("no_existe")
    assert "Error" in result


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
    result = get_package_docs("julia")
    assert "Error" in result


def test_package_docs_r_has_organize_panels_gotcha():
    result = get_package_docs("r")
    assert "pivot_longer" in result
    assert "duplicad" in result.lower() or "GOTCHA" in result


# ── get_classifiers ────────────────────────────────────────────────────────────

def test_classifiers_returns_content():
    result = get_classifiers()
    assert isinstance(result, str)
    assert len(result) > 1000
