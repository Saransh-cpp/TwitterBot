import pybamm
import pandas as pd
import os
import random


def experiment_func():

    chargeC = []
    dischargeC = []
    restC = []

    for i in range(1, 100):

        if i % 20 != 0 and i%3 != 0:
            dischargeC.append(
                [
                    "Discharge at " + str(i%3) + " C for " + str(i % 20) + " minutes",
                    "Discharge at " + str(i%3) + " A for " + str(i % 20) + " minutes",
                ]
            )

            chargeC.append(
                [
                    "Charge at " + str(i%3) + " C for " + str(i % 20) + " minutes",
                    "Charge at " + str(i%3) + " A for " + str(i % 20) + " minutes (1 minute period)",
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
    cycleC.append(chargeC[random.randint(0, 60)][random.randint(0, 1)])
    cycleC.append(restC[random.randint(0, 60)])
    cycleC.append(dischargeC[random.randint(0, 60)][random.randint(0, 1)])

    print(cycleC)
    return cycleC

def cccv_experiment():

    chargeC = []
    dischargeC = []
    Hold = []
    voltage = random.uniform(3.1, 4.1)

    for i in range(1, 100):

        if i%4 != 0:

            chargeC.append(
                # [
                    # "Charge at " + str(i%3) + " C until " + str(voltage) + " V",
                    "Charge at " + str(2) + " A until " + str(3.7) + " V",
                # ]
            )

            Hold.append("Hold at " + str(3.7) + " V until 50 mA")
            # "Hold at 1 V for 20 seconds",
            # "Hold at 4.1 V until 50 mA",
            # "Hold at 3V until C/50",

    random.shuffle(dischargeC)
    random.shuffle(Hold)
    random.shuffle(chargeC)

    cycleC = []
    cycleC.append(chargeC[random.randint(0, 60)])
    cycleC.append(Hold[random.randint(0, 60)])

    print(cycleC)
    return cycleC


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