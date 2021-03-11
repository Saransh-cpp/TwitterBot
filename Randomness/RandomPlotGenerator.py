import pybamm
import random
import sys
import importlib.util

spec = importlib.util.spec_from_file_location("Chen2020params.py", "Models/Chen2020Params.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)

def random_plot_generator():

    while True:
        current_function = random.uniform(0, 10)
        upper_voltage = random.uniform(2.5, 4.2)
        lower_voltage = random.uniform(2.5, 4.2)
        ambient_temp = random.uniform(273.18, 298.15)
        initial_temp = random.uniform(273.18, 298.15)
        reference_temp = random.uniform(273.18, 298.15)
        
        if lower_voltage < upper_voltage:
            foo.Chen2020Modelling(current_function=current_function,
            lower_voltage=lower_voltage, upper_voltage=upper_voltage,
            ambient_temp=ambient_temp, initial_temp=initial_temp,
            reference_temp=reference_temp)
            break