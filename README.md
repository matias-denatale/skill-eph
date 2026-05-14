<div align="center">
<img width="1280" height="640" alt="eph-context-social-card" src="https://github.com/user-attachments/assets/a958b0fc-15f5-4901-b071-9f9b1c42d515" />

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

> **Los modelos de IA alucinan variables de la EPH que no existen, aplican mal los ponderadores y se olvidan del panel rotante.**
> eph-context le da al modelo los diseños de registro oficiales del INDEC y las reglas metodológicas antes de que escriba una línea. Resultado: código correcto, sin inventos.

---

## ¿Qué herramienta usás?

| Herramienta | Instalación | Sección |
|-------------|-------------|---------|
| **ChatGPT** (web, sin instalar nada) | Ninguna | [→ ChatGPT](#chatgpt--sin-instalar-nada) |
| **Claude Desktop** | Muy simple | [→ Claude Desktop](#claude-desktop) |
| **Cursor** | Muy simple | [→ Cursor](#cursor) |
| **VS Code** | Muy simple | [→ vs-code) |
| **Claude Code** (terminal) | Para desarrolladores | [→ Claude Code CLI](#claude-code-cli) |

---

## ChatGPT — sin instalar nada

La opción más simple. Funciona directamente en [chatgpt.com](https://chatgpt.com) creando un **GPT personalizado** con el conocimiento de la EPH incluido.

### Qué vas a necesitar
- Una cuenta de **ChatGPT Plus** (pago) — necesaria para subir archivos de conocimiento a un GPT personalizado
- Los archivos de la carpeta `assets/` de este repositorio

### Pasos

**1. Descargá los archivos de conocimiento**

Andá a la [página principal del repositorio](https://github.com/matias-denatale/eph-context) en GitHub, hacé clic en el botón verde **Code → Download ZIP** y descomprimí el archivo en tu computadora.

**2. Creá un GPT personalizado**

En [chatgpt.com](https://chatgpt.com):
- Hacé clic en tu nombre (abajo a la izquierda) → **My GPTs** → **Create a GPT**
- En la pestaña **Configure**, completá:
  - **Name:** `Asistente EPH INDEC`
  - **Instructions:** copiá y pegá todo el contenido del archivo `gpt_instructions.md` que está en este repositorio

**3. Subí los archivos de conocimiento**

En la misma pantalla de configuración, en la sección **Knowledge**, hacé clic en **Upload files** y subí todos los archivos `.md` de la carpeta `assets/` (design, methodology, classifiers, tools).

**4. Guardá y empezá a usarlo**

Hacé clic en **Save** (arriba a la derecha) y listo. Podés empezar a preguntarle sobre la EPH o pedirle que te escriba código.

> **Nota:** Para subir archivos de conocimiento necesitás ChatGPT Plus (pago). Con la versión gratuita podés pegar el contenido de los archivos directamente en el chat cuando lo necesites.

---

## Claude Desktop

Claude Desktop es la aplicación de escritorio de Anthropic. Si no la tenés, descargala desde [claude.ai/download](https://claude.ai/download).

### Lo que vas a necesitar instalar primero: `uv`

`uv` es una herramienta que maneja las dependencias de Python. Sin ella no va a funcionar.

**En Mac o Linux**, abrí la Terminal y pegá:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**En Windows**, abrí PowerShell y pegá:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Cerrá y volvé a abrir la terminal después de instalar.

### Pasos

**1. Descargá este repositorio**

Si tenés `git` instalado, en la terminal:
```bash
git clone https://github.com/matias-denatale/eph-context.git
```

Si no tenés `git`, descargá el ZIP desde GitHub (botón verde **Code → Download ZIP**) y descomprimilo donde quieras. Guardá la ruta de la carpeta — la vas a necesitar.

**2. Abrí el archivo de configuración de Claude Desktop**

Andá a Claude Desktop → menú **Claude** (arriba) → **Settings** → **Developer** → **Edit Config**.

Se va a abrir un archivo `claude_desktop_config.json`. Si está vacío, pegá esto directamente:

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

Si ya tiene contenido, agregá solo la parte de `"eph": { ... }` dentro de `"mcpServers"`.

**3. Reemplazá la ruta**

Cambiá `/ruta/a/eph-context` por la ruta real donde descomprimiste el repositorio.

- **Mac/Linux:** algo como `/Users/tu-nombre/eph-context`
- **Windows:** algo como `C:\\Users\\tu-nombre\\eph-context` (con doble barra invertida)

**4. Guardá y reiniciá Claude Desktop**

Cerrá y volvé a abrir Claude Desktop. Las herramientas EPH van a aparecer disponibles — las podés ver haciendo clic en el ícono de herramientas (🔧) en el chat.

---

## Cursor

Cursor es un IDE basado en VS Code con IA integrada. Si no lo tenés, descargalo desde [cursor.com](https://cursor.com).

Necesitás tener `uv` instalado (ver instrucciones en [la sección de Claude Desktop](#lo-que-vas-a-necesitar-instalar-primero-uv)).

### Pasos

**1. Descargá este repositorio** (igual que en Claude Desktop, paso 1)

**2. Abrí la configuración de MCP en Cursor**

Cursor → **Settings** → **Cursor Settings** → **MCP** → **Add new MCP server**

O bien editá el archivo `~/.cursor/mcp.json` directamente y agregá:

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

**3. Reemplazá la ruta y reiniciá Cursor**

---

## VS Code

Necesitás la extensión **GitHub Copilot** o **Continue** con soporte MCP.

Necesitás tener `uv` instalado (ver instrucciones en [la sección de Claude Desktop](#lo-que-vas-a-necesitar-instalar-primero-uv)).

### Pasos

**1. Descargá este repositorio** (igual que en Claude Desktop, paso 1)

**2. Editá el archivo de configuración MCP**

Creá o editá `.vscode/mcp.json` en tu proyecto:

```json
{
  "servers": {
    "eph": {
      "type": "stdio",
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

**3. Reemplazá la ruta y reiniciá VS Code**

---

## Claude Code CLI

Para usuarios del CLI de Claude Code en terminal.

**1. Cloná el repositorio en tu carpeta de skills:**
```bash
git clone https://github.com/matias-denatale/eph-context.git ~/.claude/skills/eph
```

**2. Agregá esta línea a tu `~/.claude/CLAUDE.md`** en la tabla de skills:
```markdown
| EPH microdata, usu_hogar, usu_individual, scripts R/Python con EPH | `~/.claude/skills/eph/SKILL.md` |
```

La skill se activa automáticamente cuando Claude Code detecta consultas sobre EPH, variables como `CODUSU`, `PONDERA`, `ESTADO`, etc.

---

## ¿Qué sabe hacer?

Una vez instalado, podés pedirle cosas como:

- *"Calculá la tasa de desocupación para el 2do trimestre de 2024 con R"*
- *"¿Qué es el panel rotante y cómo afecta el análisis longitudinal?"*
- *"Escribime un script en Python para calcular informalidad laboral"*
- *"¿Cómo mergeo las bases de hogar e individual?"*
- *"¿Qué variables cambaron en el 4T2023?"*

El modelo siempre consulta los diseños de registro y la metodología oficial antes de responder. No adivina, no improvisa.

---

## Ejemplo de sesión

**Usuario:** Calculá la tasa de desocupación para el 4T2024 con R.

**El modelo (internamente):**
1. `eph_setup()` → recibe workflow obligatorio + reglas críticas
2. `get_design_record("31_aglomerados_post")` → variables `ESTADO`, `PONDERA` y sus categorías exactas
3. `get_methodology("indicadores_mercado_laboral")` → fórmula oficial INDEC

**Respuesta del modelo:**
```r
library(eph)

base <- get_microdata(year = 2024, trimester = 4, type = "individual")

base |>
  summarise(
    desocupacion = sum(PONDERA[ESTADO == 2]) / sum(PONDERA[ESTADO %in% c(1, 2)]) * 100
  )
```

Sin inventar nombres de variables. Sin ponderadores incorrectos. Sin mezclar períodos pre/post 4T2023.

---

## ¿Qué incluye?

| Contenido | Qué es |
|-----------|--------|
| **Diseños de registro** | Variables, categorías y codificaciones para EPH Continua y Total Urbano, antes y después del 4T2023 |
| **Reglas metodológicas** | Ponderadores, panel rotante, quiebre de serie, informalidad, indicadores de mercado de trabajo |
| **Documentación de packages** | Paquete `eph` para R y librería `pyeph` para Python |
| **Clasificador CNO 2001** | Clasificador Nacional de Ocupaciones completo (5 dígitos) |

---

## Agradecimientos

- **[Diego Kozlowski](https://github.com/DiegoKoz)** — creador del [paquete `eph`](https://github.com/ropensci/eph) para R
- **[Guido Weksler](https://github.com/Guidowe)** — [Introducción a R para Ciencias Sociales](https://guidowe.github.io/Curso-R-Flacso/)
- **[Pablo Tiscornia](https://github.com/Pablotis)** — [Curso R INDEC](https://github.com/pablotis/Curso_R_INDEC)

---

## Licencia

MIT. Usalo, modificálo, compartilo. Si lo mejorás, mandá un PR.
