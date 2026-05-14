from pathlib import Path

from mcp.server.fastmcp import FastMCP

ASSETS = Path(__file__).parent / "assets"

mcp = FastMCP(
    "eph",
    instructions=(
        "EPH INDEC microdata expert. "
        "Always call the relevant tool BEFORE writing any analysis code: "
        "get_design_record for variable names and codes, "
        "get_methodology for weighting rules and indicators, "
        "get_package_docs for correct API usage. "
        "Never guess variable names, weight columns, or function signatures."
    ),
)

_DESIGN = {
    "continua_pre": "EPH_PRE_4T2023.md",
    "continua_post": "EPH_POST_4T2023.md",
    "total_urbano_pre": "EPH_TotUrbano_PRE_4T2023.md",
    "total_urbano_post": "EPH_TotUrbano_POST_4T2023.md",
}

_METHODOLOGY = {
    "que_es_la_eph": "que_es_la_eph.md",
    "panel_rotante": "panel_rotante.md",
    "ponderadores": "ponderadores.md",
    "indicadores_mercado_laboral": "indicadores_mercado_laboral.md",
    "informalidad_laboral": "informalidad_laboral.md",
    "quiebre_serie_4t2023": "quiebre_serie_4t2023.md",
    "eph_continua_vs_total_urbano": "eph_continua_vs_total_urbano.md",
}

_PACKAGES = {
    "r": "eph_package_r.md",
    "python": "pyeph_package.md",
}


@mcp.tool()
def list_topics() -> dict:
    """
    Returns all valid parameter values for every EPH tool.
    Call this first when unsure which topic or record type to request.
    """
    return {
        "get_design_record.tipo": list(_DESIGN.keys()),
        "get_methodology.tema": list(_METHODOLOGY.keys()),
        "get_package_docs.lang": list(_PACKAGES.keys()),
    }


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _invalid(param: str, value: str, valid: dict) -> str:
    opts = ", ".join(f'"{k}"' for k in valid)
    return f'Error: {param}="{value}" is not valid. Must be one of: {opts}'


@mcp.tool()
def get_design_record(tipo: str) -> str:
    """
    Returns the complete variable dictionary (diseño de registro) for EPH microdata files.

    tipo values:
      "continua_pre"       — EPH Continua, trimestres before 4T2023
      "continua_post"      — EPH Continua, from 4T2023 onward (new design)
      "total_urbano_pre"   — EPH Total Urbano, before 4T2023
      "total_urbano_post"  — EPH Total Urbano, from 4T2023 onward

    Call this BEFORE referencing any variable name (ESTADO, CAT_OCUP, CH06, etc.)
    or any column from usu_hogar / usu_individual base files.
    """
    if tipo not in _DESIGN:
        return _invalid("tipo", tipo, _DESIGN)
    return _read(ASSETS / "design" / _DESIGN[tipo])


@mcp.tool()
def get_methodology(tema: str) -> str:
    """
    Returns methodological documentation for a specific EPH topic.

    tema values:
      "que_es_la_eph"                — survey overview, periodicity, geographic coverage
      "panel_rotante"                — rotating panel design, cohort tracking across waves
      "ponderadores"                 — PONDERA, PONDIH, PONDIIO: when and how to apply each
      "indicadores_mercado_laboral"  — unemployment/employment rate formulas, INDEC definitions
      "informalidad_laboral"         — informal employment classification rules
      "quiebre_serie_4t2023"         — series break at 4T2023, comparability across periods
      "eph_continua_vs_total_urbano" — coverage and methodological differences between variants
    """
    if tema not in _METHODOLOGY:
        return _invalid("tema", tema, _METHODOLOGY)
    return _read(ASSETS / "methodology" / _METHODOLOGY[tema])


@mcp.tool()
def get_classifiers() -> str:
    """
    Returns the complete CNO 2001 (Clasificador Nacional de Ocupaciones) reference.

    Use to correctly interpret or recode the P47T variable in individual-level records.
    Includes all 5-digit occupation codes with descriptions and category groupings.
    """
    return _read(ASSETS / "classifiers" / "cno_2001.md")


@mcp.tool()
def get_package_docs(lang: str) -> str:
    """
    Returns the full API reference for the official EPH data-loading package.

    lang values:
      "r"      — `eph` R package: get_microdata(), organize_labels(), calculate_tabulates()
      "python" — `pyeph` library: download(), organize(), indicator functions

    Call this BEFORE writing any import or function call that uses these packages.
    """
    if lang not in _PACKAGES:
        return _invalid("lang", lang, _PACKAGES)
    return _read(ASSETS / "tools" / _PACKAGES[lang])


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
