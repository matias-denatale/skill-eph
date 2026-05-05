# Construcción de Datos de Panel en EPH

La EPH posee un esquema de **panel rotante 2-2-2**: una vivienda es encuestada por 2 trimestres consecutivos, luego sale por 2 trimestres, y vuelve a entrar por sus últimos 2 trimestres consecutivos. Cada vivienda participa un máximo de 4 veces (ondas).

## Claves de Identificación
Para unir la misma persona a lo largo de trimestres, se debe hacer un cruce (*merge* o *join*) utilizando un conjunto de variables clave:
1. `CODUSU`: Código identificador de la vivienda.
2. `NRO_HOGAR`: Número de hogar dentro de esa vivienda.
3. `COMPONENTE`: Número de orden de la persona dentro de ese hogar.

## Prevención de Falsos Positivos
⚠️ **CRÍTICO:** La combinación `CODUSU`, `NRO_HOGAR` y `COMPONENTE` **NO ES INFALIBLE**. Las viviendas pueden sufrir rotación de inquilinos, fallecimientos o errores de carga. 

Para confirmar que es el **mismo individuo**, es OBLIGATORIO chequear variables demográficas invariantes:
- **Sexo (`CH04`)**: Debe ser idéntico en ambos trimestres.
- **Edad (`CH06`)**: La edad debe ser la misma, o a lo sumo tener +1 o +2 años de diferencia dependiendo de cuántos trimestres hayan pasado.

### Ejemplo de Panel (T1 y T2 consecutivos) en R
```R
library(dplyr)

panel_t1_t2 <- inner_join(
  base_t1, 
  base_t2, 
  by = c("CODUSU", "NRO_HOGAR", "COMPONENTE"),
  suffix = c("_t1", "_t2")
) %>%
  # Filtro de consistencia demográfica estricto
  filter(
    CH04_t1 == CH04_t2,
    CH06_t2 - CH06_t1 >= 0,
    CH06_t2 - CH06_t1 <= 1
  )
```