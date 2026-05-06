# Librería `pyeph` para Python — Referencia Completa

**Repositorio:** https://github.com/institutohumai/pyeph
**Documentación:** https://pyeph.readthedocs.io/es/latest/
**PyPI:** `pip install pyeph`
**Cita:** Trogliero, Valdez & Gaska (2022). DOI: 10.5281/zenodo.6727908

## Instalación

```bash
pip install pyeph
```

## Importación

```python
import pyeph
```

---

## Módulo `get` — Descarga de datos

### `pyeph.get()` / `pyeph.obtener()`

Función unificada para obtener datos de la EPH y sus auxiliares.

```python
pyeph.get(
    data,        # str: qué datos descargar (ver tabla abajo)
    *args,
    **kwargs
)
# Alias en español:
pyeph.obtener(data, *args, **kwargs)
```

**Valores de `data`:**

| `data` | Alias | Descripción |
|--------|-------|-------------|
| `"eph"` | `"microdata"` | Microdatos EPH (individual u hogar) |
| `"canastas"` | `"basket"` | Canasta básica alimentaria y total |
| `"adulto-equivalente"` | `"equivalent-adult"` | Tabla de adulto equivalente |

**Retorna:** `pandas.DataFrame`

---

### Descarga de microdatos EPH

```python
# EPH individual (continua, trimestral)
eph = pyeph.get(
    data      = "eph",
    year      = 2021,       # int: año
    period    = 2,          # int: trimestre (1-4) o onda (1-2)
    freq      = "trimestre",# "trimestre" (EPH continua 2004+) o "onda" (EPH puntual hasta 2003)
    base_type = "individual"# "individual" o "hogar"
)

# Alias en español
eph = pyeph.obtener(
    data      = "eph",
    ano       = 2021,
    periodo   = 2,
    frecuencia = "trimestre",
    tipo_base = "individual"
)
```

**Validaciones automáticas:**
- `year <= 2003` requiere `freq = "onda"`
- `year >= 2004` requiere `freq = "trimestre"`
- 2007 T3: no existe (levantamiento no realizado)
- 2015 T3, T4 y 2016 T1: no existen (emergencia estadística)
- 2007–2015: emite warning por cambios metodológicos

**Ejemplo:**
```python
eph_ind = pyeph.get(data="eph", year=2023, period=2, base_type="individual")
eph_hog = pyeph.get(data="eph", year=2023, period=2, base_type="hogar")
```

---

### Descarga de canastas básicas

```python
basket = pyeph.get(data="canastas")
# o
basket = pyeph.obtener(data="canastas")
```

Retorna CBA (Canasta Básica Alimentaria) y CBT (Canasta Básica Total) por región y período.

---

### Descarga de adulto equivalente

```python
adulto_eq = pyeph.get(data="adulto-equivalente")
```

Retorna tabla con valores de adulto equivalente por sexo (`CH04`) y edad (`CH06`). Campo resultante: `adequi`.

---

## Módulo `calc` — Cálculos

### `pyeph.Poverty` / `pyeph.Pobreza` — Pobreza e Indigencia

```python
poverty = pyeph.Poverty(
    eph    = eph_df,    # pandas.DataFrame: base individual
    basket = None       # pandas.DataFrame opcional: canasta; si None, descarga automáticamente
)

# Alias en español
pobreza = pyeph.Pobreza(eph=eph_df, canasta=basket_df)
```

#### Métodos

**`.population(group_by=[])` / `.poblacion(agrupar_por=[])`**

Calcula tasa de pobreza e indigencia a nivel de personas.

```python
# Sin agrupación
result = poverty.population()

# Agrupado por sexo (CH04)
result = poverty.population(group_by='CH04')

# En español
result = pobreza.poblacion(agrupar_por='CH04')
```

**Retorna:** DataFrame con tasas (%) y cantidades (#) para Pobreza e Indigencia.

**`.household()` / `.hogares()`**

Calcula tasa de pobreza e indigencia a nivel de hogares.

```python
result = poverty.household()
# En español
result = pobreza.hogares()
```

**Ejemplo completo:**
```python
import pyeph

eph    = pyeph.get(data="eph", year=2021, period=2, base_type="individual")
basket = pyeph.get(data="canastas")

poverty = pyeph.Poverty(eph, basket)

# Pobreza por sexo (% y cantidad)
pop_poverty = poverty.population(group_by='CH04')

# Pobreza de hogares
hh_poverty = poverty.household()

# Etiquetado
labeled = pyeph.map_labels(pop_poverty)
```

---

### `pyeph.LaborMarket` / `pyeph.MercadoLaboral` — Mercado Laboral

```python
labor_market = pyeph.LaborMarket(
    eph = eph_df    # pandas.DataFrame: base individual
)

# Alias en español
mercado_laboral = pyeph.MercadoLaboral(eph=eph_df)
```

**Variable clave:** `ESTADO` — condición de actividad
- `1` = Ocupado
- `2` = Desocupado
- `3` = Inactivo

#### Métodos

**`.unemployment(group_by=[], div_by="PET")` / `.desempleo()`**

Tasa de desempleo = desocupados / PEA (o PET según `div_by`).

```python
# Desempleo total
unemp = labor_market.unemployment()

# Agrupado por región
unemp = labor_market.unemployment(group_by="REGION")

# Dividir por PEA (Población Económicamente Activa, default) o PT (Población Total)
unemp = labor_market.unemployment(group_by="REGION", div_by="PET")

# En español
desempleo = mercado_laboral.desempleo(agrupar_por="REGION", div_por="PET")
```

**`div_by` / `div_por`:**
- `"PET"` — Población en Edad de Trabajar (≥ 14 años) — default para desempleo
- `"PT"` — Población Total — default para empleo y actividad

**`.employment(group_by=[], div_by="PT")` / `.empleo()`**

Tasa de empleo = ocupados / PT (o PET).

```python
emp = labor_market.employment(group_by="CH04")  # por sexo
# En español
empleo = mercado_laboral.empleo(agrupar_por="CH04")
```

**`.activity(group_by=[], div_by="PT")` / `.actividad()`**

Tasa de actividad = PEA / PT (o PET).

```python
act = labor_market.activity(group_by="REGION")
# En español
actividad = mercado_laboral.actividad(agrupar_por="REGION")
```

**Ejemplo completo:**
```python
import pyeph

eph = pyeph.get(data="eph", year=2023, period=2, base_type="individual")
lm  = pyeph.LaborMarket(eph)

# Tasas globales
tasa_desempleo = lm.unemployment()
tasa_empleo    = lm.employment()
tasa_actividad = lm.activity()

# Por región
unemp_region = lm.unemployment(group_by="REGION", div_by="PT")

# Etiquetado
labeled = pyeph.map_labels(unemp_region)
```

---

### `pyeph.Dwelling` / `pyeph.Vivienda` — Vivienda

```python
dwelling = pyeph.Dwelling(
    eph_individual = eph_ind_df,  # base individual
    eph_hogar      = eph_hog_df   # base hogar
)
```

#### Métodos

**`.agregar_habitantes_hogar(column_name="HAB_HOG")`**

Agrega columna con tamaño del hogar (cantidad de componentes).

```python
dwelling.agregar_habitantes_hogar()
```

**`.get_media_attr_hogar_by_tipo_prop(attr, aglomerado=None)`**

Retorna la media de un atributo de hogar para propietarios vs inquilinos.

```python
# Variable EPH directa
result = dwelling.get_media_attr_hogar_by_tipo_prop("ITF")
# {'propietarios': 45000.5, 'inquilinos': 32000.2}

# Alias descriptivos disponibles
# attr="ingreso_total_familiar" → ITF
# attr="dormitorios"           → II2

# Filtrado por aglomerado
result = dwelling.get_media_attr_hogar_by_tipo_prop("ITF", aglomerado=32)
```

**Variable `II7` (tenencia):**
- Propietarios: valores 1, 2, 8
- Inquilinos/otros: valores 3, 4, 5, 6, 7

**Ejemplo:**
```python
import pyeph

eph_ind = pyeph.get(data="eph", year=2023, period=2, base_type="individual")
eph_hog = pyeph.get(data="eph", year=2023, period=2, base_type="hogar")

dw = pyeph.Dwelling(eph_ind, eph_hog)
dw.agregar_habitantes_hogar()
media_por_tenencia = dw.get_media_attr_hogar_by_tipo_prop("ingreso_total_familiar")
```

---

## Módulo `tools` — Utilidades

### `pyeph.map_labels()` / `pyeph.etiquetar()`

Etiqueta variables de la EPH con sus descripciones oficiales.

```python
labeled_df = pyeph.map_labels(df)

# Alias en español
labeled_df = pyeph.etiquetar(df)
```

**Ejemplo:**
```python
eph = pyeph.get(data="eph", year=2021, period=2)
result = pyeph.LaborMarket(eph).unemployment(group_by="REGION")
result_labeled = pyeph.map_labels(result)
```

---

### `pyeph.merge()` / `pyeph.aparear()`

Fusiona bases individual y hogar de EPH usando las claves correctas (`CODUSU`, `NRO_HOGAR`).

```python
base_completa = pyeph.merge(eph_individual, eph_hogar)
# Alias
base_completa = pyeph.aparear(eph_individual, eph_hogar)
```

---

## Resumen de la API pública

```python
# DESCARGA
pyeph.get(data, ...)        # obtener(data, ...)
pyeph.obtener(data, ...)    # alias español

# CÁLCULOS
pyeph.Poverty(eph, basket)               # Pobreza(eph, canasta)
  .population(group_by)                  # .poblacion(agrupar_por)
  .household()                           # .hogares()

pyeph.LaborMarket(eph)                   # MercadoLaboral(eph)
  .unemployment(group_by, div_by)        # .desempleo(agrupar_por, div_por)
  .employment(group_by, div_by)          # .empleo(agrupar_por, div_por)
  .activity(group_by, div_by)            # .actividad(agrupar_por, div_por)

pyeph.Dwelling(eph_individual, eph_hogar)  # Vivienda(...)
  .agregar_habitantes_hogar()
  .get_media_attr_hogar_by_tipo_prop(attr, aglomerado)

# HERRAMIENTAS
pyeph.map_labels(df)         # etiquetar(df)
pyeph.merge(ind, hog)        # aparear(ind, hog)
```

---

## Workflow típico completo

```python
import pyeph

# 1. Descargar datos
eph    = pyeph.get(data="eph", year=2023, period=2, base_type="individual")
basket = pyeph.get(data="canastas")

# 2. Mercado laboral
lm = pyeph.LaborMarket(eph)
desempleo = lm.unemployment(group_by="REGION", div_by="PET")
empleo    = lm.employment(group_by="CH04")
actividad = lm.activity()

# 3. Pobreza
pov = pyeph.Poverty(eph, basket)
pob_personas = pov.population(group_by='CH04')
pob_hogares  = pov.household()

# 4. Etiquetar resultados
desempleo_etiquetado = pyeph.map_labels(desempleo)

# 5. Vivienda (requiere ambas bases)
eph_hog = pyeph.get(data="eph", year=2023, period=2, base_type="hogar")
dw = pyeph.Dwelling(eph, eph_hog)
prop_vs_inqui = dw.get_media_attr_hogar_by_tipo_prop("ingreso_total_familiar")
```

---

## Notas importantes

- **Doble API (español/inglés):** Todos los métodos tienen alias en español (`Pobreza`, `MercadoLaboral`, `obtener`, `agrupar_por`, etc.)
- **EPH puntual (hasta 2003):** usar `freq="onda"` y `period` en 1-2
- **EPH continua (2004+):** usar `freq="trimestre"` y `period` en 1-4
- **Bases faltantes:** el paquete lanza `NonExistentDBError` para períodos que no existen (2007T3, 2015T3-T4, 2016T1)
- **PONDERA vs PONDIH:** Poverty usa `PONDIH` si existe (ponderador de ingreso), sino `PONDERA`
- **Notebook de ejemplo:** https://colab.research.google.com/github/institutohumai/pyeph/blob/main/examples.ipynb
