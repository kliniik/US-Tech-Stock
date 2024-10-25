**raw_partner_headlines.csv:**
  - El único cambio realizado fue, con pandas, renombrar la columna "Unnamed: 0" a "index", cambiar sus valores para que vayan del 0 al n-1, siendo n el número de filas, y asignarlo como índice del dataset. No había ningún NA en ninguna de las columnas.

**analyst_ratings_processed:**
  - En este dataset sí había NAs, pero no por datos incompletos, sino porque algunas filas se habían dividido en dos, teniendo en estas filas el índice y el título de la noticia pero su fecha y ticker de stock correspondiente en la siguiente fila en las columnas *title* y *date*. Por ejemplo: ![image](https://github.com/user-attachments/assets/c57a60ae-d058-4905-9c67-aae58e5fed31)
  - Por lo tanto, con pandas se creó una copia del dataframe y se iteró por las filas, comprobando si había algún NA. En caso de que hubiera un NA en la fila x, se cogieron los valores de las columnas *title* y *date* de la fila x+1, se metían en las columnas *date* y *stock* de la fila x y se eliminaba la fila x+1. En total solo ocurrió esto en 1289 filas.
  - Finalmente, se reseteó el index de igual manera que en **raw_partner_headlines.csv**

 
**tweets_remaining_09042020_16072020.csv** y **tweets_labelled_09042020_16072020.csv**:

El proceso de limpieza fue similar para ambos archivos. Empecé con **tweets_labelled_09042020_16072020.csv** y al analizar los valores nulos me di cuenta de que la mayor parte de la columna *"sentiment »* estaba vacía. Decidí eliminarla por completo. Después he añadido el archivo **tweets_remaining_09042020_16072020.csv** al repositorio. No lo envié en primer lugar solo porque le faltaba la columna *"sentiment »*. Como decidimos realizar el análisis de sentimiento más tarde, opté por utilizar los archivos tal cual.

Al principio, analicé el número de valores NaN en cada columna. Como sólo la columna *"sentimiento"* estaba parcialmente vacía, no tuve que hacer más limpieza. A continuación, analicé los tweets y extraje los tickers de bolsa de la columna *"texto"* utilizando la biblioteca *yfinance*. Me di cuenta de que hay muchos tweets que contienen una referencia a más de un ticker. Por eso decidí explotar los dataframes, para que cada ticker tuviera su propia fila. 

Más tarde, me di cuenta de que, debido a que algunos textos contienen punto y coma (**";"**) e indicadores de nueva línea (**"\n"**), la estructura del dataframes se destruye. Decidí sustituir el punto y coma por una coma (**","**) y las nuevas líneas por espacios (**" "**). Después, he filtrado los datos para que solo contengan tickers de NASDAQ. Al final, he guardado los dataframes borrados en los archivos **tweets_remaining_cleared.csv** y **tweets_labelled_cleared.csv**. 
