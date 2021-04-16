import unittest
import importlib.util

spec = importlib.util.spec_from_file_location(
    "Information.py", "InformationModule/Information.py"
)
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)


class TestInformation(unittest.TestCase):
    def setUp(self):
        self.cccv_cycle = [
            (
                "Discharge at C/10 for 10 hours or until 3.3 V",
                "Rest for 1 hour",
                "Charge at 1 A until 4.1 V",
                "Hold at 4.1 V until 50 mA",
                "Rest for 1 hour",
            )
        ]

    def test_Information_with_no_solver(self):
        self.assertEqual(
            foo.information(0, None, None),
            "This is some basic information about Chen2020 parameters in a simple DFN model plotted using PyBaMM",
        )
        self.assertEqual(
            foo.information(1, None, None),
            "This is some basic information about Marquis2019 parameters in a simple DFN model plotted using PyBaMM",
        )
        self.assertEqual(
            foo.information(2, None, None),
            "This is some basic information about Ecker2015 parameters in a simple DFN model plotted using PyBaMM",
        )
        self.assertEqual(
            foo.information(3, None, None),
            "This is some basic information about Mohtat2020 parameters in a simple DFN model plotted using PyBaMM",
        )

    def test_Information_with_solver(self):
        self.assertEqual(
            foo.information("experiment", self.cccv_cycle, 1),
            "The experiment cycle- "
            + str(self.cccv_cycle)
            + ". Solver:  "
            + "Casadi"
            + ", mode:  "
            + "fast",
        )
        self.assertEqual(
            foo.information("experiment", self.cccv_cycle, 2),
            "The experiment cycle- "
            + str(self.cccv_cycle)
            + ". Solver:  "
            + "Casadi"
            + ", mode:  "
            + "safe",
        )
        self.assertEqual(
            foo.information("experiment", self.cccv_cycle, 3),
            "The experiment cycle- "
            + str(self.cccv_cycle)
            + ". Solver:  "
            + "Casadi"
            + ", mode:  "
            + "fast with events",
        )
        self.assertEqual(
            foo.information("experiment", self.cccv_cycle, 0),
            "The experiment cycle- "
            + str(self.cccv_cycle)
            + ". Solver: "
            + "None"
            + ", mode: "
            + "None",
        )


if __name__ == "__main__":
    unittest.main()