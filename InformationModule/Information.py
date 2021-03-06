def information(parameter_number, cycle, solver):

    solver_name = "None"
    mode = "None"

    if solver == 1:
        solver_name = " Casadi"
        mode = " fast"
    elif solver == 2:
        solver_name = " Casadi"
        mode = " safe"
    elif solver == 3:
        solver_name = " Casadi"
        mode = " fast with events"

    if parameter_number == 0:
        return "This is some basic information about Chen2020 parameters in a simple DFN model plotted using PyBaMM"
    elif parameter_number == 1:
        return "This is some basic information about Marquis2019 parameters in a simple DFN model plotted using PyBaMM"
    elif parameter_number == 2:
        return "This is some basic information about Ecker2015 parameters in a simple DFN model plotted using PyBaMM"
    elif parameter_number == 3:
        return "This is some basic information about Mohtat2020 parameters in a simple DFN model plotted using PyBaMM"
    elif parameter_number == "experiment":
        return (
            # "Random experiment generated and plotted using PyBaMM.
            "The experiment cycle- "
            + str(cycle)
            + ". Solver: "
            + solver_name
            + ", mode: "
            + mode
        )
    elif parameter_number == "cccv experiment":
        return (
            "Comparing 2 simulations, 1. Default initial condition, Drive cycle - https://github.com/pybamm-team/PyBaMM/blob/develop/pybamm/input/drive_cycles/US06.csv. 2. Fully charged using experiment - "
            + str(cycle)
        )
