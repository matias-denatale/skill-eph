# Consideraciones metodológicas: Quiebre de serie en 4T2023

## IMPORTANTE: el quiebre afectó a AMBAS encuestas

El quiebre de cuestionario del 4T2023 afectó simultáneamente a la **EPH 31 aglomerados urbanos** y a la **EPH Total Urbano**. No es un fenómeno exclusivo de una de las dos operaciones estadísticas. No tiene ninguna relación con la distinción entre ambas encuestas — esa diferencia es exclusivamente geográfica (cobertura territorial), no metodológica.

A partir del 4° trimestre de 2023, el INDEC implementó modificaciones metodológicas en el cuestionario de la EPH, lo que generó un **quiebre de serie histórica**.

## Cambios documentados
- **Clasificadores:** Se reemplazó el CNO (Clasificador Nacional de Ocupaciones) de 2001 por el **CNO-2010**. También se actualizó el CAES.
- **Cuestionario:** Se modificaron las preguntas del Bloque 3 (Características ocupacionales) y Bloque 4 (Ingresos). 
- **Nuevas formas de trabajo:** Se introdujeron preguntas específicas para captar el empleo mediante plataformas digitales, aplicaciones y trabajo remoto.

## Variables afectadas
- **Modificadas/Reemplazadas:**  `PP03C` (tipo de ocupación) y `PP04A` experimentaron cambios en las opciones para incluir trabajo de plataformas.
- Para procesar datos a partir de 4T2023, es OBLIGATORIO usar el **Diseño de Registro POS 4T2023**.

## Análisis de series de tiempo
⚠️ **ADVERTENCIA:** El INDEC advierte que indicadores complejos como precariedad, informalidad o deciles de ingreso **no son estrictamente comparables** entre el pre y el pos 4T2023 sin empalmes.
- Las tasas básicas (Actividad, Empleo, Desocupación) mantienen comparabilidad macro, pero las aperturas por categoría ocupacional requieren cautela.
- **Recomendación:** Al construir un panel o gráfico de serie de tiempo que cruce el año 2023, se debe agregar una línea de quiebre (o nota al pie) especificando el cambio de cuestionario. No unir la serie como si fuera continua.