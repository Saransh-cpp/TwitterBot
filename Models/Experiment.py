import pybamm
import pandas as pd
import os
import random


def experiment_func():

    charge = []
    discharge = []
    rest = []

    for i in range(1, 100):

        if i%10 != 0:
            discharge.append(
                "Discharge at 0.5 C for " + str(i%10) + " minutes",
            )
            # "Discharge at C/20 for 0.5 hours",
            # "Discharge at 1 A for 90 seconds",
            # "Discharge at 1 W for 0.5 hours",

            charge.append("Charge at 0.5 C for " + str(i%10) + " minutes")
            # "Charge at 200mA for 45 minutes (1 minute period)",
            # "Charge at 200 mW for 45 minutes",
            # "Charge at 1 C until 4.1V",

            rest.append("Rest for " + str(i%10) + " minutes")
            # "Hold at 1 V for 20 seconds",
            # "Hold at 4.1 V until 50 mA",
            # "Hold at 3V until C/50",
    
    print(len(charge))

    random.shuffle(discharge)
    random.shuffle(rest)
    random.shuffle(charge)

    cycle = []
    cycle.append(charge[random.randint(0, 49)])
    cycle.append(rest[random.randint(0, 49)])
    cycle.append(discharge[random.randint(0, 49)])

    print(cycle)

    # cycle.append("Discharge at 1C for 0.5 hours")
    # cycle.append("Discharge at C/20 for 0.5 hours")
    # test = []
    # test.append("Charge at 0.5 C for 45 minutes")
    random.shuffle(cycle)
    experiment = pybamm.Experiment(cycle * 3)

    # chemistry = pybamm.parameter_sets.Chen2020
    # parameter_values = pybamm.ParameterValues(chemistry=chemistry)

    model = pybamm.lithium_ion.DFN()

    sim = pybamm.Simulation(model, experiment=experiment)

    sim.solve()
    sim.plot()


while True:
    experiment_func()