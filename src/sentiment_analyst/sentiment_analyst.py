import tweepy
import pickle
import argparse
from src.data.credentials import (
    consumer_key,
    consumer_secret,
    access_token_secret,
    access_token,
)
import os
import nltk
import statistics
from src.sentiment_analyst.build_classifier import build_bag_of_words_features_filtered


class TweetAnalyser:
    def __init__(self, twitter_handle):
        self.sentiment_classifier = None
        self.twitter_handle = twitter_handle

    def classify_tweet(self, text):
        tokenised = nltk.word_tokenize(text)
        bag_of_words = build_bag_of_words_features_filtered(tokenised)
        result = self.sentiment_classifier.classify(bag_of_words)
        numberator = {"pos": 1, "neg": 0}
        return numberator[result]

    def main(self, twitter_handle: str):
        """

        :param twitter_handle:
        :return:
        """

        project_root_directory = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), ".."
        )

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)

        filename = os.path.join(
            project_root_directory, "models", "naive_bayes_classifier.sav"
        )
        self.sentiment_classifier = pickle.load(open(filename, "rb"))

        new_tweets = api.user_timeline(screen_name=twitter_handle, count=5)

        latest_tweets = [new_tweets[i].text for i in range(0, 4)]

        tweet_sentiments = [self.classify_tweet(tweet) for tweet in latest_tweets]

        number = statistics.mean(tweet_sentiments)
        if number > 0.5:
            tweets_are = "positive"
        elif number < 0.5:
            tweets_are = "negative"
        else:
            raise ValueError(f"The number {number} is wrong")
        print(f"The last 5 tweets of {twitter_handle} have generally been {tweets_are}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get arguments of package call.")
    parser.add_argument(
        "--twitter-handle",
        type=str,
        help="The twitter handle of the user you want to analyse the tweets of",
    )
    args = parser.parse_args()
    TweetAnalyser(args.twitter_handle)
