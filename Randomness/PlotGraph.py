import random
import pybamm
import importlib

# spec1 = importlib.util.spec_from_file_location("PDFtoPNNG.py", "Utils/PDFtoPNG.py")
# foo1 = importlib.util.module_from_spec(spec1)
# spec1.loader.exec_module(foo1)

def plot_graph(solution, sim, output_variables):

    t = solution["Time [s]"]
    final_time = int(t.entries[len(t.entries) - 1])
    plot_type = random.randint(0, 1)
    time = random.randint(0, final_time)
    print(time, plot_type)
    if plot_type == 0:
        plot = pybamm.QuickPlot(sim, time_unit='seconds')
        plot.plot(time)
        plot.fig.savefig("foo.png", dpi=300)
        # foo1.pdf_to_png('foo.pdf')
    else:
        while True:
            lower_limit = random.randint(0, len(output_variables))
            upper_limit = random.randint(0, len(output_variables))
            if upper_limit - lower_limit < 9 and upper_limit - lower_limit > 2:
                plot = pybamm.QuickPlot(sim, output_variables=output_variables[lower_limit:upper_limit], time_unit='seconds')
                plot.plot(time)
                plot.fig.savefig("foo.png", dpi=300)
                # foo1.pdf_to_png('foo.pdf')
                break
    
    return time