# Tecnica 1: Latent Dirichlet allocation (LDA)

## Descripción de la Técnica:
La Asignación Latente de Dirichlet (LDA, por sus siglas en inglés) es un método de generación de tópicos extraídos de un corpus de texto. El modelo asume que cada documento del corpus es una distribución de temas, y cada tema, a su vez, es una distribución de palabras (ambas distribuciones siguen una distribución de Dirichlet, de donde proviene el nombre del método). El objetivo del modelo es, a través de modelado bayesiano, aprender la distribución de temas para cada documento y la distribución de palabras para cada tema. Estas distribuciones permiten descubrir patrones en la semántica del texto de nuestro corpus.

## Justificación de la Técnica:
Los datos usados para el proyecto cuentan con una gran cantidad de noticias comprendidas entre los años 2012 y 2020 sobre temas financieros. Este tipo de datos, junto con el objetivo de encontrar el sentimiento y los temas de los que se habla en este ámbito, hacen que un modelo como el LDA sea adecuado para representar los temas principales de estos datos.

Como inconveniente, este método no permite añadir la característica temporal de los datos. Sin embargo, gracias a su rápida ejecución, comparada con métodos más avanzados como el modelo dinámico de tópicos, se convierte en un punto de partida adecuado para probar posteriormente estas técnicas más complejas.

## Configuración del Algoritmo:
Parámetros Utilizados, Herramientas y Librerías Aplicadas
Para implementar el modelo LDA se utilizó la librería `gensim` de Python, que cuenta con una implementación eficiente y paralelizable de este método.

Los hiperparámetros probados son:

num_topics: Este parámetro establece el número de tópicos a modelar en el corpus. Su elección es compleja; en este caso, se utilizó la métrica de coherencia de tópicos, también implementada en gensim, para evaluar qué tan coherentes son los tópicos generados. Finalmente, se seleccionó un valor de num_topics = 5, tras probar entre 2 y 60 tópicos en un subconjunto del dataset que contenía 5,000 noticias.

La elección de un número alto de tópicos se justificó por la gran cantidad de columnas/entidades del dataset, las cuales se pensaba podrían influir en la existencia de múltiples tópicos relacionados. El valor de 5 tópicos obtuvo la mayor coherencia (0.441), que aunque no fue significativamente superior a otros valores, resultó ser lo suficientemente alta como métrica. Además, dado que el número de tópicos era pequeño, se respetó el principio de la Navaja de Ockham al escoger la opción más simple que explica mejor el corpus.

passes: Este parámetro establece el número de veces que el modelo procesa todo el corpus para estimar las distribuciones. Un mayor número de pasadas permite mejorar la convergencia del modelo, pero aumenta el costo computacional.

Por lo tanto, tras ajustar estos hiperparámetros en el conjunto de prueba, se utilizó el corpus completo para entrenar el modelo LDA con 5 tópicos, obteniendo un valor de coherencia final de 0.515.


# Tecnica 2: Modelo dinámico de tópicos (DTM)

## Descripción de la Técnica:

El modelo dinámico de tópicos (Dynamic Topic Model, DTM) es una extensión del modelo LDA que permite capturar la evolución de los temas a lo largo del tiempo. A diferencia del LDA, que asume que las distribuciones de temas y palabras son fijas, el DTM incorpora un componente temporal que ajusta estas distribuciones para cada periodo de tiempo. Esto se logra a través de un enfoque bayesiano en el que las distribuciones de temas en un periodo están condicionadas por las distribuciones del periodo anterior, creando una dependencia temporal.

El DTM es particularmente útil cuando los datos contienen series temporales o se agrupan naturalmente en intervalos de tiempo (por ejemplo, meses o años). Esto permite analizar cómo cambian los temas y sus respectivas palabras representativas a lo largo del tiempo, proporcionando una visión más rica y detallada de la evolución temática.

## Justificación de la Técnica:

La inclusión del componente temporal en el modelo hace que el DTM sea particularmente adecuado para analizar el corpus de noticias financieras del proyecto, dado que estas abarcan un rango de tiempo significativo (2012-2020). Dado que los temas financieros suelen estar sujetos a cambios debido a eventos económicos, políticos o regulatorios, el DTM permite capturar dinámicamente estas transiciones.

Además, mientras que el LDA puede ofrecer una visión estática de los temas, el DTM aporta una dimensión adicional al análisis, lo que resulta esencial para estudiar tendencias, identificar rupturas o patrones emergentes y contextualizar los resultados en un marco temporal.

Por último esta técnica se eligo al ser una extensión directa del previo método LDA lo cual nos permite intentar ver alguna relación entre los tópicos del LDA y los del DTM. Además dado que la misma librería implementa la técnica resulta una ayuda frente al uso de técnicas como Topics over Time (ToT) o continious Dynamic Topic Model (cDTM)

## Configuración del Algoritmo:

Para este, se han probado los hiperparámetros de num_topics y el número de passes.

Es importante remarcar que, en el LDA original, se consiguió ejecutar el modelo sobre toda la muestra de más de dos millones de noticias. Sin embargo, dado que la implementación del DTM no permite la paralelización y es más costoso computacionalmente, se ha tenido que ejecutar con tamaños de muestra mucho más pequeños.

Tras probar con toda la muestra durante horas y no tener éxito, se optó por intentar usar el 10% de la muestra, lo cual también resultaba en un tiempo de ejecución excesivamente grande. Por esto, se decidió usar 500 muestras del dataset con una sola pasada y 10 tópicos. Tras comprobar que la ejecución resultaba en un tiempo aceptable, se decidió entrenar con el 10% de la muestra y 2 pasadas al corpus.

Por último, se estableció un num_topics de 5, al igual que en el LDA, y una chain_variance de 0.100. Dado que los tópicos en el ámbito financiero pueden tener gran varianza y ser espontáneos, se escogió un valor 20 veces mayor (0.100) que el valor por defecto de la librería (0.005).

# Tecnica 3: Análisis de sentimiento
## Descripción de técnicas utilizadas
Se usó una técnica de análisis de sentimientos. Para esto se usó un modelo fine-tuned que usa LLama 2 como base y que refinado con datos financieros para hacer análisis de sentimientos.

Para obtener el sentimiento de cada noticia de nuestro dataset se le pasó un prompt al modelo dándole instrucciones para que a partir del titular de la noticia responda con neutral, positive o negative dependiendo del sentimiento del titular.

https://www.kaggle.com/code/lucamassaron/fine-tune-llama-2-for-sentiment-analysis

## Justificación de la selección de técnicas
Se eligió esta técnica porque es la más ideal para la naturaleza de los titulares de noticias (texto) y el objetivo del proyecto (descubrir si el sentimiento general de los titulares de noticias financieras publicadas en benzinga.com fue más positivo durante la presidencia de Obama que durante la de Trump)

## Configuración de los algoritmos
El notebook que hace el fine-tuning de LLama 2 usa pytorch, transformers, peft y pandas como principales librerías. Todos los parámetros de entrenamiento se pueden encontrar en el notebook en la celda con número de ejecución 15.
