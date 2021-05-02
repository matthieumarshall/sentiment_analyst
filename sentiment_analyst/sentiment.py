import tweepy
import pickle
import argparse
from data.credentials import (
    consumer_key,
    consumer_secret,
    access_token_secret,
    access_token,
)
import os
import nltk
import statistics
from build_classifier import build_bag_of_words_features_filtered
from tools.log_setup import logger


class TweetAnalyser:
    def __init__(self, twitter_handle):
        self.sentiment_classifier = None
        logger.info(f"Initiating with a twitter handle of {twitter_handle}")
        self.twitter_handle = twitter_handle
        self.set_classifier()
        logger.debug("Classifier successfully read from pickle")

    def classify_tweet(self, text):
        logger.debug(f"Classifying tweet : {text}")
        tokenised = nltk.word_tokenize(text)
        bag_of_words = build_bag_of_words_features_filtered(tokenised)
        result = self.sentiment_classifier.classify(bag_of_words)
        numberator = {"pos": 1, "neg": 0}
        logger.debug(f"'{text}' has been classified as {numberator}")
        return numberator[result]

    def set_classifier(self):
        project_root_directory = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), ""
        )
        filename = os.path.join(
            project_root_directory, "models", "naive_bayes_classifier.sav"
        )
        with open(filename, "rb") as f:
            self.sentiment_classifier = pickle.load(f)

    def main(self):
        """
        :return: str : A message summarising the sentiment of the last 5 tweets from that twitter handle
        """

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)
        logger.debug("Tweepy API initialised")
        new_tweets = api.user_timeline(screen_name=self.twitter_handle, count=5)

        latest_tweets = [new_tweets[i].text for i in range(0, 4)]
        logger.debug(f"Latest tweets are {latest_tweets}")

        tweet_sentiments = [self.classify_tweet(tweet) for tweet in latest_tweets]
        logger.debug(f"The sentiments of these tweets are {tweet_sentiments}")

        number = statistics.mean(tweet_sentiments)
        logger.debug(f"The mean of these sentiments is {number}")
        if number > 0.5:
            tweets_are = "positive"
        elif number < 0.5:
            tweets_are = "negative"
        else:
            logger.error(f"The number {number} is wrong")
            raise ValueError(f"The number {number} is wrong")

        logger.info(
            f"The last 5 tweets of {self.twitter_handle} have generally been {tweets_are}"
        )
        return f"The last 5 tweets of {self.twitter_handle} have generally been {tweets_are}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get arguments of package call.")
    parser.add_argument(
        "--twitter-handle",
        type=str,
        help="The twitter handle of the user you want to analyse the tweets of",
    )
    args = parser.parse_args()
    logger.debug(f"sentiment_analyst/sentiment.py called with arguments : {args}")
    ta = TweetAnalyser(args.twitter_handle)
    result = ta.main()
