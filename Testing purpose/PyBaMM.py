import pybamm
import tweepy
from keys import Keys
import time
import numpy as np
import matplotlib.pyplot as plt

auth = tweepy.OAuthHandler(Keys.CONSUMER_KEY, Keys.CONSUMER_SECRET)
auth.set_access_token(Keys.ACCESS_KEY, Keys.ACCESS_SECRET)
api = tweepy.API(auth)

# mention = api.mentions_timeline()

# Setting up a PyBaMM example
model = pybamm.BaseModel()

x = pybamm.Variable("x")
y = pybamm.Variable("y")

dxdt = 4 * x - 2 * y
dydt = 3 * x - y

model.rhs = {x: dxdt, y: dydt}
model.initial_conditions = {x: pybamm.Scalar(1), y: pybamm.Scalar(2)}
model.variables = {"x": x, "y": y, "z": x + 4 * y}

disc = pybamm.Discretisation()  # use the default discretisation
disc.process_model(model)

solver = pybamm.ScipySolver()
t = np.linspace(0, 1, 20)
solution = solver.solve(model, t)

t_sol, y_sol = solution.t, solution.y  # get solution times and states
x = solution["x"]  # extract and process x from the solution
y = solution["y"]  # extract and process y from the solution

t_fine = np.linspace(0, t[-1], 1000)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 4))
ax1.plot(t_fine, 2 * np.exp(t_fine) - np.exp(2 * t_fine), t_sol, x(t_sol), "o")
ax1.set_xlabel("t")
ax1.legend(["2*exp(t) - exp(2*t)", "x"], loc="best")

ax2.plot(t_fine, 3 * np.exp(t_fine) - np.exp(2 * t_fine), t_sol, y(t_sol), "o")
ax2.set_xlabel("t")
ax2.legend(["3*exp(t) - exp(2*t)", "y"], loc="best")

plt.tight_layout()
# img = plt.show()

plt.savefig('foo.png', bbox_inches='tight') # Saving the graph
# PyBaMM model ends


def tweet_graph():

    media = api.media_upload('foo.png')
    tweet = 'test again'

    api.update_status(status=tweet, media_ids=[media.media_id])


while True:
    print('Tweeting....')
    tweet_graph()
    time.sleep(5)

