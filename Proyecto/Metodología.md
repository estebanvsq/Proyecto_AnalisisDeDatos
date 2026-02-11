# Metodología de la Investigación

La presente metodología articula las técnicas de ciencia de datos empleadas para analizar el comportamiento del Costo Unitario (CU) de prestación del servicio de energía eléctrica y sus componentes en el mercado regulado colombiano. El proceso sigue un flujo estructurado desde la selección del dato crudo hasta la generación de indicadores de riesgo y eficiencia.

La estructura metodológica consta de las siguientes 6 etapas:

## 1. Selección de datos
**Fuente y Alcance:**
Se seleccionó el conjunto de datos *"Tarifas y Costos de Energía Eléctrica para el Mercado Regulado"*, el cual recopila información reportada en cumplimiento de las Leyes 142 de 1994, 1955 de 2019 y resoluciones CREG vigentes.

*   **Periodo de análisis:** Enero 2024 - Septiembre 2025.
*   **Variables seleccionadas:**
    *   **Identificadores:** Año, Periodo (Mes), Operador de red, Nivel de tensión.
    *   **Variable Objetivo:** CU Total (Costo Unitario de prestación del servicio).
    *   **Componentes del Costo:** Costo Compra ($G$), Cargo Transporte STN ($T$), Cargo Transporte SDL ($D$), Margen de Comercialización ($Cv$), Costo de Pérdidas ($PR$), Restricciones ($R$).
*   **Formato:** Archivo plano (CSV) estructurado con registros mensuales por operador y nivel de tensión.

## 2. Inspección y verificación inicial de los datos
Se realizó una auditoría inicial para evaluar la integridad y estructura del dataset:
*   **Dimensionalidad:** Verificación de la cantidad de registros y columnas (`df.shape`).
*   **Tipos de datos:** Detección de inconsistencias en variables numéricas almacenadas como texto debido a separadores de miles/decimales (uso de `df.info()`).
*   **Valores nulos:** Conteo de valores faltantes (`null`/`nan`) por columna para determinar estrategias de imputación o filtrado.
*   **Unicidad:** Validación de duplicados y revisión de cardinalidad en variables categóricas (Operadores, Niveles).

## 3. Preprocesamiento y limpieza
Se implementó un pipeline de limpieza para estandarizar los datos antes del análisis:
1.  **Corrección de formatos numéricos:**
    *   Eliminación de comas (`,`) usadas como separadores de miles en columnas críticas (`Año`, `CU Total`).
    *   Estandarización de decimales en componentes específicos (`Cfm,j`).
    *   Conversión explícita a tipos `int` y `float`.
2.  **Normalización temporal:**
    *   Conversión de nombres de meses en español (Enero, Febrero...) a representación numérica (1, 2...).
    *   Creación de la variable `Fecha` (formato `YYYY-MM`) para habilitar el análisis de series de tiempo.
3.  **Estandarización de entidades:**
    *   Unificación de nombres de operadores con grafías inconsistentes (ej. *"CELSIA Colombia - Tolima"* → *"CELSIA - Tolima"*).
    *   Normalización de las categorías de `Nivel` de tensión.
4.  **Codificación:** Generación de códigos numéricos para variables categóricas (`OPR` para operadores, `NIV` para nivel) facilitando el procesamiento matricial.

## 4. Integración y transformación
Se derivaron nuevas variables e indicadores ("Feature Engineering") para responder a las preguntas de investigación:
*   **Cálculo de Participaciones (Shares):** Se calculó el peso porcentual de cada componente ($G, T, D, Cv, PR$) sobre el $CU Total$ para identificar la estructura de costos.
*   **Agrupación de Componentes:** Creación de variables agregadas como `Transporte_y_Perdidas` ($STN + SDL + PR$) para comparar bloques lógicos de costo.
*   **Deltas Mensuales:** Cálculo de variaciones absolutas y porcentuales mes a mes ($\Delta CU$, $\Delta G$) para analizar la volatilidad temporal.
*   **Scores de Riesgo:**
    *   *Riesgo de Salto Tarifario:* Índice compuesto por frecuencia de aumentos, magnitud máxima y volatilidad.
    *   *Ineficiencia Estructural:* Índice proxy basado en la persistencia de altos costos de transporte/pérdidas.

## 5. Validación de calidad de datos
Se aplicaron técnicas estadísticas para identificar anomalías que pudieran sesgar los resultados:
*   **Detección de Outliers (IQR):** Implementación de la función `buscar_outliers` basada en el Rango Intercuartílico ($Q3 - Q1$). Se definieron límites ($Q1 - 1.5 \times IQR$ y $Q3 + 1.5 \times IQR$) para marcar valores atípicos en todos los componentes del costo.
*   **Z-Score Robusto:** Para el Margen de Comercialización ($Cv$), se utilizó una métrica robusta basada en la Mediana y el MAD (Median Absolute Deviation) para detectar operadores con márgenes sistemáticamente desviados del mercado, reduciendo la sensibilidad a valores extremos puntuales.

## 6. Análisis exploratorio de datos (EDA)
El análisis siguió el enfoque univariado sistemático para responder cuatro preguntas regulatorias clave:
1.  **Drivers de Aumento del CU:**
    *   *Técnica:* Correlación de Deltas y análisis de contribución relativa en periodos de alza.
    *   *Objetivo:* Determinar si los aumentos del CU obedecen más a choques de oferta (Costo de Compra $G$) o a costos estructurales de red (Transporte + Pérdidas).
2.  **Análisis de Márgenes Atípicos:**
    *   *Técnica:* Comparación de medianas por operador y cálculo de "Tasa de Outliers" en el tiempo.
    *   *Objetivo:* Identificar operadores con políticas de comercialización disonantes frente al promedio nacional.
3.  **Riesgo de Saltos Tarifarios:**
    *   *Técnica:* Identificación de eventos donde la variación porcentual $|\% \Delta CU|$ supera el percentil 95 (umbral crítico).
    *   *Objetivo:* Ranking de operadores con mayor inestabilidad tarifaria para el usuario final.
4.  **Ineficiencia Estructural:**
    *   *Técnica:* Evaluación multicriterio (Share de Pérdidas + Share de Transporte + Volatilidad).
    *   *Objetivo:* Priorización de operadores que requieren revisión regulatoria por ineficiencias en la gestión de redes.
