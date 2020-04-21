import nltk
import pandas as pd
import numpy as np
import string

data_source_url = "https://raw.githubusercontent.com/kolaveridi/kaggle-Twitter-US-Airline-Sentiment-/master/Tweets.csv"
airline_tweets = pd.read_csv(data_source_url, sep=",")

is_positive = tweets['airline_sentiment'].str.contains("positive")
is_negative = tweets['airline_sentiment'].str.contains("negative")
is_neutral = tweets['airline_sentiment'].str.contains("neutral")

positive_tweets = tweets[is_positive]
negative_tweets = tweets[is_negative]
neutral_tweets = tweets[is_neutral]

nltk.download("punkt")
nltk.download("stopwords")

useless_words = nltk.corpus.stopwords.words("english") + list(string.punctuation)