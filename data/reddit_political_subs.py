import pandas as pd
import datasets
from datasets import Features, Value, ClassLabel, Image, DownloadManager
import logging
import requests
from PIL.Image import Image as PIL_Image
import io

_URLS = {
    "my_data": "https://drive.google.com/uc?export=download&id=1t7qllYbonoCgNzzh7w9NhmnMZ4pmqERo",
}

class RedditPoliticalSubs(datasets.GeneratorBasedBuilder):
    """A Dataset builder for a DataFrame with Reddit data."""

    VERSION = datasets.Version('1.0.0')

    def _info(self):
        return datasets.DatasetInfo(
            description=("This dataset contains Reddit posts with various attributes."),
            features=Features({
                "author": Value("string"),
                "created_utc": Value("string"),
                "domain": Value("string"),
                "title": Value("string"),
                "selftext": Value("string"),
                "subreddit": Value("string"),
                "score": Value("int32"),
                "num_comments": Value("int32"),
                "ups": Value("float32"),
                "downs": Value("float32"),
                "permalink": Value("string"),
                "is_self": Value("bool"),
                "url": Value("string"),
                "subreddit_subscribers": Value("float32"),
                "upvote_ratio": Value("float32"),
                "is_original_content": Value("string"),
                "media": Value("string"),
                "selftext_html": Value("string"),
                "author_flair_text": Value("string"),
                "link_flair_text": Value("string"),
                "image": Image(),
                "image_text": Value("string"),
            }),
            supervised_keys=None,
            homepage='https://www.reddit.com/',
            citation="",
        )

    def _split_generators(self, dl_manager: DownloadManager):
        downloaded_file = dl_manager.download_and_extract(_URLS["my_data"])
        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                gen_kwargs={"dataframe_path": downloaded_file}, # light config
            ),
        ]

    def _generate_examples(self, dataframe_path): #light config
        """Yields examples."""
        df = pd.read_csv(dataframe_path)

        for idx, row in df.iterrows():

          yield idx, {
                "author": row["author"],
                "created_utc": row["created_utc"],
                "domain": row["domain"] if pd.notna(row["domain"]) else "",
                "title": row["title"],
                "selftext": row["selftext"] if pd.notna(row["selftext"]) else "",
                "subreddit": row["subreddit"],
                "score": row["score"],
                "num_comments": row["num_comments"],
                "ups": row["ups"] if pd.notna(row["ups"]) else 0,
                "downs": row["downs"] if pd.notna(row["downs"]) else 0,
                "permalink": row["permalink"],
                "is_self": row["is_self"],
                "url": row["url"] if pd.notna(row["url"]) else "",
                "subreddit_subscribers": row["subreddit_subscribers"] if pd.notna(row["subreddit_subscribers"]) else 0.0,
                "upvote_ratio": row["upvote_ratio"] if pd.notna(row["upvote_ratio"]) else 0.0,
                "is_original_content": row["is_original_content"] if pd.notna(row["is_original_content"]) else False,
                "media": row["media"] if pd.notna(row["media"]) else "",
                "selftext_html": row["selftext_html"] if pd.notna(row["selftext_html"]) else "",
                "author_flair_text": row["author_flair_text"] if pd.notna(row["author_flair_text"]) else "",
                "link_flair_text": row["link_flair_text"] if pd.notna(row["link_flair_text"]) else "",
                "image": row['url'] if pd.notna(row['url']) else "",
                "image_text": row['image_text'] if pd.notna(row['image_text']) else "",
            }