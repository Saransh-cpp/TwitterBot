import pybamm
import random
import sys
import importlib.util

spec = importlib.util.spec_from_file_location("BaseModel.py", "Models/BaseModel.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)

spec1 = importlib.util.spec_from_file_location(
    "PlotGraph.py", "Randomness/PlotGraph.py"
)
foo1 = importlib.util.module_from_spec(spec1)
spec1.loader.exec_module(foo1)

spec2 = importlib.util.spec_from_file_location(
    "Experiment.py", "Experiments/Experiment.py"
)
foo2 = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(foo2)


def random_plot_generator(
    choice=None,
    parameter_number=None,
    output_variables=None,
    time=None,
    cycle=None,
):
    reply = True

    while True:

        if choice == None:
            choice = random.randint(0, 1)
            reply = False

        if choice == 0:
            if parameter_number == None:
                parameter_number = random.randint(0, 1)

            if parameter_number == 0:
                current_function = random.uniform(0, 10)
                upper_voltage = random.uniform(2.5, 4.2)
                lower_voltage = random.uniform(2.5, 4.2)
                ambient_temp = random.uniform(273.18, 298.15)
                initial_temp = random.uniform(273.18, 298.15)
                reference_temp = random.uniform(273.18, 298.15)

            elif parameter_number == 1:
                current_function = random.uniform(0, 2)
                upper_voltage = random.uniform(3.1, 4.1)
                lower_voltage = random.uniform(3.1, 4.1)
                ambient_temp = random.uniform(273.18, 298.15)
                initial_temp = random.uniform(273.18, 298.15)
                reference_temp = random.uniform(273.18, 298.15)

            if lower_voltage < upper_voltage:
                (
                    parameter_values,
                    sim,
                    solution,
                    output_variables,
                    parameter_number,
                ) = foo.BaseModel(
                    current_function=current_function,
                    upper_voltage=upper_voltage,
                    lower_voltage=lower_voltage,
                    ambient_temp=ambient_temp,
                    initial_temp=initial_temp,
                    reference_temp=reference_temp,
                    parameter_number=parameter_number,
                )
                time = foo1.plot_graph(solution, sim, output_variables, reply=reply)

                if not reply:
                    return parameter_values, time, parameter_number, None, None, None
                elif reply:
                    return parameter_values, time

        elif choice == 1:
            repeat = True
            reply = True
            while repeat:
                if cycle == None:
                    reply = False
                    (
                        cycle,
                        number,
                        model,
                        parameter_values,
                        output_variables,
                    ) = foo2.experiment_func()
                    experiment = pybamm.Experiment(cycle * number)
                else:
                    (
                        cycle,
                        model,
                        parameter_values,
                        output_variables,
                    ) = foo2.experiment_func(cycle)
                    experiment = pybamm.Experiment(cycle)

                Solver = random.randint(0, 2)

                if Solver == 0:
                    sim = pybamm.Simulation(model, experiment=experiment)
                elif Solver == 1:
                    sim = pybamm.Simulation(
                        model,
                        experiment=experiment,
                        solver=pybamm.CasadiSolver(mode="fast"),
                    )
                elif Solver == 2:
                    sim = pybamm.Simulation(
                        model, experiment=experiment, solver=pybamm.CasadiSolver()
                    )
                # else:
                #     sim = pybamm.Simulation(
                #         model,
                #         experiment=experiment,
                #         solver=pybamm.CasadiSolver(mode="fast with events"),
                #     )
                feasible = True
                if not reply:
                    try:
                        sim.solve()
                        solution = sim.solution
                        t = solution["Time [s]"]
                        repeat = False
                    except:
                        repeat = True
                elif reply:
                    try:
                        sim.solve()
                        solution = sim.solution
                        t = solution["Time [s]"]
                        repeat = False
                    except:
                        # feasible = False
                        repeat = True

            time = foo1.plot_graph(solution, sim, output_variables, reply=reply)

            if not reply:
                return parameter_values, time, "experiment", cycle, Solver, number
            elif reply:
                return time, feasible
