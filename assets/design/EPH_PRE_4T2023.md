EPH 3T2019 — Extracción a TXT del diseño de registro
Fuente: EPH_registro_3t19.pdf

BASE HOGAR

### Identificación
|Campo|Tipo|Descripción|
|---|---|---|
|CODUSU|C(29)|Código para distinguir VIVIENDAS, permite aparearlas con Hogares y Personas. Además permite hacer el seguimiento a través de los trimestres.|
|NRO_HOGAR|N(1)|Código para distinguir HOGARES, permite aparearlos con Personas.|
|REALIZADA|N(1)|Entrevista realizada. = Sí / = No (hogar no respuesta)|
|ANO4|N(4)|Año de relevamiento (4 dígitos).|
|TRIMESTRE|N(1)|Ventana de observación. 1=1er trimestre; 2=2do trimestre; 3=3er trimestre; 4=4to trimestre.|
|REGION|N(2)|Código de región. 01=Gran Buenos Aires; 40=NOA; 41=NEA; 42=Cuyo; 43=Pampeana; 44=Patagonia.|
|MAS_500|C(1)|Aglomerados según tamaño. N=Conjunto de aglomerados de menos de 500.000 hab.; S=Conjunto de aglomerados de 500.000 y más hab.|
|AGLOMERADO|N(2)|Código de aglomerado. 02=Gran La Plata; 03=Bahía Blanca-Cerri; 04=Gran Rosario; 05=Gran Santa Fé; 06=Gran Paraná; 07=Posadas; 08=Gran Resistencia; 09=Cdro. Rivadavia-R.Tilly; 10=Gran Mendoza; 12=Corrientes; 13=Gran Córdoba; 14=Concordia; 15=Formosa; 17=Neuquén-Plottier; 18=S. del Estero-La Banda; 19=Jujuy-Palpalá; 20=Río Gallegos; 22=Gran Catamarca; 23=Salta; 25=La Rioja; 26=San Luis-El Chorrillo; 27=Gran San Juan; 29=Gran Tucumán-T. Viejo; 30=Santa Rosa-Toay; 31=Ushuaia-Río Grande; 32=Ciudad de Bs As; 33=Partidos del GBA; 34=Mar del Plata-Batán; 36=Río Cuarto; 38=San Nicolás-Villa Constitución; 91=Rawson-Trelew; 93=Viedma-Carmen de Patagones.|
|PONDERA|N(6)|Ponderación.|

### Características de la vivienda
|Campo|Tipo|Descripción|
|---|---|---|
|IV1|N(1)|Tipo de vivienda (por observación). 1=Casa; 2=Departamento; 3=Pieza de inquilinato; 4=Pieza en hotel/pensión; 5=Local no construido para habitación; 6=Otros.|
|IV1_ESP|C(45)|Otros. Especificar.|
|IV2|N(2)|Cantidad de ambientes/habitaciones de la vivienda en total (sin contar baño/s, cocina, pasillo/s, lavadero, garage).|
|IV3|N(1)|Material predominante de los pisos interiores. 1=Mosaico/baldosa/madera/cerámica/alfombra; 2=Cemento/ladrillo fijo; 3=Ladrillo suelto/tierra; 4=Otros.|
|IV3_ESP|C(45)|Otros. Especificar.|
|IV4|N(2)|Cubierta exterior del techo. 1=Membrana/cubierta asfáltica; 2=Baldosa/losa sin cubierta; 3=Pizarra/teja; 4=Chapa de metal sin cubierta; 5=Chapa de fibrocemento/plástico; 6=Chapa de cartón; 7=Caña/tabla/paja con barro/paja sola; 9=N/S depto. en propiedad horizontal.|
|IV5|N(1)|El techo tiene cielorraso/revestimiento interior. 1=Sí; 2=No.|
|IV6|N(1)|Tiene agua. 1=Por cañería dentro de la vivienda; 2=Fuera de la vivienda pero dentro del terreno; 3=Fuera del terreno.|
|IV7|N(1)|Origen del agua. 1=Red pública; 2=Perforación con bomba a motor; 3=Perforación con bomba manual; 4=Otra fuente.|
|IV7_ESP|C(45)|Otra fuente. Especificar.|
|IV8|N(1)|Tiene baño/letrina. 1=Sí; 2=No.|
|IV9|N(1)|Ubicación del baño/letrina. 1=Dentro de la vivienda; 2=Fuera de la vivienda pero dentro del terreno; 3=Fuera del terreno.|
|IV10|N(1)|Tipo de baño. 1=Inodoro con botón/mochila/cadena y arrastre de agua; 2=Inodoro sin botón/cadena y con arrastre de agua (a balde); 3=Letrina.|
|IV11|N(1)|Desagüe del baño. 1=A red pública; 2=A cámara séptica y pozo ciego; 3=Sólo a pozo ciego; 4=A hoyo/excavación en la tierra.|
|IV12_1|N(1)|Vivienda ubicada cerca de basural/es (3 cuadras o menos). 1=Sí; 2=No.|
|IV12_2|N(1)|Vivienda ubicada en zona inundable (en los últimos 12 meses). 1=Sí; 2=No.|
|IV12_3|N(1)|Vivienda ubicada en villa de emergencia (por observación). 1=Sí; 2=No.|

### Características habitacionales del hogar
|Campo|Tipo|Descripción|
|---|---|---|
|II1|N(2)|Cantidad de ambientes/habitaciones de uso exclusivo del hogar.|
|II2|N(2)|De esos, cuántos usan habitualmente para dormir.|
|II3|N(1)|Utiliza alguno exclusivamente como lugar de trabajo. 1=Sí; 2=No.|
|II3_1|N(1)|Si utiliza alguno exclusivamente como lugar de trabajo, cuántos.|
|II4_1|N(1)|Tiene cuarto de cocina. 1=Sí; 2=No.|
|II4_2|N(1)|Tiene lavadero. 1=Sí; 2=No.|
|II4_3|N(1)|Tiene garage. 1=Sí; 2=No.|
|II5|N(1)|De esos, usan alguno para dormir. 1=Sí; 2=No.|
|II5_1|N(2)|Si utiliza alguno para dormir, cuántos.|
|II6|N(1)|De esos, utiliza alguno exclusivamente como lugar de trabajo. 1=Sí; 2=No.|
|II6_1|N(2)|Si utiliza alguno exclusivamente como lugar de trabajo, cuántos.|
|II7|N(2)|Régimen de tenencia. 01=Propietario de la vivienda y el terreno; 02=Propietario de la vivienda solamente; 03=Inquilino/arrendatario; 04=Ocupante por pago de impuestos/expensas; 05=Ocupante en relación de dependencia; 06=Ocupante gratuito (con permiso); 07=Ocupante de hecho (sin permiso); 08=Está en sucesión; 09=Otra situación.|
|II7_ESP|C(45)|Otra situación. Especificar.|
|II8|N(1)|Combustible utilizado para cocinar. 01=Gas de red; 02=Gas de tubo/garrafa; 03=Kerosene/leña/carbón; 04=Otro.|
|II8_ESP|C(45)|Otro. Especificar.|
|II9|N(1)|Baño (tenencia y uso). 01=Uso exclusivo del hogar; 02=Compartido con otro/s hogar/es de la misma vivienda; 03=Compartido con otra/s vivienda/s; 04=No tiene baño.|

### Estrategias del hogar
|Campo|Tipo|Descripción|
|---|---|---|
|V1|N(1)|En los últimos tres meses vivieron de lo que ganan en el trabajo. 1=Sí; 2=No.|
|V2|N(1)|Vivieron de alguna jubilación o pensión. 1=Sí; 2=No.|
|V21|N(1)|Aguinaldo de alguna jubilación o pensión cobrada el mes anterior. 1=Sí; 2=No.|
|V22|N(1)|Retroactivo de alguna jubilación o pensión cobrado el mes anterior. 1=Sí; 2=No.|
|V3|N(2)|Vivieron de indemnización por despido. 1=Sí; 2=No.|
|V4|N(1)|Vivieron de seguro de desempleo. 1=Sí; 2=No.|
|V5|N(1)|Vivieron de subsidio o ayuda social en dinero del gobierno, iglesias, etc. 1=Sí; 2=No.|
|V6|N(1)|Vivieron con mercaderías/ropa/alimentos del gobierno, iglesias, escuelas, etc. 1=Sí; 2=No.|
|V7|N(1)|Vivieron con mercaderías/ropa/alimentos de familiares, vecinos u otras personas que no viven en el hogar. 1=Sí; 2=No.|
|V8|N(1)|Vivieron de algún alquiler de su propiedad. 1=Sí; 2=No.|
|V9|N(1)|Vivieron de ganancias de algún negocio en el que no trabajan. 1=Sí; 2=No.|
|V10|N(1)|Vivieron de intereses o rentas por plazos fijos/inversiones. 1=Sí; 2=No.|
|V11|N(1)|Vivieron de una beca de estudio. 1=Sí; 2=No.|
|V12|N(1)|Vivieron de cuotas de alimentos o ayuda en dinero de personas que no viven en el hogar. 1=Sí; 2=No.|
|V13|N(1)|Vivieron de gastar lo que tenían ahorrado. 1=Sí; 2=No.|
|V14|N(1)|Vivieron de pedir préstamos a familiares/amigos. 1=Sí; 2=No.|
|V15|N(1)|Vivieron de pedir préstamos a bancos/financieras/etc. 1=Sí; 2=No.|
|V16|N(1)|Compran en cuotas o al fiado con tarjeta de crédito o libreta. 1=Sí; 2=No.|
|V17|N(1)|Han tenido que vender alguna de sus pertenencias. 1=Sí; 2=No.|
|V18|N(1)|Tuvieron otros ingresos en efectivo (limosnas, juegos de azar, etc.). 1=Sí; 2=No.|
|V19_A|N(1)|Menores de 10 años ayudan con algún dinero trabajando. 1=Sí; 2=No.|
|V19_B|N(1)|Menores de 10 años ayudan con algún dinero pidiendo. 1=Sí; 2=No.|

### Resumen del hogar
|Campo|Tipo|Descripción|
|---|---|---|
|IX_TOT|N(2)|Cantidad de miembros del hogar.|
|IX_MEN10|N(2)|Cantidad de miembros del hogar menores de 10 años.|
|IX_MAYEQ10|N(2)|Cantidad de miembros del hogar de 10 y más años.|

### Ingreso total familiar
|Campo|Tipo|Descripción|
|---|---|---|
|ITF|N(12)|Monto de ingreso total familiar (ver Anexo I).|
|DECIFR|C(2)|Nº de decil del ingreso total del hogar del total EPH (ver Anexo I).|
|IDECIFR|C(2)|Nº de decil del ingreso total del hogar del interior (ver Anexo I).|
|RDECIFR|C(2)|Nº de decil del ingreso total del hogar de la región (ver Anexo I).|
|GDECIFR|C(2)|Nº de decil del ingreso total del hogar del conjunto de aglomerados de 500 mil y más habitantes (ver Anexo I).|
|PDECIFR|C(2)|Nº de decil del ingreso total del hogar del conjunto de aglomerados de menos de 500 mil habitantes (ver Anexo I).|
|ADECIFR|C(2)|Nº de decil del ingreso total del hogar del aglomerado (ver Anexo I).|

### Ingreso per cápita familiar
|Campo|Tipo|Descripción|
|---|---|---|
|IPCF|N(12)|Monto de ingreso per cápita familiar (ver Anexo I).|
|DECCFR|C(2)|Nº de decil del ingreso per cápita familiar del total EPH (ver Anexo I).|
|IDECCFR|C(2)|Nº de decil del ingreso per cápita familiar del interior (ver Anexo I).|
|RDECCFR|C(2)|Nº de decil del ingreso per cápita familiar de la región (ver Anexo I).|
|GDECCFR|C(2)|Nº de decil del ingreso per cápita familiar del conjunto de aglomerados de 500 mil y más habitantes (ver Anexo I).|
|PDECCFR|C(2)|Nº de decil del ingreso per cápita familiar del conjunto de aglomerados de menos de 500 mil habitantes (ver Anexo I).|
|ADECCFR|C(2)|Nº de decil del ingreso per cápita familiar del aglomerado (ver Anexo I).|
|PONDIH|C(6)|Ponderador del ingreso total familiar y del ingreso per cápita familiar (ver Anexo I).|

### Organización del hogar
|Campo|Tipo|Descripción|
|---|---|---|
|VII1_1|N(2)|Realización de las tareas de la casa. Número de componente del hogar. 96=Servicio doméstico; 97=Otra persona que no vive en el hogar.|
|VII1_2|N(2)|Realización de las tareas de la casa. Número de componente del hogar. 96=Servicio doméstico; 97=Otra persona que no vive en el hogar.|
|VII2_1|N(2)|Otras personas que ayudan en las tareas de la casa. Número de componente del hogar. 96=Servicio doméstico; 97=Otra persona que no vive en el hogar; 98=Ninguna.|
|VII2_2|N(2)|Otras personas que ayudan en las tareas de la casa. Número de componente del hogar. 96=Servicio doméstico; 97=Otra persona que no vive en el hogar; 98=Ninguna.|
|VII2_3|N(2)|Otras personas que ayudan en las tareas de la casa. Número de componente del hogar. 96=Servicio doméstico; 97=Otra persona que no vive en el hogar; 98=Ninguna.|
|VII2_4|N(2)|Otras personas que ayudan en las tareas de la casa. Número de componente del hogar. 96=Servicio doméstico; 97=Otra persona que no vive en el hogar; 98=Ninguna.|

BASE PERSONAS

### Identificación
|Campo|Tipo|Descripción|
|---|---|---|
|CODUSU|C(29)|Código para distinguir viviendas; permite aparearlas con Hogares y Personas y hacer seguimiento a través de los trimestres.|
|NRO_HOGAR|N(2)|Código para distinguir hogares. 51=Servicio doméstico en hogares; 71=Pensionistas en hogares.|
|COMPONENTE|N(2)|Número de componente. Casos especiales: 51=Servicio doméstico en hogares; 71=Pensionistas en hogares.|
|H15|N(1)|Entrevista individual realizada. 1=Sí; 2=No.|
|ANO4|N(4)|Año de relevamiento (4 dígitos).|
|TRIMESTRE|N(1)|Ventana de observación. 1=1er trimestre; 2=2do trimestre; 3=3er trimestre; 4=4to trimestre.|
|REGION|N(2)|Código de región. 01=Gran Buenos Aires; 40=Noroeste; 41=Nordeste; 42=Cuyo; 43=Pampeana; 44=Patagónica.|
|MAS_500|C(1)|Aglomerados según tamaño. N=Menos de 500.000 hab.; S=500.000 y más hab.|
|AGLOMERADO|N(2)|Código de aglomerado. Mismo detalle de códigos que en base hogar.|
|PONDERA|N(6)|Ponderación.|

### Características de los miembros del hogar
|Campo|Tipo|Descripción|
|---|---|---|
|CH03|N(2)|Relación de parentesco. 01=Jefe/a; 02=Cónyuge/Pareja; 03=Hijo/Hijastro/a; 04=Yerno/Nuera; 05=Nieto/a; 06=Madre/Padre; 07=Suegro/a; 08=Hermano/a; 09=Otros familiares; 10=No familiares.|
|CH04|N(1)|Sexo. 1=Varón; 2=Mujer.|
|CH05|date|Fecha de nacimiento (día, mes y año).|
|CH06|N(2)|Edad en años cumplidos.|
|CH07|N(1)|Estado conyugal. 1=Unido; 2=Casado; 3=Separado/a o divorciado/a; 4=Viudo/a; 5=Soltero/a.|
|CH08|N(3)|Cobertura médica. 1=Obra social; 2=Mutual/Prepaga/Servicio de emergencia; 3=Planes y seguros públicos; 4=No paga ni le descuentan; 9=Ns./Nr.; 12=Obra social y mutual/prepaga; 13=Obra social y planes/seguros públicos; 23=Mutual/prepaga y planes/seguros públicos; 123=Obra social, mutual/prepaga y planes/seguros públicos.|
|CH09|N(1)|Sabe leer y escribir. 1=Sí; 2=No; 3=Menor de 2 años.|
|CH10|N(1)|Asiste o asistió a establecimiento educativo. 1=Sí, asiste; 2=No asiste, pero asistió; 3=Nunca asistió.|
|CH11|N(1)|Tipo de establecimiento. 1=Público; 2=Privado; 9=Ns./Nr.|
|CH12|N(2)|Nivel más alto que cursa o cursó. 1=Jardín/Preescolar; 2=Primario; 3=EGB; 4=Secundario; 5=Polimodal; 6=Terciario; 7=Universitario; 8=Posgrado Univ.; 9=Educación especial.|
|CH13|N(1)|Finalizó ese nivel. 1=Sí; 2=No; 9=Ns./Nr.|
|CH14|C(2)|Último año aprobado. 00=Ninguno; 01=Primero; 02=Segundo; 03=Tercero; 04=Cuarto; 05=Quinto; 06=Sexto; 07=Séptimo; 08=Octavo; 09=Noveno; 98=Educación especial; 99=Ns./Nr.|
|CH15|N(1)|Lugar de nacimiento. 1=En esta localidad; 2=En otra localidad de esta provincia; 3=En otra provincia; 4=En un país limítrofe; 5=En otro país; 9=Ns./Nr.|
|CH15_COD|C(3)|Código de especificación para CH15 cuando corresponde a otra provincia, país limítrofe u otro país.|
|CH16|N(1)|Dónde vivía hace 5 años. 1=En esta localidad; 2=En otra localidad de esta provincia; 3=En otra provincia; 4=En un país limítrofe; 5=En otro país; 6=No había nacido; 9=Ns./Nr.|
|CH16_COD|C(3)|Código de especificación para CH16 cuando corresponde.|
|NIVEL_ED|N(1)|Nivel educativo. 1=Primaria incompleta (incluye educación especial); 2=Primaria completa; 3=Secundaria incompleta; 4=Secundaria completa; 5=Superior universitaria incompleta; 6=Superior universitaria completa; 7=Sin instrucción; 9=Ns./Nr.|
|ESTADO|N(1)|Condición de actividad. 0=Entrevista individual no realizada; 1=Ocupado; 2=Desocupado; 3=Inactivo; 4=Menor de 10 años.|
|CAT_OCUP|N(1)|Categoría ocupacional. 1=Patrón; 2=Cuenta propia; 3=Obrero o empleado; 4=Trabajador familiar sin remuneración; 9=Ns./Nr.|
|CAT_INAC|N(1)|Categoría de inactividad. 1=Jubilado/Pensionado; 2=Rentista; 3=Estudiante; 4=Ama de casa; 5=Menor de 6 años; 6=Discapacitado; 7=Otros.|
|IMPUTA|N(1)|Indica los casos que han sido imputados.|

### Búsqueda de trabajo
|Campo|Tipo|Descripción|
|---|---|---|
|PP02C1|N(1)|Buscó trabajo haciendo contactos/entrevistas.|
|PP02C2|N(1)|Mandó currículum, puso o contestó avisos.|
|PP02C3|N(1)|Se presentó en establecimientos.|
|PP02C4|N(1)|Hizo algo para ponerse por su cuenta.|
|PP02C5|N(1)|Puso carteles en negocios, preguntó en el barrio.|
|PP02C6|N(1)|Consultó a parientes/amigos.|
|PP02C7|N(1)|Se anotó en bolsas, listas, planes de empleo, agencias, contratistas, o alguien le está buscando trabajo.|
|PP02C8|N(1)|Buscó de otra forma activa.|
|PP02E|N(1)|Durante esos 30 días no buscó trabajo porque. 1=Está suspendido; 2=Ya tiene trabajo asegurado; 3=Se cansó de buscar trabajo; 4=Hay poco trabajo en esta época del año; 5=Por otras razones.|
|PP02H|N(1)|En los últimos 12 meses buscó trabajo en algún momento. 1=Sí; 2=No.|
|PP02I|N(1)|En los últimos 12 meses trabajó en algún momento. 1=Sí; 2=No.|

### Ocupados que trabajaron en la semana de referencia
|Campo|Tipo|Descripción|
|---|---|---|
|PP03C|N(1)|Tenía un solo empleo o más de uno. 1=Un solo empleo; 2=Más de un empleo.|
|PP03D|N(1)|Cantidad de ocupaciones.|
|PP3E_TOT|N(5,1)|Total de horas trabajadas en la semana en la ocupación principal.|
|PP3F_TOT|N(5,1)|Total de horas trabajadas en la semana en otras ocupaciones.|
|PP03G|N(1)|Quería trabajar más horas. 1=Sí; 2=No.|
|PP03H|N(1)|Si hubiera conseguido más horas. 1=Podía trabajarlas esa semana; 2=Podía empezar en dos semanas a más tardar; 3=No podía trabajar más horas; 9=Ns./Nr.|

### Para todos los ocupados
|Campo|Tipo|Descripción|
|---|---|---|
|PP03I|N(1)|En los últimos treinta días buscó trabajar más horas. 1=Sí; 2=No; 9=Ns./Nr.|
|PP03J|N(1)|Aparte de este/os trabajo/s, estuvo buscando algún empleo/ocupación/actividad. 1=Sí; 2=No; 9=Ns./Nr.|
|INTENSI|N(1)|Intensidad de la ocupación. 1=Subocupado por insuficiencia horaria; 2=Ocupado pleno; 3=Sobreocupado; 4=Ocupado que no trabajó en la semana; 9=Ns./Nr.|

### Ocupación principal
|Campo|Tipo|Descripción|
|---|---|---|
|PP04A|N(1)|Tipo de negocio/empresa/institución/actividad donde trabaja. 1=Estatal; 2=Privada; 3=Otro tipo.|
|PP04B_COD|N(5)|Actividad del negocio/empresa/institución. Ver CAES-MERCOSUR.|
|PP04B1|N(1)|Si presta servicio doméstico en hogares particulares. 1=Casa de familia.|
|PP04B2|N(1)|En cuántas casas trabaja.|
|PP04B3_MES|N(2)|Tiempo que hace que trabaja allí: meses.|
|PP04B3_ANO|N(2)|Tiempo que hace que trabaja allí: años.|
|PP04B3_DIA|N(2)|Tiempo que hace que trabaja allí: días.|
|PP04C|N(2)|Cantidad de personas que trabajan allí en total. 1=1 persona; 2=2; 3=3; 4=4; 5=5; 6=6 a 10; 7=11 a 25; 8=26 a 40; 9=41 a 100; 10=101 a 200; 11=201 a 500; 12=más de 500; 99=Ns./Nr.|
|PP04C99|N(1)|Agrupación de tamaño. 1=Hasta 5; 2=De 6 a 40; 3=Más de 40; 9=Ns./Nr.|
|PP04D_COD|C(5)|Código de ocupación. Ver CNO 2001.|
|PP04G|N(2)|Lugar principal donde realiza tareas. 1=Local/oficina/establecimiento/negocio/taller/chacra/finca; 2=Puesto o kiosco fijo callejero; 3=Vehículos (no transporte); 4=Vehículo para transporte de personas o mercaderías; 5=Obras en construcción/infraestructura/minería; 6=En esta vivienda; 7=En la vivienda del socio o patrón; 8=En domicilio/local de clientes; 9=En la calle/espacios públicos/ambulante; 10=Otro lugar.|

### Ocupación principal de los trabajadores independientes
|Campo|Tipo|Descripción|
|---|---|---|
|PP05B2_MES|N(2)|Tiempo que trabaja en ese empleo en forma continua: meses.|
|PP05B2_ANO|N(2)|Tiempo que trabaja en ese empleo en forma continua: años.|
|PP05B2_DIA|N(2)|Tiempo que trabaja en ese empleo en forma continua: días.|
|PP05C_1|N(1)|Tiene maquinarias/equipos. 1=Propio; 2=Prestado/alquilado; 3=No tiene.|
|PP05C_2|N(1)|Tiene local. 1=Propio; 2=Prestado/alquilado; 3=No tiene.|
|PP05C_3|N(1)|Tiene vehículo. 1=Propio; 2=Prestado/alquilado; 3=No tiene.|
|PP05E|N(1)|En los últimos 3 meses tuvo gastos para la actividad. 1=Sí; 2=No.|
|PP05F|N(1)|Trabaja habitualmente para. 6=Un solo cliente; 7=Distintos clientes.|
|PP05H|N(1)|Antigüedad continua en ese empleo. 1=Menos de 1 mes; 2=1 a 3 meses; 3=Más de 3 a 6 meses; 4=Más de 6 meses a 1 año; 5=Más de 1 a 5 años; 6=Más de 5 años; 9=Ns./Nr.|

### Ingresos de la ocupación principal de los trabajadores independientes
|Campo|Tipo|Descripción|
|---|---|---|
|PP06A|N(1)|Tiene socios o familiares asociados. 1=Sí; 2=No.|
|PP06C|N(10)|Monto de ingreso de patrones y cuenta propia sin socios.|
|PP06D|N(10)|Monto de ingreso de patrones y cuenta propia con socios.|
|PP06E|N(1)|Forma societaria. 1=Sociedad jurídicamente constituida; 2=Sociedad de otra forma legal; 3=Sociedad convenida de palabra.|
|PP06H|N(10)|Actividad familiar (solo para 2 y 3 de PP06E). 1=Sí; 2=No.|

### Ocupación principal de los asalariados
|Campo|Tipo|Descripción|
|---|---|---|
|PP07A|N(1)|Antigüedad en el empleo. 1=Menos de 1 mes; 2=1 a 3 meses; 3=Más de 3 a 6 meses; 4=Más de 6 a 12 meses; 5=Más de 1 a 5 años; 6=Más de 5 años; 9=Ns./Nr.|
|PP07C|N(1)|Ese empleo tiene tiempo de finalización. 1=Sí; 2=No; 9=Ns./Nr.|
|PP07D|N(1)|Por cuánto tiempo es ese trabajo. 1=Sólo fue esa vez/sólo cuando lo llaman; 2=Hasta 3 meses; 3=Más de 3 a 6 meses; 4=Más de 6 a 12 meses; 5=Más de 1 año; 9=Ns./Nr.|
|PP07E|N(1)|Ese trabajo es. 1=Plan de empleo; 2=Período de prueba; 3=Beca/pasantía/aprendizaje; 4=Ninguno de éstos.|
|PP07F1|N(1)|Le dan de comer gratis en el lugar de trabajo. 1=Sí; 2=No.|
|PP07F2|N(1)|Le dan vivienda. 1=Sí; 2=No.|
|PP07F3|N(1)|Le dan algún producto o mercadería. 1=Sí; 2=No.|
|PP07F4|N(1)|Le dan algún otro beneficio. 1=Sí; 2=No.|
|PP07F5|N(1)|No recibe ninguno. 1=Sí.|
|PP07G1|N(1)|Tiene vacaciones pagas. 1=Sí; 2=No.|
|PP07G2|N(1)|Tiene aguinaldo. 1=Sí; 2=No.|
|PP07G3|N(1)|Tiene días pagos por enfermedad. 1=Sí; 2=No.|
|PP07G4|N(1)|Tiene obra social. 1=Sí; 2=No.|
|PP07G_59|N(1)|No tiene ninguno. 5=Sí.|
|PP07H|N(1)|Tiene descuento jubilatorio. 1=Sí; 2=No.|
|PP07I|N(1)|Aporta por sí mismo a algún sistema jubilatorio. 1=Sí; 2=No.|
|PP07J|N(1)|Turno habitual. 1=De día; 2=De noche; 3=Otro tipo.|
|PP07K|N(1)|Al cobrar. 1=Le dan recibo con sello/membrete/firma del empleador; 2=Le dan un papel/recibo sin nada; 3=Entrega una factura; 4=No le dan ni entrega nada; 5=No cobra, es trabajador sin pago/ad honorem.|

### Ingresos de la ocupación principal de los asalariados
|Campo|Tipo|Descripción|
|---|---|---|
|PP08D1|N(10)|Monto total de sueldos/jornales, salario familiar, horas extras, otras bonificaciones habituales y tickets/vales/similares.|
|PP08D4|N(10)|Monto percibido en tickets.|
|PP08F1|N(10)|Monto cobrado por comisión por venta/producción.|
|PP08F2|N(10)|Monto cobrado por propinas.|
|PP08J1|N(6)|Monto aguinaldo.|
|PP08J2|N(6)|Monto otras bonificaciones no habituales.|
|PP08J3|N(6)|Monto retroactivos.|

### Movimientos interurbanos
|Campo|Tipo|Descripción|
|---|---|---|
|PP09A|N(1)|Solo ocupados de Ciudad de Buenos Aires y Partidos del GBA: dónde trabaja. 1=Ciudad de Buenos Aires; 2=Partidos del GBA; 3=Ambos; 4=En otro lugar.|
|PP09A_ESP|C(90)|Especificación de otro lugar.|
|PP09B|N(1)|Solo ocupados de Posadas, Formosa, Corrientes, Resistencia, Santa Fe, Paraná y Neuquén: trabaja en esta ciudad. 1=Sí; 2=No.|
|PP09C|N(1)|Dónde trabaja. 1=En otro lugar de esta provincia; 2=En otra provincia; 3=En otro país.|
|PP09C_ESP|C(90)|Descripción de otro lugar según PP09C.|

### Desocupados
|Campo|Tipo|Descripción|
|---|---|---|
|PP10A|N(1)|Tiempo que está buscando trabajo. 1=Menos de 1 mes; 2=1 a 3 meses; 3=Más de 3 a 6 meses; 4=Más de 6 a 12 meses; 5=Más de 1 año.|
|PP10C|N(1)|Durante ese tiempo hizo algún trabajo/changa. 1=Sí; 2=No.|
|PP10D|N(1)|Ha trabajado alguna vez. 1=Sí; 2=No.|
|PP10E|N(1)|Tiempo desde que terminó su último trabajo/changa. 1=Menos de 1 mes; 2=1 a 3 meses; 3=Más de 3 a 6 meses; 4=Más de 6 a 12 meses; 5=Más de 1 a 3 años; 6=Más de 3 años.|

### Desocupados con empleo anterior
|Campo|Tipo|Descripción|
|---|---|---|
|PP11A|N(1)|El negocio/empresa/institución/actividad donde trabajaba era. 1=Estatal; 2=Privada; 3=Otro tipo.|
|PP11B_COD|N(5)|Actividad del negocio/empresa/institución anterior. Ver CAES-MERCOSUR.|
|PP11B1|N(1)|Si prestaba servicio doméstico en hogares particulares. 1=Casa de familia.|
|PP11B2_MES|N(2)|Tiempo trabajado allí: meses.|
|PP11B2_ANO|N(2)|Tiempo trabajado allí: años.|
|PP11B2_DIA|N(2)|Tiempo trabajado allí: días.|
|PP11C|N(2)|Cantidad de personas que trabajaban allí en total. 1=1; 2=2; 3=3; 4=4; 5=5; 6=6 a 10; 7=11 a 25; 8=26 a 40; 9=41 a 100; 10=101 a 200; 11=201 a 500; 12=Más de 500; 99=Ns./Nr.|
|PP11C99|N(1)|Agrupación de tamaño para PP11C=99. 1=Hasta 5; 2=De 6 a 40; 3=Más de 40; 9=Ns./Nr.|
|PP11D_COD|C(5)|Código de ocupación anterior. Ver CNO 2001.|
|PP11G_ANO|N(2)|Tiempo seguido que estuvo trabajando en ese lugar: años.|
|PP11G_MES|N(2)|Tiempo seguido que estuvo trabajando en ese lugar: meses.|
|PP11G_DIA|N(2)|Tiempo seguido que estuvo trabajando en ese lugar: días.|
|PP11L|N(1)|Razón principal por la que dejó esa actividad. 1=Falta de clientes/clientes que no pagan; 2=Falta de capital/equipamiento; 3=Trabajo estacional; 4=Gastos demasiado altos; 5=Otras causas laborales; 6=Jubilación/retiro; 7=Causas personales.|
|PP11L1|N(1)|Ese trabajo era. 1=Changa/trabajo transitorio/por tarea u obra/suplencia; 2=Trabajo permanente/fijo/estable/de planta; 3=Ns./Nr.|
|PP11M|N(1)|Ese trabajo era. 1=Plan de empleo; 2=Período de prueba; 3=Otro tipo de trabajo.|
|PP11N|N(1)|En ese trabajo le hacían descuento jubilatorio. 1=Sí; 2=No; 9=Ns./Nr.|
|PP11O|N(2)|Razón principal por la que dejó ese trabajo. 1=Despido/cierre; 2=Retiro voluntario del sector público; 3=Jubilación; 4=Fin de trabajo temporario/estacional; 5=Le pagaban poco/no le pagaban; 6=Malas relaciones laborales/malas condiciones de trabajo; 7=Renuncia obligada/pactada; 8=Otras causas laborales; 9=Razones personales.|
|PP11P|N(1)|Cerró la empresa. 1=Sí; 2=No; 9=Ns./Nr.|
|PP11Q|N(1)|Fue la única persona que quedó sin trabajo. 1=Sí; 2=No; 9=Ns./Nr.|
|PP11R|N(1)|Le enviaron telegrama. 1=Sí; 2=No.|
|PP11S|N(1)|Le pagaron indemnización. 1=Sí; 2=No.|
|PP11T|N(1)|Está cobrando seguro de desempleo. 1=Sí; 2=No; 9=Ns./Nr.|

### Ingresos de la ocupación principal
|Campo|Tipo|Descripción|
|---|---|---|
|P21|N(10)|Monto de ingreso de la ocupación principal.|
|DECOCUR|C(2)|Nº de decil de ingreso de la ocupación principal del total EPH.|
|IDECOCUR|C(2)|Nº de decil de ingreso de la ocupación principal del interior EPH.|
|RDECOCUR|C(2)|Nº de decil de ingreso de la ocupación principal de la región.|
|GDECOCUR|C(2)|Nº de decil de ingreso de la ocupación principal del conjunto de aglomerados de 500 mil y más habitantes.|
|PDECOCUR|C(2)|Nº de decil de ingreso de la ocupación principal del conjunto de aglomerados de menos de 500 mil habitantes.|
|ADECOCUR|C(2)|Nº de decil de ingreso de la ocupación principal del aglomerado.|
|PONDIIO|N(6)|Ponderador del ingreso de la ocupación principal.|

### Ingreso de otras ocupaciones
|Campo|Tipo|Descripción|
|---|---|---|
|TOT_P12|N(12)|Monto de ingreso de otras ocupaciones. Incluye ocupación secundaria, ocupación previa a la semana de referencia, deudas/retroactivos por ocupaciones anteriores al mes de referencia, etc.|

### Ingreso total individual
|Campo|Tipo|Descripción|
|---|---|---|
|P47T|N(10)|Monto de ingreso total individual (sumatoria de ingresos laborales y no laborales).|
|DECINDR|C(2)|Nº de decil de ingreso total individual del total EPH.|
|IDECINDR|C(2)|Nº de decil de ingreso total individual del interior EPH.|
|RDECINDR|C(2)|Nº de decil de ingreso total individual de la región.|
|GDECINDR|C(2)|Nº de decil de ingreso total individual del conjunto de aglomerados de 500 mil y más habitantes.|
|PDECINDR|C(2)|Nº de decil de ingreso total individual del conjunto de aglomerados de menos de 500 mil habitantes.|
|ADECINDR|C(2)|Nº de decil de ingreso total individual del aglomerado.|
|PONDII|N(6)|Ponderador para ingreso total individual.|

### Ingresos no laborales
|Campo|Tipo|Descripción|
|---|---|---|
|V2_M|N(6)|Monto del ingreso por jubilación o pensión.|
|V3_M|N(6)|Monto del ingreso por indemnización por despido.|
|V4_M|N(6)|Monto del ingreso por seguro de desempleo.|
|V5_M|N(6)|Monto del ingreso por subsidio o ayuda social en dinero.|
|V8_M|N(6)|Monto del ingreso por alquiler de su propiedad.|
|V9_M|N(6)|Monto del ingreso por ganancias de algún negocio en el que no trabajó.|
|V10_M|N(6)|Monto del ingreso por intereses o rentas por plazos fijos/inversiones.|
|V11_M|N(6)|Monto del ingreso por beca de estudio.|
|V12_M|N(6)|Monto del ingreso por cuotas de alimentos o ayuda en dinero de personas que no viven en el hogar.|
|V18_M|N(6)|Monto del ingreso por otros ingresos en efectivo.|
|V19_AM|N(6)|Monto del ingreso por trabajo de menores de 10 años.|
|V21_M|N(6)|Monto del ingreso por aguinaldo.|
|T_VI|N(12,4)|Monto total de ingresos no laborales.|

### Ingreso total familiar e IPCF en base personas
|Campo|Tipo|Descripción|
|---|---|---|
|ITF|N(12,2)|Monto del ingreso total familiar.|
|DECIFR|C(2)|Nº de decil de ingreso total familiar del total EPH.|
|IDECIFR|C(2)|Nº de decil de ingreso total familiar del interior EPH.|
|RDECIFR|C(2)|Nº de decil de ingreso total familiar de la región.|
|GDECIFR|C(2)|Nº de decil de ingreso total familiar del conjunto de aglomerados de 500 mil y más habitantes.|
|PDECIFR|C(2)|Nº de decil de ingreso total familiar del conjunto de aglomerados de menos de 500 mil habitantes.|
|ADECIFR|C(2)|Nº de decil de ingreso total familiar del aglomerado.|
|IPCF|N(12,2)|Monto del ingreso per cápita familiar.|
|DECCFR|C(2)|Nº de decil de ingreso per cápita familiar del total EPH.|
|IDECCFR|C(2)|Nº de decil de ingreso per cápita familiar del interior EPH.|
|RDECCFR|C(2)|Nº de decil de ingreso per cápita familiar de la región.|
|GDECCFR|C(2)|Nº de decil de ingreso per cápita familiar del conjunto de aglomerados de 500 mil y más habitantes.|
|PDECCFR|C(2)|Nº de decil de ingreso per cápita familiar del conjunto de aglomerados de menos de 500 mil habitantes.|
|ADECCFR|C(2)|Nº de decil de ingreso per cápita familiar del aglomerado.|
|PONDIH|N(6)|Ponderador del ingreso total familiar y del ingreso per cápita familiar, para hogares.|

ANEXO I — RECOMENDACIONES TÉCNICAS PARA EL USO DE LA INFORMACIÓN DE INGRESOS

### Montos de ingreso
- Se incluyen montos de ingreso captados en los cuestionarios y variables construidas por sumatoria de distintas fuentes: P21, P47T, ITF e IPCF.
- P21 agrega el total de ingresos habituales de la ocupación principal del individuo.
- P47T es la sumatoria de los ingresos laborales y no laborales del individuo.
- ITF es la sumatoria de los ingresos individuales totales de todos los componentes del hogar.
- IPCF es el ingreso per cápita del hogar, es decir, el ITF dividido por la cantidad de miembros del hogar.

### Escalas decílicas
Se incluyen las siguientes escalas:
- Ingreso total individual: DECINDR, ADECINDR, RDECINDR, PDECINDR, GDECINDR, IDECINDR.
- Ingreso de la ocupación principal: DECOCUR, ADECOCUR, RDECOCUR, PDECOCUR, GDECOCUR, IDECOCUR.
- Ingreso total familiar: DECIFR, ADECIFR, RDECIFR, PDECIFR, GDECIFR, IDECIFR.
- Ingreso per cápita familiar: DECCFR, ADECCFR, RDECCFR, PDECCFR, GDECCFR, IDECCFR.

Categorías de los deciles:
00 = Sin ingresos
1 = decil 1
2 = decil 2
3 = decil 3
4 = decil 4
5 = decil 5
6 = decil 6
7 = decil 7
8 = decil 8
9 = decil 9
10 = decil 10
12 = No respuesta de ingresos
13 = Entrevista individual no realizada

FACTORES DE EXPANSIÓN

- Para minimizar el efecto de la no respuesta de ingresos, a los no respondentes se les asignó el comportamiento de los respondentes por estrato de la muestra.
- Para ingresos y pobreza se presentan dos tipos de ponderadores:
1. PONDERA, sin corrección, que se utiliza además para el resto de las variables.
2. PONDII, PONDIIO y PONDIH, con corrección por no respuesta.

Detalle:
- PONDII: para ingreso total individual (P47T, DECINDR, ADECINDR, RDECINDR, PDECINDR, GDECINDR, IDECINDR).
- PONDIIO: para ingreso de la ocupación principal (P21, PP06C, PP06D, PP08D1, PP08D4, PP08F1, PP08F2, PP08J1, PP08J2, PP08J3, DECOCUR, ADECOCUR, RDECOCUR, PDECOCUR, GDECOCUR, IDECOCUR).
- PONDIH: para ingreso total familiar (ITF, DECIFR, ADECIFR, RDECIFR, PDECIFR, GDECIFR, IDECIFR) e ingreso per cápita familiar (IPCF, DECCFR, ADECCFR, RDECCFR, PDECCFR, GDECCFR, IDECCFR).

- Los campos de deciles se presentan calculados con estos ponderadores con corrección por no respuesta.
- El usuario también puede elaborar los deciles sin la corrección utilizando PONDERA y los campos de ingreso correspondientes.

COMENTARIOS GENERALES

- Los códigos 9, 99, 999, 9999 corresponden, salvo indicación en contrario, a la categoría No sabe/No responde.
- Excepción: en los montos de ingreso, la no respuesta se identifica con el código -9.
- Además, los montos captados en PP06C y PP06D presentan también:
-7 = No tenía esa ocupación en el mes de referencia.
-8 = No tuvo ingresos por el mes de referencia.
- El código 0 identifica los casos a los cuales no les corresponde la secuencia analizada.

FIN DEL ARCHIVO
