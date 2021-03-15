import pybamm
import random
import sys
import importlib.util

spec = importlib.util.spec_from_file_location("BaseModel.py", "Models/BaseModel.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)

spec1 = importlib.util.spec_from_file_location("PlotGraph.py", "Randomness/PlotGraph.py")
foo1 = importlib.util.module_from_spec(spec1)
spec1.loader.exec_module(foo1)

def random_plot_generator():

    while True:

        parameter_sets = ['Chen2020', 'Marquis2019', 'Ecker2015', 'Mohtat2020']
        parameter_number = (0, 1)

        if parameter_number == 0:
            current_function = random.uniform(0, 10)
            upper_voltage = random.uniform(2.5, 4.2)
            lower_voltage = random.uniform(2.5, 4.2)
            ambient_temp = random.uniform(273.18, 298.15)
            initial_temp = random.uniform(273.18, 298.15)
            reference_temp = random.uniform(273.18, 298.15)

        elif parameter_number == 1:
            current_function = random.uniform(0, 5)
            upper_voltage = random.uniform(3.1, 4.1)
            lower_voltage = random.uniform(3.1, 4.1)
            ambient_temp = random.uniform(273.18, 298.15)
            initial_temp = random.uniform(273.18, 298.15)
            reference_temp = random.uniform(273.18, 298.15)

        if lower_voltage < upper_voltage:
            parameter_values, sim, solution, output_variables, parameter_number = foo.BaseModel(current_function=current_function, upper_voltage=upper_voltage,
            lower_voltage=lower_voltage, ambient_temp=ambient_temp, initial_temp=initial_temp,
            reference_temp=reference_temp, parameter_number=parameter_number)
            time = foo1.plot_graph(solution, sim, output_variables)

            return parameter_values, time, parameter_number