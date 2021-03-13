import pybamm
import random
import sys
import importlib.util

spec = importlib.util.spec_from_file_location("Chen2020params.py", "Models/Chen2020Params.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)

spec1 = importlib.util.spec_from_file_location("PlotGraph.py", "Randomness/PlotGraph.py")
foo1 = importlib.util.module_from_spec(spec1)
spec1.loader.exec_module(foo1)

spec3 = importlib.util.spec_from_file_location("Marquis2019params.py", "Models/Marquis2019Params.py")
foo3 = importlib.util.module_from_spec(spec3)
spec3.loader.exec_module(foo3)

def random_plot_generator():

    while True:
        current_function = random.uniform(0, 10)
        upper_voltage = random.uniform(2.5, 4.2)
        lower_voltage = random.uniform(2.5, 4.2)
        ambient_temp = random.uniform(273.18, 298.15)
        initial_temp = random.uniform(273.18, 298.15)
        reference_temp = random.uniform(273.18, 298.15)

        parameter_sets = ['Chen2020', 'Ecker2015', 'Marquis2019', 'Mohtat2020']
        # parameter_number = random.randint(0, len(parameter_sets))
        parameter_number = random.randint(0, 1)
        # parameter_number = 1/

        if lower_voltage < upper_voltage:
            if parameter_number == 0:
                parameter_values, sim, solution, output_variables = foo.Chen2020Modelling(current_function=current_function,
                lower_voltage=lower_voltage, upper_voltage=upper_voltage,
                ambient_temp=ambient_temp, initial_temp=initial_temp,
                reference_temp=reference_temp)
                time = foo1.plot_graph(solution, sim, output_variables)

                return parameter_values, time, parameter_number
            
            elif parameter_number == 1:
                parameter_values, sim, solution, output_variables = foo3.Marquis2019Modelling(current_function=current_function,
                lower_voltage=lower_voltage, upper_voltage=upper_voltage,
                ambient_temp=ambient_temp, initial_temp=initial_temp,
                reference_temp=reference_temp)
                time = foo1.plot_graph(solution, sim, output_variables)
                print(time)

                return parameter_values, time, parameter_number