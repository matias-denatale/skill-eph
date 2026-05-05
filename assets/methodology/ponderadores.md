# Uso de factores de expansión (Ponderadores)

Según las clases oficiales del INDEC, la EPH es una encuesta muestral. Para obtener estimaciones poblacionales válidas es imprescindible ponderar los datos.

## ¿Qué ponderador utilizar?
- **`PONDERA`**: Ponderador poblacional a nivel INDIVIDUAL. Se utiliza para contar personas (ej: PEA, ocupados, desocupados, inactivos).
- **`PONDIH`**: Ponderador a nivel HOGAR. Se utiliza para contar hogares (ej: hogares bajo la línea de pobreza, hogares con NBI).
- **`PONDIIO`**: Ponderador específico para el Ingreso de la Ocupación Principal.

## Cómo calcular frecuencias absolutas
⚠️ **ERROR COMÚN:** Hacer `count()` o contar filas (n). Esto sólo da el número de encuestados en la muestra.
Se debe **sumar** el ponderador correspondiente a cada filtro.

### En R (basado en Curso R INDEC)
```R
library(dplyr)
library(questionr) # Recomendado por P. Tiscornia

# Opción 1: dplyr
datos %>% 
  group_by(ESTADO) %>% 
  summarise(poblacion = sum(PONDERA, na.rm = TRUE))

# Opción 2: questionr
wtd.table(datos$ESTADO, weights = datos$PONDERA)
```

## Cálculo de promedios
Para calcular un promedio representativo (por ejemplo, edad promedio), no se usa `mean()`, sino el promedio ponderado:

### En R
```R
datos %>% 
  summarise(Edad_prom = weighted.mean(EDAD, w = PONDERA, na.rm = TRUE))
```

### En Python (Pandas)
```python
import numpy as np
import pandas as pd

# Promedio ponderado
np.average(df['EDAD'], weights=df['PONDERA'])

# Población por estado
df.groupby('ESTADO')['PONDERA'].sum()
```