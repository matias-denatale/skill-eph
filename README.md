<div align="center">

# eph-context

### Que la IA escriba tu código de EPH sin inventar lo que no existe

[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![MCP](https://img.shields.io/badge/MCP-server-8A2BE2)](https://modelcontextprotocol.io)
[![Claude Code](https://img.shields.io/badge/Claude_Code-skill-black)](https://claude.ai/code)
[![EPH](https://img.shields.io/badge/EPH-INDEC-0056A0)](https://www.indec.gob.ar/indec/web/Institucional-Indec-Bases-EPH)
[![R](https://img.shields.io/badge/R-ready-276DC3?logo=r)](https://www.r-project.org/)
[![Python](https://img.shields.io/badge/Python-ready-3776AB?logo=python)](https://www.python.org/)

</div>

---

<blockquote>
<strong>Contexto EPH correcto para cualquier modelo de IA, en cualquier IDE.</strong><br>
Inyecta los diseños de registro oficiales del INDEC y las reglas metodológicas directamente en el contexto del modelo — como MCP server o como Claude Code skill.<br>
<strong>Resultado: código que respeta la realidad de los datos, sin alucinaciones.</strong>
</blockquote>

---

## ¿Para quién es esto?

> **¿Investigador de la EPH que no confía en que la IA respete la metodología?**
> Esta herramienta le da al modelo el manual del INDEC antes de que escriba una línea. No improvisa — lee la documentación real.

> **¿Usuario eventual que quiere hacer cruces sin saberse de memoria las variables?**
> Los diseños de registro completos y la documentación metodológica están disponibles para el modelo en cada consulta.

> **¿Experto que quiere que la IA le ahorre tiempo sin cometer errores básicos?**
> Exactamente para eso fue creado.

---

## El problema: las alucinaciones existen y la EPH no perdona

Los modelos de lenguaje alucinan. Una variable que no existe, un ponderador mal aplicado, un tratamiento incorrecto del panel rotante — puede invalidar todo un análisis sin que te des cuenta.

**eph-context viene a solucionar eso.**

En lugar de dejar que el modelo "recuerde" cómo funciona la EPH, le inyecta en el contexto los diseños de registro oficiales, la metodología documentada y las reglas de tratamiento de variables. El resultado: código que respeta la realidad de los microdatos.

---

## Instalación

### Opción A — MCP server (Claude Desktop, Cursor, VS Code, cualquier cliente MCP)

Requiere [uv](https://docs.astral.sh/uv/getting-started/installation/).

**1. Cloná el repo:**
```bash
git clone https://github.com/matias-denatale/eph-context.git
```

**2. Agregá esto a tu `claude_desktop_config.json` (u otro cliente MCP):**

```json
{
  "mcpServers": {
    "eph": {
      "command": "uv",
      "args": [
        "--directory",
        "/ruta/a/eph-context",
        "run",
        "server.py"
      ]
    }
  }
}
```

En Windows: `"C:\\ruta\\a\\eph-context"`. En Mac/Linux: `/ruta/a/eph-context`.

**3. Reiniciá el cliente.** Las tools EPH aparecen disponibles automáticamente.

---

### Opción B — Claude Code skill (Claude Code CLI)

**1. Cloná el repo en tu carpeta de skills:**
```bash
git clone https://github.com/matias-denatale/eph-context.git ~/.claude/skills/eph
```

**2. Agregá esto a tu `~/.claude/CLAUDE.md`:**
```markdown
| EPH microdata, usu_hogar, usu_individual, scripts R/Python con EPH | `~/.claude/skills/eph/SKILL.md` |
```

La skill se activa automáticamente cuando Claude Code detecta consultas relacionadas con la EPH, microdatos INDEC, o variables como `CODUSU`, `PONDERA`, `ESTADO`, etc.

---

## ¿Qué incluye?

| Categoría | Contenido |
|-----------|-----------|
| **Diseños de registro** | Variables, categorías y codificaciones para los diseños PRE y POST del 4T2023 — EPH Continua y Total Urbano |
| **Reglas metodológicas** | Uso correcto de ponderadores (`PONDERA`, `PONDIH`, `PONDIIO`), panel rotante, quiebres de serie, informalidad laboral, indicadores del mercado de trabajo |
| **Referencia de packages** | Documentación completa del paquete `eph` para R y la librería `pyeph` para Python |
| **Clasificador CNO 2001** | El Clasificador Nacional de Ocupaciones completo con estructura de 5 dígitos |

### Tools MCP disponibles

| Tool | Parámetro | Para qué |
|------|-----------|----------|
| `list_topics` | — | Lista todos los valores válidos de cada tool |
| `get_design_record` | `tipo` | Diccionario de variables del diseño de registro |
| `get_methodology` | `tema` | Documentación metodológica por tema |
| `get_classifiers` | — | CNO 2001 completo |
| `get_package_docs` | `lang` | API del paquete R o Python |

---

## Estructura del repositorio

```
eph-context/
├── server.py             # MCP server (FastMCP, 5 tools)
├── pyproject.toml        # Dependencias (mcp>=1.0.0)
├── SKILL.md              # Instrucciones para Claude Code skill
├── README.md             # Este archivo
└── assets/
    ├── design/           # Diccionarios de variables por diseño de registro
    │   ├── EPH_PRE_4T2023.md
    │   ├── EPH_POST_4T2023.md
    │   ├── EPH_TotUrbano_PRE_4T2023.md
    │   └── EPH_TotUrbano_POST_4T2023.md
    ├── methodology/      # Documentación metodológica curada
    │   ├── que_es_la_eph.md
    │   ├── ponderadores.md
    │   ├── panel_rotante.md
    │   ├── quiebre_serie_4t2023.md
    │   ├── informalidad_laboral.md
    │   ├── indicadores_mercado_laboral.md
    │   └── eph_continua_vs_total_urbano.md
    ├── tools/            # Referencia de packages de procesamiento EPH
    │   ├── eph_package_r.md
    │   └── pyeph_package.md
    └── classifiers/      # Clasificadores oficiales INDEC
        └── cno_2001.md
```

---

## Agradecimientos

Esta herramienta se apoya en el conocimiento abierto de la comunidad:

- **[Diego Kozlowski](https://github.com/DiegoKoz)** — creador del [paquete `eph`](https://github.com/ropensci/eph) para R
- **[Guido Weksler](https://github.com/Guidowe)** — [Introducción a R para Ciencias Sociales](https://guidowe.github.io/Curso-R-Flacso/)
- **[Pablo Tiscornia](https://github.com/Pablotis)** — [Curso R INDEC](https://github.com/pablotis/Curso_R_INDEC)

---

## Licencia

MIT. Usalo, modificálo, compartilo. Si lo mejorás, mandá un PR.
