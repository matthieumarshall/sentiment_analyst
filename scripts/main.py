import nltk
import pandas as pd
import numpy as np
import string
from nltk.classify import NaiveBayesClassifier

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

def build_bag_of_words_features_filtered(words):
    return {
        word:1 for word in words \
        if not word in useless_words}

tokenized_negative_tweets = []
for text in negative_tweets['text']:
        tokenized_negative_tweets.append(nltk.word_tokenize(text))

negative_features = [
    (build_bag_of_words_features_filtered(text), 'neg') \
    for text in tokenized_negative_tweets
]

tokenized_positive_tweets = []
for text in positive_tweets['text']:
        tokenized_positive_tweets.append(nltk.word_tokenize(text))

positive_features = [
    (build_bag_of_words_features_filtered(text), 'pos') \
    for text in tokenized_positive_tweets
]

tokenized_neutral_tweets = []
for text in neutral_tweets['text']:
        tokenized_neutral_tweets.append(nltk.word_tokenize(text))

neutral_features = [
    (build_bag_of_words_features_filtered(text), 'neu') \
    for text in tokenized_neutral_tweets
]

split = 2000

sentiment_classifier = NaiveBayesClassifier.train(positive_features[:split]+negative_features[:split])

nltk.classify.util.accuracy(sentiment_classifier, positive_features[:split]+negative_features[:split])*100

positive_features_verify = positive_features[split:]
negative_features_verify = negative_features[split:2363]

nltk.classify.util.accuracy(sentiment_classifier, positive_features_verify+negative_features_verify)*100