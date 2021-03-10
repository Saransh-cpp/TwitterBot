import pybamm
import tweepy
from keys import Keys
import time
import numpy as np
import matplotlib.pyplot as plt
import random
import os

os.chdir(pybamm.__path__[0]+'/..')


def Chen2020Modelling(current_function, lower_voltage, upper_voltage,
                        ambient_temp, initial_temp, reference_temp):

    chemistry = pybamm.parameter_sets.Chen2020
    # print(chemistry)

    model = pybamm.lithium_ion.DFN()
    parameter_values = pybamm.ParameterValues(chemistry=chemistry)
    # print(parameter_values)
    # print(parameter_values.search("temperature"))

    parameter_values["Current function [A]"] = current_function
    parameter_values["Lower voltage cut-off [V]"] = lower_voltage
    parameter_values["Upper voltage cut-off [V]"] = upper_voltage
    parameter_values["Ambient temperature [K]"] = ambient_temp
    parameter_values["Initial temperature [K]"] = initial_temp
    parameter_values["Reference temperature [K]"] = reference_temp

    sim = pybamm.Simulation(model, parameter_values=parameter_values)
    sim.solve([0, 3600])
    sim.plot()


def random_plot_generator():

    while True:
        current_function = random.randint(0, 10)
        print(current_function)
        upper_voltage = random.randint(0, 10)
        print(upper_voltage)
        lower_voltage = random.randint(0, 10)
        print(lower_voltage)
        # ambient_temp = random.uniform(273.18, 298.15)
        # print(ambient_temp)
        # initial_temp = random.uniform(273.18, 298.15)
        # print(initial_temp)
        # reference_temp = random.uniform(273.18, 298.15)
        # print(reference_temp)
        if lower_voltage < upper_voltage:
            Chen2020Modelling(current_function=current_function,
            lower_voltage=lower_voltage, upper_voltage=upper_voltage,
            ambient_temp=298.15, initial_temp=298.15,
            reference_temp=298.15)
            break


random_plot_generator()