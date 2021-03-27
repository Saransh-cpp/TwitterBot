import pybamm
import pandas as pd
import os
import random


def experiment_func(cycle=None):

    charge = []
    discharge = []
    rest = []
    hold = []

    model = pybamm.lithium_ion.DFN()
    parameter_values = model.default_parameter_values

    while True:
        vmin = single_decimal_point(3.1, 4.2, 0.1)
        vmax = single_decimal_point(3.1, 4.2, 0.1)
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


def cccv_experiment_cycle():

    charge = []
    discharge = []
    Hold = []
    voltage = single_decimal_point(3.1, 4.2, 0.1)

    charge.append(
        # [
        # "Charge at " + str(i%3) + " C until " + str(voltage) + " V",
        "Charge at " + str(random.randint(0, 4)) + " A until " + str(voltage) + " V",
        # ]
    )

    Hold.append(
        "Hold at " + str(voltage) + " V until " + random.randint(1, 100) + " mA"
    )
    # "Hold at 1 V for 20 seconds",
    # "Hold at 4.1 V until 50 mA",
    # "Hold at 3V until C/50",

    random.shuffle(discharge)
    random.shuffle(Hold)
    random.shuffle(charge)

    cycleC = []
    cycleC.append(charge[0])
    cycleC.append(Hold[0])

    print(cycleC)
    return cycleC


# def cccv_experiment():
#     model = pybamm.lithium_ion.DFN()
#     # import drive cycle from file
#     drive_cycle = pd.read_csv("US06.csv", comment="#", header=None).to_numpy()
#     # create interpolant
#     param = model.default_parameter_values
#     timescale = param.evaluate(model.timescale)
#     current_interpolant = pybamm.Interpolant(
#         drive_cycle[:, 0], drive_cycle[:, 1], timescale * pybamm.t
#     )
#     # set drive cycle
#     param["Current function [A]"] = current_interpolant

#     sim_US06_1 = pybamm.Simulation(
#         model, parameter_values=param, solver=pybamm.CasadiSolver(mode="fast")
#     )
#     sol_US06_1 = sim_US06_1.solve()

#     solved = False
#     print("REACHED")
#     while not solved:
#         try:
#             print("TRYING")
#             # cycle = cccv_experiment_cycle()
#             # print(cycle)
#             cycle = ["Charge at 1 A until 4.1 V", "Hold at 4.1 V until 50 mA"]

#             experiment = pybamm.Experiment(cycle)
#             sim_cccv = pybamm.Simulation(model, experiment=experiment)
#             sol_cccv = sim_cccv.solve()
#             new_model = model.set_initial_conditions_from(sol_cccv, inplace=False)
#             sim_US06_2 = pybamm.Simulation(
#                 new_model,
#                 parameter_values=param,
#                 solver=pybamm.CasadiSolver(mode="fast"),
#             )
#             sol_US06_2 = sim_US06_2.solve()
#             pybamm.dynamic_plot(
#                 [sol_US06_1, sol_US06_2],
#                 labels=["Default initial conditions", "Fully charged"],
#             )
#             # solution = [sol_US06_1, sol_US06_2]
#             # sim = [sim_US06_1, sim_US06_2]
#             # t = solution[0]["Time [s]"]
#             # final_time = int(t.entries[len(t.entries) - 1])
#             # time = random.randint(0, final_time)
#             # plot = pybamm.QuickPlot(sim)
#             # plot.plot(time)
#             # plot.fig.savefig("foo.png", dpi=300)
#             print(sol_US06_1)
#             solved = True

#         except:
#             pass
#     return sol_US06_2, sol_US06_1, sim_US06_2, sim_US06_1
    # A = model.param.I_typ
    # omega = 0.1
    # param["Current function [A]"] = my_fun(A,omega)
