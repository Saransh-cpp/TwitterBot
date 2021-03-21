import pybamm
import tweepy
import time
import matplotlib.pyplot as plt
import importlib.util
import os

spec1 = importlib.util.spec_from_file_location(
    "RandomPlotGenerator.py", "Randomness/RandomPlotGenerator.py"
)
foo1 = importlib.util.module_from_spec(spec1)
spec1.loader.exec_module(foo1)

spec2 = importlib.util.spec_from_file_location(
    "Information.py", "Information/Information.py"
)
foo2 = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(foo2)

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_KEY = os.environ.get("ACCESS_KEY")
ACCESS_SECRET = os.environ.get("ACCESS_SECRET")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def tweet_graph():

    (
        parameter_values,
        time_of_png,
        parameter_number,
        cycle,
        solver,
        number,
    ) = foo1.random_plot_generator()
    print(time_of_png)
    info_string = (
        foo2.information(parameter_number, str(cycle) + " * " + str(number), solver)
        + ", at time = "
        + str(time_of_png)
    )
    # +"with parameter values: " + str(parameter_values)

    # Uncomment to tweet
    media = api.media_upload("foo.png")
    test_string = "https://github.com/Saransh-cpp/TwitterBot " + info_string
    tweet = test_string

    api.update_status(status=tweet, media_ids=[media.media_id])

    os.remove("foo.png")
    plt.clf()


# Simulate tweeting process
while True:
    print("Tweeting....")
    tweet_graph()
    time.sleep(3600)

# Uncomment to run the code only once
# tweet_graph()