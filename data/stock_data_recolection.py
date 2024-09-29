import yfinance

tickets = ["MSFT", "GOOGL", "META", "AMZN", "NVDA", "IBM", "CRM"]

start_date = "2021-01-01"
end_date = "2024-01-01"

for ticket in tickets:
    data = yfinance.download(ticket, start=start_date, end=end_date)
    data.to_csv(f"data/{ticket}.csv")