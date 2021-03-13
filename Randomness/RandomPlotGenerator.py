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
        parameter_number = 0

        if lower_voltage < upper_voltage:
            if parameter_number == 0:
                parameter_values, sim, solution, output_variables = foo.Chen2020Modelling(current_function=current_function,
                lower_voltage=lower_voltage, upper_voltage=upper_voltage,
                ambient_temp=ambient_temp, initial_temp=initial_temp,
                reference_temp=reference_temp)
                time = foo1.plot_graph(solution, sim, output_variables)
            # t = solution["Time [s]"]
            # final_time = int(t.entries[len(t.entries) - 1])
            # plot_type = random.randint(0, 1)
            # time = random.randint(0, final_time)
            # print(time, plot_type)
            # if plot_type == 0:
            #     plot = pybamm.QuickPlot(sim, time_unit='seconds')
            #     plot.plot(time)
            #     plot.fig.savefig("foo.pdf", dpi=300)
            #     foo1.pdf_to_png('foo.pdf')
            # else:
            #     while True:
            #         lower_limit = random.randint(0, len(output_variables))
            #         upper_limit = random.randint(0, len(output_variables))
            #         if upper_limit - lower_limit < 9 and upper_limit - lower_limit > 2:
            #             plot = pybamm.QuickPlot(sim, output_variables=output_variables[lower_limit:upper_limit], time_unit='seconds')
            #             plot.plot(time)
            #             plot.fig.savefig("foo.pdf", dpi=300)
            #             foo1.pdf_to_png('foo.pdf')
            #             break
    

                return parameter_values, time