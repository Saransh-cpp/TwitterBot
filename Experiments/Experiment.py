import pybamm
import pandas as pd
import os
import random


def experiment_func(cycle=None):

    charge = []
    discharge = []
    rest = []
    # voltage = random.uniform(3.1, 4.2)

    model = pybamm.lithium_ion.DFN()
    parameter_values = model.default_parameter_values
    output_variables = model.variable_names()
    random.shuffle(output_variables)

    if cycle == None:
        for i in range(1, 100):
            if i % 10 != 0 and i % 3 != 0:
                discharge.append(
                    [
                        "Discharge at " + str(i % 3) + " C for " + str(i % 10) + " minutes",
                        "Discharge at " + str(i % 3) + " A for " + str(i % 10) + " minutes",
                    ]
                )

                charge.append(
                    [
                        "Charge at " + str(i % 3) + " C for " + str(i % 10) + " minutes",
                        # "Charge at " + str(i % 3) + " C until " + str(voltage) + " V",

                        "Charge at "
                        + str(i % 3)
                        + " A for "
                        + str(i % 10)
                        + " minutes (1 minute period)",
                    ]
                )

                rest.append(
                    [
                        "Rest for " + str(i % 10) + " minutes",
                    ]
                )
                # "Hold at " + str(voltage) + " V for " + str(i % 10) + " minutes",
                # "Hold at 1 V for 20 seconds",
                # "Hold at 4.1 V until 50 mA",
                # "Hold at 3V until C/50",

        random.shuffle(discharge)
        random.shuffle(rest)
        random.shuffle(charge)

        cycleC = []
        # num = random.randint(0, 2)
        # restnum = random.randint(0, 1)
        # if restnum == 1:
        #     num = 1

        cycleC.append(discharge[random.randint(0, 50)][random.randint(0, 1)])
        cycleC.append(rest[random.randint(0, 50)][0])
        cycleC.append(charge[random.randint(0, 50)][random.randint(0,1)])

        number = random.randint(1, 3)
        print(cycleC * number)
        return cycleC, number, model, parameter_values, output_variables

    else:
        print("yes")
        return cycle, model, parameter_values, output_variables

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