# IntegrationAPI/integrationapi/social_media.py

import tweepy

class TwitterAPI:
    def __init__(self, api_key, api_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def get_user_tweets(self, username, count=10):
        try:
            tweets = self.api.user_timeline(screen_name=username, count=count)
            return [tweet.text for tweet in tweets]
        except tweepy.TweepError as e:
            raise Exception(f"Twitter API Error: {str(e)}")
