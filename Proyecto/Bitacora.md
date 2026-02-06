# Limpieza de datos

- Modificación de las columnas "Año", "CU Total", "Cfm,j ($/fact.)", se eliminaron las comas y se pasaron a int y float

- Creación de una nueva columna "Num_Periodo" para pasar los meses a números y así poder realizar otra columna "Fecha" con formato fecha (año y mes)

- En operadores de red se encontraron datos similares q correspondían a la misma empresa, por lo que se unificaron para poder trabajarlos como el mismo dato ("CELSIA Colombia - Valle del Cauca = "CELSIA - Valle del Cauca" y "CELSIA Colombia - Tolima" = "CELSIA - Tolima")

- Cambio de errores de digitación en "Nivel"

- Se categorizó en una nueva columna "OPR" los operadors de red y otra columna "NIV" los niveles

- Correción comas en "Cfm,j ($/fact.)" para corregir los outliers

- Realizar una copida del dataframe en otra variable para no trabajar sobre el original.

- Se crea una nueva columna "VAL_COT" con la finalidad de saber cuáles datos son válidos para hacer comparaciones en la columna de COT, debido a que en esta se presenta una gran cantidad de ceros. Esto podría deberse a 3 factores: Datos faltantes o no reportados, que realmente se deba a que en este caso no el valor es de $0, o un error de registro / dato corrupto.

- Se observa que en varios registros el COT es igual a cero, lo cual no indica ausencia de costos de operación y transporte, sino que dichos costos se encuentran incorporados en otros componentes tarifarios, de acuerdo con el esquema regulatorio aplicado.

- El operador no reporta el componente COT de manera explícita ni indica su integración en otros cargos dentro del esquema tarifario presentado.

- En algunos registros el componente COT toma valor cero sin indicación explícita de su inclusión en otros cargos. En estos casos, se interpreta que el costo no se encuentra desagregado en la información publicada por el operador, por lo cual no es posible identificar su reconocimiento específico dentro de la estructura tarifaria.

- Se identifica que EMCALI no reporta el componente COT de forma explícita en ninguno de los períodos analizados, mientras que CELSIA Colombia (Tolima) deja de desagregar dicho componente a partir de julio de 2025. Este comportamiento sugiere diferencias estructurales en los esquemas de reporte y reconocimiento de costos, lo cual limita la comparabilidad directa entre operadores y periodos.