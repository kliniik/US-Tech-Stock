# Análisis del impacto del partido gobernante estadounidense en la imagen de las empresas tecnológicas en el mercado bursátil.

## Descripción del Proyecto:

El objetivo de nuestro proyecto es analizar si el partido gobernante puede influir en la imagen de las empresas tecnológicas en bolsa. 

Queremos comprobar los datos del mandato del Partido Demócrata (presidencia de Barack Obama entre los años 2013 y 2017) y del Partido Republicano (presidencia de Donald Trump entre los años 2017 y 2020).

Para esto se estudiará el mercado bursátil, en concreto acciones del índice NASQAD y el sentimiento en noticias financieras y tweets de mercado entre los años 2012 al 2020.

### Hipotesis preliminar:

Queremos comprobar si el partido gobernante puede influir principalente en los valores de las acciones del índice NASDAQ y el sentimiento en noticias financieras y tweets de mercado entre los años 2012 y 2020.
  
## Instrucciones para Reproducir los Experimentos:

- Encontrar datos en el NASDAQ, quizá tweets o noticias financieras y datos bursátiles relevantes.
- Filtrar los datos a los periodos de tiempo pertinentes durante la presidencia de cada candidato.
- Formular hipótesis adecuadas.
- Realizar el preprocesamiento correspondiente y crear un nuevo conjunto de datos, con el valor de cierre de la bolsa, las noticias sobre las empresas en cuestión y el sentimiento correspondiente asignado a las noticias.
- Aplicar técnicas de minería de datos como LDA, análisis de sentimientos y análisis de series temporales.
- Comprobar si los cambios en el sentimiento de la bolsa y las noticias están relacionados con acontecimientos importantes en el mundo de la política estadounidense.
- Extraer conclusiones a partir de los resultados obtenidos como consecuencia de la minería de datos, consultar si se cumplen las hipótesis.
  
## Dependencias y Entorno: 

Las librerías requeridas para recolectar los datos se encuentran en `data/requirements_data_recollection.txt` principalmente se ha usado la librería `yfinance`, `huggingface_hub` y `datasets` de Python.
