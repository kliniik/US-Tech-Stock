# Objetivo General del Proyecto
Comprobar si existió alguna diferencia entre el comportamiento de los valores en bolsa de los stocks del índice NASDAQ y/o el sentimiento de los títulos de noticias/tweets relativos a estos stocks durante la presidencia de Barack Obama (2012-2016) y la de Donald Trump (2016-2020).

# Preguntas de Investigación o Hipótesis
Detallar las preguntas o hipótesis que se pretende explorar o validar mediante el análisis de los datos preparados.

- El sentimiento de las noticias y tweets financieros relacionados con los stocks del índice NASDAQ tuvo un sentimiento hasta dos veces más positivo durante la presidencia de Obama (durante el periodo 2012-2016) que durante la presidencia de Trump (2016-2020).
- La prediccion de la serie temporal de rendimiento del stock de Apple en bolsa en el periodo 2012-2020 obtiene mejores métricas al usar como variable exogena el sentimiento de las noticias y tweets financieros relacionados con el stock.
- Los días detectados como outliers por el filtro Hampel en la serie temporal de rendimiento del indice NASDAQ en el periodo 2012-2020 coinciden con días en los que un evento político importante tuvo lugar.
- Los temas dominantes en las noticias financieras durante la presidencia de Obama están más enfocados en la recuperación económica post-crisis de 2008, mientras que los temas dominantes durante la presidencia de Trump están más relacionados con conflictos comerciales y políticas proteccionistas.
- Los temas dominantes identificados mediante el método LDA en el corpus durante la presidencia de Trump están más centrados en la volatilidad del mercado y las políticas fiscales, mientras que durante la presidencia de Obama están más enfocados en la estabilidad económica y las políticas de estímulo.

# Justificación de los Datos Seleccionados
Los datos obtenidos son, por una parte, series temporales de datos financieros (los valores en bolsa de los stocks) y, por otra, datos no estructurados (texto) relativo a estos stocks, ya sean títulos de noticias o tweets obtenidos mediante webscraping.

Son adecuados para responder a las preguntas planteadas porque nos permiten hacer un seguimiento del comportamiento en bolsa de los distintos stocks y obtener un sentimiento medio de los escritores de noticias financieras relativas a los stocks durante los dos periodos analizados.

# Desafíos Potenciales con los Datos Limpiados
- Sesgo de datos: al contar con 100 empresas en el índice NASDAQ, pueden aparecer sesgos, al ser más probable que haya más noticias/tweets sobre las empresas más populares del índice (Apple, Microsoft...) que sobre las demás no tan populares.
