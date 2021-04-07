import unittest
import sys
import pybamm
import os
sys.path.append('C:\\Users\\Saransh\\Saransh_softwares\\Python Files\\TwitterBot\\Randomness')

from PlotGraph import plot_graph
# print(sys.path)

class TestPlotting(unittest.TestCase):

    def setUp(self):
        self.model = pybamm.lithium_ion.DFN()
        self.parameter_values = self.model.default_parameter_values

    def tearDown(self):
        os.remove('foo.png')
        sys.path.pop()

    def test_plot_graph(self):
        sim = pybamm.Simulation(self.model, parameter_values=self.parameter_values)
        sim.solve([0, 3600])
        solution = sim.solution
        plot_graph(solution=solution, sim=sim)
        path = 'foo.png'

        assert os.path.exists(path)

if __name__ == '__main__':
    unittest.main()