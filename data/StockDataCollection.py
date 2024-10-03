import yfinance

tickets = ["MSFT", "GOOGL", "META", "AMZN", "NVDA", "IBM", "CRM"]

start_date = "2012-01-01"
end_date = "2021-01-01"

for i,ticket in enumerate(tickets):
    print(f"{i+1}/{len(tickets)} Recolectando datos de {ticket}...")
    data = yfinance.download(ticket, start=start_date, end=end_date)
    data.to_csv(f"data/raw/{ticket}.csv")