# EPH 31 aglomerados urbanos vs EPH Total Urbano

## Concepto central

Estas son dos operaciones estadísticas distintas del INDEC. La diferencia fundamental es **geográfica**: qué territorio representan. El contenido del cuestionario (variables, bloques, preguntas) es esencialmente el mismo en ambas.

---

## EPH 31 aglomerados urbanos

- **Cobertura:** Los 31 principales aglomerados urbanos del país.
- **Frecuencia:** Se publica **todos los trimestres** (T1, T2, T3, T4 de cada año).
- **Representatividad:** Aproximadamente el 63% de la población total del país.
- **Uso:** Cualquier análisis del mercado de trabajo, ingresos, condiciones de vida, educación, vivienda — tanto de coyuntura como estructural. No está limitada a series de tiempo: también se usa para análisis transversales, estudios de pobreza, informalidad, y cualquier otro tema socioeconómico.
- **Título correcto en tablas y gráficos:** "31 Aglomerados Urbanos".
- **Denominación:** Llamarla "EPH Continua" tiende a generar confusión. Preferir siempre "EPH 31 aglomerados urbanos".

### Variables de identificación geográfica
- `AGLOMERADO` — 31 códigos (02 a 93). Ver diseño de registro para lista completa.
- `REGION` — región del país (01=GBA, 40=NOA, 41=NEA, 42=Cuyo, 43=Pampeana, 44=Patagonia).
- `MAS_500` — tamaño del aglomerado (N=menos de 500.000 hab.; S=500.000 y más).
- No tiene variable `PROVINCIA`.

---

## EPH Total Urbano (EPH-TU)

- **Cobertura:** Todos los aglomerados urbanos de **2.000 y más habitantes** del país. Incluye los 31 aglomerados de la encuesta trimestral más el resto de las localidades urbanas de cada provincia.
- **Frecuencia:** Se publica **una sola vez al año**, referida exclusivamente al **Tercer Trimestre (T3)**.
- **Representatividad:** Cobertura urbana nacional exhaustiva, incluyendo localidades pequeñas y medianas no captadas por los 31 aglomerados.
- **Uso:** Estimaciones con representatividad urbana nacional, análisis provinciales, estudios que requieren cobertura geográfica más amplia.
- **Título correcto en tablas y gráficos:** "Total Aglomerados Urbanos".

### Variables de identificación geográfica
- `AGLOMERADO` — códigos extendidos: los 31 aglomerados habituales **más** los "Resto" provinciales (Resto Buenos Aires = 40, Resto Catamarca = 41, Resto Córdoba = 42, etc.).
- `PROVINCIA` — variable presente en Total Urbano, **ausente** en los 31 aglomerados.
- No tiene `REGION` ni `MAS_500`.

### Gotcha técnico — nombre de variable inconsistente (POST 4T2023)
En la base **Hogar** de EPH Total Urbano POST 4T2023, la variable de período se llama **`TRIM`** (no `TRIMESTRE`).
En la base **Personas** del mismo período, se llama `TRIMESTRE`.
Prestar atención al usar esta base: el nombre difiere entre los dos archivos.

---

## Relación con el quiebre de serie 4T2023

⚠️ **El quiebre de cuestionario del 4T2023 afectó a AMBAS encuestas simultáneamente.**
No hay relación entre el quiebre metodológico y la distinción entre las dos operaciones estadísticas. Ambas adoptaron el nuevo diseño de registro al mismo tiempo.

---

## Reglas de comparabilidad

⚠️ **NUNCA** comparar directamente un dato de EPH 31 aglomerados con EPH Total Urbano: el denominador geográfico es distinto y los resultados no son equivalentes.

- Se puede filtrar la EPH Total Urbano a los 31 aglomerados si se necesita empalmar con la serie trimestral (usar `AGLOMERADO <= 93` o los códigos específicos de los 31 aglomerados).
- Para análisis provinciales: usar Total Urbano (tiene `PROVINCIA`). Los 31 aglomerados no permiten desagregación provincial directa.
