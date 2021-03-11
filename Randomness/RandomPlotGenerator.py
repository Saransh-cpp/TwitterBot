import pybamm
import random
import sys
from Chen2020Params import Chen2020Modelling

def random_plot_generator():

    while True:
        current_function = random.uniform(0, 10)
        upper_voltage = random.uniform(2.5, 4.2)
        lower_voltage = random.uniform(2.5, 4.2)
        ambient_temp = random.uniform(273.18, 298.15)
        initial_temp = random.uniform(273.18, 298.15)
        reference_temp = random.uniform(273.18, 298.15)
        
        if lower_voltage < upper_voltage:
            Chen2020Modelling(current_function=current_function,
            lower_voltage=lower_voltage, upper_voltage=upper_voltage,
            ambient_temp=ambient_temp, initial_temp=initial_temp,
            reference_temp=reference_temp)
            break

random_plot_generator()