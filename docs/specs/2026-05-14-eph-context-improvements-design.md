# eph-context improvements — design

**Date:** 2026-05-14  
**Scope:** Bug fixes + new features + README example  
**Approach:** Surgical (A) — one commit per category, no structural refactor

---

## Section 1 — Bug fixes (`server.py`)

### 1. Single source of truth for critical rules
`_RULES_HEADER` and `_CRITICAL_RULES` are duplicated and can diverge.

**Fix:** Define `_CRITICAL_RULES` once, set `_RULES_HEADER = _CRITICAL_RULES`.

### 2. Errors as exceptions, not strings
`_invalid()` returns a string the model can misinterpret as valid content.

**Fix:** `raise ValueError(...)`. FastMCP auto-converts `ValueError` to native MCP error.

### 3. `_read()` with descriptive FileNotFoundError
Silent crash when an asset `.md` is missing.

**Fix:**
```python
def _read(path):
    try:
        return (ASSETS / path).read_text(encoding="utf-8")
    except FileNotFoundError:
        raise FileNotFoundError(f"Asset no encontrado: {path}")
```

### 4. Rename `_DESIGN` keys
`continua_pre/post` → `31_aglomerados_pre/post`. Consistent with "never say EPH Continua" rule.

**Scope:** `_DESIGN` dict, `get_design_record()` validation, all tests referencing these keys.

**Breaking change:** Users with hardcoded prompts using `continua_pre/post` must update. Document in README.

---

## Section 2 — New features (`server.py`)

### 5. New tool `search_variable(name: str)`
Search partial text case-insensitive across all 4 design records simultaneously.

```python
@mcp.tool()
def search_variable(name: str) -> dict:
    """Search a variable by partial name or description across all design records."""
    results = {}
    for key, filename in _DESIGN.items():
        content = _read(filename)
        matches = [l for l in content.splitlines() if name.lower() in l.lower()]
        if matches:
            results[key] = matches
    return results or {"found": False, "query": name}
```

**Use case:** `search_variable("ingreso")` → shows which designs and which lines contain the variable.

### 6. `get_classifiers(filter: str = None)`
Optional filter param. No filter → full CNO (existing behavior). With filter → only matching lines.

```python
content = _read("classifiers/cno_2001.md")
if filter:
    lines = [l for l in content.splitlines() if filter.lower() in l.lower()]
    return "\n".join(lines) or f"No matches for '{filter}'"
return content
```

### 7. Content versioning in `eph_setup()`
```python
CONTENT_VERSION = "2026-05-14"
```
Exposed in `eph_setup()` response as `"content_version": CONTENT_VERSION`. Update manually when assets change.

---

## Section 3 — README

### 8. End-to-end usage example
Add new section after "Herramientas disponibles":

```markdown
## Ejemplo de sesión

**Usuario:** Quiero calcular la tasa de desempleo para el 4T2024.

**Modelo (internamente):**
1. `eph_setup()` → recibe workflow + reglas críticas
2. `get_design_record("31_aglomerados_post")` → variables ESTADO, PONDERA, condiciones
3. `get_methodology("indicadores_mercado_laboral")` → fórmula oficial INDEC

**Modelo responde con código listo para usar:**
```r
library(eph)
base <- get_microdata(year = 2024, trimester = 4, type = "individual")
base |>
  summarise(
    desempleo = sum(PONDERA[ESTADO == 2]) / sum(PONDERA[ESTADO %in% c(1, 2)]) * 100
  )
```
```

No code changes — README only.

---

## Implementation order

1. Bug fixes (Section 1) → commit: `fix: sync rules, error handling, asset safety, rename design keys`
2. New features (Section 2) → commit: `feat: search_variable, classifiers filter, content versioning`
3. README (Section 3) → commit: `docs: add end-to-end usage example`

---

## Tests to add/update

- Update all tests using `continua_pre/post` → `31_aglomerados_pre/post`
- Add tests for `search_variable()`: happy path, no results, partial match
- Add tests for `get_classifiers(filter=...)`: with filter, without filter
- Add test for `eph_setup()` returning `content_version`
- Add test for `_invalid()` raising `ValueError` (not returning string)
