# import pybamm
# import tweepy
# from keys import Keys
# import time
# import numpy as np
# import os
# import matplotlib.pyplot as plt
# import random

# os.chdir(pybamm.__path__[0] + "/..")

# auth = tweepy.OAuthHandler(Keys.CONSUMER_KEY, Keys.CONSUMER_SECRET)
# auth.set_access_token(Keys.ACCESS_KEY, Keys.ACCESS_SECRET)
# api = tweepy.API(auth)


# def pybamm1():
#     model = pybamm.BaseModel()

#     x = pybamm.Variable("x")
#     y = pybamm.Variable("y")

#     dxdt = 4 * x - 2 * y
#     dydt = 3 * x - y

#     model.rhs = {x: dxdt, y: dydt}
#     model.initial_conditions = {x: pybamm.Scalar(1), y: pybamm.Scalar(2)}
#     model.variables = {"x": x, "y": y, "z": x + 4 * y}

#     disc = pybamm.Discretisation()  # use the default discretisation
#     disc.process_model(model)

#     solver = pybamm.ScipySolver()
#     t = np.linspace(0, 1, 20)
#     solution = solver.solve(model, t)

#     t_sol, y_sol = solution.t, solution.y  # get solution times and states
#     x = solution["x"]  # extract and process x from the solution
#     y = solution["y"]  # extract and process y from the solution

#     t_fine = np.linspace(0, t[-1], 1000)

#     fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 4))
#     ax1.plot(t_fine, 2 * np.exp(t_fine) - np.exp(2 * t_fine), t_sol, x(t_sol), "o")
#     ax1.set_xlabel("t")
#     ax1.legend(["2*exp(t) - exp(2*t)", "x"], loc="best")

#     ax2.plot(t_fine, 3 * np.exp(t_fine) - np.exp(2 * t_fine), t_sol, y(t_sol), "o")
#     ax2.set_xlabel("t")
#     ax2.legend(["3*exp(t) - exp(2*t)", "y"], loc="best")

#     plt.tight_layout()
#     # img = plt.show()

#     plt.savefig("foo.png", bbox_inches="tight")  # Saving the graph
#     # PyBaMM model ends


# def pybamm2():
#     # Writing lead-acid model example

#     full = pybamm.lead_acid.Full()

#     loqs = pybamm.lead_acid.LOQS()

#     composite = pybamm.lead_acid.Composite()

#     # load models
#     models = [loqs, composite, full]

#     # process parameters
#     param = models[0].default_parameter_values
#     param["Current function [A]"] = "[input]"
#     for model in models:
#         param.process_model(model)

#     for model in models:
#         # load and process default geometry
#         geometry = model.default_geometry
#         param.process_geometry(geometry)

#         # discretise using default settings
#         mesh = pybamm.Mesh(geometry, model.default_submesh_types, model.default_var_pts)
#         disc = pybamm.Discretisation(mesh, model.default_spatial_methods)
#         disc.process_model(model)

#     timer = pybamm.Timer()
#     solutions = {}
#     t_eval = np.linspace(0, 3600 * 17, 100)  # time in seconds
#     solver = pybamm.CasadiSolver()
#     for model in models:
#         timer.reset()
#         solution = solver.solve(model, t_eval, inputs={"Current function [A]": 1})
#         print("Solved the {} in {}".format(model.name, timer.time()))
#         solutions[model] = solution

#     for model in models:
#         time = solutions[model]["Time [h]"].entries
#         voltage = solutions[model]["Terminal voltage [V]"].entries
#         plt.plot(time, voltage, lw=2, label=model.name)
#     plt.xlabel("Time [h]", fontsize=15)
#     plt.ylabel("Terminal voltage [V]", fontsize=15)
#     plt.legend(fontsize=15)

#     # plt.show()
#     plt.savefig("foo1.png")

#     # Another graph
#     # solution_values = [solutions[model] for model in models]
#     # quick_plot = pybamm.QuickPlot(solution_values)
#     # quick_plot.dynamic_plot();

#     # # Another graph
#     # t_eval = np.linspace(0, 3600, 100)
#     # for model in models:
#     #     solutions[model] = solver.solve(model, t_eval, inputs={"Current function [A]": 20})

#     # # Plot
#     # solution_values = [solutions[model] for model in models]
#     # quick_plot = pybamm.QuickPlot(solution_values)
#     # quick_plot.dynamic_plot();
#     # PyBaMM ends here


# def tweet_graph():

#     x = random.randint(0, 1)
#     print(x)
#     if x == 0:
#         pybamm1()
#         media = api.media_upload("foo.png")
#     else:
#         pybamm2()
#         media = api.media_upload("foo1.png")

#     tweet = "random graph test"

#     api.update_status(status=tweet, media_ids=[media.media_id])


# while True:
#     print("Tweeting....")
#     tweet_graph()
#     time.sleep(5)
