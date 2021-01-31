from sentiment import TweetAnalyser
from unittest.mock import patch
from unittest import mock


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
