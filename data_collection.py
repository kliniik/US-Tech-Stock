'''
This is an example of how the data was collected for a large subreddit (post level).
'''

import pandas as pd
import json

master_df = pd.DataFrame()
path = '/content/drive/MyDrive/project 1 data (sta 663)/The_Donald/'
chunks = []
for i in range(1,9):
  chunks.append(path + 'The_Donald_submissions.00' + str(i))

# chunks = ["/content/drive/MyDrive/project 1 data (sta 663)/The_Donald"]

# read line by line
for chunk in chunks:
    data = []
    with open(chunk, 'r') as file:
        for line in file:
            try:
                # Parse the JSON line and append to the list
                data.append(json.loads(line))
            except json.JSONDecodeError as e:
                # Output the error and skip this line
                print(f"Error decoding JSON: {e}") # usually due to post deletion or incorrect type

    df = pd.DataFrame(data)

    # 'created_utc' to a datetime column
    df['created_utc'] = pd.to_datetime(df['created_utc'], unit='s')

    # extract the year from the 'created_utc' column
    df['year'] = df['created_utc'].dt.year

    # filtering the years for 2014 to the current year
    df_filtered = df[(df['year'] >= 2014)]

    master_df = pd.concat([master_df, df_filtered])

# can sort and get the top 100 posts per year by score
master_df_sorted = master_df.sort_values(by=['year', 'score'], ascending=[True, False])
top_posts_per_year = master_df_sorted.groupby('year').head(100)