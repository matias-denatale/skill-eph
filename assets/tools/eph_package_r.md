# Paquete `eph` para R — Referencia Completa

**Versión:** 1.0.2 (CRAN, 2024-06-23)
**Repositorio:** https://github.com/ropensci/eph
**Mantenedora:** Carolina Pradier
**Licencia:** MIT
**Idioma de documentación:** Español
**Disclaimer global:** Las funciones de cálculo NO son productos oficiales de INDEC.

## Instalación

```r
install.packages("eph")
library(eph)
```

## Dependencias principales

`dplyr`, `expss`, `purrr`, `tibble`, `stringr`, `readxl`, `tidyr`, `utils`, `zoo`, `leaflet`, `htmltools`, `rlang`, `stats`, `cli`, `httr`, `curl`, `tidyselect`

---

## Funciones de descarga de datos

### `get_microdata()` — Descarga bases EPH

Descarga bases de la EPH del INDEC a partir de 1996.

```r
get_microdata(
  year    = 2018,        # integer o vector: año(s) desde 2003 (EPH continua) o desde 1996 (EPH puntual)
  period  = 1,           # integer o vector: trimestre (1-4) para continua; onda (1-2) para puntual
  type    = "individual",# "individual" o "hogar"
  vars    = "all",       # vector de variables a seleccionar; "all" trae todas
  destfile = NULL        # path .RDS opcional: si existe, lee del disco; si no existe, descarga y guarda
)
```

**Detalles:**
- EPH puntual: `period` = número de onda (1-2), alcance onda 1/1996 a onda 1/2003
- EPH continua: `period` = número de trimestre (1-4), alcance 3T2003 a la actualidad

**Ejemplo:**
```r
base_individual <- get_microdata(
  year   = 2018:2019,
  period = 1,
  type   = "individual",
  vars   = c("PONDERA", "ESTADO", "CAT_OCUP")
)
```

---

### `get_total_urbano()` — Descarga bases EPH Total Urbano

Descarga bases de la EPH Total Urbano del INDEC a partir de 2016.

```r
get_total_urbano(
  year     = 2016,        # integer o vector desde 2016
  type     = "individual",# "individual" o "hogar"
  vars     = "all",
  destfile = NULL
)
```

**Ejemplo:**
```r
base_individual <- get_total_urbano(
  year = 2016,
  type = "hogar",
  vars = c("PONDERA", "IV1", "IV2")
)
```

---

### `get_eahu()` — Descarga bases EAHU

Descarga bases de la Encuesta Anual de Hogares Urbanos (EAHU) del INDEC, 2010–2014.

```r
get_eahu(
  year     = 2010,        # integer o vector entre 2010 y 2014
  type     = "individual",# "individual" o "hogar"
  vars     = "all",
  destfile = NULL
)
```

**Ejemplo:**
```r
base_individual <- get_eahu(
  year = 2010,
  type = "individual",
  vars = c("SUBDOMINIO", "PONDERA", "ESTADO", "CAT_OCUP")
)
```

---

### `get_poverty_lines()` — Descarga canastas básicas

Descarga la CBA y CBT a partir de abril 2016.

```r
get_poverty_lines(
  regional = FALSE  # TRUE: canastas regionales (para calculate_poverty)
                    # FALSE: serie de GBA provista por INDEC
)
```

**Ejemplo:**
```r
canasta <- get_poverty_lines(regional = TRUE)
```

---

## Funciones de cálculo

### `calculate_poverty()` — Pobreza e Indigencia

Calcula pobreza e indigencia siguiendo la metodología de línea del INDEC.

```r
calculate_poverty(
  base          ,           # base individual de uno o más periodos
  basket        ,           # canasta con estructura de canastas_reg_example
  print_summary = TRUE,     # imprime tasas en consola
  window        = "quarter",# "quarter" (trimestral) o "semester" (semestral)
  group_vars    = c()       # variables agrupadoras adicionales
)
```

**Retorna:** la base con 5 columnas nuevas indicando situación del hogar (indigente / pobre / no pobre).

**Ejemplo:**
```r
bases <- dplyr::bind_rows(
  toybase_individual_2016_03,
  toybase_individual_2016_04
)
base_pobreza <- calculate_poverty(
  base       = bases,
  basket     = canastas_reg_example,
  print_summary = TRUE,
  group_vars = c(CH04, NIVEL_ED),
  window     = "semestral"
)
```

---

### `calculate_tabulates()` — Tabulados ponderados

Crea tabulados uni o bivariados con ponderación, totales y porcentajes.

```r
calculate_tabulates(
  base           ,           # dataframe
  x              ,           # string: variable a tabular
  y              = NULL,     # string opcional: segunda variable (tabla doble entrada)
  weights        = NULL,     # string: variable de ponderación
  affix_sign     = FALSE,    # TRUE agrega "%" al resultado
  digits         = 1,        # dígitos significativos
  add.totals     = "none",   # "none", "row", "col", "both"
  add.percentage = "none"    # "none", "row", "col"
)
```

**Ejemplo:**
```r
# Tabla simple
calculate_tabulates(
  base    = toybase_individual_2016_04,
  x       = "REGION", y = "CH04",
  weights = "PONDERA"
)

# Con totales por fila y porcentajes por columna
calculate_tabulates(
  base           = toybase_individual_2016_04,
  x              = "REGION", y = "CH04",
  weights        = "PONDERA",
  add.totals     = "row",
  add.percentage = "col"
)
```

---

### `calculate_errors()` — Error muestral

Asigna el desvío estándar o coeficiente de variación a estimaciones de totales poblacionales, según tablas de error muestral de INDEC para EPH continua desde 2T2003.

```r
calculate_errors(
  value       ,              # vector numérico de estimaciones de población
  codigo_aglo = "Total",     # código del aglomerado; "Total" = 31 aglomerados
  periodo_eph = "2014.03",   # "2014.03" (3T2014 en adelante) o "2003.03_2014.02"
  measure     = "cv"         # "cv" = coeficiente de variación; "ds" = desvío estándar
)
```

**Ejemplo:**
```r
tabla <- eph::toybase_individual_2016_03 %>%
  eph::organize_labels() %>%
  dplyr::filter(AGLOMERADO == 32) %>%
  eph::calculate_tabulates(x = "CH03", weights = "PONDERA", add.totals = "row")

tabla %>%
  dplyr::mutate(
    ds = calculate_errors(Freq, codigo_aglo = "32", periodo_eph = "2014.03", measure = "ds")
  )
```

---

## Funciones de organización

### `organize_labels()` — Etiquetado de bases

Etiqueta las variables de la base EPH según el diseño de registro oficial. No renombra columnas, agrega etiquetas.

```r
organize_labels(
  df   ,                   # base de microdatos EPH
  type = "individual"      # "individual" o "hogar"
)
```

**Ejemplo:**
```r
df <- organize_labels(toybase_individual_2016_04, type = "individual")
```

---

### `organize_panels()` — Pool de datos en panel

Arma un pool de datos en panel de EPH continua concatenando observaciones de distintos periodos.

```r
organize_panels(
  bases     ,              # lista de bases de microdatos
  variables ,              # vector de nombres de variables de interés
  window    = "anual"      # "anual" o "trimestral"
)
```

**Nota:** Usa `CODUSU` para el seguimiento de personas entre trimestres.

**⚠️ GOTCHA — columnas duplicadas al hacer `pivot_longer()`:**
`organize_panels()` devuelve las variables de interés **dos veces**: con sufijo `_t0`/`_t1` Y sin sufijo. Si luego se hace `pivot_longer()`, falla con `Names must be unique` porque `ANO4`, `TRIMESTRE`, `ESTADO`, etc. aparecen duplicadas.

**Fix:** antes de pivotar, descartar las columnas sin sufijo que tienen su versión sufijada:

```r
panel <- organize_panels(bases = lista_bases, variables = c("P21", "ESTADO"), window = "trimestral")

# Columnas de identificación del panel (sin sufijo, se conservan tal cual)
id_vars <- c("CODUSU", "NRO_HOGAR", "COMPONENTE")

# Descartar columnas sin sufijo que tienen versión _t0/_t1
vars_sufijadas <- names(panel)[grepl("_t[01]$", names(panel))]
bases_sufijadas <- unique(sub("_t[01]$", "", vars_sufijadas))
cols_a_descartar <- setdiff(bases_sufijadas, id_vars)

panel_limpio <- panel |> select(-any_of(cols_a_descartar))

# Ahora pivot_longer funciona correctamente
panel_long <- panel_limpio |>
  pivot_longer(
    cols      = matches("_t[01]$"),
    names_to  = c(".value", "tiempo"),
    names_pattern = "^(.+)_(t[01])$"
  )
```

**Ejemplo completo:**
```r
lista_bases <- list(toybase_individual_2016_03, toybase_individual_2016_04)
pool_trimestral <- organize_panels(
  bases     = lista_bases,
  variables = c("P21", "ESTADO"),
  window    = "trimestral"
)
```

---

### `organize_cno()` — Clasificador de Ocupaciones

Clasifica las ocupaciones según las 4 dimensiones del CNO 2001. Agrega 4 columnas nuevas.

```r
organize_cno(base)  # base individual de uno o más periodos
```

**IMPORTANTE:** Verificar que el CNO 2001 sea compatible con la base utilizada.

**Retorna:** base con 4 columnas nuevas (carácter, jerarquía, tecnología, calificación del CNO).

**Variable de entrada:** `PP04D_COD` — código de ocupación de 5 dígitos en microdatos EPH.

**Ejemplo:**
```r
bases <- dplyr::bind_rows(toybase_individual_2016_03, toybase_individual_2016_04)
bases_clasificadas <- organize_cno(base = bases)
```

---

### `organize_caes()` — Clasificador de Actividades

Clasifica las actividades económicas según CAES Mercosur 1.0 (actualización 2018). Agrega 8 columnas nuevas.

```r
organize_caes(base)  # base individual de uno o más periodos
```

**IMPORTANTE:** Considerar los cambios de codificación entre versiones del CAES para series largas.

**Variable de entrada:** `PP04B_COD` — código de actividad económica (4 dígitos) en microdatos EPH.

**Retorna:** base con columnas: `caes_version`, `PP04B_COD`, `PP04B_label`, `caes_seccion_cod`, `caes_seccion_label`, `caes_division_cod`, `caes_division_label`, `caes_eph_cod`, `caes_eph_label`.

**Ejemplo:**
```r
bases <- dplyr::bind_rows(toybase_individual_2016_03, toybase_individual_2016_04)
bases_clasificadas <- organize_caes(base = bases)
```

---

### `map_agglomerates()` — Mapa de indicadores

Genera un mapa interactivo (leaflet) de indicadores por aglomerado.

```r
map_agglomerates(
  .data        ,            # dataframe con datos
  agglomerates ,            # variable con códigos de aglomerado
  indicator    ,            # variable con los indicadores
  alpha        = 0.75,      # opacidad de los puntos
  palette      = "viridis"  # "viridis", "magma", "inferno", "plasma"
)
```

**Ejemplo:**
```r
toybase_individual_2016_04 %>%
  dplyr::group_by(AGLOMERADO) %>%
  dplyr::summarise(tasa_actividad = sum(PONDERA[ESTADO == 1]) / sum(PONDERA)) %>%
  map_agglomerates(
    agglomerates = AGLOMERADO,
    indicator    = tasa_actividad
  )
```

---

## Datasets incluidos

| Dataset | Descripción | Filas × Cols |
|---------|-------------|--------------|
| `adulto_equivalente` | Valores de adulto equivalente por sexo (CH04) y edad (CH06). Campo `adequi`. | 222 × 3 |
| `caes` | Clasificador CAES Mercosur 1.0. Variable EPH: `PP04B_COD` (4 dígitos). | 140 × 8 |
| `CNO` | Categorías de las 4 dimensiones del CNO 2001. | 63 × 4 |
| `diccionario_aglomerados` | Códigos y nombres de 32 aglomerados EPH. | 32 × 2 |
| `diccionario_regiones` | Códigos y nombres de 6 regiones EPH. | 6 × 2 |
| `errores_muestrales` | Errores muestrales INDEC para EPH continua desde 2T2003. | 1687 × 5 |
| `canastas_reg_example` | Canastas básicas por región y trimestre (formato para `calculate_poverty`). | 12 × 5 |
| `centroides_aglomerados` | Latitud y longitud de los 32 aglomerados EPH. | 32 × 4 |

### Estructura de `CNO` (dataset)

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `digit` | character | Dígito que identifica la dimensión |
| `value` | integer | Valor que toma la categoría dentro de esa dimensión |
| `label` | character | Nombre de la categoría |
| `variable` | character | Nombre de la dimensión del CNO |

### Estructura de `caes` (dataset)

| Campo | Descripción |
|-------|-------------|
| `PP04B_COD` | Código clase CAES (4 dígitos) — variable en microdatos EPH |
| `PP04B_label` | Etiqueta clase CAES |
| `caes_seccion_cod` | Código sección (2 dígitos, nivel 2) |
| `caes_seccion_label` | Etiqueta sección |
| `caes_division_cod` | Código división (letra, nivel 1) |
| `caes_division_label` | Etiqueta división |
| `caes_eph_cod` | Código reagrupamiento EPH (nivel 1) |
| `caes_eph_label` | Etiqueta reagrupamiento EPH |

---

## Bases de prueba (toybase)

| Dataset | Descripción |
|---------|-------------|
| `toybase_individual_2016_03` | 2000 casos de la base individual 2016 T3 (177 variables) |
| `toybase_individual_2016_04` | 2000 casos de la base individual 2016 T4 (177 variables) |
| `toybase_hogar_2016_04` | 2000 casos de la base hogar 2016 T4 (177 variables) |

Estas bases tienen exactamente la misma estructura que las bases reales descargables con `get_microdata()`.

---

## Workflow típico completo

```r
library(eph)
library(dplyr)

# 1. Descargar datos
base <- get_microdata(year = 2023, period = 2, type = "individual")

# 2. Etiquetar variables
base <- organize_labels(base, type = "individual")

# 3. Calcular indicadores de mercado laboral
calculate_tabulates(base, x = "ESTADO", weights = "PONDERA", add.totals = "row")

# 4. Clasificar ocupaciones
base_con_cno <- organize_cno(base)

# 5. Calcular pobreza
canastas <- get_poverty_lines(regional = TRUE)
base_pobreza <- calculate_poverty(base = base, basket = canastas)

# 6. Panel de datos (dos trimestres consecutivos)
base_t1 <- get_microdata(year = 2023, period = 1, type = "individual")
base_t2 <- get_microdata(year = 2023, period = 2, type = "individual")
panel <- organize_panels(
  bases     = list(base_t1, base_t2),
  variables = c("P21", "ESTADO", "CAT_OCUP"),
  window    = "trimestral"
)
```
