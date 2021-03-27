import random
import pybamm
import importlib


def plot_graph(solution, sim, t=None, reply=False, comparing=False):

    if t == None and not comparing:
        t = solution["Time [s]"]
    final_time = int(t.entries[len(t.entries) - 1])
    # plot_type = random.randint(0, 1)
    time = random.randint(0, final_time)
    print(time)
    # if plot_type == 0:
    plot = pybamm.QuickPlot(sim, time_unit="seconds")
    plot.plot(time)
    if not reply:
        plot.fig.savefig("foo.png", dpi=300)
    elif reply:
        plot.fig.savefig("replyFoo.png", dpi=300)

    # if comparing:
    #     print(solution[0])
    #     t = solution[0]["Time [s]"]
    #     final_time = int(t.entries[len(t.entries) - 1])
    #     time = random.randint(0, final_time)
    #     plot = pybamm.QuickPlot(sim)
    #     plot.plot(time)
    #     plot.fig.savefig("foo.png", dpi=300)

    
    # Below was the code to plot random output variables (not needed right now)
    # else:
    #     while True:
    #         lower_limit = random.randint(0, len(output_variables))
    #         upper_limit = random.randint(0, len(output_variables))
    #         if upper_limit - lower_limit < 9 and upper_limit - lower_limit > 2:
    #             plot = pybamm.QuickPlot(
    #                 sim,
    #                 output_variables=output_variables[lower_limit:upper_limit],
    #                 time_unit="seconds",
    #             )
    #             plot.plot(time)
    #             if not reply:
    #                 plot.fig.savefig("foo.png", dpi=300)
    #             elif reply:
    #                 plot.fig.savefig("replyFoo.png", dpi=300)
    #             # foo1.pdf_to_png('foo.pdf')
    #             break

    return time