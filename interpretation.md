Elaborar un análisis detallado de los resultados obtenidos en un documento titulado interpretation.md:

Análisis de Patrones Descubiertos: Interpretar los patrones, relaciones y tendencias identificadas en los datos, explicando qué significan en el contexto del problema planteado.

Relación con las Preguntas de Investigación: Conectar los resultados obtenidos con las preguntas de investigación o hipótesis formuladas en la Entrega 2. Identificar claramente si los hallazgos apoyan o contradicen las hipótesis iniciales.

Ejemplos Ilustrativos: Proporcionar ejemplos específicos de los datos que ilustren los patrones o resultados más significativos.

# Filtro de Hampel: Los días detectados como outliers por el filtro Hampel en la serie temporal de rendimiento del indice NASDAQ en el periodo 2012-2020 coinciden con días en los que un evento político importante tuvo lugar.

Utilizando el filtro de hampel en la serie agregada de los tickers a estudiar se obtienen 50 diferentes valores atípicos. Buscando noticias de los sucesos en 10 de estos días se observó como comunmente se aprecian noticias de eventos relacionados con la especulacion del mercado, algunos eventos politicos como ayudas de bancos centrales y muy comunmente eventos referentes al precio del petroleo.

Dados los resultados aunque algunos eventos se pueden atribuir a eventos politicos menores, la mayoria son fruto de la especulación del mercado y eventos comunes del mercado. Por lo que no se puede concluir que los eventos politicos sean los causantes de los valores atípicos.

Ejemplos de esto son:
| Fecha       | Diferencia         | Razón                                                                 | Referencia |
|-------------|--------------------|-----------------------------------------------------------------------|------------|
| 2012-08-09  | 1.360670e+11       | Overperformed: Central bank action to help economy. Lower jobless rates in the US. | [Fuente](https://www.benzinga.com/news/12/08/2819781/market-wrap-for-august-9-2012) |

# LDA y DTM: Los temas dominantes en las noticias financieras durante la presidencia de Obama están más enfocados en la recuperación económica post-crisis de 2008, mientras que los temas dominantes durante la presidencia de Trump están más relacionados con conflictos comerciales y políticas proteccionistas.

