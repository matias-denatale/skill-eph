# Medición de la Informalidad Laboral

Basado en el documento metodológico oficial de INDEC (Nº 43, 2025), la medición de la informalidad requiere diferenciar entre el "empleo informal" (asalariados sin descuento jubilatorio) y el "sector informal" de las unidades económicas.

## Asalariados (Sector de unidades económicas de asalariados)
Según el algoritmo oficial (Anexo 8.b):
- **Sector Formal:** 
  - Si `PP04A = 1` (Estatal)
  - Si `PP04A` es (2,3,9) y `PP07H = 1` (Tiene descuento jubilatorio)
  - Si es asalariado no registrado (`PP07H = 2`), pero trabaja en una empresa grande, sociedad, etc. Evaluado a través de variables del bloque 7 (`7i2`, `7i3`, `7i4`).
- **Sector Hogares:** Si `PP04B1 = 1` (Servicio doméstico) o se identifican características específicas (`4a=3` y `7h=2` sin características formales).
- **Sector Informal:** Aquellos no registrados (`PP07H = 2`) en unidades pequeñas/informales (Resto de las combinaciones).
- **Sector Ignorado:** Independientes cautivos (`5g=1`) o falta de respuesta en bloque 7.

## Trabajadores Independientes (Sector Formal / Informal)
El algoritmo oficial evalúa las características de la unidad económica:
- **Sector Formal:** 
  - Si `PP06A = 1` (Es sociedad) y `PP06E = (1,2)`.
  - Si no es sociedad (`6a=2`), pero tiene local/oficina independiente (`5i = 1,2,3`).
  - Si tiene un tamaño mayor (`5k=1`) o características formales cruzadas con `6e1`.
- **Sector Informal:**
  - Sin local y tamaño pequeño/informal (Múltiples combinaciones de `5i=(4,9)`, `5j=1`, `5k=2`, etc.).

## Implementación en R / Python
Debido a la complejidad de las combinaciones y saltos del cuestionario de 4T2023, para calcular con rigor el "Sector Informal" se requiere seguir línea a línea el Anexo 8.b de la Metodología Nº 43. 
Si el objetivo es solo el **"Empleo asalariado no registrado"**, basta con el filtro:
```R
# Tasa de asalariados sin descuento jubilatorio
asalariados_informales <- base %>%
  filter(ESTADO == 1 & CAT_OCUP == 3 & PP07H == 2)
```