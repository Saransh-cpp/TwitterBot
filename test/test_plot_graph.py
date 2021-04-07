import unittest
import pybamm
import os
import importlib.util

spec = importlib.util.spec_from_file_location(
    "PlotGraph.py", "Randomness/PlotGraph.py"
)
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)


class TestPlotting(unittest.TestCase):

    def setUp(self):
        self.model = pybamm.lithium_ion.DFN()
        self.parameter_values = self.model.default_parameter_values

    def tearDown(self):
        os.remove('foo.png')

    def test_plot_graph(self):
        sim = pybamm.Simulation(self.model, parameter_values=self.parameter_values)
        sim.solve([0, 3600])
        solution = sim.solution
        foo.plot_graph(solution=solution, sim=sim)
        path = 'foo.png'

        assert os.path.exists(path)

if __name__ == '__main__':
    unittest.main()