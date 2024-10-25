**raw_partner_headlines.csv:**
  - El único cambio realizado fue, con pandas, renombrar la columna "Unnamed: 0" a "index", cambiar sus valores para que vayan del 0 al n-1, siendo n el número de filas, y asignarlo como índice del dataset. No había ningún NA en ninguna de las columnas.

**analyst_ratings_processed:**
  - En este dataset sí había NAs, pero no por datos incompletos, sino porque algunas filas se habían dividido en dos, teniendo en estas filas el índice y el título de la noticia pero su fecha y ticker de stock correspondiente en la siguiente fila en las columnas *title* y *date*. Por ejemplo: ![image](https://github.com/user-attachments/assets/c57a60ae-d058-4905-9c67-aae58e5fed31)
  - Por lo tanto, con pandas se creó una copia del dataframe y se iteró por las filas, comprobando si había algún NA. En caso de que hubiera un NA en la fila x, se cogieron los valores de las columnas *title* y *date* de la fila x+1, se metían en las columnas *date* y *stock* de la fila x y se eliminaba la fila x+1. En total solo ocurrió esto en 1289 filas.
  - Finalmente, se reseteó el index de igual manera que en **raw_partner_headlines.csv**
