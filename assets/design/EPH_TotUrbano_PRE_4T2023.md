EPH Total Urbano 2024 — Extracción a TXT del diseño de registro
Fuente: EPH_tot_urbano_estructura_bases_2024.pdf

BASE HOGAR

### Identificación
|Campo|Tipo|Descripción|
|---|---|---|
|CODUSU|C(29)|Código para distinguir viviendas, permite aparearlas con Hogares y Personas. Además permite hacer el seguimiento a través de los trimestres.|
|NRO_HOGAR|N(1)|Código para distinguir Hogares, permite aparearlos con Personas.|
|REALIZADA|N(1)|Entrevista realizada = Sí = No (hogar no respuesta)|
|ANO4|N(4)|Año de relevamiento (4 dígitos)|
|TRIM|N(1)|Ventana de observación = 1° trimestre = 2° trimestre = 3° trimestre = 4° trimestre|
|AGLOMERADO|N(2)|Código de aglomerado 02 = Gran La Plata 03 = Bahía Blanca-Cerri 04 = Gran Rosario 05 = Gran Santa Fe 06 = Gran Paraná 07 = Posadas 08 = Gran Resistencia 09 = Comodoro Rivadavia-Rada Tilly 10 = Gran Mendoza 12 = Corrientes|
|PROVINCIA|N(2)|Código de provincia 02 = Ciudad de Buenos Aires 06 = Buenos Aires 10 = Catamarca 14 = Córdoba 18 = Corrientes 22 = Chaco 26 = Chubut 30 = Entre Ríos 34 = Formosa 38 = Jujuy 42 = La Pampa 46 = La Rioja 50 = Mendoza 54 = Misiones|
|PONDERA|N(6)|Ponderación|
### Características de la vivienda
|Campo|Tipo|Descripción|
|---|---|---|
|IV1|N(1)|Tipo de vivienda (por observación) 1. casa 2. departamento 3. pieza de inquilinato 4. pieza en hotel/pensión 5. local no construido para habitación|
|IV1_ESP|C(45)|6. otros, especificar:|
|IV2|N(2)|¿Cuántos ambientes/habitaciones tiene la vivienda en total? (sin contar baño/s, cocina, pasillo/s, lavadero, garage)|
|IV3|N(1)|Los pisos interiores son principalmente de… 1. mosaico/baldosa/madera/cerámica/alfombra 2. cemento/ladrillo fijo 3. ladrillo suelto/tierra|
|IV3_ESP|C(45)|4. otros, especificar:|
|IV4|N(2)|La cubierta exterior del techo es de 1. membrana/cubierta asfáltica 2. baldosa/losa sin cubierta 3. pizarra/teja|
### Identificación
|Campo|Tipo|Descripción|
|---|---|---|
|IV5|N(1)|¿El techo tiene cielorraso/revestimiento interior? 1 = Sí 2 = No|
|IV6|N(1)|Tiene agua 1. por cañería dentro de la vivienda 2. fuera de la vivienda pero dentro del terreno 3. fuera del terreno|
|IV7|N(1)|El agua es de 1. red pública (agua corriente) 2. perforación con bomba a motor 3. perforación con bomba manual|
|IV7_ESP|C(45)|4. otra fuente, especificar:|
|IV8|N(1)|¿Tiene baño/letrina? 1 = Sí 2 = No|
|IV9|N(1)|El baño o letrina está 1. dentro de la vivienda 2. fuera de la vivienda, pero dentro del terreno 3. fuera del terreno|
|IV10|N(1)|El baño tiene 1. inodoro con botón/mochila/cadena y arrastre de agua 2. inodoro sin botón/cadena y con arrastre de agua (a balde) 3. letrina (sin arrastre de agua)|
|IV11|N(1)|El desague del baño es 1. a red pública (cloaca)|
|IV12_1|N(1)|La vivienda está ubicada cerca de basural/es (3 cuadras o menos) 1 = Sí 2 = No|
|IV12_2|N(1)|La vivienda está ubicada en zona inundable (en los últimos 12 meses) 1 = Sí 2 = No|
|IV12_3|N(1)|La vivienda está ubicada en villa de emergencia (por observación) 1 = Sí 2 = No|
### Características habitacionales del hogar
|Campo|Tipo|Descripción|
|---|---|---|
|II1|N(2)|¿Cuántos ambientes/habitaciones tiene este hogar para su uso exclusivo?|
|II2|N(2)|De esos, ¿cuántos usan habitualmente para dormir?|
|II3|N(1)|Utiliza alguno exclusivamente como lugar de trabajo (para consultorio, estu- dio, taller, negocio, etc.) 1 = Sí 2 = No|
|II3_1|N(1)|Si utiliza alguno exclusivamente como lugar de trabajo, ¿cuántos?|
|II4|N(1)|Tiene además|
|II4_1|N(1)|cuarto de cocina 1 = Sí 2 = No|
|II4_2|N(1)|lavadero 1 = Sí 2 = No|
|II4_3|N(1)|garage 1 = Sí 2 = No|
### Identificación
|Campo|Tipo|Descripción|
|---|---|---|
|II5|N(1)|De esos (los sí de la pregunta 4) ¿usan alguno para dormir? 1 = Sí 2 = No|
|II5_1|N(2)|Si utiliza alguno para dormir, ¿cuántos?|
|II6|N(1)|De esos (los sí de la pregunta 4) utiliza alguno de estos exclusivamente como lugar de trabajo (consultorio, estudio, taller, negocio, etc.) 1 = Sí 2 = No|
|II7|N(2)|Régimen de tenencia 01 = Propietario de la vivienda y el terreno 02 = Propietario de la vivienda solamente 03 = Inquilino/arrendatario de la vivienda 04 = Ocupante por pago de impuestos/expensas 05 = Ocupante en relación de dependencia 06 = Ocupante gratuito (con permiso) 07 = Ocupante de hecho (sin permiso) 08 = Está en sucesión|
|II7_ESP|C(45)|09 = Otra situación (especificar)|
|II8|N(1)|Combustible utilizado para cocinar 01 = Gas de red 02 = Gas de tubo/garrafa 03 = Kerosene/leña/carbón|
|II8_ESP|C(45)|04 = Otro (especificar)|
|II9|N(1)|Baño (tenencia y uso) 01 = Uso exclusivo del hogar 02 = Compartido con otro/s hogar/es de la misma vivienda 03 = Compartido con otra/s vivienda/s 04 = No tiene baño|
### Estrategias del hogar
|Campo|Tipo|Descripción|
|---|---|---|
|V1|N(1)|de lo que ganan en el trabajo? 1 = Sí 2 = No|
|V2|N(1)|de alguna jubilación o pensión? 1 = Sí 2 = No|
|V21|N(1)|del aguinaldo de alguna jubilación o pensión cobrada el mes anterior? 1 = Sí 2 = No|
|V22|N(1)|del retroactivo de alguna jubilación o cobró el mes anterior? 1 = Sí 2 = No|
|V3|N(2)|de indemnización por despido? 1 = Sí 2 = No|
|V4|N(1)|de seguro de desempleo? 1 = Sí 2 = No|
|V5|N(1)|de subsidio o ayuda social (en dinero) del gobierno, iglesias, etc.? 1 = Sí 2 = No|
|V6|N(1)|con mercaderías, ropa, alimentos gobierno, iglesias, escuelas, etc.? 1 = Sí 2 = No|
|V7|N(1)|con mercaderías, ropa, alimentos de familiares, vecinos u otras personas que no viven en este hogar? 1 = Sí 2 = No|
### Identificación
|Campo|Tipo|Descripción|
|---|---|---|
|V8|N(1)|de algún alquiler (por una vivienda, terreno, oficina, etc.) de su propiedad? 1 = Sí 2 = No|
|V9|N(1)|de ganancias de algún negocio en el que no trabajan? 1 = Sí 2 = No|
|V10|N(1)|de intereses o rentas por plazos fijos/inversiones? 1 = Sí 2 = No|
|V11|N(1)|de una beca de estudio? 1 = Sí 2 = No|
|V12|N(1)|de cuotas de alimentos o ayuda en dinero de personas que no viven en el hogar? 1 = Sí 2 = No|
|V13|N(1)|teniendo que gastar lo que tenían ahorrado? 1 = Sí 2 = No|
|V14|N(1)|de pedir préstamos a familiares/amigos 1 = Sí 2 = No|
|V15|N(1)|de pedir préstamos a bancos, financieras, etc.? 1 = Sí 2 = No|
|V16|N(1)|¿Compran en cuotas o al fiado, con tarjeta de crédito o libreta? 1 = Sí 2 = No|
|V17|N(1)|¿Han tenido que vender alguna de sus pertenencias? 1 = Sí 2 = No|
|V18|N(1)|Tuvieron otros ingresos en efectivo (limosnas, juegos de azar, etc.) 1 = Sí 2 = No|
|V19_A|N(1)|menores de 10 años ayudan con algún dinero trabajando? 1 = Sí 2 = No|
|V19_B|N(1)|menores de 10 años ayudan con algún menores pidiendo? 1 = Sí 2 = No|
### Resumen del hogar
|Campo|Tipo|Descripción|
|---|---|---|
|IX_TOT|N(2)|Cantidad de miembros del hogar|
|IX_MEN10|N(2)|Cantidad de miembros del hogar menores de 10 años|
|IX_MAYEQ10|N(2)|Cantidad de miembros del hogar de 10 y más años|
### Ingreso total familiar
|Campo|Tipo|Descripción|
|---|---|---|
|ITF|N(12)|Monto de ingreso total familiar (ver Anexo I)|
### Ingreso per cápita familiar
|Campo|Tipo|Descripción|
|---|---|---|
|IPCF|N(12)|Monto de ingreso per cápita familiar (ver Anexo I)|
|PONDIH|C(6)|Ponderador del ingreso total familiar y del ingreso per cápita familiar (ver Anexo I)|
### Organización del hogar
|Campo|Tipo|Descripción|
|---|---|---|
|VII 1_1|N(2)|Realización de las tareas de la casa. Número de componente del hogar 96 = Servicio doméstico 97 = Otra persona que no vive en el hogar|
|VII 1_2|N(2)|Realización de las tareas de la casa. Número de componente del hogar 96 = Servicio doméstico 97 = Otra persona que no vive en el hogar|
### Identificación
|Campo|Tipo|Descripción|
|---|---|---|
|VII 2_1|N(2)|Otras personas que ayudan en las tareas de la casa. Número de componente del hogar 96: Servicio doméstico 97: Otra persona que no vive en el hogar 98: Ninguna|
|VII 2_2|N(2)|Otras personas que ayudan en las tareas de la casa. Número de componente del hogar 96: Servicio doméstico 97: Otra persona que no vive en el hogar 98: Ninguna|
|VII 2_3|N(2)|Otras personas que ayudan en las tareas de la casa. Número de componente del hogar 96: Servicio doméstico 97: Otra persona que no vive en el hogar 98: Ninguna|
|VII 2_4|N(2)|Otras personas que ayudan en las tareas de la casa. Número de componente del hogar 96: Servicio doméstico 97: Otra persona que no vive en el hogar 98: Ninguna|

BASE PERSONAS

### Identificación
|Campo|Tipo|Descripción|
|---|---|---|
|CODUSU|C(29)|Código para distinguir VIVIENDAS, permite aparearlas con Hogares y Personas. Además permite hacer el seguimiento a través de los trimestres.|
|NRO_HOGAR|N(1)|Código para distinguir Hogares, permite aparearlos con Personas.|
|COMPONENTE|N(2)|Número de componente: número de orden que se asigna a las personas que conforman cada hogar de la vivienda.|
|H15|N(1)|Entrevista individual realizada|
|ANO4|N(4)|Año de relevamiento (4 dígitos)|
|TRIMESTRE|N(1)|Ventana de observación 1 = 1° trimestre 2 = 2° trimestre 3 = 3° trimestre 4 = 4° trimestre|
|AGLOMERADO|N(2)|Código de aglomerado 02 = Gran La Plata 03 = Bahía Blanca-Cerri 04 = Gran Rosario 05 = Gran Santa Fe 06 = Gran Paraná 07 = Posadas 08 = Gran Resistencia 09 = Comodoro Rivadavia-Rada Tilly 10 = Gran Mendoza 12 = Corrientes 13 = Gran Córdoba|
|PROVINCIA|N(2)|Código de provincia 02 = Ciudad de Buenos Aires 06 = Buenos Aires 10 = Catamarca 14 = Córdoba 18 = Corrientes 22 = Chaco 26 = Chubut 30 = Entre Ríos 34 = Formosa 38 = Jujuy 42 = La Pampa 46 = La Rioja 50 = Mendoza 54 = Misiones|
|PONDERA|N(6)|Ponderación|
### Características de los miembros del hogar
|Campo|Tipo|Descripción|
|---|---|---|
|CH03|N(2)|Relación de parentesco 01 = Jefe/a 02 = Cónyuge/pareja 03 = Hijo / hijastro/a 04 = Yerno / nuera 05 = Nieto/a 06 = Madre / padre 07 = Suegro/a 08 = Hermano/a 09 = Otros familiares 10 = No familiares|
|CH04|N(1)|Sexo 1 = varón 2 = mujer|
|CH05|date|Fecha de nacimiento (día, mes y año)|
|CH06|N(2)|¿Cuántos años cumplidos tiene?|
### Identificación
|Campo|Tipo|Descripción|
|---|---|---|
|CH07|N(1)|¿Actualmente está 1 = unido? 2 = casado? 3 = separado/a o divorciado/a? 4 = viudo/a? 5 = soltero/a?|
|CH08|N(3)|¿Tiene algún tipo de cobertura médica por la que paga o le descuentan? 1 = Obra social (incluye PAMI) 2 = Mutual/prepaga/servicio de emergencia 3 = Planes y seguros públicos 4 = No paga ni le descuentan 9 = Ns/Nr 12 = Obra social y mutual/prepaga/servicio de emergencia 13 = Obra social y planes y seguros públicos 23 = Mutual/prepaga/servicio de emergencia/planes y seguros públicos 123 = obra social, mutual/prepaga/servicio de emergencia y planes y seguros públicos|
|CH09|N(1)|¿Sabe leer y escribir? 1 = Sí 2 = No 3 = Menor de 2 años|
|CH10|N(1)|¿Asiste o asistió a algún establecimiento educativo? (colegio, escuela, universidad) 1 = Sí, asiste 2 = No asiste, pero asistió 3 = Nunca asistió|
|CH11|N(1)|Ese establecimiento es… 1 = público 2 = privado 9 = Ns/Nr|
|CH12|N(2)|¿Cuál es el nivel más alto que cursa o cursó? 1 = Jardín/preescolar 2 = Primario 3 = EGB 4 = Secundario 5 = Polimodal 6 = Terciario 7 = Universitario 8 = Posgrado universitario 9 = Educación especial (discapacitado)|
|CH13|N(1)|¿Finalizó 1 ese nivel? 1 = Sí 2 = No 3 = Ns/Nr|
|CH14|N(2)|¿Cuál fue el último año que aprobó? 00 = Ninguno 01 = Primero 02 = Segundo 03 = Tercero 04 = Cuarto 05 = Quinto 06 = Sexto 07 = Séptimo 08 = Octavo 09 = Noveno 98 = Educación especial 99 = Ns/Nr|
|CH15|N(1)|¿Dónde nació? 1. En esta localidad|
|CH15_COD|C(3)|Especificar: contiene el código que corresponde a: 3. En otra provincia 4. En un país limítrofe 5. En otro país|
|CH16|N(1)|¿Dónde vivía hace 5 años? 1. En esta localidad 2. En otra localidad de esta provincia 3. En otra provincia (especificar) 4. En un país limítrofe (especificar: Brasil, Bolivia, Chile, Paraguay, Uruguay) 5. En otro país (especificar) 6. No había nacido 9. Ns/Nr|
|CH16_COD|C(3)|Especificar: contiene el código que corresponde a: 3. en otra provincia 4. en un país limítrofe 5. en otro país|
|NIVEL_ED|N(1)|Nivel educativo 1 = Primario incompleto (incluye educación especial) 2 = Primario completo 3 = Secundario incompleto 4 = Secundario completo 5 = Superior universitario incompleto 6 = Superior universitario completo 7 = Sin instrucción 9 = Ns/ Nr|
|ESTADO|N(1)|Condición de actividad 0 = Entrevista individual no realizada (no respuesta al cuestionario individual) 1 = Ocupado 2 = Desocupado 3 = Inactivo 4 = Menor de 10 años|
|CAT_OCUP|N(1)|Categoría ocupacional (Para ocupados y desocupados con ocupación anterior) 1 = Patrón 2 = Cuenta propia 3 = Obrero o empleado 4 = Trabajador familiar sin remuneración 9 = Ns/Nr|
|CAT_INAC|N(1)|Categoría de inactividad 1 = Jubilado/Pensionado 2 = Rentista 3 = Estudiante 4 = Ama de casa 5 = Menor de 6 años 6 = Discapacitado 7 = Otros|
|IMPUTA|N(1)|Indica los casos que han sido imputados ¿De qué manera estuvo buscando trabajo?|
|PP02C1|N(1)|Hizo contactos, entrevistas|
|PP02C2|N(1)|Mandó currículum, puso, contestó avisos (diarios, internet)|
|PP02C3|N(1)|Se presentó en establecimientos|
|PP02C4|N(1)|Hizo algo para ponerse por su cuenta|
|PP02C5|N(1)|Puso carteles en negocios, preguntó en el barrio|
|PP02C6|N(1)|Consultó a parientes, amigos|
|PP02C7|N(1)|Se anotó en bolsas, listas, planes de empleo, agencias, contratistas, o alguien le está buscando trabajo|
|PP02C8|N(1)|De otra forma activa|
|PP02E|N(1)|Durante esos 30 días, no buscó trabajo porque… 1 = está suspendido 2 = ya tiene trabajo asegurado 3 = se cansó de buscar trabajo 4 = hay poco trabajo en esta época del año 5 = por otras razones|
|PP02H|N(1)|En los últimos 12 meses ¿buscó trabajo en algún momento? 1 = Sí 2 = No|
|PP02I|N(1)|En los últimos 12 meses ¿trabajó en algún momento? 1 = Sí 2 = No|
### Ocupados que trabajaron en la semana de referencia
|Campo|Tipo|Descripción|
|---|---|---|
|PP03C|N(1)|La semana pasada, ¿tenía 1 = un solo empleo / ocupación / actividad? 2 = más de un empleo / ocupación / actividad?|
|PP03D|N(1)|Cantidad de ocupaciones|
|PP3E_TOT|N(5,1)|Total de horas que trabajó en la semana en la ocupación principal|
|PP3F_TOT|N(5,1)|Total de horas que trabajó en la semana en otras ocupaciones|
|PP03G|N(1)|La semana pasada, ¿quería trabajar más horas? 1 = Sí 2 = No|
|PP03H|N(1)|¿Si hubiera conseguido más horas 1 = podía trabajarlas esa semana? 2 = podía empezar a trabajarlas en dos semanas a más tardar? 3 = no podía trabajar más horas? 9 = Ns/Nr|
### Para todos los ocupados
|Campo|Tipo|Descripción|
|---|---|---|
|PP03I|N(1)|En los últimos treinta días, ¿buscó trabajar más horas? 1 = Sí|
### Identificación
|Campo|Tipo|Descripción|
|---|---|---|
|PP03J|N(1)|Aparte de este/os trabajo/s, ¿estuvo buscando algún empleo/ocupación/ actividad? 1 = Sí 2 = No 9 = Ns/Nr|
|INTENSI|N(1)|1 = Subocupado por insuficiencia horaria 2 = Ocupado pleno 3 = Sobreocupado 4 = Ocupado que no trabajó en la semana 9 = Ns/Nr|
### Ocupación principal
|Campo|Tipo|Descripción|
|---|---|---|
|PP04A|N(1)|¿El negocio/empresa/institución/actividad en la que trabaja es (se refiere al que trabaja más horas semanales) 1 = estatal? 2 = privada? 3 = de otro tipo? (especificar) ¿A qué se dedica o produce el negocio/empresa/institución?|
|PP04B_COD|N(5)|(Ver Clasificador de Actividades Económicas para Encuestas Sociodemográficas del Mercosur, CAES-Mercosur)|
|PP04B1|N(1)|Si presta servicio doméstico en hogares particulares 1 = casa de familia|
|PP04B2|N(1)|¿En cuántas casas trabaja? (cantidad) ¿Cuánto tiempo hace que trabaja allí? (en la casa que tiene más horas)|
|PP04B3_MES|N(2)|mes|
|PP04B3_ANO|N(2)|año|
|PP04B3_DIA|N(2)|día|
|PP04C|N(2)|¿Cuántas personas, incluido trabajan allí en total? 1 = 1 persona 2 = 2 personas|
### Identificación
|Campo|Tipo|Descripción|
|---|---|---|
|PP04C99|N(1)|1 = hasta 5 2 = de 6 a 40 3 = más de 40 9 = Ns/Nr|
|PP04D COD|C(5)|Código de ocupación (Ver Clasificador Nacional de Ocupaciones, CNO, versión 2001)|
|PP04G|N(2)|¿Dónde realiza principalmente sus tareas? 1 = En un local/oficina/establecimiento/negocio/taller/chacra/finca 2 = En puesto o kiosco fijo callejero 3 = En vehículos: bicicleta, moto, auto, barco, bote (no incluye servicio de transporte) 4 = En vehículo para transporte de personas y mercaderías – aéreos, marítimo, terrestre– incluye taxis, colectivos, camiones, furgones, transporte de combustible, mudanzas, etc.) 5 = En obras en construcción, de infraestructura, minería o similares 6 = En esta vivienda. (sin lugar exclusivo) 7 = En la vivienda del socio o del patrón 8 = En el domicilio/local de los clientes 9 = En la calle, espacios públicos, ambulante, de casa en casa, puesto móvil callejero 10 = En otro lugar (especificar)|
### Ocupación principal de los trabajadores independientes
|Campo|Tipo|Descripción|
|---|---|---|
|PP05B2_MES|N(2)|meses|
|PP05B2_ANO|N(2)|años|
|PP05B2_DIA|N(2)|días ¿En ese negocio/empresa/actividad, tiene?|
|PP05C_1|N(1)|maquinarias/equipos? 1 = propio (del negocio) 2 = prestado/alquilado 3 = no tiene|
|PP05C_2|N(1)|local (incluye kiosco/puesto fijo) 1 = propio (del negocio) 2 = prestado/alquilado 3 = no tiene|
|PP05C_3|N(1)|vehículo? 1 = propio (del negocio) 2 = prestado/alquilado 3 = no tiene|
|PP05E|N(1)|¿Para la actividad del negocio, en los últimos 3 meses, tuvo que gastar en la compra de materias primas, productos, pagar servicios u otros gastos? 1 = Sí 2 = No|
|PP05F|N(1)|¿Ese negocio/empresa/actividad, trabaja habitualmente para… 6 = un solo cliente? (persona, empresa) 7 = distintos clientes? (incluye público en general)|
|PP05H|N(1)|¿Durante cuánto tiempo ha estado trabajando en ese empleo en forma conti- nua? (con interrupciones laborales no mayores de 15 días) 1 = menos de 1 mes 2 = de 1 a 3 meses 3 = más de 3 a 6 meses|
### Identificación
### Ingresos de la ocupación principal de los trabajadores independientes
|Campo|Tipo|Descripción|
|---|---|---|
|PP06A|N(1)|En ese negocio/empresa/actividad ¿tiene socios o familiares asociados? 1 = Sí 2 = No|
|PP06C|N(10)|Monto de ingreso de patrones y cuenta propia sin socios|
|PP06D|N(10)|Monto de ingreso de patrones y cuenta propia con socios|
|PP06E|N(1)|Ese negocio/empresa/actividad 1 = es una sociedad jurídicamente constituida? (SA, SRL, Comandita por Acciones, etc.) 2 = es una sociedad de otra forma legal? 3 = o es una sociedad convenida de palabra?|
|PP06H|N(10)|¿Es una actividad familiar? (solo para 2 y 3 de PP06E) 1 = Sí 2 = No Ocupación principal de los asalariados (excepto servicio doméstico) ¿Cuánto tiempo hace que está trabajando en ese empleo en forma continua?|
|PP07A|N(1)|(sin interrupciones de la relación laboral en la misma empresa/negocio/institu- ción) 1 = menos de 1 mes 2 = 1 a 3 meses 3 = más de 3 a 6 meses 4 = más de 6 a 12 meses 5 = más de 1 a 5 años 6 = más de 5 años 9 = Ns/Nr|
|PP07C|N(1)|¿Ese empleo tiene tiempo de finalización? 1 = Sí (incluye changa, trabajo transitorio, por tarea u obra, suplencia, etc.) 2 = No (incluye permanente, fijo, estable, de planta) 9 = Ns/Nr|
### Identificación
|Campo|Tipo|Descripción|
|---|---|---|
|PP07D|N(1)|¿Por cuánto tiempo es ese trabajo? (Para los que tienen en PP07C= 1) 1 = solo fue esa vez/solo cuando lo llaman 2 = hasta 3 meses 3 = más de 3 a 6 meses 4 = más de 6 a 12 meses 5 = más de 1 año 9 = Ns/Nr|
|PP07E|N(1)|¿Ese trabajo es 1 = un plan de empleo? 2 = un período de prueba? 3 = una beca/pasantía/aprendizaje? 4 = ninguno de estos Ocupación principal de los asalariados (incluido servicio doméstico)|
|PP07F1|N(1)|¿En este trabajo le dan (no excluyentes)… de comer gratis en el lugar de trabajo? 1 = Sí 2 = No|
|PP07F2|N(1)|vivienda? 1 = Sí 2 = No|
|PP07F3|N(1)|algún producto o mercadería? 1 = Sí 2 = No|
|PP07F4|N(1)|algún otro beneficio? (automóvil, teléfono celular, pasajes, etc.) 1 = Sí 2 = No|
|PP07F5|N(1)|¿No recibe ninguno? 1 = Sí vacaciones pagas?|
|PP07G1|N(1)|vacaciones pagas? 1 = Sí 2 = No|
|PP07G2|N(1)|aguinaldo? 1 = Sí 2 = No|
|PP07G3|N(1)|días pagos por enfermedad? 1 = Sí 2 = No|
|PP07G4|N(1)|obra social? 1 = Sí 2 = No|
|PP07G_59|N(1)|no tiene ninguno 5 = Sí|
|PP07H|N(1)|¿Por ese trabajo tiene descuento jubilatorio? 1 = Sí 2 = No|
|PP07I|N(1)|¿Aporta por sí mismo a algún sistema jubilatorio? 1 = Sí 2 = No|
|PP07J|N(1)|¿El turno habitual de trabajo es 1 = de día? (mañana/tarde) 2 = de noche? 3 = de otro tipo? (rotativo, día y noche, guardias con franco)|
|PP07K|N(1)|¿Cuando cobra 1 = le dan recibo con sello/membrete/firma del empleador? 2 = le dan un papel/recibo sin nada? 3 = entrega una factura? 4 = no le dan ni entrega nada? 5 = no cobra, es trabajador sin pago/ad honorem|
|PP08D1|N(10)|¿Cuánto cobró por ese mes por estos conceptos? Monto total de sueldos/jornales, salario familiar, horas extras, otras bonifica- ciones habituales y tickets, vales o similares|
|PP08D4|N(10)|Por el mes de (mes) ¿cobró … monto percibido en tickets?|
|PP08F1|N(10)|¿Cuánto cobró por ese mes de (mes) … monto en pesos cobrado por comisión por venta/producción?|
|PP08F2|N(10)|¿Cuánto cobró por ese mes de (mes) … monto en pesos cobrado por propinas?|
|PP08J1|N(6)|¿Cuánto cobró por ese mes de (mes) … monto aguinaldo?|
|PP08J2|N(6)|¿Cuánto cobró por ese mes de (mes) … monto otras bonificaciones no habituales?|
|PP08J3|N(6)|¿Cuánto cobró por ese mes de (mes) … monto retroactivo? Desocupado|
|PP10A|N(1)|¿Cuánto hace que está buscando trabajo? 1 = menos de 1 mes 2 = de 1 a 3 meses 3 = más de 3 a 6 meses 4 = más de 6 a 12 meses 5 = más de 1 año|
|PP10C|N(1)|¿Durante ese tiempo hizo algún trabajo/changa? 1= Sí 2= No|
|PP10D|N(1)|¿Ha trabajado alguna vez? 1= Sí 2= No|
|PP10E|N(1)|¿Cuánto tiempo hace que terminó su último trabajo/changa? 1 = menos de 1 mes? 2 = de 1 a 3 meses? 3 = más de 3 a 6 meses? 4 = más de 6 a 12 meses? 5 = más de 1 a 3 años? 6 = más de 3 años? Desocupados con empleo anterior: última ocupación/changa (finalizada hace 3 años o menos)|
|PP11A|N(1)|¿El negocio/empresa/institución/actividad en la que trabajaba era 1 = estatal? 2 = privada? 3 = de otro tipo?|
|PP11B_COD|N(5)|A qué se dedicaba o qué producía ese negocio/empresa/ institución? (Ver Clasificador de Rama de Actividad, CAES-Mercosur)|
|PP11B1|N(1)|Si prestaba servicios domésticos en hogares particulares 1 = casa de familia ¿Cuánto tiempo trabajó allí?|
|PP11B2_MES|N(2)|meses|
|PP11B2_ANO|N(2)|años|
|PP11B2_DIA|N(2)|días|
|PP11C|N(2)|¿Cuántas personas, incluido trabajaban allí en total? 1 = 1 persona 2 = 2 personas 3 = 3 personas 4 = 4 personas 5 = 5 personas 6 = 6 a 10 personas 7 = 11 a 25 personas 8 = 26 a 40 personas 9 = 41 a 100 personas|
|PP11C99|N(1)|Para los que responden PP11C=99 1 = hasta 5 2 = de 6 a 40 3 = más de 40 9 = Ns/Nr|
|PP11D_COD|C(5)|¿Cómo se llamaba la ocupación que tenía? (Ver Clasificador Nacional de Ocupaciones, CNO, versión 2001) ¿Cuánto tiempo seguido estuvo trabajando en ese lugar?|
|PP11G_ANO|N(2)|años|
|PP11G_MES|N(2)|meses|
|PP11G_DIA|N(2)|días|
|PP11L|N(1)|¿Cuál fue la razón principal por la que dejó esa actividad? 1 = falta de clientes/clientes que no pagan 2 = falta de capital/equipamiento 3 = trabajo estacional 4 = tenía gastos demasiado altos 5 = otras causas laborales (especificar) 6 = jubilación/retiro 7 = causas personales (matrimonio, embarazo cuidado de hijos o familiar, estudio, enfermedad)|
|PP11L1|N(1)|¿Ese trabajo era 1 = una changa, trabajo transitorio, por tarea u obra, suplencia, etc.? 2 = un trabajo permanente, fijo, estable, de planta, etc.? 3 = Ns/Nr|
|PP11M|N(1)|¿Ese trabajo era 1 = un plan de empleo? 2 = un período de prueba? 3 = otro tipo de trabajo?|
|PP11N|N(1)|¿En ese trabajo le hacían descuento jubilatorio? 1 = Sí 2 = No 9 = Ns/Nr|
|PP11O|N(2)|¿Cuál fue la razón principal por la que dejó ese trabajo? 1 = despido/cierre (quiebra/venta/traslado de la empresa, reestructuración o recorte de personal/falta de ventas o clientes) 2 = retiro voluntario del sector público 3 = jubilación 4 = fin de trabajo temporario/estacional 5 = le pagaban poco/no le pagaban 6 = malas relaciones laborales/malas condiciones de trabajo (insalubre, cambios de horarios, etc.) 7 = renuncia obligada/pactada 8 = otras causas laborales (especificar) 9 = razones personales (matrimonio, embarazo, cuidado de hijos o familia, estudio, enfermedad)|
|PP11P|N(1)|¿Cerró la empresa? (Para quienes responden en PP11O=1) 1 = Sí 2 = No 9 = Ns/Nr|
|PP11Q|N(1)|¿Fue la única persona que quedó sin trabajo? 1 = Sí 2 = No 9 = Ns/Nr|
|PP11R|N(1)|¿Le enviaron telegrama? 1 = Sí 2 = No|
|PP11S|N(1)|¿Le pagaron indemnización? 1 = Sí 2 = No|
|PP11T|N(1)|¿Está cobrando seguro de desempleo? 1 = Sí 2 = No Ingresos de la ocupación principal|
|P21|N(10)|Monto de ingreso de la ocupación principal|
|PONDIIO|N(6)|Ponderador del ingreso de la ocupación principal (Ver Anexo I)|
### Ingreso de otras ocupaciones
|Campo|Tipo|Descripción|
|---|---|---|
|TOT_P12|N(12)|ocupación previa a la semana de referencia, deudas/retroactivos por ocupaciones anteriores al mes de referencia, etc.)|
### Ingreso total individual
|Campo|Tipo|Descripción|
|---|---|---|
|P47T|N(10)|Monto de ingreso total individual (sumatoria ingresos laborales y no laborales, ver Anexo I)|
|PONDII|N(6)|Ponderador para ingreso total individual (ver Anexo I)|
### Ingresos no laborales
|Campo|Tipo|Descripción|
|---|---|---|
|V2_M|N(6)|Monto del ingreso por jubilación o pensión|
|V3_M|N(6)|Monto del ingreso por indemnización por despido|
|V4_M|N(6)|Monto del ingreso por seguro de desempleo|
|V5_M|N(6)|Monto del ingreso por subsidio o ayuda social (en dinero) del gobierno, iglesias, etc.|
|V8_M|N(6)|Monto del ingreso por alquiler (vivienda, terreno, oficina, etc.) de su propiedad|
|V9_M|N(6)|Monto del ingreso por ganancias de algún negocio en el que no trabajó|
|V10_M|N(6)|Monto del ingreso por intereses o rentas por plazos fijos/inversiones|
|V11_M|N(6)|Monto del ingreso por beca de estudio|
|V12_M|N(6)|Monto del ingreso por cuotas de alimentos o ayuda en dinero de personas que no viven en el hogar|
|V18_M|N(6)|Monto del ingreso por otros ingresos en efectivo (limosnas, juegos de azar, etc.)|
|V19_AM|N(6)|Monto del ingreso por trabajo de menores de 10 años|
|V21_M|N(6)|Monto del ingreso por aguinaldo|
|T_VI|N(12,4)|Monto total de ingresos no laborales|
### Ingreso total familiar
|Campo|Tipo|Descripción|
|---|---|---|
|ITF|N(12,2)|Monto del ingreso total familiar|
### Ingreso per cápita familiar
|Campo|Tipo|Descripción|
|---|---|---|
|IPCF|N(12,2)|Monto del ingreso per cápita familiar|
|PONDIH|N(6)|Ponderador del ingreso total familiar y del ingreso per cápita familiar, para hogares (ver Anexo I)|

ANEXO I — RECOMENDACIONES TÉCNICAS PARA EL USO DE LA INFORMACIÓN DE INGRESOS

### Montos de ingreso
Se incluyen montos de ingreso captados en los cuestionarios y variables construidas por sumatoria de distintas fuentes (campos P21, P47T, ITF e IPCF). • El campo P21 agrega el total de ingresos habituales de la ocupación principal de la persona. • El campo P47T es la sumatoria de los ingresos laborales y los no laborales de la persona. • El campo ITF es la sumatoria de los ingresos individuales totales de todos los componentes del hogar. • El campo IPCF es el ingreso per cápita del hogar, es decir, el ITF dividido la cantidad de miembros del hogar

### Factores de expansión
Para minimizar el efecto de la no respuesta de ingresos, se asignó a las personas no respon- dentes el comportamiento de las respondentes por estrato de la muestra. Por lo tanto, para el tratamiento de los ingresos y la pobreza se presentan dos tipos de ponderadores: 1. El campo PONDERA, sin corrección, que se utiliza además para el resto de las variables. 2. Los campos PONDII, PONDIIO, PONDIH con corrección por no respuesta: • PONDII para el tratamiento del ingreso total individual (p47t). • PONDIIO para el ingreso de la ocupación principal (p21, pp06c, pp06d, pp08d1, pp08d4, pp08f1, pp08f2). • PONDIH para el ingreso total familiar (ITF), el ingreso per cápita familiar (IPCF)

### Comentarios generales
Los códigos 9, 99, 999, 9999 corresponden, salvo indicación en contrario, a la categoría No sabe/No responde. Una excepción la constituyen los montos de ingreso, en cuyo caso la no respuesta se iden- tifica con el código -9. Además, los montos captados en pp06c y pp06d presentan también los códigos -7, “No te- nía esa ocupación en el mes de referencia”; y -8, “No tuvo ingresos por el mes de referencia”. El código 0 identifica los casos a los cuales no les corresponde la secuencia analizada

FIN DEL ARCHIVO
