from sentiment_analyst import TweetAnalyser


def test_classify_tweet():
    ta = TweetAnalyser("matthieu_run")
    result = ta.classify_tweet("All is happy and well.")
    assert result == 1
