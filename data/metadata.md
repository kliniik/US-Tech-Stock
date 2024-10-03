# Fuente de los Datos:
Origen de los datos (p. ej., sitio web, API, dataset público).

- Valores de tickers de stocks (AMZN, CRM, GOOGL...): Recogidos a través de la librería `yfinance` de Python que use la API de yahoo.

- David-Chew-HL/Tech-Stocks-News_train.csv, ic-fspml/stock_news_sentiment_*.csv , mjw_stock/market_tweets_train.csv y StephanAkkerman_stock/market-tweets-data_train: Recodigo a través de la libreria `datasets` de Python con conexión a la API de Hugging Face.

- Headlines de noticias financieras de benzinga.com de stocks del NYSE, NASDAQ y otros: https://www.kaggle.com/datasets/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests

# Fecha de Recogida:
- Valores de tickers de stocks: Datos desde el 2012-01-01 al 2021-01-01.

- David-Chew-HL/Tech-Stocks-News: Datos desde el 2015-01-01 al 2024-01-29

- ic-fspml/stock_news_sentiment: datos desde el 2009 al 2020 

- mjw_stock/market_tweets_train: datos desde el 2015 al 2019

- StephanAkkerman_stock/market-tweets-data_train: datos del año 2020

- Headlines de noticias: 2009-02-14 a 2020-06-11

# Formato de los Datos:
- Valores de tickets de stocks: Archivos CSV.

- David-Chew-HL/Tech-Stocks-News_train: Archivo CSV.

- ic-fspml/stock_news_sentiment_*: Archivo CSV. Dividido en train, validation y test.

- mjw_stock/market_tweets_train: Archivo CSV.

- StephanAkkerman_stock/market-tweets-data_train: Archivo CSV.

- Headlines de noticias: Dos CSV.

# Licencia de Uso:
- Valores de tickets de stocks: La librería usada `yfinance` usa licencia Apache 2.0 pero emplea la API publica de yahoo.

- David-Chew-HL/Tech-Stocks-News: Licencia Apache 2.0.

- ic-fspml/stock_news_sentiment: Licencia no conocida.

- mjw_stock/market_tweets_train: Licencia Apache 2.0.

- StephanAkkerman_stock/market-tweets-data_train: Licencia Creative Commons Attribution 4.0

- Headlines de noticias: CC0: Public Domain

# Descripción de las Variables o Atributos:
- Valores de tickers de stocks:
    - Date: La fecha del registro.

    Para cada ticker differente tenemos sus variables <ticker\>_<variable\>:

    - Open: El precio al que se abrió la acción en esa fecha.
    - High: El precio más alto al que llegó la acción durante el día.
    - Low: El precio más bajo al que llegó la acción durante el día.
    - Close: El precio al que cerró la acción al final del día.
    - Adj Close: El precio de cierre ajustado por dividendos, splits u otros factores.
    - Volume: El número total de acciones intercambiadas ese día.

- David-Chew-HL/Tech-Stocks-News:
    - headline: Titulo del articulo 
    - date: Fecha de publicacion

- ic-fspml/stock_news_sentiment_*:
    - ticker: Ticket del stock que habla el articulo
    - name: Nombre de la compañía del ticker
    - type: Tipo de instrumento financiero (e.g., acciones, fondo mutuo, ETF).
    - sector: Sector de la empresa
    - article_date: Fecha del articulo
    - article_headline: Titutlo del articulo
    - label: Sentimiento del articulo

- mjw_stock/market_tweets_train:
    - tweet_id: ID del tweet
    - writer: Autor del tweet
    - post_date: Fecha del tweet
    - body: Cuerpo del tweet
    - comment_num: Numeros de comentarios
    - retweet_num: Numeros de retweets
    - like_num: Numeros de likes
    - ticker_symbol: Ticker del stock sobre el que se habla en el tweet

- StephanAkkerman_stock/market-tweets-data_train:
    - created_at: Fecha del tweet
    - text: Contenido del tweet
 
- Headlines de noticias:
    - raw_partner_headlines.csv:
      - id: ID del headline
      - headline: Headline del artículo
      - url: URL al artículo
      - publisher: Autor o publicante del artículo
      - date: Fecha del artículo
      - stock: Ticker del stock
    - analyst_ratings_processed.csv:
      - #: ID del headline
      - title: Headline del artículo
      - date: Fecha del artículo
      - stock: Ticker del stock
