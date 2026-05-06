# Construcción de Datos de Panel en EPH

La EPH posee un esquema de **panel rotante 2-2-2**: una vivienda es encuestada por 2 trimestres consecutivos, luego sale por 2 trimestres, y vuelve a entrar por sus últimos 2 trimestres consecutivos. Cada vivienda participa un máximo de 4 veces (ondas).

---

## Esquema 2-2-2 (vigente desde 2003)

```
T1  T2  T3  T4  T5  T6  T7  T8
[X] [X] [-] [-] [X] [X] (sale)
```

- Ingresa y se encuesta **2 trimestres consecutivos**.
- Sale **2 trimestres consecutivos**.
- Vuelve a ser encuestada **2 trimestres consecutivos**.
- Después de las 4 mediciones, se reemplaza por otra vivienda del área.

> Una vivienda relevada por primera vez en la semana 2 del 3T será encuestada otra vez en la semana 2 del 3T del año siguiente (5 trimestres totales desde su ingreso).

## Grupos de rotación

En cada aglomerado la muestra se divide en **4 grupos de rotación**. Cada grupo es una submuestra de aproximadamente un cuarto del total. Los 4 grupos están equilibrados a lo largo del trimestre y conviven en distinta fase del esquema 2-2-2.

## Solapamiento entre trimestres

| Comparación | % de viviendas en común (esperado) |
|-------------|:---------------------------------:|
| T → T+1 | ~50% |
| T → T+2 | 0% (grupo en descanso) |
| T → T+3 | ~50% (mismo grupo, segunda fase) |
| T → T+4 (mismo trimestre, año siguiente) | ~50% |

> El solapamiento del 50% es útil para estimar cambios trimestrales con menor varianza, pero introduce **autocorrelación** que hay que considerar en análisis longitudinales.

---

## Claves de identificación

Para unir la misma persona a lo largo de trimestres, usar:

| Variable | Descripción |
|----------|-------------|
| `CODUSU` | Código de la **vivienda** (char 29). Llave principal del seguimiento longitudinal. |
| `NRO_HOGAR` | Número de hogar dentro de la vivienda. |
| `COMPONENTE` | Número de orden de la persona dentro del hogar. |
| `ANO4` + `TRIMESTRE` | Fecha del trimestre relevado. |

---

## Construcción del panel en R

### Usando el paquete `eph`

La función `organize_panels()` del paquete `eph` (ropensci) automatiza el apareamiento entre trimestres:

```r
library(eph)

base_t1 <- get_microdata(year = 2023, period = 1, type = "individual")
base_t2 <- get_microdata(year = 2023, period = 2, type = "individual")

panel <- organize_panels(
  bases     = list(base_t1, base_t2),
  variables = c("ESTADO", "PONDERA", "CAT_OCUP"),
  window    = "trimestral"  # o "anual"
)
```

`organize_panels()` usa `CODUSU + NRO_HOGAR + COMPONENTE` internamente para el join y agrega una columna `consistencia` que marca registros con inconsistencias demográficas.

### Construcción manual

```r
library(dplyr)

panel_t1_t2 <- inner_join(
  base_t1,
  base_t2,
  by = c("CODUSU", "NRO_HOGAR", "COMPONENTE"),
  suffix = c("_t1", "_t2")
) %>%
  filter(
    CH04_t1 == CH04_t2,          # mismo sexo
    CH06_t2 - CH06_t1 >= 0,      # edad no retrocede
    CH06_t2 - CH06_t1 <= 1       # edad sube como máximo 1 año
  )
```

---

## Prevención de falsos positivos

⚠️ **CRÍTICO:** La combinación `CODUSU + NRO_HOGAR + COMPONENTE` **NO ES INFALIBLE**. Las viviendas pueden sufrir rotación de inquilinos, fallecimientos o errores de carga.

Para confirmar que es el **mismo individuo**, verificar:

- **Sexo (`CH04`)**: debe ser idéntico en ambos trimestres.
- **Edad (`CH06`)**: debe ser igual o tener +1 año (en un panel trimestral). Para paneles anuales, +1 o +2 años.
- **Inconsistencia general**: el campo `consistencia` que devuelve `organize_panels()` marca el flag amplio.

### Tipos de inconsistencia (detección granular)

```r
panel <- panel %>%
  mutate(
    inc_sexo  = !is.na(CH04) & !is.na(CH04_t1) & CH04 != CH04_t1,
    inc_edad  = !is.na(CH06) & !is.na(CH06_t1) &
                (CH06_t1 < CH06 | CH06_t1 > CH06 + 1L),
    inc_total = !consistencia   # flag de organize_panels()
  )
```

---

## Calidad efectiva del panel (~50%)

En la práctica, **no todos los hogares esperados en t1 aparecen en la base**. La tasa efectiva de panel encontrado ronda el 50% del total de t0, por:

- No respuesta (rechazo, ausencia, mudanza)
- Hogares que dejaron de existir
- Errores de apareamiento

> Esto significa que cualquier análisis de panel trabaja con una submuestra: hay que reportar tanto el N del panel como el N de t0 para que el lector evalúe la representatividad.

---

## Dúos: pares de trimestres para análisis longitudinal

Un **dúo** es el par de trimestres que se compara en un análisis de panel. Hay dos tipos:

### Dúos trimestrales (consecutivos)

| Dúo | Trimestres | Cuándo existe |
|-----|-----------|---------------|
| `1-2` | T1 → T2 del mismo año | Si existen ambas bases |
| `2-3` | T2 → T3 del mismo año | Si existen ambas bases |
| `3-4` | T3 → T4 del mismo año | Si existen ambas bases |
| `4-1` | T4 año X → T1 año X+1 | Si existen ambas bases |

### Dúos anuales (mismo trimestre, año siguiente)

| Dúo | Descripción |
|-----|-------------|
| `T1` | T1 año X → T1 año X+1 |
| `T2` | T2 año X → T2 año X+1 |
| `T3` | T3 año X → T3 año X+1 |
| `T4` | T4 año X → T4 año X+1 |

> Los dúos anuales permiten comparar el **mismo trimestre estacional** entre años, eliminando efectos estacionales.

---

## Análisis de flujos entre estados

Con el panel armado se pueden calcular **transiciones entre estados laborales** (Condición de Actividad = `ESTADO`):

| Código `ESTADO` | Categoría |
|:-:|-----------|
| 1 | Ocupado |
| 2 | Desocupado |
| 3 | Inactivo |

### Flujos ponderados

```r
# Tabla de transición ponderada (base t0)
tabla_flujos <- panel %>%
  group_by(ESTADO, ESTADO_t1) %>%
  summarise(personas = sum(PONDERA), .groups = "drop") %>%
  group_by(ESTADO) %>%
  mutate(pct = round(personas / sum(personas) * 100, 1))

# Tasas destacadas por categoría
# Persistencia: % que permanece en el mismo estado
# Salida: % que abandona el estado
# Entrada: % que proviene de otro estado (base t1)
```

### Variante: Categoría Ocupacional (`CAT_OCUP`)

| Código `CAT_OCUP` | Categoría |
|:-:|-----------|
| 1 | Patrón |
| 2 | Cuenta propia |
| 3 | Asalariado |
| 4 | Trabajador familiar sin remuneración (TFSR) |

---

## Informalidad en panel

### Definición clásica EPH (desde 2003)

Solo aplica a **asalariados** (`CAT_OCUP == 3`):

```r
mutate(formalidad = case_when(
  CAT_OCUP == 3 & PP07H == 1 ~ 1L,  # Formal (con descuento jubilatorio)
  CAT_OCUP == 3 & PP07H == 2 ~ 2L,  # Informal
  TRUE                       ~ NA_integer_
))
```

| Código | Descripción |
|:-:|-------------|
| `PP07H == 1` | Tiene descuento jubilatorio → **Formal** |
| `PP07H == 2` | No tiene descuento jubilatorio → **Informal** |

### Definición ampliada OIT 2023 (desde 4T2023)

Extiende la clasificación a **todos los ocupados**:

```r
mutate(formalidad_ampliada = case_when(
  CAT_OCUP == 3 & PP07H == 1                           ~ 1L,  # Asalariado formal
  CAT_OCUP == 3 & PP07H == 2                           ~ 2L,  # Asalariado informal
  CAT_OCUP %in% c(1L, 2L) & (PP05I == 1 | PP05K == 1) ~ 1L,  # Patrón/Cta.propia formal
  CAT_OCUP %in% c(1L, 2L) & PP05I == 2 & PP05K == 2   ~ 2L,  # Patrón/Cta.propia informal
  CAT_OCUP == 4                                        ~ 2L,  # TFSR siempre informal
  TRUE                                                 ~ NA_integer_
))
```

| Variable | Descripción |
|----------|-------------|
| `PP07H` | ¿Le descuentan jubilación? (asalariados) |
| `PP05I` | ¿Tiene obra social o mutual por su trabajo? (no asalariados) |
| `PP05K` | ¿Está inscripto como autónomo o monotributista? (no asalariados) |

> ⚠️ La definición ampliada OIT 2023 solo es aplicable a partir del **4T2023** (quiebre de serie). No comparar con períodos anteriores sin empalme.

---

## Variables requeridas según análisis

| Análisis | Variables mínimas en el panel |
|----------|-------------------------------|
| Condición de actividad | `ESTADO`, `PONDERA`, `CODUSU`, `NRO_HOGAR`, `COMPONENTE` |
| Categoría ocupacional | + `CAT_OCUP` |
| Informalidad clásica | + `CAT_OCUP`, `PP07H` |
| Informalidad ampliada OIT | + `CAT_OCUP`, `PP07H`, `PP05I`, `PP05K` |
| Calidad del panel | + `CH04` (sexo), `CH06` (edad) |

---

## Advertencias para análisis longitudinales

1. **Para estimaciones puntuales** (un trimestre): usar `PONDERA` o variantes ajustadas.
2. **Para cambios entre trimestres**: aprovechar el solapamiento pero usar varianza que considera el panel.
3. **Para análisis longitudinales**: aparear con `CODUSU + NRO_HOGAR + COMPONENTE`, verificar consistencia demográfica, considerar la **erosión del panel** (no respuesta acumulada).
4. **Reportar calidad**: siempre informar N del panel y N de t0 para que el lector evalúe la representatividad.
5. **2T2020 (pandemia)**: relevamiento telefónico con ajustes por propensity score y calibración. Mayor erosión del panel por el cambio de modalidad.
6. **Quiebre 4T2023**: si la serie de panel cruza ese período, advertir sobre la no comparabilidad. Ver `quiebre_serie_4t2023.md`.
