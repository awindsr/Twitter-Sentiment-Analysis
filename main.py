import tweepy
import csv
import pandas as pd
import numpy as np
import re 
import matplotlib.pyplot as plt
from Twitter_config import *


#Twitter Authentication using credentials in config file
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
API = tweepy.API(auth,wait_on_rate_limit=True)

#Hashtag to analyze
hashtag = input("Type your hashtag: ")

# Open/Create a file to 
csvFile = open("./Data/tweets.csv", 'w')

#Use csv Writer
csvWriter = csv.writer(csvFile)

#Searching for tweets based on the hashtag provided
for tweet in tweepy.Cursor(API.search_tweets,q=hashtag,count=10000,
                           lang="en",
                           ).items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])


colnames=['Date', 'Tweet'] 
data = pd.read_csv('./Data/tweets.csv',names=colnames, header=None)
df  = pd.DataFrame(data)
df.tail()

def remove_pattern(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)        
    return input_txt
def clean_tweets(tweets):
    #remove twitter Return handles (RT @xxx:)
    tweets = np.vectorize(remove_pattern)(tweets, "RT @[\w]*:") 
    
    #remove twitter handles (@xxx)
    tweets = np.vectorize(remove_pattern)(tweets, "@[\w]*")
    
    #remove URL links (httpxxx)
    tweets = np.vectorize(remove_pattern)(tweets, "https?://[A-Za-z0-9./]*")

    #remove special characters, numbers, punctuations (except for #)
    tweets = np.core.defchararray.replace(tweets, "[^a-zA-Z]", " ")
    
    return tweets

df['Tweet']= clean_tweets(df['Tweet']) #The function clean_tweets were put to use.
df.tail()
# df.to_csv("tweetcleaned.csv")


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

#Dictionary to store scores 
scores = []
# Declare variables for scores
compound_list = []
positive_list = []
negative_list = []
neutral_list = []
for i in range(df['Tweet'].shape[0]):
    compound = analyzer.polarity_scores(df['Tweet'][i])["compound"]
    pos = analyzer.polarity_scores(df['Tweet'][i])["pos"]
    neu = analyzer.polarity_scores(df['Tweet'][i])["neu"]
    neg = analyzer.polarity_scores(df['Tweet'][i])["neg"]
    
    scores.append({"Compound": compound,
                       "Positive": pos,
                       "Negative": neg,
                       "Neutral": neu
                  })

#Appending the scores into the dataframe for further analysis 
sentiments_score = pd.DataFrame.from_dict(scores)
df = df.join(sentiments_score)
df.head()

#Plotting the Sentiment scores.
plt.subplot(2,2,1)
plt.hist(df['Negative'], bins=20, alpha=0.5, label='Negative')
plt.title('Negative')

plt.subplot(2,2,2)
plt.hist(df['Positive'], bins=20, alpha=0.5, label='Positive')
plt.title('Positive')

plt.subplot(2,2,3)
plt.hist(df['Compound'], bins=20, alpha=0.5, label='Compound')
plt.title('Compound')

plt.subplot(2,2,4)
plt.hist(df['Neutral'], bins=20, alpha=0.5, label='Neutral')
plt.title('Neutral')

plt.show()