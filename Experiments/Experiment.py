import pybamm
import pandas as pd
import os
import random


def experiment_func(cycle=None):

    charge = []
    discharge = []
    rest = []

    model = pybamm.lithium_ion.DFN()
    parameter_values = model.default_parameter_values

    while True:
        vmin = random.uniform(3.1, 4.2)
        vmax = random.uniform(3.1, 4.2)
        if cycle == None and vmin < vmax:
            for i in range(1, 100):
                if i % 10 != 0 and i % 3 != 0:
                    discharge.append(
                        # [
                        "Discharge at " + str(i % 3) + " C until " + str(vmin) + " V",
                        # "Discharge at "
                        # + str(i % 3)
                        # + " A for "
                        # + str(i % 10)
                        # + " minutes",
                        # ]
                    )

                    charge.append(
                        # [
                        "Charge at " + str(i % 3) + " C until " + str(vmax) + " V",
                        # "Charge at " + str(i % 3) + " C until " + str(voltage) + " V",
                        # "Charge at "
                        # + str(i % 3)
                        # + " A for "
                        # + str(i % 10)
                        # + " minutes (1 minute period)",
                        # ]
                    )

                    rest.append(
                        # [
                        "Rest for " + str(i % 10) + " minutes",
                        # ]
                    )
                    # "Hold at " + str(voltage) + " V for " + str(i % 10) + " minutes",
                    # "Hold at 1 V for 20 seconds",
                    # "Hold at 4.1 V until 50 mA",
                    # "Hold at 3V until C/50",

            random.shuffle(discharge)
            random.shuffle(rest)
            random.shuffle(charge)

            cycleC = []

            cycleC.append(discharge[random.randint(0, 50)])
            cycleC.append(rest[random.randint(0, 50)])
            cycleC.append(charge[random.randint(0, 50)])

            number = random.randint(1, 3)
            print(cycleC * number)
            return cycleC, number, model, parameter_values

        # elif cycle != None:
        #     print("Cycle != None", cycle)
        #     return cycle, model, parameter_values


# def cccv_experiment():

#     charge = []
#     discharge = []
#     Hold = []
#     voltage = random.uniform(3.1, 4.1)

#     for i in range(1, 100):

#         if i%4 != 0:

#             charge.append(
#                 # [
#                     # "Charge at " + str(i%3) + " C until " + str(voltage) + " V",
#                     "Charge at " + str(1) + " A until " + str(voltage) + " V",
#                 # ]
#             )

#             Hold.append("Hold at " + str(voltage) + " V until 50 mA")
#             # "Hold at 1 V for 20 seconds",
#             # "Hold at 4.1 V until 50 mA",
#             # "Hold at 3V until C/50",

#     random.shuffle(discharge)
#     random.shuffle(Hold)
#     random.shuffle(charge)

#     cycleC = []
#     cycleC.append(charge[random.randint(0, 60)])
#     cycleC.append(Hold[random.randint(0, 60)])

#     print(cycleC)
#     return cycleC


# random.shuffle(cycleC)
# experiment = pybamm.Experiment(cycleC * 3)

# # chemistry = pybamm.parameter_sets.Chen2020
# # parameter_values = pybamm.ParameterValues(chemistry=chemistry)

# model = pybamm.lithium_ion.DFN()

# sim = pybamm.Simulation(model, experiment=experiment)

# sim.solve()
# sim.plot()


# while True:
#     try:
#         experiment_func()
#     except:
#         experiment_func()