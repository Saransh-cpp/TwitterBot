import pybamm
import tweepy
import time
import matplotlib.pyplot as plt
import importlib.util
import os

spec = importlib.util.spec_from_file_location("Chen2020params.py", "keys.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)

spec1 = importlib.util.spec_from_file_location("RandomPlotGenerator.py", "Randomness/RandomPlotGenerator.py")
foo1 = importlib.util.module_from_spec(spec1)
spec1.loader.exec_module(foo1)

spec2 = importlib.util.spec_from_file_location("Information.py", "Information/Information.py")
foo2 = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(foo2)


auth = tweepy.OAuthHandler(foo.Keys.CONSUMER_KEY, foo.Keys.CONSUMER_SECRET)
auth.set_access_token(foo.Keys.ACCESS_KEY, foo.Keys.ACCESS_SECRET)
api = tweepy.API(auth)

def tweet_graph():

    parameter_values, time_of_png, parameter_number, cycle, solver = foo1.random_plot_generator()
    print(time_of_png)
    info_string = foo2.information(parameter_number, cycle, solver) + ', at time = ' + str(time_of_png) 
    # + 'with parameter values: ' + str(parameter_values)

    # Uncomment to tweet
    media = api.media_upload('fooimage.png')
    test_string = 'https://github.com/Saransh-cpp/TwitterBot ' + info_string 
    tweet = test_string

    api.update_status(status=tweet, media_ids=[media.media_id])

    os.remove('fooimage.png')
    os.remove('foo.pdf')
    plt.clf()

# Simulate tweeting process
while True:
    print('Tweeting....')
    tweet_graph()
    time.sleep(15)

# Uncomment to run the code only once
# tweet_graph()