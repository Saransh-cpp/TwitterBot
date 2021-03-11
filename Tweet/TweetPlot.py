import pybamm
import tweepy
import time
import matplotlib.pyplot as plt
import importlib.util


spec = importlib.util.spec_from_file_location("Chen2020params.py", "keys.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)

spec1 = importlib.util.spec_from_file_location("RandomPlotGenerator.py", "Randomness/RandomPlotGenerator.py")
foo1 = importlib.util.module_from_spec(spec1)
spec1.loader.exec_module(foo1)

spec2 = importlib.util.spec_from_file_location("RandomPlotGenerator.py", "Information/Information.py")
foo2 = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(foo2)


auth = tweepy.OAuthHandler(foo.Keys.CONSUMER_KEY, foo.Keys.CONSUMER_SECRET)
auth.set_access_token(foo.Keys.ACCESS_KEY, foo.Keys.ACCESS_SECRET)
api = tweepy.API(auth)

def tweet_graph():

    foo1.random_plot_generator()
    print(foo2.information('Chen2020'))

    # Uncomment to tweet
    # media = api.media_upload('foo.png')
    # tweet = foo2.information('Chen2020')

    # api.update_status(status=tweet, media_ids=[media.media_id])


while True:
    print('Tweeting....')
    tweet_graph()
    time.sleep(5)