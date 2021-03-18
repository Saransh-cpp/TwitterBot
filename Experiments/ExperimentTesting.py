import pybamm
import pandas as pd
import os
import numpy as np
from Experiment import experiment_func, cccv_experiment

# def my_fun(A, omega):
#     def current(t):
#         return A * pybamm.sin(2 * np.pi * omega * t)

#     return current

model = pybamm.lithium_ion.DFN()

# import drive cycle from file
drive_cycle = pd.read_csv("US06.csv", comment="#", header=None).to_numpy()
# create interpolant
param = model.default_parameter_values
timescale = param.evaluate(model.timescale)
current_interpolant = pybamm.Interpolant(
    drive_cycle[:, 0], drive_cycle[:, 1], timescale * pybamm.t
)
# set drive cycle
param["Current function [A]"] = current_interpolant

sim_US06_1 = pybamm.Simulation(
    model, parameter_values=param, solver=pybamm.CasadiSolver(mode="fast with events")
)
sol_US06_1 = sim_US06_1.solve()

# cycle = experiment_func()
cycle = cccv_experiment()

experiment = pybamm.Experiment(
    cycle
)
sim_cccv = pybamm.Simulation(model, experiment=experiment, solver=pybamm.CasadiSolver(mode="fast"))
sol_cccv = sim_cccv.solve()
print('yes')
new_model = model.set_initial_conditions_from(sol_cccv, inplace=False)

# A = model.param.I_typ
# omega = 0.1
# param["Current function [A]"] = my_fun(A,omega)

print('Yes')
sim_US06_2 = pybamm.Simulation(
    new_model, parameter_values=param, solver=pybamm.CasadiSolver(mode="fast")
)

sol_US06_2 = sim_US06_2.solve()
print('Yes')

pybamm.dynamic_plot(
    [sol_US06_1, sol_US06_2], labels=["Default initial conditions", "Fully charged"]
)
# Example: simulate for 30 seconds
# simulation_time = 30  # end time in seconds
# npts = int(50 * simulation_time * omega)  # need enough timesteps to resolve output
# t_eval = np.linspace(0, simulation_time, npts)
# solution = simulation.solve(t_eval)
# label = ["Frequency: {} Hz".format(omega)]

# plot current and voltage
# output_variables = ["Current [A]", "Terminal voltage [V]"]
# simulation.plot(labels=label)
