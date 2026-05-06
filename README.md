<div align="center">

#  Skill EPH

### Que la IA escriba tu código de EPH sin inventar lo que no existe

[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![Claude Code](https://img.shields.io/badge/claude_code-skill-8A2BE2)](https://claude.ai)
[![EPH](https://img.shields.io/badge/EPH-INDEC-0056A0)](https://www.indec.gob.ar/indec/web/Institucional-Indec-Bases-EPH)
[![R](https://img.shields.io/badge/R-ready-276DC3?logo=r)](https://www.r-project.org/)
[![Python](https://img.shields.io/badge/Python-ready-3776AB?logo=python)](https://www.python.org/)

</div>

---

<blockquote>
<strong>Usá inteligencia artificial para procesar los microdatos de la EPH sin miedo a que el modelo invente variables, aplique mal los ponderadores o se olvide del panel rotante.</strong><br>
Esta skill inyecta los diseños de registro del INDEC y las reglas metodológicas directamente en el contexto del modelo.<br>
<strong>Resultado: código que respeta la realidad de los datos.</strong>
</blockquote>

---

##  ¿Para quién es esto?

> **¿Sos investigador de la EPH y no estás acostumbrado a codear con inteligencia artificial?**
> Esta skill te da la confianza de que el código que genera el modelo respeta las reglas metodológicas del INDEC. No vas a tener que andar corrigiendo errores como que use `PONDERA` mal o se olvide del panel rotante.

> **¿Sos un usuario eventual de la EPH que no sabe muy bien cómo funciona y querés hacer cruces y probar cosas?**
> Acá tenés un punto de partida sólido. La skill incluye los diseños de registro completos y documentación metodológica curada. No necesitás saberte de memoria el manual del INDEC para empezar a trabajar.

> **¿Sos un experto que a veces, en el apuro, no quiere escribir el código y quiere que la IA lo haga pero no confiás en ella?**
> Te entiendo. Por eso creé esta skill: fuerza al modelo a leer las reglas antes de escribir código. No es magia — es darle contexto de calidad para que no invente.

---

##  El problema: las alucinaciones existen y la EPH no perdona

Los modelos de lenguaje alucinan. Es un hecho. Y cuando trabajás con la EPH, un error pequeño — una variable que no existe, un ponderador mal aplicado, un tratamiento incorrecto del panel rotante — te puede invalidar todo un análisis sin que te des cuenta.

**Esta skill viene a solucionar eso.**

En lugar de dejar que el modelo "recuerde" cómo funciona la EPH —que no es su punto fuerte—, la skill le inyecta en el contexto los diseños de registro oficiales, la metodología documentada y las reglas de tratamiento de variables. El resultado: código que respeta la realidad de los microdatos.

---

##  ¿Qué es una skill y cómo funciona?

Una skill es un conjunto de instrucciones y archivos de contexto que se cargan automáticamente cuando el agente de IA detecta que estás trabajando con un tema específico — en este caso, la EPH.

### ¿Cómo funciona por el fondo?

| Paso | Qué pasa |
|:----:|----------|
| **1** | Le pedís al agente algo como *"escribime un script en R que calcule la tasa de informalidad para el tercer trimestre de 2023"* |
| **2** | El agente reconoce que estás hablando de la EPH y carga automáticamente `assets/design/` (diseños de registro con todas las variables) y `assets/methodology/` (reglas metodológicas) |
| **3** | Con ese contexto cargado, el modelo genera el código. **No improvisa — lee la documentación real.** |

> Es como darle el manual del INDEC al modelo justo antes de que escriba. Sin la skill, el modelo improvisa basándose en lo que "recuerda" de su entrenamiento. Con la skill, tiene la fuente de verdad a mano.

---

##  ¿Qué incluye?

| Categoría | Contenido |
|-----------|-----------|
|  **Diseños de registro** | Variables, categorías y codificaciones para los diseños PRE y POS del 4T2023 — EPH Continua y Tot Urbano |
|  **Reglas metodológicas** | Uso correcto de ponderadores (`PONDERA`, `PONDIH`, `PONDII`), panel rotante, quiebres de serie, informalidad laboral, indicadores del mercado de trabajo |
|  **Referencia de packages** | Documentación completa del paquete `eph` para R y la librería `pyeph` para Python: funciones, parámetros y ejemplos |
|  **Clasificador CNO 2001** | El Clasificador Nacional de Ocupaciones completo (40 páginas INDEC) con su estructura de 5 dígitos y la tabla de todas las ocupaciones |
|  **Orientación automática** | La skill guía al modelo para estructurar pipelines de datos respetando la metodología INDEC sin que vos le expliques cada detalle |

---

##  Agradecimientos

Esta skill se apoya en el conocimiento abierto de la comunidad. Aproveché los recursos y cursos de tres referentes que vienen compartiendo material de calidad sobre el trabajo con microdatos de la EPH:

- **[Diego Kozlowski](https://github.com/DiegoKoz)** — creador del [paquete `eph`](https://github.com/ropensci/eph) para R y del [Curso R EPH](https://github.com/DiegoKoz/Curso_R_EPH_clases)
- **[Guido Weksler](https://github.com/Guidowe)** — [Introducción a R para Ciencias Sociales](https://guidowe.github.io/Curso-R-Flacso/) con aplicación práctica en la EPH
- **[Pablo Tiscornia](https://github.com/Pablotis)** — [Curso R INDEC](https://github.com/pablotis/Curso_R_INDEC) e [introducción al procesamiento de datos de la EPH](https://pablotis.github.io/r_iigg/)

Sin esa base comunitaria, esto no existiría. La skill no reemplaza ese conocimiento: lo empaqueta para que la IA lo use correctamente.

---

##  Instalación

```bash
# 1. Cloná el repositorio en tu carpeta de skills
git clone https://github.com/matias-denatale/skill-eph.git

# 2. Configurá tu agente para que cargue los archivos de la skill
#    (las instrucciones específicas dependen de tu plataforma)
```

La skill se activa automáticamente cuando el agente detecta consultas relacionadas con la EPH, microdatos del INDEC, o variables como `CODUSU`, `PONDERA`, `ESTADO`, etc.

---

##  Estructura del repositorio

```
skill-eph/
├── SKILL.md              # Instrucciones y capacidades de la skill
├── README.md             # Este archivo
└── assets/
    ├── design/           # Diccionarios de variables por diseño de registro
    │   ├── EPH_POS_4T2023.md
    │   ├── EPH_PRE_4T2023.md
    │   ├── EPH_TotUrbano_POS_4T2023.md
    │   └── EPH_TotUrbano_PRE_4T2023.md
    ├── methodology/      # Documentación metodológica curada
    │   ├── ponderadores.md
    │   ├── panel_rotante.md
    │   ├── quiebre_serie_4t2023.md
    │   ├── informalidad_laboral.md
    │   ├── indicadores_mercado_laboral.md
    │   └── eph_continua_vs_total_urbano.md
    ├── tools/            # Referencia de packages de procesamiento EPH
    │   ├── eph_package_r.md   # Paquete `eph` para R (ropensci, v1.0.2)
    │   └── pyeph_package.md   # Librería `pyeph` para Python
    └── classifiers/      # Clasificadores oficiales INDEC
        └── cno_2001.md        # Clasificador Nacional de Ocupaciones 2001
```

---

##  Licencia

Este proyecto es abierto. Usalo, modificálo, compartilo. Si lo mejorás, mandá un PR así nos beneficiamos todos.
