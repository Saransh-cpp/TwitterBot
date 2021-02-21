import pybamm
import tweepy
from keys import Keys
import time
import numpy as np
import matplotlib.pyplot as plt
import random


auth = tweepy.OAuthHandler(Keys.CONSUMER_KEY, Keys.CONSUMER_SECRET)
auth.set_access_token(Keys.ACCESS_KEY, Keys.ACCESS_SECRET)
api = tweepy.API(auth)



def tweet_graph():

    x = random.randint(0,1)
    print(x)
    if x == 0:
        pybamm1()
        media = api.media_upload('foo.png')
    else:
        pybamm2()
        media = api.media_upload('foo1.png')

    tweet = 'random graph test'

    api.update_status(status=tweet, media_ids=[media.media_id])

