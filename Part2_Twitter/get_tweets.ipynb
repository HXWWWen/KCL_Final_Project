import datetime
import tweepy
import time
from tweepy import OAuthHandler
import json
import os
import sys
import pandas as pd
import re

# 填写twitter提供的开发Key和secret
consumer_key = 'DyZCQkkGy1'
consumer_secret = 'XhOTIu77Bl1XRIaS90LS8zhdY'
access_token = '1427276807791804419-Z31lqkTl1'
access_token_secret = 'mqqxjyBGE9mcgbzHaYACuBfqeLS03E0RF8'

# 提交你的Key和secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
    
raw_data = pd.read_excel('raw_data_0610.xlsx')
data_used = raw_data[['url', 'title', 'title_after', 'catelogue', 'tag', 'n_rate', 'p_rate', 'adj_rate', 'm_rate', 'v_rate', 'adv_rate', 'len']]

def str_left(s):
    return re.sub('[^a-zA-Z]+', ' ', s)
    
def recent_popular(query):
    query = str_left(query)
    response = client.get_all_tweets_count(query, granularity="day")
    popular_num = 0
    for response in response.data:
        popular_num += response['tweet_count']
    
    return popular_num

bearer_token = "AAAAAAAAAAAAAAAAAAAAAGDLdQEAAAAAglWrqnsvNzp1EdbITDxjEOpq5L0%3DpxhvrLa6Vj10V9eTV5d6zHFvOnPFezfOL"
client = tweepy.Client(bearer_token)

data_used = data_used.dropna()

data_used = data_used.reset_index()


for i in range(len(data_used)):
    if i >= 9000:
        if i != 0 and i % 300 == 0:
            print(str(i)+'--'+str(len(data_used)))
            data_used.to_excel('current_data_v7.xlsx')
            time.sleep(900)
            data_used.loc[i, 'popular_num'] = recent_popular(data_used['title_after'][i])
            print(i)
        else:
            data_used.loc[i, 'popular_num'] = recent_popular(data_used['title_after'][i])
            print(i)
