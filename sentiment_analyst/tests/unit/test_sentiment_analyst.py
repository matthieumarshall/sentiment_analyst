from sentiment import TweetAnalyser
from unittest.mock import patch
from unittest import mock
import pytest


def test_classify_tweet():
    ta = TweetAnalyser("matthieu_run")
    result = ta.classify_tweet("All is happy and well.")
    assert result == 1


@patch("sentiment.pickle")
@patch("sentiment.os.path.abspath")
def test_set_classifier(mock_os_abspath, mock_pickle):
    mock_os_abspath.return_value = (
        "C:\\Users\\matth\\source\\repos\\sentiment_analyst\\sentiment_analyst\\ELSE.py"
    )
    mo = mock.mock_open(read_data="1")
    with patch("builtins.open", mo):
        TweetAnalyser("matthieu_run")
    mo.assert_called_once()
    mock_pickle.load.assert_called_once()


class TestTweet:
    def __init__(self, tweet):
        self.text = tweet


@pytest.mark.parametrize(
    "new_tweets, expected_result",
    [
        (
            [
                TestTweet("happy"),
                TestTweet("happy"),
                TestTweet("happy"),
                TestTweet("happy"),
                TestTweet("happy"),
            ],
            "positive",
        ),
        (
            [
                TestTweet("sad"),
                TestTweet("sad"),
                TestTweet("sad"),
                TestTweet("sad"),
                TestTweet("sad"),
            ],
            "negative",
        ),
    ],
)
@patch("sentiment.tweepy")
def test_main(mock_tweepy, new_tweets, expected_result):
    ta = TweetAnalyser("matthieu_run")
    mock_api = mock.MagicMock()
    mock_tweepy.API.return_value = mock_api
    mock_api.user_timeline.return_value = new_tweets
    result = ta.main()
    mock_tweepy.OAuthHandler.assert_called_once()
    assert (
        result
        == f"The last 5 tweets of matthieu_run have generally been {expected_result}"
    )
