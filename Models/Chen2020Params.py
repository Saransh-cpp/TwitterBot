import pybamm
import numpy as np
import matplotlib.pyplot as plt
import random
from pdf2image import convert_from_path

def pdf_to_png(path):
    page = convert_from_path(path)
    page[0].save('fooimage' + '.png', 'PNG')

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
    plot_type = random.randint(0, 1)
    time = random.randint(0, 3000)
    print(time)
    if plot_type == 0:
        plot = pybamm.QuickPlot(sim, time_unit='seconds')
        plot.plot(time)
        plot.fig.savefig("foo.pdf", dpi=300)
        pdf_to_png('foo.pdf')
    else:
        while True:
            lower_limit = random.randint(0, len(output_variables))
            upper_limit = random.randint(0, len(output_variables))
            if upper_limit - lower_limit < 9 and upper_limit - lower_limit > 2:
                plot = pybamm.QuickPlot(sim, output_variables=output_variables[lower_limit:upper_limit], time_unit='seconds')
                plot.plot(time)
                plot.fig.savefig("foo.pdf", dpi=300)
                pdf_to_png('foo.pdf')
                break

    return parameter_values, time
