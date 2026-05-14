EPH Total Urbano POST 4T2023 — Diseño de registro oficial

⚠️ TRIM vs TRIMESTRE: en base Hogar la variable de período se llama TRIM. En base Personas se llama TRIMESTRE. Prestar atención al hacer joins.

---

## Códigos de referencia (comunes a base Hogar y base Personas)

**AGLOMERADO** N(2):
02=Gran La Plata 03=Bahía Blanca-Cerri 04=Gran Rosario 05=Gran Santa Fe 06=Gran Paraná 07=Posadas 08=Gran Resistencia 09=Comodoro Rivadavia-Rada Tilly 10=Gran Mendoza 12=Corrientes 13=Gran Córdoba 14=Concordia 15=Formosa 17=Neuquén-Plottier 18=Santiago del Estero-La Banda 19=Jujuy-Palpalá 20=Río Gallegos 22=Gran Catamarca 23=Gran Salta 25=La Rioja 26=Gran San Luis 27=Gran San Juan 29=Gran Tucumán-Tafí Viejo 30=Santa Rosa-Toay 31=Ushuaia-Río Grande 32=Ciudad Autónoma de Buenos Aires 33=Partidos del Gran Buenos Aires 34=Mar del Plata 36=Río Cuarto 38=San Nicolás-Villa Constitución 91=Rawson-Trelew 93=Viedma-Carmen de Patagones — Restos provinciales: 40=Resto Buenos Aires 41=Resto Catamarca 42=Resto Córdoba 43=Resto Corrientes 44=Resto Chaco 45=Resto Chubut 46=Resto Entre Ríos 47=Resto Formosa 48=Resto Jujuy 49=Resto La Pampa 50=Resto La Rioja 51=Resto Mendoza 52=Resto Misiones 53=Resto Neuquén 54=Resto Río Negro 55=Resto Salta 56=Resto San Juan 57=Resto San Luis 58=Resto Santa Cruz 60=Resto Santa Fe 61=Resto Santiago del Estero 62=Resto Tucumán

**PROVINCIA** N(2):
02=Ciudad Autónoma de Buenos Aires 06=Buenos Aires 10=Catamarca 14=Córdoba 18=Corrientes 22=Chaco 26=Chubut 30=Entre Ríos 34=Formosa 38=Jujuy 42=La Pampa 46=La Rioja 50=Mendoza 54=Misiones 58=Neuquén 62=Río Negro 66=Salta 70=San Juan 74=San Luis 78=Santa Cruz 82=Santa Fe 86=Santiago del Estero 90=Tucumán 94=Tierra del Fuego

---

BASE HOGAR

### Identificación
|Campo|Tipo|Descripción|
|---|---|---|
|CODUSU|C(29)|Código para distinguir viviendas. Permite aparearlas con Hogares y Personas. Permite el seguimiento a través de los trimestres.|
|NRO_HOGAR|N(2)|Código para distinguir hogares. Permite aparearlos con Personas.|
|REALIZADA|N(1)|Entrevista realizada 1=Sí|
|ANO4|N(4)|Año de relevamiento (4 dígitos)|
|TRIM|N(1)|Período 1=T1 2=T2 3=T3 4=T4. NOTA: base Hogar usa TRIM; base Personas usa TRIMESTRE.|
|AGLOMERADO|N(2)|[ver Códigos AGLOMERADO al inicio]|
|PROVINCIA|N(2)|[ver Códigos PROVINCIA al inicio]|
|PONDERA|N(6)|Ponderación|

### Características de la vivienda (sección raramente usada en análisis laboral)
|Campo|Tipo|Descripción|
|---|---|---|
|IV1|N(1)|Tipo vivienda 1=Casa 2=Depto 3=Pieza inquilinato 4=Pieza hotel/pensión 5=Local no habitación|
|IV1_ESP|C(45)|6=Otros|
|IV2|N(2)|Nro de ambientes totales (sin baño, cocina, pasillo, lavadero, garage)|
|IV3|N(1)|Piso interior 1=Mosaico/baldosa/madera/cerámica/alfombra 2=Cemento/ladrillo fijo 3=Ladrillo suelto/tierra|
|IV3_ESP|C(45)|4=Otros|
|IV4|N(2)|Cubierta techo 1=Membrana/cubierta asfáltica 2=Baldosa/losa sin cubierta 3=Pizarra/teja 4=Chapa metal sin cubierta 5=Chapa fibrocemento/plástico 6=Chapa cartón 7=Caña/tabla/paja 9=N/S|
|IV5|N(1)|Cielorraso/revestimiento interior 1=Sí 2=No|
|IV6|N(1)|Agua 1=Cañería dentro vivienda 2=Fuera vivienda, dentro terreno 3=Fuera terreno|
|IV7|N(1)|Fuente agua 1=Red pública 2=Perforación bomba motor 3=Perforación bomba manual|
|IV7_ESP|C(45)|4=Otra fuente|
|IV8|N(1)|¿Tiene baño/letrina? 1=Sí 2=No|
|IV9|N(1)|Ubicación baño 1=Dentro vivienda 2=Fuera vivienda, dentro terreno 3=Fuera terreno|
|IV10|N(1)|Tipo baño 1=Inodoro con cadena/arrastre 2=Inodoro sin cadena/a balde 3=Letrina|
|IV11|N(1)|Desague baño 1=Red pública (cloaca) 2=Cámara séptica y pozo ciego 3=Solo pozo ciego 4=Hoyo/excavación|
|IV12_1|N(1)|Cerca de basural (≤3 cuadras) 1=Sí 2=No|
|IV12_2|N(1)|Zona inundable (últimos 12 meses) 1=Sí 2=No|
|IV12_3|N(1)|Villa de emergencia (por observación) 1=Sí 2=No|

### Características habitacionales del hogar (sección raramente usada en análisis laboral)
|Campo|Tipo|Descripción|
|---|---|---|
|II1|N(2)|Ambientes de uso exclusivo del hogar (excl. baño, cocina, pasillo, lavadero, garage)|
|II2|N(2)|De esos, ¿cuántos para dormir?|
|II3|N(1)|¿Alguno exclusivo como lugar de trabajo? 1=Sí 2=No|
|II3_1|N(1)|Si sí, ¿cuántos?|
|II4|N(1)|¿Tiene además alguno de los siguientes?|
|II4_1|N(1)|Cuarto de cocina 1=Sí 2=No|
|II4_2|N(1)|Lavadero 1=Sí 2=No|
|II4_3|N(1)|Garage 1=Sí 2=No|
|II5|N(1)|¿Usa alguno de los anteriores para dormir? 1=Sí 2=No|
|II5_1|N(2)|Si sí, ¿cuántos?|
|II6|N(1)|¿Usa alguno exclusivo como lugar de trabajo? 1=Sí 2=No|
|II6_1|N(1)|Si sí, ¿cuántos?|
|II7|N(2)|Tenencia 1=Propietario vivienda y terreno 2=Propietario solo vivienda 3=Inquilino/arrendatario 4=Ocupante por impuestos/expensas 5=Ocupante relación dependencia 6=Ocupante gratuito con permiso 7=Ocupante de hecho 8=Sucesión|
|II7_ESP|C(45)|9=Otra situación|
|II8|N(1)|Combustible cocina 1=Gas red 2=Gas tubo/garrafa 3=Kerosene/leña/carbón|
|II8_ESP|C(45)|4=Otro|
|II9|N(1)|Uso baño 1=Exclusivo hogar 2=Compartido con otro/s hogar/es 3=Compartido con otra/s vivienda/s 4=No tiene|

### Estrategias del hogar
|Campo|Tipo|Descripción|
|---|---|---|
|V1|N(1)|¿En los últimos 3 meses han vivido de lo que ganan en el trabajo? 1=Sí 2=No|
|V2|N(1)|de alguna jubilación o pensión? 1=Sí 2=No|
|V2_01|N(1)|¿Jubilación/pensión por aportes del trabajo? 1=Sí 2=No|
|V21_01|N(1)|aguinaldo de esa jubilación/pensión? 1=Sí 2=No|
|V22_01|N(1)|retroactivo de esa jubilación/pensión? 1=Sí 2=No|
|V2_02|N(1)|¿Jubilación/pensión de ama de casa o moratoria? 1=Sí 2=No|
|V21_02|N(1)|aguinaldo de esa jubilación/pensión? 1=Sí 2=No|
|V22_02|N(1)|retroactivo de esa jubilación/pensión? 1=Sí 2=No|
|V2_03|N(1)|¿Otras pensiones (discapacidad, Madre 7 hijos, PUAM, vejez)? 1=Sí 2=No|
|V21_03|N(1)|aguinaldo de esas pensiones? 1=Sí 2=No|
|V22_03|N(1)|retroactivo de esas pensiones? 1=Sí 2=No|
|V3|N(2)|de indemnización por despido? 1=Sí 2=No|
|V4|N(1)|de seguro de desempleo? 1=Sí 2=No|
|V5_1|N(1)|de AUH y/o Asignación por Embarazo (incluye Tarjeta Alimentar)? 1=Sí 2=No|
|V5_2|N(1)|de otro plan social/subsidio del gobierno? 1=Sí 2=No|
|V5_3|N(1)|de ayuda en dinero de iglesias/ONGs? 1=Sí 2=No|
|V6|N(1)|con mercaderías/alimentos del gobierno/iglesias/escuelas? 1=Sí 2=No|
|V7|N(1)|con mercaderías/alimentos de familiares/vecinos? 1=Sí 2=No|
|V8|N(1)|de algún alquiler de su propiedad? 1=Sí 2=No|
|V9|N(1)|de ganancias de negocio en que no trabajan? 1=Sí 2=No|
|V10|N(1)|de intereses/rentas por plazos fijos/inversiones? 1=Sí 2=No|
|V11_1|N(1)|de beca del gobierno (Progresar u otras)? 1=Sí 2=No|
|V11_2|N(1)|de beca de instituciones no gubernamentales? 1=Sí 2=No|
|V12|N(1)|de cuotas alimentarias/ayuda en dinero de personas externas al hogar? 1=Sí 2=No|
|V13|N(1)|Han tenido que gastar ahorros? 1=Sí 2=No|
|V14|N(1)|pedir préstamos a familiares/amigos? 1=Sí 2=No|
|V15|N(1)|pedir préstamos a bancos/financieras? 1=Sí 2=No|
|V16|N(1)|¿Compran en cuotas/al fiado con tarjeta o libreta? 1=Sí 2=No|
|V17|N(1)|¿Han tenido que vender pertenencias? 1=Sí 2=No|
|V18|N(1)|¿Tuvieron otros ingresos en efectivo? (limosnas, azar) 1=Sí 2=No|
|V19_A|N(1)|¿Niños (<10 años) aportan dinero trabajando? 1=Sí 2=No|
|V19_B|N(1)|¿Niños (<10 años) aportan dinero pidiendo? 1=Sí 2=No|

### Resumen del hogar
|Campo|Tipo|Descripción|
|---|---|---|
|IX_TOT|N(2)|Cantidad de miembros del hogar|
|IX_MEN10|N(2)|Cantidad de miembros menores de 10 años|
|IX_MAYEQ10|N(2)|Cantidad de miembros de 10 años y más|
|ITF|N(12)|Monto de ingreso total familiar (ver notas ponderadores)|
|IPCF|N(12,2)|Monto de ingreso per cápita familiar|
|PONDIH|N(6)|Ponderador del ITF e IPCF (ver notas ponderadores)|

### Organización del hogar (sección raramente usada en análisis laboral)
|Campo|Tipo|Descripción|
|---|---|---|
|VII1_1|N(2)|Quién realiza las tareas de la casa — nro de componente. 96=Servicio doméstico 97=Persona externa|
|VII1_2|N(2)|Ídem (segundo informante)|
|VII2_1|N(2)|Otras personas que ayudan — nro componente. 96=Servicio doméstico 97=Persona externa 98=Ninguna|
|VII2_2|N(2)|Ídem|
|VII2_3|N(2)|Ídem|
|VII2_4|N(2)|Ídem|

---

BASE PERSONAS

### Identificación
|Campo|Tipo|Descripción|
|---|---|---|
|CODUSU|C(29)|Código para distinguir viviendas. Permite aparearlas con Hogar y Personas. Permite el seguimiento a través de los trimestres.|
|NRO_HOGAR|N(2)|Código para distinguir hogares. 51=Servicio doméstico en hogares 71=Pensionistas en hogares|
|COMPONENTE|N(2)|Número de orden de la persona dentro del hogar.|
|H15|N(1)|Entrevista individual realizada 1=Sí 2=No|
|ANO4|N(4)|Año de relevamiento (4 dígitos)|
|TRIMESTRE|N(1)|Período 1=T1 2=T2 3=T3 4=T4. NOTA: base Personas usa TRIMESTRE; base Hogar usa TRIM.|
|AGLOMERADO|N(2)|[ver Códigos AGLOMERADO al inicio]|
|PROVINCIA|N(2)|[ver Códigos PROVINCIA al inicio]|
|PONDERA|N(6)|Ponderación|

### Características de los miembros del hogar
|Campo|Tipo|Descripción|
|---|---|---|
|CH03|N(2)|Parentesco 1=Jefe/a 2=Cónyuge/pareja 3=Hijo/a/hijastro/a 4=Yerno/nuera 5=Nieto/a 6=Madre/padre 7=Suegro/a 8=Hermano/a 9=Otros familiares 10=No familiares|
|CH04|N(1)|Sexo 1=Varón 2=Mujer|
|CH05|date|Fecha de nacimiento (día, mes, año)|
|CH06|N(3)|Edad en años cumplidos|
|CH07|N(1)|Estado civil 1=Unido 2=Casado 3=Separado/divorciado 4=Viudo/a 5=Soltero/a|
|CH08|N(3)|Cobertura médica 1=Obra social (incl. PAMI) 2=Mutual/prepaga/emergencia 3=Planes y seguros públicos 4=No paga ni le descuentan 9=Ns/Nr|
|CH09|N(1)|¿Sabe leer y escribir? 1=Sí 2=No 3=Menor de 2 años|
|CH10|N(1)|¿Asiste o asistió a establecimiento educativo? 1=Sí asiste 2=No asiste pero asistió 3=Nunca asistió|
|CH11|N(1)|Tipo establecimiento 1=Público 2=Privado 9=Ns/Nr|
|CH12|N(2)|Nivel educativo máximo 1=Jardín/preescolar 2=Primario 3=EGB 4=Secundario 5=Polimodal 6=Terciario 7=Universitario 8=Posgrado universitario 9=Educación especial|
|CH13|N(1)|¿Finalizó ese nivel? 1=Sí 2=No 9=Ns/Nr|
|CH14|N(2)|Último año aprobado 00=Ninguno 01=Primero 02=Segundo 03=Tercero 04=Cuarto 05=Quinto 06=Sexto 07=Séptimo 08=Octavo 09=Noveno 98=Ed. especial 99=Ns/Nr|
|CH15|N(1)|¿Dónde nació? 1=En esta localidad 2=En otra localidad de esta provincia 3=En otra provincia 4=En país limítrofe 5=En otro país|
|CH15_Cod|C(3)|Código provincia/país (para CH15=3,4,5)|
|CH16|N(1)|¿Dónde vivía hace 5 años? 1=Aquí 2=Otra localidad misma provincia 3=Otra provincia 4=País limítrofe 5=Otro país 6=No había nacido 9=Ns/Nr|
|CH16_Cod|C(3)|Código provincia/país (para CH16=3,4,5)|
|NIVEL_ED|N(1)|Nivel educativo sintético 1=Primario incompleto (incl. ed. especial) 2=Primario completo 3=Secundario incompleto 4=Secundario completo 5=Superior/universitario incompleto 6=Superior/universitario completo 7=Sin instrucción 9=Ns/Nr|

### Cuestionario Individual — Variables de actividad
|Campo|Tipo|Descripción|
|---|---|---|
|ESTADO|N(1)|Condición de actividad 0=Entrevista no realizada 1=Ocupado 2=Desocupado 3=Inactivo 4=Menor de 10 años|
|CAT_OCUP|N(1)|Categoría ocupacional (ocupados y desocupados con ocup. anterior) 1=Patrón 2=Cuenta propia 3=Obrero/empleado 4=Trabajador familiar sin remuneración 9=Ns/Nr|
|CAT_INAC|N(1)|Categoría inactividad 1=Jubilado/pensionado 2=Rentista 3=Estudiante 4=Ama de casa 5=Menor de 6 años 6=Discapacitado 7=Otros|
|IMPUTA|N(1)|Indica casos imputados|
|EMPLEO|N(1)|Informalidad del empleo individual 1=Formal 2=Informal 9=Ns/Nr. Solo disponible POST 4T2023.|
|SECTOR|N(1)|Informalidad de la unidad económica 1=Formal 2=Informal 3=Hogares 9=Ns/Nr. Solo disponible POST 4T2023.|
|PP02A|N(1)|Si conseguía trabajo ¿podía empezar ya (o en ≤2 semanas)?|
|PP02B|N(1)|¿En los últimos 30 días buscó trabajo?|
|PP02C1|N(1)|Buscó: hizo contactos/entrevistas|
|PP02C2|N(1)|Buscó: mandó CV/contestó avisos|
|PP02C3|N(1)|Buscó: se presentó en establecimientos|
|PP02C4|N(1)|Buscó: hizo algo para ponerse por su cuenta|
|PP02C5|N(1)|Buscó: puso carteles/preguntó en el barrio|
|PP02C6|N(1)|Buscó: consultó parientes/amigos|
|PP02C7|N(1)|Buscó: se anotó en bolsas/agencias/planes|
|PP02C8|N(1)|Buscó: otra forma activa|
|PP02D|N(1)|¿Consultó amigos/parientes, puso carteles, hizo algo para ponerse por su cuenta?|
|PP02E|N(1)|No buscó porque: 1=Suspendido 2=Ya tiene trabajo asegurado 3=Se cansó de buscar 4=Poco trabajo en esta época 5=Otras razones|
|PP02F|N(1)|¿En los últimos 30 días buscó trabajo (segunda pasada)?|
|PP02G|N(1)|¿Puede empezar a trabajar ya (o ≤2 semanas)? 1=Sí 2=No|
|PP02H|N(1)|En los últimos 12 meses ¿buscó trabajo? 1=Sí 2=No|
|PP02I|N(1)|En los últimos 12 meses ¿trabajó? 1=Sí 2=No|

### Ocupados que trabajaron en la semana de referencia
|Campo|Tipo|Descripción|
|---|---|---|
|PP03C|N(1)|¿Tenía 1=un solo empleo/ocupación/actividad? 2=más de uno?|
|PP03D|N(1)|Cantidad de ocupaciones|
|PP3E_TOT|N(3)|Total horas trabajadas en semana — ocupación principal|
|PP3F_TOT|N(3)|Total horas trabajadas en semana — otras ocupaciones|
|PP03G|N(1)|¿Quería trabajar más horas? 1=Sí 2=No|
|PP03H|N(1)|Si hubiera conseguido más horas: 1=Podía trabajarlas esa semana 2=Podía en ≤2 semanas 3=No podía 9=Ns/Nr|
|PP03I|N(1)|En los últimos 30 días ¿buscó trabajar más horas? 1=Sí 2=No 9=Ns/Nr|
|PP03J|N(1)|Aparte de este/os trabajo/s ¿buscó otro empleo?|
|PP03K|N(1)|¿Buscó porque: 1=quería cambiar 2=quería agregar 3=se termina 4=estaba sin trabajo?|
|INTENSI|N(1)|1=Subocupado por insuficiencia horaria 2=Ocupado pleno 3=Sobreocupado 4=Ocupado que no trabajó en la semana 9=Ns/Nr|

### Ocupación principal
|Campo|Tipo|Descripción|
|---|---|---|
|PP04A|N(1)|El negocio/empresa/institución/actividad (el de más horas semanales) es: 1=Estatal 2=Privada 3=Otro tipo|
|PP04A1|N(1)|Si estatal: 1=Nacional 2=Provincial 3=Municipal 9=Ns/Nr|
|PP04B_COD|N(4)|Rama de actividad — CAES-Mercosur (4 dígitos)|
|PP04B1|N(1)|Servicio doméstico en hogares: 1=Casa de familia|
|PP04B2|N(1)|¿En cuántas casas trabaja?|
|PP04B3_MES|N(2)|Antigüedad en ese empleo: meses|
|PP04B3_ANO|N(2)|años|
|PP04B3_DIA|N(2)|días|
|PP04C|N(2)|Tamaño del establecimiento: 1=1 persona 2=2 3=3 4=4 5=5 6=6 a 10 7=11 a 25 8=26 a 40 9=41 a 100 10=101 a 200 11=201 a 500 12=más de 500 99=Ns/Nr|
|PP04C99|N(1)|Tamaño simplificado: 1=Hasta 5 2=De 6 a 40 3=Más de 40 9=Ns/Nr|
|PP04D_COD|C(5)|Código de ocupación — CNO versión 2001 (5 dígitos)|
|PP04G|N(2)|Lugar de trabajo: 11=Local/oficina/establecimiento 12=En esta vivienda con lugar exclusivo 13=Chacra/finca 2=Puesto/kiosco fijo callejero 3=Vehículo sin transporte 4=Vehículo de transporte (taxi, colectivo, camión, etc.) 5=Obras/minería 6=Vivienda sin lugar exclusivo 7=Vivienda del socio/patrón 8=Domicilio del cliente 9=Calle/espacios públicos/ambulante 10=Otro|

### Ocupación principal — trabajadores independientes
|Campo|Tipo|Descripción|
|---|---|---|
|PP05B2_MES|N(2)|Antigüedad continua en ese empleo: meses|
|PP05B2_ANO|N(2)|años|
|PP05B2_DIA|N(2)|días|
|PP05B3|N(1)|¿El negocio/actividad puede emitir facturas?|
|PP05C_1|N(1)|¿Tiene maquinarias/equipos? 1=Propio del negocio 2=Prestado/alquilado 3=No tiene|
|PP05C_2|N(1)|¿Tiene local (incl. kiosco/puesto fijo)? 1=Propio 2=Prestado/alquilado 3=No tiene|
|PP05C_3|N(1)|¿Tiene vehículo? 1=Propio 2=Prestado/alquilado 3=No tiene|
|PP05E|N(1)|¿En los últimos 3 meses gastó en insumos/materias primas/servicios? 1=Sí 2=No|
|PP05F|N(1)|¿Trabaja para: 6=Un solo cliente 7=Distintos clientes (incl. público en general)?|
|PP05H|N(1)|Tiempo en ese empleo en forma continua: 1=<1 mes 2=1 a 3 meses 3=>3 a 6 meses 4=>6 meses a 1 año 5=>1 a 5 años 6=>5 años 9=Ns/Nr|
|PP05I|N(1)|Aportes: 1=Monotributista 2=Monotrib. social 3=Autónomo/caja profesional 4=Ninguno|
|PP05J|N(1)|No realizó aportes porque: 1=No se inscribió 2=Los pagaba y dejó 3=Otra razón|
|PP05K|N(1)|¿El negocio/actividad puede emitir facturas? 1=Sí 2=No 9=Ns/Nr|

### Ingresos de la ocupación principal — independientes
|Campo|Tipo|Descripción|
|---|---|---|
|PP06A|N(1)|¿Tiene socios o familiares asociados? 1=Sí 2=No|
|PP06C|N(10)|Monto ingreso de patrones/cuenta propia sin socios|
|PP06D|N(10)|Monto ingreso de patrones/cuenta propia con socios|
|PP06E|N(1)|El negocio es: 1=Sociedad jurídicamente constituida (SA, SRL, etc.) 2=Sociedad de otra forma legal 3=Sociedad de palabra|
|PP06E1|N(1)|¿Recurre a servicios de contador/oficina contable?|
|PP06H|N(1)|¿Es actividad familiar? (solo para PP06E=2 o 3) 1=Sí 2=No|
|PP06K|N(1)|El cobro corresponde a trabajo de: 1=Todo el mes todos los días|
|PP06K_SEM|N(1)|Si no: ¿cuántos días por semana?|
|PP06K_MES|N(2)|¿Cuántos días en el mes?|
|PP06L|N(2)|¿A cuántas horas por día corresponde?|

### Ocupación principal — trabajadores asalariados (excepto serv. doméstico)
|Campo|Tipo|Descripción|
|---|---|---|
|PP07A|N(1)|Antigüedad continua en ese empleo (sin interrupciones de la relación laboral)|
|PP07B1_01|N(1)|¿Cobra algún plan (Potenciar u otro)? 1=Sí 2=No|
|PP07C|N(1)|¿El empleo tiene tiempo de finalización? 1=Sí (changa/transitorio/por tarea) 2=No (permanente/fijo/estable) 9=Ns/Nr|
|PP07D|N(1)|¿Por cuánto tiempo? (para PP07C=1 o 9): 1=Solo esa vez/cuando lo llaman 2=Hasta 3 meses 3=>3 a 6 meses 4=>6 a 12 meses 5=>1 año 9=Ns/Nr|
|PP07E|N(1)|¿Ese trabajo es: 2=Período de prueba 3=Beca/pasantía/aprendizaje 4=Ninguno de estos?|

### Ocupación principal — asalariados (incluido serv. doméstico)
|Campo|Tipo|Descripción|
|---|---|---|
|PP07F1|N(1)|¿Le dan de comer gratis en el trabajo? 1=Sí 2=No|
|PP07F2|N(1)|¿Le dan vivienda? 1=Sí 2=No|
|PP07F3|N(1)|¿Le dan algún producto/mercadería? 1=Sí 2=No|
|PP07F4|N(1)|¿Le dan otro beneficio (auto, celular, pasajes)? 1=Sí 2=No|
|PP07F5|N(1)|¿No recibe ninguno? 5=Sí|
|PP07F1_1|N(1)|¿Usa sus propias maquinarias/equipos? 1=Sí 2=No|
|PP07F1_2|N(1)|¿Usa local propio? 1=Sí 2=No|
|PP07F1_3|N(1)|¿Usa vehículo propio? 1=Sí 2=No|
|PP07G1|N(1)|¿Tiene vacaciones pagas? 1=Sí 2=No|
|PP07G2|N(1)|¿Tiene aguinaldo? 1=Sí 2=No|
|PP07G3|N(1)|¿Tiene días pagos por enfermedad? 1=Sí 2=No|
|PP07G4|N(1)|¿Tiene obra social? 1=Sí 2=No|
|PP07G_59|N(1)|No tiene ninguno: 5=Sí|
|PP07H|N(1)|¿Tiene descuento jubilatorio? 1=Sí 2=No|
|PP07I|N(1)|¿Aporta por sí mismo a sistema jubilatorio? 1=Sí 2=No|

### Ocupación principal — asalariados (excl. serv. doméstico y sector estatal)
|Campo|Tipo|Descripción|
|---|---|---|
|PP07I2|N(1)|¿El empleador le hace descuento jubilatorio a alguno de sus empleados?|
|PP07I3|N(1)|¿El empleador emite facturas? 1=Sí siempre 2=Sí pero no siempre 3=No se emiten 9=Ns/Nr|
|PP07I4|N(1)|¿El empleador cuenta con contador/oficina contable?|

### Ocupación principal — asalariados (incluido serv. doméstico y sector estatal)
|Campo|Tipo|Descripción|
|---|---|---|
|PP07J|N(1)|Turno de trabajo: 1=De día (mañana/tarde) 2=De noche 3=Otro (rotativo/guardias)|
|PP07K|N(1)|Al cobrar: 1=Recibo con sello/firma 2=Papel/recibo sin nada 3=Entrega factura 4=No recibe ni entrega nada 5=No cobra (ad honorem)|
|PP07L|N(1)|El recibo abarca: 1=La totalidad del sueldo 2=Solo una parte 9=Ns/Nr|
|PP07M|N(1)|Parte no en recibo: 1=Menos de la mitad 2=La mitad o más 9=Ns/Nr|

### Ingresos de la ocupación principal — asalariados
|Campo|Tipo|Descripción|
|---|---|---|
|PP08D1|N(10)|Monto total: sueldos/jornales + salario familiar + horas extras + bonificaciones habituales + tickets (sin retroactivos)|
|PP08D4|N(10)|Monto percibido en tickets|
|PP08F1|N(10)|Monto por comisión por venta/producción|
|PP08F2|N(10)|Monto por propinas|
|PP08G|N(1)|El cobro corresponde a: 1=Todo el mes todos los días|
|PP08G_DSEM|N(1)|Si no: ¿cuántos días por semana?|
|PP08G_DMES|N(2)|¿Cuántos días en el mes?|
|PP08H|N(2)|¿A cuántas horas por día corresponde?|
|PP08J1|N(8)|Monto aguinaldo|
|PP08J2|N(8)|Monto otras bonificaciones no habituales|
|PP08J3|N(8)|Monto retroactivo|

### Movimientos interurbanos (solo ocupados de ciertas ciudades)
|Campo|Tipo|Descripción|
|---|---|---|
|PP09A|N(1)|Ocupados de CABA/GBA: ¿trabaja en esta ciudad?|
|PP09A_ESP|C(90)|Especificación texto libre|
|PP09B|N(1)|Ocupados de Posadas/Formosa/Corrientes/Resistencia/Santa Fe/Paraná/Neuquén: ¿trabaja en esta ciudad?|
|PP09C|N(1)|¿Dónde trabaja? 1=Otro lugar de esta provincia 2=Otra provincia 3=Otro país|
|PP09C_ESP|C(90)|Especificación texto libre|

### Desocupados
|Campo|Tipo|Descripción|
|---|---|---|
|PP10A|N(1)|¿Cuánto hace que busca trabajo? 1=<1 mes 2=1 a 3 meses 3=>3 a 6 meses 4=>6 a 12 meses 5=>1 año|
|PP10B1|N(1)|Razones para no encontrar: recién empezó a buscar 1=Sí 2=No|
|PP10B2|N(1)|Por la edad 1=Sí 2=No|
|PP10B3|N(1)|Falta de trabajo en su especialidad 1=Sí 2=No|
|PP10B4|N(1)|No tiene experiencia/capacitación 1=Sí 2=No|
|PP10B5|N(1)|Le faltan vinculaciones 1=Sí 2=No|
|PP10B6|N(1)|No hay trabajo 1=Sí 2=No|
|PP10B7|N(1)|No le alcanza para salir a buscar 1=Sí 2=No|
|PP10B8|N(1)|Suspendido 1=Sí 2=No|
|PP10B9|N(1)|Otras razones 1=Sí 2=No|
|PP10B10|N(1)|Desconoce (solo autoinformante) 1=Sí 2=No|
|PP10C|N(1)|¿Hizo algún trabajo/changa durante ese tiempo? 1=Sí 2=No|
|PP10D|N(1)|¿Ha trabajado alguna vez? 1=Sí 2=No|
|PP10E|N(1)|¿Cuánto hace que terminó su último trabajo? 1=<1 mes 2=1 a 3 meses 3=>3 a 6 meses 4=>6 a 12 meses 5=>1 a 3 años 6=>3 años|

### Desocupados — última ocupación (finalizada hace ≤3 años)
|Campo|Tipo|Descripción|
|---|---|---|
|PP11A|N(1)|El negocio/empresa/institución era: 1=Estatal 2=Privada 3=Otro tipo|
|PP11B_COD|N(4)|Rama de actividad — CAES-Mercosur|
|PP11B1|N(1)|Servicio doméstico: 1=Casa de familia|
|PP11B2_MES|N(2)|Tiempo trabajado allí: meses|
|PP11B2_ANO|N(2)|años|
|PP11B2_DIA|N(2)|días|
|PP11C|N(2)|Tamaño: 1=1 pers 2=2 3=3 4=4 5=5 6=6-10 7=11-25 8=26-40 9=41-100 10=101-200 11=201-500 12=>500 99=Ns/Nr|
|PP11C99|N(1)|Simplificado: 1=Hasta 5 2=6 a 40 3=Más de 40 9=Ns/Nr|
|PP11D_COD|N(5)|Código de ocupación — CNO versión 2001|
|PP11G_ANO|N(2)|Tiempo en ese lugar en forma continua: años|
|PP11G_MES|N(2)|meses|
|PP11G_DIA|N(2)|días|
|PP11L|N(1)|Razón principal por la que dejó: 1=Falta clientes/pago 2=Falta capital/equipamiento 3=Trabajo estacional 4=Gastos altos 5=Otras causas laborales 6=Jubilación/retiro 7=Causas personales|
|PP11L1|N(1)|¿Cobraba algún plan? 1=Sí 2=No|
|PP11L2|N(1)|Era: 1=Changa/transitorio 2=Permanente/estable 3=Ns/Nr|
|PP11M|N(1)|Era: 2=Período de prueba/pasantía 3=Otro tipo|
|PP11N|N(1)|¿Le hacían descuento jubilatorio? 1=Sí 2=No 9=Ns/Nr|
|PP11O|N(2)|Razón por la que dejó: 1=Despido/cierre 2=Retiro voluntario sector público 3=Jubilación 4=Fin trabajo temporario 5=Le pagaban poco/no pagaban 6=Malas condiciones laborales 7=Renuncia obligada/pactada 8=Otras causas laborales 9=Razones personales|
|PP11P|N(1)|¿Cerró la empresa? (PP11O=1) 1=Sí 2=No 9=Ns/Nr|
|PP11Q|N(1)|¿Fue la única persona que quedó sin trabajo? 1=Sí 2=No 9=Ns/Nr|
|PP11R|N(1)|¿Le enviaron telegrama? 1=Sí 2=No|
|PP11S|N(1)|¿Le pagaron indemnización? 1=Sí 2=No|
|PP11T|N(1)|¿Está cobrando seguro de desempleo? 1=Sí 2=No 9=Ns/Nr|

### Ingresos de la ocupación principal
|Campo|Tipo|Descripción|
|---|---|---|
|P21|N(12)|Monto del ingreso de la ocupación principal|
|PONDIIO|N(6)|Ponderador del ingreso de la ocupación principal (ver notas ponderadores)|
|TOT_P12|N(12)|Monto ingreso de otras ocupaciones (incluye ocup. secundaria, ocup. previa, retroactivos)|
|P47T|N(12)|Monto ingreso total individual (sumatoria laborales + no laborales)|
|PONDII|N(6)|Ponderador para ingreso total individual|

### Ingresos no laborales
|Campo|Tipo|Descripción|
|---|---|---|
|V2_01_M|N(11)|Monto jubilación/pensión por aportes del trabajo|
|V21_01_M|N(11)|Monto aguinaldo de esa jubilación/pensión|
|V22_01_M|N(11)|Monto retroactivo de esa jubilación/pensión|
|V2_02_M|N(11)|Monto jubilación/pensión de ama de casa o moratoria|
|V21_02_M|N(11)|Monto aguinaldo de esa jubilación/pensión|
|V22_02_M|N(11)|Monto retroactivo de esa jubilación/pensión|
|V2_03_M|N(11)|Monto otras pensiones (discapacidad, Madre 7 hijos, PUAM, vejez)|
|V21_03_M|N(11)|Monto aguinaldo de esas pensiones|
|V22_03_M|N(11)|Monto retroactivo de esas pensiones|
|V3_M|N(11)|Monto indemnización por despido|
|V4_M|N(11)|Monto seguro de desempleo|
|V5_01_M|N(11)|Monto AUH y/o Asignación por Embarazo (incl. Tarjeta Alimentar)|
|V5_02_M|N(11)|Monto otro plan social/subsidio del gobierno|
|V5_03_M|N(11)|Monto ayuda en dinero de iglesias/ONGs|
|V8_M|N(11)|Monto ingreso por alquiler de su propiedad|
|V9_M|N(11)|Monto ganancias de negocio en que no trabajó|
|V10_M|N(11)|Monto intereses/rentas por plazos fijos/inversiones|
|V11_01_M|N(11)|Monto beca del gobierno (Progresar u otras)|
|V11_02_M|N(11)|Monto beca de instituciones no gubernamentales|
|V12_M|N(11)|Monto cuotas alimentarias/ayuda de personas externas al hogar|
|V18_M|N(11)|Monto otros ingresos en efectivo (limosnas, juegos de azar)|
|V19_AM|N(11)|Monto ingreso por trabajo de menores de 10 años|
|T_VI|N(12)|Monto total de ingresos no laborales|
|ITF|N(12)|Monto ingreso total familiar|
|IPCF|N(12,2)|Monto ingreso per cápita familiar|
|PONDIH|N(6)|Ponderador del ITF e IPCF|

---

## Notas técnicas

**Ponderadores:**
- PONDERA: ponderación general (personas, características no monetarias)
- PONDIIO: ponderador del ingreso de la ocupación principal (P21, PP06C, PP06D, PP08D1, PP08D4, PP08F1, PP08F2)
- PONDII: ponderador del ingreso total individual (P47T)
- PONDIH: ponderador del ingreso total familiar (ITF) e ingreso per cápita familiar (IPCF)

**Códigos de no respuesta:** 9, 99, 999, 9999 = Ns/Nr salvo indicación en contrario. Montos de ingreso: -9=no respuesta; PP06C y PP06D además usan -7 (sin esa ocupación en el mes) y -8 (sin ingresos en ese mes). Código 0 = no le corresponde la secuencia.
