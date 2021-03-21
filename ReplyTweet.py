import pybamm
import tweepy
import time
import matplotlib.pyplot as plt
import importlib.util
import os

spec = importlib.util.spec_from_file_location(
    "RandomPlotGenerator.py.py", "Randomness/RandomPlotGenerator.py"
)
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)

# spec1 = importlib.util.spec_from_file_location(
#     "PlotGraph.py", "Randomness/PlotGraph.py"
# )
# foo1 = importlib.util.module_from_spec(spec1)
# spec1.loader.exec_module(foo1)

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_KEY = os.environ.get("ACCESS_KEY")
ACCESS_SECRET = os.environ.get("ACCESS_SECRET")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


FILE_NAME = "lastSeenId.txt"


def retrieve_last_seen_id(file_name):
    f_read = open(file_name, "r")
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, "w")
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def reply_to_tweet():
    print("replying...")
    last_seen_id = retrieve_last_seen_id(FILE_NAME)

    mention = api.mentions_timeline(last_seen_id, tweet_mode="extended")

    for singleMention in reversed(mention):
        print(
            str(singleMention.id) + " - " + singleMention.full_text
        )  # printing all my tweets
        last_seen_id = singleMention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if (
            "#batbot" in singleMention.full_text.lower()
            and "#help" in singleMention.full_text.lower()
        ):
            print("Help required")
            api.update_status(
                "@"
                + singleMention.user.screen_name
                + " Hi there! What would you like to simulate today?",
                singleMention.id,
            )
        elif (
            "#batbot" in singleMention.full_text.lower()
            and "plot" in singleMention.full_text.lower()
        ):
            if "model" in singleMention.full_text.lower():
                if "dfn" in singleMention.full_text.lower():
                    if "chen2020" in singleMention.full_text.lower():
                        parameter_values, time = foo.random_plot_generator(0, 0)
                    elif "marquis2019" in singleMention.full_text.lower():
                        parameter_values, time = foo.random_plot_generator(0, 1)
                    if "experiment" in singleMention.full_text.lower():
                        experiment = singleMention.full_text.split("[")
                        print(type(experiment), "\n", experiment)
                        experiment = experiment[1].split("]")
                        print(type(experiment), "\n", experiment)
                        experiment = experiment[0]
                        print(type(experiment), "\n", experiment)
                        experiment = experiment.split(",")
                        print(type(experiment), "\n", experiment)
                        # experiment = [
                        #     "Discharge at C/10 for 10 hours or until 3.3 V",
                        #     "Rest for 1 hour",
                        #     "Charge at 1 A until 4.1 V",
                        #     "Hold at 4.1 V until 50 mA",
                        #     "Rest for 1 hour",
                        # ]
                        # print(experiment)
                        time = foo.random_plot_generator(choice=1, cycle=experiment)

            media = api.media_upload("replyFoo.png")
            test_string = (
                "@"
                + singleMention.user.screen_name
                + " Here is your plot at time = "
                + str(time)
                + " seconds"
            )
            tweet = test_string

            api.update_status(
                status=tweet,
                media_ids=[media.media_id],
                in_reply_to_status_id=singleMention.id,
            )

            os.remove("replyFoo.png")
            plt.clf()
        else:
            api.update_status(
                "@"
                + singleMention.user.screen_name
                + " I'm sorry, could you be a bit more specific (remember this is only the testing phase)",
                singleMention.id,
            )


while True:
    reply_to_tweet()
    time.sleep(15)