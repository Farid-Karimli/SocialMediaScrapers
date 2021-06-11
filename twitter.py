import snscrape.modules.twitter as sntwitter
import pandas as pd

import banks

# Using TwitterSearchScraper to scrape data and append tweets to list
def get_tweets(search_prompt):
    tweets_list2 = []
    prompt = search_prompt
    for i, tweet in enumerate(
            sntwitter.TwitterSearchScraper(search_prompt).get_items()):
        if i > 20:
            break
        tweets_list2.append([tweet.date, tweet.id, tweet.content])

    return tweets_list2

def retrieve():
    print('Starting Twitter retrieval')
    print()
    for prompt in banks.banks:

        if prompt == 'Million':
            search_prompt = 'milliön near:me'
        else:
            search_prompt = prompt

        tweets_list = get_tweets(search_prompt)
        filename = 'Twitter/' + prompt + ".csv"

        if tweets_list:
            tweets_pd = pd.DataFrame(tweets_list, columns=['Tweet Date', 'Tweet Id', 'Text'])
            # print(tweets_pd.head())
            tweets_pd.to_csv(filename)
            print('Found tweets about', prompt)
        else:
            print('Couldn\'t find tweets about', prompt)
            print(tweets_list)

