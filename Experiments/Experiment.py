import pybamm
import pandas as pd
import os
import random


def single_decimal_point():
    start = 3.1
    stop = 4.2
    step = 0.1
    precision = 0.1
    f = 1 / precision
    return random.randrange(start * f, stop * f, step * f) / f


def experiment_func(cycle=None):

    charge = []
    discharge = []
    rest = []
    hold = []

    model = pybamm.lithium_ion.DFN()
    parameter_values = model.default_parameter_values

    while True:
        vmin = single_decimal_point()
        vmax = single_decimal_point()
        ccharge = random.randint(1, 5)
        cdischarge = random.randint(1, 5)
        ccutoff = random.randint(1, 100)
        if cycle == None and vmin < vmax:
            discharge.append(
                # [
                "Discharge at " + str(cdischarge) + " C until " + str(vmin) + " V",
                # "Discharge at "
                # + str(i % 3)
                # + " A for "
                # + str(i % 10)
                # + " minutes",
                # ]
            )

            charge.append(
                # [
                "Charge at " + str(ccharge) + " C until " + str(vmax) + " V",
                # "Charge at " + str(i % 3) + " C until " + str(voltage) + " V",
                # "Charge at "
                # + str(i % 3)
                # + " A for "
                # + str(i % 10)
                # + " minutes (1 minute period)",
                # ]
            )

            rest.append(
                [
                    "Rest for " + str(random.randint(1, 10)) + " minutes",
                    "Rest for " + str(random.randint(1, 10)) + " minutes",
                ]
            )

            hold.append(
                "Hold at " + str(vmax) + " V until " + str(ccutoff) + " mA",
            )

            random.shuffle(discharge)
            random.shuffle(rest)
            random.shuffle(charge)

            cycleC = []

            cycleC.append(discharge[0])
            if random.randint(0, 1) == 0:
                cycleC.append(rest[0][0])
            cycleC.append(charge[0])
            cycleC.append(hold[0])
            if random.randint(0, 1) == 0:
                cycleC.append(rest[0][1])

            number = random.randint(1, 3)
            print(cycleC * number)
            return cycleC, number, model, parameter_values

        elif cycle != None:
            return cycle, model, parameter_values


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