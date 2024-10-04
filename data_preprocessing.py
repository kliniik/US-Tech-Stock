'''
This code outlines the data pre-processing work done (text: cleaning/ tokenizing and images: extracting text from the image using pytesseract). 
The dataset in the repo is the processed one.
'''

! pip install datasets q

from datasets import load_dataset

dataset = load_dataset("mo-mittal/reddit_political_subs", trust_remote_code=True)

# Install Tesseract OCR
!sudo apt install tesseract-ocr

# Install pytesseract
!pip install pytesseract

import pytesseract
from concurrent.futures import ThreadPoolExecutor

# this assumes 'dataset' is already loaded and contains the earlier data. I had done the preprocessing on an earlier version of the current dataset.

#### you can also check how many CPU cores are available for the threadpool processor

# import os
# num_cores = os.cpu_count()
# print(f"Number of available CPU cores: {num_cores}")


def ocr_image(index):
    try:
        # Retrieve the image and associated URL from the dataset.
        image_pil = dataset['train'][index]['image']
        url = dataset['train'][index]['url']

        # Check if 'image_text' is empty and if the word 'imgur' is in the 'url' field.
        if (dataset['train'][index]['image_text'] == '') and ('imgur' in url):
            text = pytesseract.image_to_string(image_pil)
            print(f'Sublime! Processed img at {index}')
            return text
    except Exception as e:
        return None

# Create a ThreadPoolExecutor to parallelize image processing.
num_workers = 8  # Adjust this number based on your machine's capabilities.
imgur_text = []

with ThreadPoolExecutor(max_workers=num_workers) as executor:
    # Use map to apply 'ocr_image' function to each index.
    results = list(executor.map(ocr_image, range(len(dataset['train']))))

# Now 'results' contains the OCR results or None for each image.
# Filter out None values and add the text to 'imgur_text' list.
imgur_text.extend(filter(None, results))

# 'imgur_text' now contains all the OCR results. This can take quite a while to process! (About 7503 images and 12 hours for an 8 core CPU)

## for text cleaning 

import pandas as pd

df = pd.DataFrame(dataset['train'].remove_columns(['image']))
# df.head()

results_list = list(results)

for i, text in enumerate(results_list):
    if text is not None:
        df.loc[i, 'image_text'] = text

# df.to_csv('reddit_political_subs.csv', index=False)
import pandas as pd

df = pd.read_csv('reddit_political_subs.csv')

import nltk
nltk.download('stopwords')

import re
from nltk.corpus import stopwords
import string

def clean_text(text):
    text = re.sub(r'\\n', ' ', text)
    text = re.sub(r'\\x..', '', text)
    text = re.sub(r'[@|\\]', '', text)

    text = text.translate(str.maketrans('', '', string.punctuation))
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word not in stop_words])

    text = ' '.join(text.split())
    text = text.lower()

    return text

df['image_text'] = df['image_text'].apply(clean_text)
