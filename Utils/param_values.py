import random

def param_values(parameter_name):

    if parameter_name == 'Chen2020':
        current_function = random.uniform(0, 10)
        upper_voltage = random.uniform(2.5, 4.2)
        lower_voltage = random.uniform(2.5, 4.2)
        ambient_temp = random.uniform(273.18, 298.15)
        initial_temp = random.uniform(273.18, 298.15)
        reference_temp = random.uniform(273.18, 298.15)

    elif parameter_name == "Marquis2019":
        current_function = random.uniform(0, 2)
        upper_voltage = random.uniform(3.1, 4.1)
        lower_voltage = random.uniform(3.1, 4.1)
        ambient_temp = random.uniform(273.18, 298.15)
        initial_temp = random.uniform(273.18, 298.15)
        reference_temp = random.uniform(273.18, 298.15)

    return current_function, upper_voltage, lower_voltage, ambient_temp, initial_temp, reference_temp