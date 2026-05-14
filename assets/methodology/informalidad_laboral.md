# Medición de la Informalidad Laboral

## Variables pre-calculadas — solo disponibles desde 4T2023

A partir del 4T2023, el INDEC incorporó dos variables que condensan el algoritmo de informalidad directamente en la base de microdatos:

| Variable | Valores | Qué mide |
|----------|---------|----------|
| `EMPLEO` | 1=Formal / 2=Informal / 9=Ns/Nr | Informalidad del **empleo individual** (asalariado sin descuento jubilatorio y equivalentes) |
| `SECTOR` | 1=Formal / 2=Informal / 3=Hogares / 9=Ns/Nr | Informalidad de la **unidad económica** donde trabaja la persona |

**Para datos POST 4T2023: usar `EMPLEO` y `SECTOR` directamente.** No es necesario reimplementar el algoritmo — el INDEC ya lo aplicó.

```r
# POST 4T2023 — tasa de informalidad laboral (empleo informal)
informales <- base_individual %>%
  filter(ESTADO == 1, EMPLEO == 2)

# POST 4T2023 — trabajadores en sector informal (excluye hogares)
sector_informal <- base_individual %>%
  filter(ESTADO == 1, SECTOR == 2)

# POST 4T2023 — trabajadores en hogares (servicio doméstico y similares)
sector_hogares <- base_individual %>%
  filter(ESTADO == 1, SECTOR == 3)
```

---

## Algoritmo manual — necesario para datos PRE 4T2023

Para períodos anteriores al 4T2023, no existen `EMPLEO` ni `SECTOR`. La informalidad debe construirse siguiendo el algoritmo del Anexo 8.b de la Metodología INDEC Nº 43.

Basado en el documento metodológico oficial de INDEC (Nº 43, 2025), la medición requiere diferenciar entre el "empleo informal" (asalariados sin descuento jubilatorio) y el "sector informal" de las unidades económicas.

### Asalariados (Sector de unidades económicas)

Según el algoritmo oficial (Anexo 8.b):

- **Sector Formal:**
  - Si `PP04A = 1` (Estatal)
  - Si `PP04A` es (2, 3, 9) y `PP07H = 1` (tiene descuento jubilatorio)
  - Si es asalariado no registrado (`PP07H = 2`), pero trabaja en empresa grande, sociedad, etc. — evaluado a través de variables del bloque 7 (`PP07I2`, `PP07I3`, `PP07I4`).
- **Sector Hogares:** Si `PP04B1 = 1` (servicio doméstico) o características específicas (`PP04A = 3` y `PP07H = 2` sin rasgos de formalidad).
- **Sector Informal:** No registrados (`PP07H = 2`) en unidades pequeñas/informales (resto de combinaciones).
- **Sector Ignorado:** Independientes cautivos (`PP05F = 1`) o falta de respuesta en bloque 7.

### Trabajadores Independientes

- **Sector Formal:**
  - Si `PP06A = 1` (es sociedad) y `PP06E` ∈ (1, 2).
  - Si no es sociedad (`PP06A = 2`), pero tiene local/oficina independiente.
  - Si tiene tamaño mayor o características formales cruzadas con `PP06E1`.
- **Sector Informal:**
  - Sin local y tamaño pequeño/informal (múltiples combinaciones de `PP05C_1`, `PP05C_2`, `PP05F`, `PP05K`).

### Implementación

Debido a la complejidad de las combinaciones y saltos del cuestionario, para calcular con rigor el Sector Informal en datos PRE 4T2023 se requiere seguir línea a línea el Anexo 8.b de la Metodología Nº 43.

Si el objetivo es solo el **empleo asalariado no registrado** (proxy simple de informalidad):

```r
# PRE 4T2023 — asalariados sin descuento jubilatorio
asalariados_informales <- base_individual %>%
  filter(ESTADO == 1, CAT_OCUP == 3, PP07H == 2)
```

---

## Series de tiempo que cruzan el 4T2023

Al comparar períodos PRE y POST 4T2023 en una misma serie de informalidad:

- PRE: construir la variable manualmente con el algoritmo del Anexo 8.b
- POST: usar `EMPLEO` o `SECTOR` directamente

Verificar que la definición aplicada en ambos períodos sea equivalente antes de empalmar la serie. El INDEC publica notas metodológicas sobre la compatibilidad de la medición entre ambos diseños.
