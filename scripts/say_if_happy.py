import tweepy
import pickle
from data.credentials import *
import os
import nltk
from scripts.build_classifier import build_bag_of_words_features_filtered

project_root_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

filename = os.path.join(project_root_directory, "models", "naive_bayes_classifier.sav")

sentiment_classifier = pickle.load(open(filename, 'rb'))

results = api.search(q='cheese', count=100)

twitter_user = api.get_user("matthieu_run")

new_tweets = api.user_timeline(screen_name="matthieu_run", count=5)

latest_tweet = new_tweets[0].text

text = "I am happy today"

text2 = "I am upset today"

tokenised_tweet = nltk.word_tokenize(latest_tweet)

tokenised_text = nltk.word_tokenize(text)

tokenised_text2 = nltk.word_tokenize(text2)

bag_of_words_latest_tweet = build_bag_of_words_features_filtered(tokenised_tweet)

bag_of_words = build_bag_of_words_features_filtered(tokenised_text)

bag_of_words2 = build_bag_of_words_features_filtered(tokenised_text2)


result = sentiment_classifier.classify(bag_of_words)

result2 = sentiment_classifier.classify(bag_of_words2)

result3 = sentiment_classifier.classify(bag_of_words_latest_tweet)

print("{} has been classified as {}".format(text, result))
print("{} has been classified as {}".format(text2, result2))
print("{} has been classified as {}".format(latest_tweet, result3))
