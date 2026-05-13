# ¿Qué es la EPH?

## La encuesta

La **Encuesta Permanente de Hogares (EPH)** es la principal fuente de datos sobre el mercado de trabajo y los ingresos de los hogares en Argentina. La realiza el **INDEC** (Instituto Nacional de Estadística y Censos), que es el organismo oficial del Estado argentino encargado de producir estadísticas públicas.

La EPH se hace **cuatro veces por año** (un trimestre = tres meses). Cada trimestre, encuestadores visitan hogares en 31 aglomerados urbanos de todo el país y hacen preguntas sobre empleo, desempleo, ingresos, características del hogar y condiciones de vida.

## ¿Qué mide?

La EPH permite conocer:

- **Cuánta gente trabaja** y cuánta no puede encontrar trabajo
- **Cuánto ganan** los trabajadores según su ocupación, sector o nivel educativo
- **Quiénes son informales**: trabajadores sin descuento jubilatorio, sin obra social
- **Características de los hogares**: cuántas personas viven, quién es el jefe, qué nivel educativo tienen
- **Ingresos no laborales**: jubilaciones, pensiones, planes sociales

## Los indicadores más conocidos

| Indicador | Qué mide |
|:---|:---|
| Tasa de actividad | % de personas en edad de trabajar que trabajan o buscan trabajo |
| Tasa de empleo | % de personas en edad de trabajar que tienen trabajo |
| Tasa de desocupación | % de los activos que no tienen trabajo pero lo buscan |
| Tasa de subocupación | % de los activos que trabajan menos de 35 horas y quieren trabajar más |
| Informalidad laboral | % de asalariados sin aportes jubilatorios |

## Cobertura geográfica

La EPH **no cubre todo el país** — solo los 31 aglomerados urbanos más grandes. Eso representa aproximadamente el 70% de la población urbana argentina. Las zonas rurales y ciudades pequeñas no están incluidas.

Además del EPH trimestral (31 aglomerados), el INDEC publica una vez por año el **EPH Total Urbano**, que amplía la cobertura a más localidades.

## Los microdatos

Cuando los investigadores, periodistas o analistas quieren hacer sus propios cálculos, el INDEC publica los **microdatos**: las respuestas anonimizadas de cada hogar y cada persona encuestada. Son archivos de texto (.txt) que se pueden abrir con R o Python.

Hay dos bases por trimestre:
- `usu_hogar_TXTYYYY.txt` — una fila por hogar
- `usu_individual_TXTYYYY.txt` — una fila por persona

Para analizarlos correctamente hace falta conocer el **diseño de registro**: el diccionario que explica qué significa cada columna, qué valores puede tomar y cómo están codificados.

## Quiebre metodológico en 4T2023

En el cuarto trimestre de 2023, el INDEC cambió el cuestionario. Algunas variables desaparecieron, otras se dividieron en varias, y aparecieron preguntas nuevas. Esto significa que las series de tiempo que cruzan ese período necesitan un tratamiento especial para ser comparables.

## Más información

- Microdatos y documentación oficial: [indec.gob.ar](https://www.indec.gob.ar/indec/web/Institucional-Indec-BasesDeDatos)
- Paquete R para trabajar con EPH: [github.com/ropensci/eph](https://github.com/ropensci/eph)
- Librería Python: [github.com/institutohumai/pyeph](https://github.com/institutohumai/pyeph)
