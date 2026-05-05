# Cálculo de Indicadores del Mercado Laboral

## Definición de `ESTADO`
La condición de actividad de las personas está resumida en la variable `ESTADO`:
- **1 = Ocupado:** Trabajó al menos una hora en la semana de referencia.
- **2 = Desocupado:** No trabajó, pero buscó activamente empleo y está disponible.
- **3 = Inactivo:** No trabajó y no buscó empleo.
- **4 = Menor de 10 años:** (Fuera del universo de análisis laboral).
- **0 = Entrevista individual no realizada.**

## Fórmulas Oficiales (INDEC)
⚠️ **ERROR FRECUENTE:** Usar el total de la población como denominador para la Tasa de Desocupación. El denominador correcto es la **Población Económicamente Activa (PEA)**.

- **Población Total (PT):** Suma de `PONDERA` de toda la base.
- **PEA:** Suma de `PONDERA` donde `ESTADO == 1` o `ESTADO == 2`.
- **Ocupados (O):** Suma de `PONDERA` donde `ESTADO == 1`.
- **Desocupados (D):** Suma de `PONDERA` donde `ESTADO == 2`.

1. **Tasa de Actividad (TA):** `(PEA / PT) * 100`
2. **Tasa de Empleo (TE):** `(O / PT) * 100`
3. **Tasa de Desocupación (TD):** `(D / PEA) * 100`

### Snippet R
```R
library(dplyr)

indicadores <- base_eph %>%
  summarise(
    Poblacion = sum(PONDERA),
    PEA = sum(PONDERA[ESTADO %in% c(1, 2)]),
    Ocupados = sum(PONDERA[ESTADO == 1]),
    Desocupados = sum(PONDERA[ESTADO == 2]),
    
    Tasa_Actividad = (PEA / Poblacion) * 100,
    Tasa_Empleo = (Ocupados / Poblacion) * 100,
    Tasa_Desocupacion = (Desocupados / PEA) * 100
  )
```