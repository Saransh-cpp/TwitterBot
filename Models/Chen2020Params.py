import pybamm
import numpy as np
import matplotlib.pyplot as plt
import random


def Chen2020Modelling(current_function, lower_voltage, upper_voltage,
                        ambient_temp, initial_temp, reference_temp):

    chemistry = pybamm.parameter_sets.Chen2020

    model = pybamm.lithium_ion.DFN()
    parameter_values = pybamm.ParameterValues(chemistry=chemistry)

    parameter_values["Current function [A]"] = current_function
    parameter_values["Lower voltage cut-off [V]"] = lower_voltage
    parameter_values["Upper voltage cut-off [V]"] = upper_voltage
    parameter_values["Ambient temperature [K]"] = ambient_temp
    parameter_values["Initial temperature [K]"] = initial_temp
    parameter_values["Reference temperature [K]"] = reference_temp


    output_variables = model.variable_names()
    random.shuffle(output_variables)

    sim = pybamm.Simulation(model, parameter_values=parameter_values)
    sim.solve([0, 3600])
    solution = sim.solution

    return parameter_values, sim, solution, output_variables
