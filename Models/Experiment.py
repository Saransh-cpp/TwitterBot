import pybamm
import pandas as pd
import os

model = pybamm.lithium_ion.DFN()

drive_cycle = pd.read_csv(
    "US06.csv", comment="#", header=None
).to_numpy()
# # create interpolant
param = model.default_parameter_values
timescale = param.evaluate(model.timescale)
current_interpolant = pybamm.Interpolant(drive_cycle[:, 0], drive_cycle[:, 1], timescale * pybamm.t)
# set drive cycle
param["Current function [A]"] = current_interpolant

# sim_US06_1 = pybamm.Simulation(
#     model, parameter_values=param, solver=pybamm.CasadiSolver(mode="fast")
# )
# sol_US06_1 = sim_US06_1.solve(t_eval=None)




experiment = pybamm.Experiment(
    ["Charge at 1 A until 4.1 V", "Hold at 4.1 V until 50 mA"]
)
sim_cccv = pybamm.Simulation(model, experiment=experiment)
sol_cccv = sim_cccv.solve()

# MODEL RE-INITIALIZATION: #############################################################
# Now initialize the model with the solution of the charge, and then discharge with
# the US06 drive cycle
# We could also do this inplace by setting inplace to True, which modifies the original
# model in place
new_model = model.set_initial_conditions_from(sol_cccv, inplace=False)
########################################################################################

sim_US06_2 = pybamm.Simulation(
    new_model, parameter_values=param, solver=pybamm.CasadiSolver(mode="fast")
)
sol_US06_2 = sim_US06_2.solve()

pybamm.dynamic_plot(
    [sol_US06_2], labels=["Fully charged"]
)