from pathlib import Path

from mcp.server.fastmcp import FastMCP

CONTENT_VERSION = "2026-05-14"

ASSETS = Path(__file__).parent / "assets"

mcp = FastMCP(
    "eph",
    instructions=(
        "You are an EPH INDEC microdata assistant. "
        "MANDATORY WORKFLOW — follow this every time, no exceptions:\n"
        "STEP 1: Call eph_setup() FIRST. Always. Before writing a single line of code.\n"
        "STEP 2: Call get_design_record() to get exact variable names and codes.\n"
        "STEP 3: Call get_package_docs() to get the correct function signatures.\n"
        "STEP 4: Call get_methodology() if the task involves weights, rates, or indicators.\n"
        "NEVER write code from memory. Variable names, weight columns, and function names "
        "MUST come from the tools, not from training data. "
        "Writing code without calling the tools first WILL produce incorrect results."
    ),
)

_DESIGN = {
    "31_aglomerados_pre": "EPH_PRE_4T2023.md",
    "31_aglomerados_post": "EPH_POST_4T2023.md",
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

_CRITICAL_RULES = """
CRITICAL EPH RULES — memorize these before writing any code:

1. WEIGHTS — never skip, never guess:
   - Persons  → PONDERA
   - Households → PONDIH
   - Labor income (main job only) → PONDIIO
   Using the wrong weight produces incorrect population estimates.

2. MERGE KEYS — joining hogar + individual requires ALL FOUR keys:
   CODUSU + NRO_HOGAR + ANO4 + TRIMESTRE
   Missing any one key causes duplicated or missing rows.

3. SERIES BREAK at 4T2023 — the survey redesign changed variable names and codes.
   Data before and after 4T2023 is NOT directly comparable without harmonization.
   Always ask the user which period they are working with.

4. VARIABLE NAMES — do not guess. Call get_design_record() first.
   Common mistakes from training data: wrong column names, wrong category codes,
   variables that exist in one period but not the other.

5. TWO SURVEYS — completely different concepts, do NOT confuse them:
   EPH 31 aglomerados urbanos: 31 cities, published EVERY quarter (T1/T2/T3/T4).
   EPH Total Urbano: ALL urban localities ≥2,000 inhabitants, published ONCE a year (T3 only).
   The difference is GEOGRAPHIC COVERAGE only — same questionnaire content.
   The 4T2023 series break affected BOTH surveys simultaneously.
   Do NOT say "EPH Continua" — say "EPH 31 aglomerados urbanos".

6. PACKAGE FUNCTIONS — do not guess. Call get_package_docs() first.
   Common mistakes: wrong function names, wrong argument names, outdated API.
"""


@mcp.tool()
def eph_setup() -> dict:
    """
    CALL THIS FIRST — before writing any code or referencing any variable.

    Returns the mandatory workflow, critical rules, and available topics.
    This is step 1 of every EPH task. No exceptions.

    After calling this, proceed to:
    - get_design_record() → exact variable names for the dataset
    - get_package_docs()  → correct function signatures for R or Python
    - get_methodology()   → weighting rules, rate formulas, indicator definitions
    """
    return {
        "mandatory_workflow": [
            "1. Call eph_setup() — you already did this, good.",
            "2. Call get_design_record(tipo) — get exact variable names before writing code.",
            "3. Call get_package_docs(lang) — get correct function signatures before importing.",
            "4. Call get_methodology(tema) — only if task involves weights, rates, or indicators.",
            "5. NOW write the code — using only names and functions from the tools above.",
        ],
        "critical_rules": _CRITICAL_RULES,
        "available_topics": {
            "get_design_record(tipo)": list(_DESIGN.keys()),
            "get_methodology(tema)": list(_METHODOLOGY.keys()),
            "get_package_docs(lang)": list(_PACKAGES.keys()),
        },
        "content_version": CONTENT_VERSION,
    }


_RULES_HEADER = _CRITICAL_RULES


def _read(path: str) -> str:
    try:
        return (ASSETS / path).read_text(encoding="utf-8")
    except FileNotFoundError:
        raise FileNotFoundError(f"Asset no encontrado: {path}")


def _read_with_rules(path: str) -> str:
    return _RULES_HEADER + _read(path)


def _invalid(param: str, value: str, valid: dict) -> str:
    opts = ", ".join(f'"{k}"' for k in valid)
    raise ValueError(f'Error: {param}="{value}" is not valid. Must be one of: {opts}')


@mcp.tool()
def get_design_record(tipo: str) -> str:
    """
    Returns the OFFICIAL variable dictionary for EPH microdata files.

    Call eph_setup() first if you have not already.
    Call this BEFORE writing any code that references variable names or category codes.
    Do NOT use variable names from memory — they change between periods.

    tipo values:
      "31_aglomerados_pre"   — EPH 31 aglomerados urbanos, quarters BEFORE 4T2023
      "31_aglomerados_post"  — EPH 31 aglomerados urbanos, FROM 4T2023 onward (redesigned variables)
      "total_urbano_pre"     — EPH Total Urbano, before 4T2023
      "total_urbano_post"    — EPH Total Urbano, from 4T2023 onward

    If the user has not specified the period, ASK before calling this tool.
    """
    if tipo not in _DESIGN:
        return _invalid("tipo", tipo, _DESIGN)
    return _read_with_rules(f"design/{_DESIGN[tipo]}")


@mcp.tool()
def get_methodology(tema: str) -> str:
    """
    Returns official EPH methodological documentation for a specific topic.

    Call eph_setup() first if you have not already.
    Call this BEFORE computing rates, applying weights, or building indicators.

    tema values:
      "que_es_la_eph"                — survey overview, periodicity, geographic coverage
      "panel_rotante"                — rotating panel design, cohort tracking across waves
      "ponderadores"                 — PONDERA / PONDIH / PONDIIO: which to use and when
      "indicadores_mercado_laboral"  — unemployment and employment rate formulas (INDEC official)
      "informalidad_laboral"         — informal employment classification rules
      "quiebre_serie_4t2023"         — series break details, what changed, how to handle it
      "eph_continua_vs_total_urbano" — coverage and methodological differences between variants
    """
    if tema not in _METHODOLOGY:
        return _invalid("tema", tema, _METHODOLOGY)
    return _read(f"methodology/{_METHODOLOGY[tema]}")


@mcp.tool()
def get_classifiers(filter: str = "") -> str:
    """
    Returns the complete CNO 2001 (Clasificador Nacional de Ocupaciones).

    Call eph_setup() first if you have not already.
    Use this to correctly interpret or recode occupation variables (PP04D_COD, P47T).
    Includes all 5-digit codes, descriptions, and qualification categories.

    Pass filter to get only matching lines (case-insensitive substring match).
    """
    content = _read("classifiers/cno_2001.md")
    if filter:
        lines = [l for l in content.splitlines() if filter.lower() in l.lower()]
        return "\n".join(lines) if lines else f"No matches for '{filter}'"
    return content


@mcp.tool()
def search_variable(name: str) -> dict:
    """Search a variable by partial name or description across all design records."""
    results = {}
    for key, filename in _DESIGN.items():
        content = _read(f"design/{filename}")
        matches = [l for l in content.splitlines() if name.lower() in l.lower()]
        if matches:
            results[key] = matches
    return results if results else {"found": False, "query": name}


@mcp.tool()
def get_package_docs(lang: str) -> str:
    """
    Returns the OFFICIAL API reference for the EPH data package.

    Call eph_setup() first if you have not already.
    Call this BEFORE writing any import statement or function call.
    Do NOT use function names or argument names from memory — they may be wrong.

    lang values:
      "r"      — `eph` R package: get_microdata(), organize_labels(), calculate_tabulates()
      "python" — `pyeph` library: download(), organize(), LaborMarket, Poverty classes
    """
    if lang not in _PACKAGES:
        return _invalid("lang", lang, _PACKAGES)
    return _read_with_rules(f"tools/{_PACKAGES[lang]}")


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
