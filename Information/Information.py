def information(parameter_number, cycle):
    if parameter_number == 0:
        return "This is some basic information about Chen2020 parameters in a simple DFN model plotted using PyBaMM"
    elif parameter_number == 1:
        return "This is some basic information about Marquis2019 parameters in a simple DFN model plotted using PyBaMM"
    elif parameter_number == 1:
        return "This is some basic information about Ecker2015 parameters in a simple DFN model plotted using PyBaMM"
    elif parameter_number == 1:
        return "This is some basic information about Mohtat2020 parameters in a simple DFN model plotted using PyBaMM"
    elif parameter_number == 'experiment':
        return "This is a random experiment generated plotted using PyBaMM. The experiment cycle - " + str(cycle)