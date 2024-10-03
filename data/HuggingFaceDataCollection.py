from datasets import load_dataset

def download_ds_to_csv(ds_name):
    ds = load_dataset(ds_name)
    for split in ds.keys():
        ds[split].to_csv(f"raw/{ds_name.replace("/","_")}_{split}.csv")

datasets = [
    "ic-fspml/stock_news_sentiment",
    "David-Chew-HL/Tech-Stocks-News",
    "mjw/stock_market_tweets",
    "StephanAkkerman/stock-market-tweets-data",
]

for ds_name in datasets:
    download_ds_to_csv(ds_name)
