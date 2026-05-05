# Diferencias: EPH Continua vs Total Urbano

Es fundamental distinguir qué base de datos se está procesando para no reportar estimaciones incorrectas de cobertura geográfica.

## EPH Continua (Bases trimestrales)
- **Cobertura:** 31 principales aglomerados urbanos del país.
- **Frecuencia:** Se publica cada trimestre (T1, T2, T3, T4).
- **Representatividad:** Representa aproximadamente al **63%** de la población total del país (y algo más del 70% de la población urbana).
- **Uso:** Construcción de series de tiempo de coyuntura (tasas de empleo, pobreza trimestral/semestral).

## EPH Total Urbano (EPH-TU)
- **Cobertura:** Todos los aglomerados urbanos de **2.000 y más habitantes**. Incluye los 31 aglomerados de la continua más el resto de las localidades urbanas.
- **Frecuencia:** Se publica **una sola vez al año**, referida exclusivamente al **Tercer Trimestre (T3)** de cada año.
- **Uso:** Estimaciones con representatividad nacional (urbana) exhaustiva, análisis estructural, o estudios provinciales más detallados.

## Reglas de Comparabilidad
⚠️ **NUNCA** comparar directamente un dato de la EPH Trimestral (31 aglomerados) con la EPH Total Urbano, ya que el denominador geográfico es distinto.
- Si se utiliza la base del Total Urbano, el título de cualquier tabla o gráfico debe decir "Total Aglomerados Urbanos".
- Si se usa la EPH trimestral habitual, el título debe especificar "31 Aglomerados Urbanos".
- Se puede filtrar a los 31 aglomerados dentro del archivo de Total Urbano si se necesita empalmar con la Continua.