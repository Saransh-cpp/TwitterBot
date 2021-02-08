import tweepy
from keys import Keys

auth = tweepy.OAuthHandler(Keys.CONSUMER_KEY, Keys.CONSUMER_SECRET)
auth.set_access_token(Keys.ACCESS_KEY, Keys.ACCESS_SECRET)
api = tweepy.API(auth)



