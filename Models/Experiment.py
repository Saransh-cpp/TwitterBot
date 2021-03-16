import pybamm
import pandas as pd
import os
import random


def experiment_func():

    chargeC = []
    dischargeC = []
    restC = []

    for i in range(1, 100):

        if i % 20 != 0 and i % 50 != 0:
            dischargeC.append(
                [
                    "Discharge at 0.5 C for " + str(i % 20) + " minutes",
                    "Discharge at 1 A for " + str(i % 50) + " seconds",
                ]
            )

            chargeC.append(
                [
                    "Charge at 0.5 C for " + str(i % 20) + " minutes",
                    "Charge at 200mA for " + str(i % 20) + " minutes (1 minute period)",
                ]
            )

            restC.append("Rest for " + str(i % 20) + " minutes")
            # "Hold at 1 V for 20 seconds",
            # "Hold at 4.1 V until 50 mA",
            # "Hold at 3V until C/50",

    print(len(chargeC))

    random.shuffle(dischargeC)
    random.shuffle(restC)
    random.shuffle(chargeC)

    # print(chargeC)
    # print(dischargeC)

    cycleC = []
    cycleC.append(chargeC[random.randint(0, 90)][random.randint(0, 1)])
    cycleC.append(restC[random.randint(0, 90)])
    cycleC.append(dischargeC[random.randint(0, 90)][random.randint(0, 1)])

    print(cycleC)

    random.shuffle(cycleC)
    experiment = pybamm.Experiment(cycleC * 3)

    chemistry = pybamm.parameter_sets.Chen2020
    parameter_values = pybamm.ParameterValues(chemistry=chemistry)

    model = pybamm.lithium_ion.DFN()

    sim = pybamm.Simulation(model, experiment=experiment)

    sim.solve()
    sim.plot()


while True:
    experiment_func()