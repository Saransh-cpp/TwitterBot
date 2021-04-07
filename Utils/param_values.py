import random
import importlib

spec = importlib.util.spec_from_file_location(
    "single_decimal_point.py", "Utils/single_decimal_point.py"
)
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)


def param_values(parameter_name):

    if parameter_name == "Chen2020":
        current_function = foo.single_decimal_point(1, 10, 0.1)
        upper_voltage = foo.single_decimal_point(2.5, 4.2, 0.1)
        lower_voltage = foo.single_decimal_point(2.5, 4.2, 0.1)
        ambient_temp = random.uniform(273.18, 298.15)
        initial_temp = random.uniform(273.18, 298.15)
        reference_temp = random.uniform(273.18, 298.15)

    elif parameter_name == "Marquis2019":
        current_function = foo.single_decimal_point(1, 5, 0.1)
        upper_voltage = foo.single_decimal_point(3.1, 4.1, 0.1)
        lower_voltage = foo.single_decimal_point(3.1, 4.1, 0.1)
        ambient_temp = random.uniform(273.18, 298.15)
        initial_temp = random.uniform(273.18, 298.15)
        reference_temp = random.uniform(273.18, 298.15)

    return (
        current_function,
        upper_voltage,
        lower_voltage,
        ambient_temp,
        initial_temp,
        reference_temp,
    )
