import nltk
import pandas as pd
import string
from nltk.classify import NaiveBayesClassifier
import pickle
import os


useless_words = nltk.corpus.stopwords.words("english") + list(string.punctuation)


def build_bag_of_words_features_filtered(words: list):
    """
    Function which returns a dictionary of words that are not useless words
    :param words: a list of words
    :return: a dictionary
    """
    return {
        word: 1 for word in words
        if word not in useless_words}


def main():
    project_root_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

    data_source_url = "https://raw.githubusercontent.com/kolaveridi/kaggle-Twitter-US-Airline-Sentiment-/master" \
                      "/Tweets.csv"
    airline_tweets = pd.read_csv(data_source_url, sep=",")

    is_positive = airline_tweets['airline_sentiment'].str.contains("positive")
    is_negative = airline_tweets['airline_sentiment'].str.contains("negative")
    is_neutral = airline_tweets['airline_sentiment'].str.contains("neutral")

    positive_tweets = airline_tweets[is_positive]
    negative_tweets = airline_tweets[is_negative]
    neutral_tweets = airline_tweets[is_neutral]

    nltk.download("punkt")
    nltk.download("stopwords")

    tokenized_negative_tweets = []
    for text in negative_tweets['text']:
        tokenized_negative_tweets.append(nltk.word_tokenize(text))

    negative_features = [
        (build_bag_of_words_features_filtered(text), 'neg')
        for text in tokenized_negative_tweets
    ]

    tokenized_positive_tweets = []
    for text in positive_tweets['text']:
        tokenized_positive_tweets.append(nltk.word_tokenize(text))

    positive_features = [
        (build_bag_of_words_features_filtered(text), 'pos')
        for text in tokenized_positive_tweets
    ]

    tokenized_neutral_tweets = []
    for text in neutral_tweets['text']:
        tokenized_neutral_tweets.append(nltk.word_tokenize(text))

    neutral_features = [
        (build_bag_of_words_features_filtered(text), 'neu')
        for text in tokenized_neutral_tweets
    ]

    split = 2000

    sentiment_classifier = NaiveBayesClassifier.train(positive_features[:split]+negative_features[:split])

    accuracy_on_trained_data = nltk.classify.util.accuracy(sentiment_classifier, positive_features[:split] +
                                                           negative_features[:split])*100

    positive_features_verify = positive_features[split:]
    negative_features_verify = negative_features[split:2363]

    accuracy_on_test_data = nltk.classify.util.accuracy(sentiment_classifier, positive_features_verify +
                                                        negative_features_verify)*100

    print("The accuracy on the trained data is {}".format(accuracy_on_trained_data))

    print("The accuracy on the test data is {}".format(accuracy_on_test_data))

    filename = os.path.join(project_root_directory, "models", "naive_bayes_classifier.sav")

    print("Saving model to {}".format(filename))

    pickle.dump(sentiment_classifier, open(filename, 'wb'))
