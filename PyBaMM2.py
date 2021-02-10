import pybamm
import tweepy
from keys import Keys
import time
# from IPython.display import display
import numpy as np
import matplotlib.pyplot as plt
# import sympy as sp
# from sympy.interactive import printing
# printing.init_printing(use_latex=True)

auth = tweepy.OAuthHandler(Keys.CONSUMER_KEY, Keys.CONSUMER_SECRET)
auth.set_access_token(Keys.ACCESS_KEY, Keys.ACCESS_SECRET)
api = tweepy.API(auth)