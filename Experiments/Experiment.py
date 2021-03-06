import pybamm
import pandas as pd
import os
import random
import importlib

spec = importlib.util.spec_from_file_location(
    "single_decimal_point.py", "Utils/single_decimal_point.py"
)
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)

spec1 = importlib.util.spec_from_file_location(
    "PlotGraph.py", "Randomness/PlotGraph.py"
)
foo1 = importlib.util.module_from_spec(spec1)
spec1.loader.exec_module(foo1)

def experiment_func(cycle=None):

    charge = []
    discharge = []
    rest = []
    hold = []

    model = pybamm.lithium_ion.DFN()
    parameter_values = model.default_parameter_values

    while True:
        vmin = foo.single_decimal_point(3.1, 4.2, 0.1)
        vmax = foo.single_decimal_point(3.1, 4.2, 0.1)
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


def US06_experiment_cycle():

    charge = []
    discharge = []
    Hold = []
    voltage = foo.single_decimal_point(3.8, 4.2, 0.1)

    current = random.randint(1, 2)

    charge.append("Charge at " + str(current) + " A until " + str(voltage) + " V")

    Hold.append(
        "Hold at " + str(voltage) + " V until " + str(random.randint(40, 60)) + " mA"
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

    # cycleC = ["Charge at 1 A until 4.1 V", "Hold at 4.1 V until 50 mA"]

    print(cycleC)
    return cycleC


def US06_experiment(reply=False):
    model = pybamm.lithium_ion.DFN()
    # import drive cycle from file
    if reply: 
        drive_cycle = pd.read_csv("drive_cycle.csv", comment="#", header=None).to_numpy()
    elif not reply:
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
        model, parameter_values=param, solver=pybamm.CasadiSolver(mode="fast")
    )
    sol_US06_1 = sim_US06_1.solve()

    if reply:
        time = foo1.plot_graph(sol_US06_1, sim_US06_1, reply=reply)
        return time

    solved = False
    print("REACHED")
    while not solved:
        try:
            cycle = US06_experiment_cycle()
            # cycle = ["Charge at 1 A until 4.1 V", "Hold at 4.1 V until 50 mA"]

            experiment = pybamm.Experiment(cycle)
            sim_cccv = pybamm.Simulation(model, experiment=experiment)
            sol_cccv = sim_cccv.solve()
            new_model = model.set_initial_conditions_from(sol_cccv, inplace=False)
            sim_US06_2 = pybamm.Simulation(
                new_model,
                parameter_values=param,
                solver=pybamm.CasadiSolver(mode="fast"),
            )
            sol_US06_2 = sim_US06_2.solve()
            # pybamm.dynamic_plot(
            #     [sol_US06_1, sol_US06_2],
            #     labels=["Default initial conditions", "Fully charged"],
            # )
            solution = [sol_US06_1, sol_US06_2]
            sim = [sim_US06_1, sim_US06_2]
            t = solution[0]["Time [s]"]
            final_time = int(t.entries[len(t.entries) - 1])
            time = random.randint(0, final_time)
            plot = pybamm.QuickPlot(
                sim,
                labels=["Default initial conditions", "Fully charged"],
                time_unit="seconds",
            )
            plot.plot(time)
            plot.fig.savefig("foo.png", dpi=300)
            print(sol_US06_1)
            solved = True

        except:
            pass
            # print("Exception")
    return time, cycle


# A = model.param.I_typ
# omega = 0.1
# param["Current function [A]"] = my_fun(A,omega)
# cccv_experiment()
