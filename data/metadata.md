# Fuente de los Datos:
Origen de los datos (p. ej., sitio web, API, dataset público).
- Valores de tickets de stocks (AMZN, CRM, GOOGL...): Recogidos a través de la librería `yfinance` de Python que use la API de yahoo.
# Fecha de Recogida:
- Valores de tickets de stocks (AMZN, CRM, GOOGL...): Recolectado datos desde el 2021-01-01 al 2024-01-01.
# Formato de los Datos:
- Valores de tickets de stocks (AMZN, CRM, GOOGL...): Archivos CSV, uno por cada ticket denominado con el mismo nombre.
# Licencia de Uso:
- Valores de tickets de stocks (AMZN, CRM, GOOGL...): La librería usada `yfinance` usa licencia Apache 2.0 pero emplea la API publica de yahoo.
# Descripción de las Variables o Atributos:
- Valores de tickets de stocks (AMZN, CRM, GOOGL...):
    - Date: La fecha del registro.
    - Open: El precio al que se abrió la acción en esa fecha.
    - High: El precio más alto al que llegó la acción durante el día.
    - Low: El precio más bajo al que llegó la acción durante el día.
    - Close: El precio al que cerró la acción al final del día.
    - Adj Close: El precio de cierre ajustado por dividendos, splits u otros factores.
    - Volume: El número total de acciones intercambiadas ese día.