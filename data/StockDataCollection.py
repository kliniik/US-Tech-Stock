import yfinance

# Get tickers from NASDAQ
with open("data/nasdaq-listed-symbols_csv.csv") as f:
    lines = f.readlines()
    tickets = [line.split(",")[0] for line in lines[1:]]

# Select dates to get stock data
start_date = "2012-01-01"
end_date = "2021-01-01"

# Get stock data and reorder columns for a better .csv format
data = yfinance.download(tickets, start=start_date, end=end_date)
data.columns = [f"{ticker}_{type}" for type, ticker in data.columns]
data = data.reindex(sorted(data.columns), axis=1)
data.to_csv("data.csv")