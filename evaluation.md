Utilizar métricas específicas y adecuadas para evaluar la validez de los resultados obtenidos en la Entrega 3 y documentar en el fichero evaluation.md:

Descripción de las Métricas Utilizadas: Explicar qué métricas se emplearon y por qué son relevantes para evaluar los resultados.

Resultados de las Evaluaciones: Presentar los valores obtenidos de cada métrica y discutir su significado en el contexto del análisis.

Limitaciones en la Evaluación: Describir cualquier limitación o desafío en la aplicación de estas métricas (p. ej., tamaño de muestra, sesgo de datos).

# Tecnica 1: Latent Dirichlet allocation (LDA)

## Coherence Score

La métrica de coherencia de tópicos es una medida fundamental para evaluar la calidad de los tópicos generados por el modelo LDA. En este caso, se utilizó la implementación de la métrica C_v de la librería gensim, la cual calcula la coherencia de un conjunto de palabras dentro de un tema. Esta métrica se basa en la idea de que las palabras que coexisten frecuentemente en contextos similares (en documentos o dentro de un corpus) son más semánticamente coherentes entre sí. El método C_v se enfoca en medir la similitud semántica entre las palabras más representativas de un tema, utilizando el embedding de palabras en este caso un bow (bag of words) para calcular la coherencia de los tópicos generados. Los valores de coherencia de tópicos varían entre 0 y 1, donde un valor más alto indica una mayor coherencia semántica entre las palabras de un tópico.

La coherencia de tópicos es importante porque nos da una indicación de si las palabras que componen un tópico están relacionadas entre sí de manera significativa. Un alto valor de coherencia sugiere que las palabras dentro de un tópico comparten un contexto semántico similar, lo que implica que el tópico es interpretable y consistente. 

En este caso en el modelo obtuvo un coherence score de 0.503. Este valor indica que los tópicos generados por el modelo LDA tienen una coherencia moderada.

En este caso la mayor limitación surge de la naturaleza del corpus y realizar un preprocesado exhaustivo dado que como se comentará en la sección de resultados los tópicos comunmente tienen palabras o muy generales o solamente de empresas concretas. Quizá con un preproceasado para evitar nombres de empresas y otros tickers de bolsa se pudiera mejorar la coherencia de los tópicos.

## Log Perplexity

El log-perplexity es otra métrica comúnmente utilizada para evaluar modelos de tópicos, en particular en el contexto de LDA. En este caso, se utilizó el valor de log-perplexity de la librería gensim para medir qué tan bien el modelo es capaz de predecir nuevos documentos a partir de los tópicos generados.

La perplejidad mide cómo de bien el modelo representa el corpus utilizado. Cuanto más bajo sea el valor de perplejidad, mayor calidad tiene el modelo. Se calcula teniendo en cuenta la probabilidad de observar cada palabra dada la distribución de tópicos en el corpus y la distribución de palabras en cada tópico.

El log-perplexity es simplemente el logaritmo de la perplejidad, lo que permite interpretarlo de manera más fácil. Cuanto más bajo es el log-perplexity, mejor es el ajuste del modelo.

En este caso, el modelo LDA obtuvo un log-perplexity de --8.193. Un valor negativo indica que el modelo es capaz de predecir correctamente las palabras en un documento, lo que sugiere que el modelo LDA tiene un buen ajuste a los datos.

# Tecnica 2: Modelo dinámico de tópicos (DTM)

## Coherence Score

La métrica de coherencia de tópicos también se puede aplicar a modelos dinámicos de tópicos, como el DTM. En este caso, se utilizó la implementación de la métrica C_v de la librería gensim para evaluar la coherencia de los tópicos generados por el modelo DTM en cada uno de los períodos de tiempo.

Tiene la misma interpretación que en el caso de LDA, donde un valor más alto indica una mayor coherencia semántica entre las palabras de un tópico.

La gráfica de coherencia de tópicos a lo largo del tiempo es la siguiente:
![Coherence Score DTM](assets/imgs/DTM_Coherences_Overtime_v2.png)

En este caso, el modelo DTM obtuvo un coherence score en torno al 0.5, aunque está métrica fue decreciendo a lo largo del tiempo. Esto sugiere que los tópicos generados por el modelo DTM son moderadamente coherentes, pero que la coherencia disminuye a medida que avanzamos en el tiempo.

Como limitación, cabe destacar que debido a la cantidad de datos manejados y la complejidad del modelo DTM, el tiempo de entrenamiento y evaluación del modelo se realizó sobre una muestra aleatoria simple de 1000 noticias. Esto puede afectar a como de representativos son los tópicos generados y por lo tanto las métricas obtenidas.