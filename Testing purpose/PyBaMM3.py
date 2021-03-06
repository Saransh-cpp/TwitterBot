# import pybamm
# import tweepy
# from keys import Keys
# import time
# import numpy as np
# import matplotlib.pyplot as plt
# import random
# import os

# os.chdir(pybamm.__path__[0]+'/..')


# auth = tweepy.OAuthHandler(Keys.CONSUMER_KEY, Keys.CONSUMER_SECRET)
# auth.set_access_token(Keys.ACCESS_KEY, Keys.ACCESS_SECRET)
# api = tweepy.API(auth)

# def tut4():
#     parameter_sets = ['Chen2020', 'Ecker2015', 'Marquis2019', 'Mohtat2020']

#     i = random.randint(0, 10)
#     # single_parameter = parameter_sets[i]

#     chemistry = pybamm.parameter_sets.Chen2020

#     print(chemistry)

#     # parameter_values = pybamm.ParameterValues(chemistry=chemistry)

#     # model = pybamm.lithium_ion.DFN()
#     # sim = pybamm.Simulation(model, parameter_values=parameter_values)
#     # sim.solve([0, 3600])
#     # sim.plot()

#     model = pybamm.lithium_ion.DFN()
#     parameter_values = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Chen2020)

#     parameter_values["Current function [A]"] = i

#     sim = pybamm.Simulation(model, parameter_values=parameter_values)
#     sim.solve([0, 3600])
#     sim.plot()

# # tut4()

# def tut5():

#     experiment = pybamm.Experiment(
#         [
#             "Discharge at C/10 for 10 hours or until 3.3 V",
#             "Rest for 1 hour",
#             "Charge at 1 A until 4.1 V",
#             "Hold at 4.1 V until 50 mA",
#             "Rest for 1 hour",
#         ] * 3
#     )

#     model = pybamm.lithium_ion.DFN()

#     sim = pybamm.Simulation(model, experiment=experiment)

#     sim.solve()
#     sim.plot()

# tut5()

# def tweet_graph():

#     x = random.randint(0,1)
#     print(x)
#     if x == 0:
#         pybamm1()
#         media = api.media_upload('foo.png')
#     else:
#         pybamm2()
#         media = api.media_upload('foo1.png')

#     tweet = 'random graph test'

#     api.update_status(status=tweet, media_ids=[media.media_id])

# while True:
#     print('Tweeting....')
#     tweet_graph()
#     time.sleep(5)

import pybamm
import numpy as np
import os
os.chdir(pybamm.__path__[0]+'/..')

# create the model
model = pybamm.lithium_ion.DFN()

# set the default model parameters
param = model.default_parameter_values

# change the current function to be an input parameter
param["Current function [A]"] = "[input]"

# set up simlation
simulation = pybamm.Simulation(model, parameter_values=param)

# solve the model at the given time points, passing the current as an input
t_eval = np.linspace(0, 600, 300)
print(t_eval)
simulation.solve(t_eval, inputs={"Current function [A]": 1.6})

# plot
simulation.plot()
