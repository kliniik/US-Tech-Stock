# Analysis of the Impact of the U.S. Ruling Party on the Perception of Technology Companies in the Stock Market

## Project Description
This project aims to analyze whether the ruling U.S. party influences the public perception of technology companies in the stock market. We focus on two presidential terms:
- Democratic Party – Barack Obama's presidency (2013–2017)
- Republican Party – Donald Trump's presidency (2017–2020)

To explore this, we examine stock market trends—specifically NASDAQ index stocks—as well as sentiment in financial news and market-related tweets from 2012 to 2020.

**Note:** The project has been developed in Spanish.

## Preliminary Hypothesis
We hypothesize that the party in power has a significant impact on NASDAQ stock prices and public sentiment (as reflected in financial news and market-related tweets). This influence may be tied to major political events, policy changes and regulatory decisions.

## Instructions for Replicating Experiments
To replicate our analysis, follow these steps:

### 1. Collect Data:
- Retrieve historical NASDAQ stock prices.
- Gather financial news articles and market-related tweets.

### 2. Filter Data:
Focus on data from the relevant time periods (Obama's and Trump's presidencies).

### 3. Formulate Hypotheses:
Define key research questions based on potential political influence on stock performance and sentiment.

### 4. Preprocess Data:
Structure a dataset containing:
  - Stock closing values
  - Company-related news articles
  - Sentiment analysis of news and tweets

### 5. Apply Analytical Techniques:
- Use Latent Dirichlet Allocation (LDA) for topic modeling.
- Perform sentiment analysis on news articles and tweets.
- Conduct time series analysis to track sentiment and stock fluctuations.

### 6. Analyze Results:
- Identify correlations between political events, stock trends, and sentiment shifts.
- Test whether our hypotheses hold.

## Dependencies and Environment
To collect and process data, install the required libraries listed in:
`data/requirements_data_recollection.txt`

Key Python packages used:
- `yfinance` – for retrieving stock data
- `huggingface_hub` – for sentiment analysis models
- `datasets` – for managing large-scale data

Collaborators
[Natalia Klinik](https://github.com/kliniik)  
[Luis Gutiérrez Llamedo](https://github.com/luisgtez)  
[Sergio González Suárez](https://github.com/sergioglezsuarez)  

