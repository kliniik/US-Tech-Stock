import yfinance
import pandas as pd

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

# Set the number of parts
n_parts = 4  # Change this value to divide into more or fewer parts

# Split data into n parts and save
n = len(data) // n_parts
for i in range(n_parts):
    start_index = i * n
    end_index = (i + 1) * n if i < n_parts - 1 else len(data)
    data.iloc[start_index:end_index].to_csv(f"data/raw/NASDAQ_stock_data_part{i + 1}.csv")
