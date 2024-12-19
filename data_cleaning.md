# Descripción de los métodos utilizados para la limpieza de datos y justificación de las decisiones tomadas durante el proceso de limpieza.

## Valores de tickers de stocks (NASQAD_stock_data_processed.csv)

- Se ha comprobado que los datos recogidos son los correctos en cuanto al rango de fechas que describen, teniendo en cuenta el cierre del mercado de inversiones en festivos Estadounidenses y fines de semana.
- Se han descartado todos aquellos tickers de los cuales no se tuviera la muestra completa en el rango de fechas estudiado, reduciendo así la muestra de 2967 tickers a 1149. Se considera que aunque la cantidad de tickers se pierden es considerable, contar con la serie temporal original ininterrumpida puede ser de mayor utilidad.
- Se ha filtrado las columnas para obtener solo los precios ajustados de los stocks. Estos precios reflejan de mejor forma el valor real en mercado al ajustar los precios por diversos factores como dividendos, splits, etc.
- Se ha cambiado el tipo de los datos para sean acorde a las columnas (fechas para "date", enteros para "volume" y punto flotante para los valores de los stocks).

## David-Chew-HL/Tech-Stocks-News (david_check_stock_news_processed_part1.csv y part2) 

- No hay valores faltantes en ninguna de las columnas.
- Se analizó si los titulares estan duplicados. Se encontró una gran cantidad de filas duplicadas, es decir que el mismo titular se ha publicado en el mismo día. Al analizar si tambien se duplicaba el titular en diferentes días, se enontraron solo 17 ejemplos. Se procedió a eliminar todas las filas duplicadas que estuvieran en mismos días. Esto se realizó bajo la premisa de que si se han publicado en diferentes días, la noticia puede tener mayor o menor relevancia que si se publica en el mismo día.


## ic-fspml/stock_news_sentiment (ic-fspml_stock_news_sentiment_processed.csv)

- Se comprobaron los valores faltantes. Se observó como los valores faltantes aparecían en la columna "name" que representa el nombre de la compañía de la que se trata el ticker. Se analizó como esto ocurre para los mismos tickers en todas las ocasiones así que se deja como están.
- Se observaron NANs también en la columna "sector" que repsenta el sector de la compañía. Como más adelante filtraremos los tickers que buscamos no se realizó ninguna acción sobre ella.
- Filtramos los datos por los tickers que estamos investigando y el rango de fechas que queremos.

## mjw_stock/market_tweets_train (mjw_sotck_tweets_cleaned_part1.csv y part2 y 3)  

- Este conjunto de datos tenía NANs en la columna "writer" que representa el autor del tweet. Como no es de mayor utilidad esta columna se mantuvieron las filas con NAN.
- Las demás columnas parecen correctas. Se comprobo que no hubiera tweets repetidos ni filas duplicadas.

## StephanAkkerman_stock/market-tweets-data_train (stepahnakkerman_tweets_cleaned_part1.csv y part2)

- No se encuentran valores faltantes en ninguna de las columnas.
- Se comprobó la duplicidad de los datos. Se encontró una gran cantidad de tweets duplicados pero al analizar si se duplicaban en el mismo día la cantidad se redujo mucho. Esto es, un mismo tweet se publica mas de una vez pero en diferentes días. Se cree que el impacto que puede tener un tweet duplicado es pequeño pero se mantuvo los tweets duplicados que estuvieran en diferentes días mientras que se eliminaron los que estuvieran en el mismo día.
- Los datos entran todos en el rango de fechas que queremos asi que nos quedamos con todas las filas.


## raw_partner_headlines.csv
  - El único cambio realizado fue, con pandas, renombrar la columna "Unnamed: 0" a "index", cambiar sus valores para que vayan del 0 al n-1, siendo n el número de filas, y asignarlo como índice del dataset. No había ningún NA en ninguna de las columnas.

## analyst_ratings_processed
  - En este dataset sí había NAs, pero no por datos incompletos, sino porque algunas filas se habían dividido en dos, teniendo en estas filas el índice y el título de la noticia pero su fecha y ticker de stock correspondiente en la siguiente fila en las columnas *title* y *date*. Por ejemplo: ![image](assets\imgs\data_clean_analyst_ratings_processed.png)
  - Por lo tanto, con pandas se creó una copia del dataframe y se iteró por las filas, comprobando si había algún NA. En caso de que hubiera un NA en la fila x, se cogieron los valores de las columnas *title* y *date* de la fila x+1, se metían en las columnas *date* y *stock* de la fila x y se eliminaba la fila x+1. En total solo ocurrió esto en 1289 filas.
  - Finalmente, se reseteó el index de igual manera que en **raw_partner_headlines.csv**

 
**tweets_remaining_09042020_16072020.csv** y **tweets_labelled_09042020_16072020.csv**:

El proceso de limpieza fue similar para ambos archivos. Empecé con **tweets_labelled_09042020_16072020.csv** y al analizar los valores nulos me di cuenta de que la mayor parte de la columna *"sentiment »* estaba vacía. Decidí eliminarla por completo. Después he añadido el archivo **tweets_remaining_09042020_16072020.csv** al repositorio. No lo envié en primer lugar solo porque le faltaba la columna *"sentiment »*. Como decidimos realizar el análisis de sentimiento más tarde, opté por utilizar los archivos tal cual.

Al principio, analicé el número de valores NaN en cada columna. Como sólo la columna *"sentimiento"* estaba parcialmente vacía, no tuve que hacer más limpieza. A continuación, analicé los tweets y extraje los tickers de bolsa de la columna *"texto"* utilizando la biblioteca *yfinance*. Me di cuenta de que hay muchos tweets que contienen una referencia a más de un ticker. Por eso decidí explotar los dataframes, para que cada ticker tuviera su propia fila. 

Más tarde, me di cuenta de que, debido a que algunos textos contienen punto y coma (**";"**) e indicadores de nueva línea (**"\n"**), la estructura del dataframes se destruye. Decidí sustituir el punto y coma por una coma (**","**) y las nuevas líneas por espacios (**" "**). Después, he filtrado los datos para que solo contengan tickers de NASDAQ. Al final, he guardado los dataframes limpios en los archivos **tweets_remaining_cleared.csv** y **tweets_labelled_cleared.csv**. 


## Dataset final conjunto
  - Para juntar los datasets procesados se ha optado por crear un dataframe donde cada fila representa un dia, desde el inicio de rango de fechas de observación hasta el último día. Así cada columna representa un ticker que se está investigando y contiene un diccionario en formato string en el cual tiene el sigueinte formato:

  ```python
  {
    "val_adj_close": <VALOR AJUSTADO DEL TICKER>,
    "noticias": [
      {
        "noticia": <TEXTO DE LA NOTACIA>,
        "sentimiento": <SENTIMENTO DE LA NOTACIA>
      },
      {
        "noticia": <TEXTO DE LA NOTACIA>,
        "sentimiento": <SENTIMENTO DE LA NOTACIA>
       },
      ...
    ]
  }
  ```

  De esta manera creemos que podemos trabajar con un conjunto de datos que tiene toda la informacion requerida para un dia y un ticker de forma accesible, otras opciones serían trabajar con el join de todos los conjuntos de datos en base a su fecha pero esto nos generaria un dataframe con miles de columans de las cuales la gran mayoría estarían vacías.

  Debido a limites de Github hemos tenido que dividir el dataset en 10 partes para que ninguna de ellas supere el limite de 100MB por archivo.
