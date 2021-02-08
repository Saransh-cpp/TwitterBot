import pybamm
import tweepy
from keys import Keys
import time
from IPython.display import display
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy.interactive import printing
printing.init_printing(use_latex=True)

auth = tweepy.OAuthHandler(Keys.CONSUMER_KEY, Keys.CONSUMER_SECRET)
auth.set_access_token(Keys.ACCESS_KEY, Keys.ACCESS_SECRET)
api = tweepy.API(auth)

# mention = api.mentions_timeline()

model = pybamm.BaseModel()

x = pybamm.Variable("x")
y = pybamm.Variable("y")

dxdt = 4 * x - 2 * y
dydt = 3 * x - y

# func = sp.Function('func')
# X = sp.Symbol('x')
# Y = sp.Symbol('y')
# func = sp.sin(X)
# inte = sp.Derivative(func, X)
#
# display(inte)

model.rhs = {x: dxdt, y: dydt}
model.initial_conditions = {x: pybamm.Scalar(1), y: pybamm.Scalar(2)}
model.variables = {"x": x, "y": y, "z": x + 4 * y}

disc = pybamm.Discretisation()  # use the default discretisation
disc.process_model(model)

solver = pybamm.ScipySolver()
t = np.linspace(0, 1, 20)
solution = solver.solve(model, t)

t_sol, y_sol = solution.t, solution.y  # get solution times and states
x = solution["x"]  # extract and process x from the solution
y = solution["y"]  # extract and process y from the solution

t_fine = np.linspace(0, t[-1], 1000)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 4))
ax1.plot(t_fine, 2 * np.exp(t_fine) - np.exp(2 * t_fine), t_sol, x(t_sol), "o")
ax1.set_xlabel("t")
ax1.legend(["2*exp(t) - exp(2*t)", "x"], loc="best")

ax2.plot(t_fine, 3 * np.exp(t_fine) - np.exp(2 * t_fine), t_sol, y(t_sol), "o")
ax2.set_xlabel("t")
ax2.legend(["3*exp(t) - exp(2*t)", "y"], loc="best")

plt.tight_layout()
# img = plt.show()

plt.savefig('foo.png', bbox_inches='tight')


def plot_graph():

    media = api.media_upload('foo.png')
    tweet = inte

    api.update_status(status=tweet, media_ids=[media.media_id])


while True:
    print('Tweeting....')
    plot_graph()
    time.sleep(5)

# Python program creating a
# small document using pylatex

import numpy as np

# importing from a pylatex module
# from pylatex import Document, Section, Subsection, Tabular
# from pylatex import Math, TikZ, Axis, Plot, Figure, Matrix, Alignat
# from pylatex.utils import italic
# import os
#
# if __name__ == '__main__':
#
# 	geometry_options = {"tmargin": "1cm", "lmargin": "10cm"}
# 	doc = Document(geometry_options=geometry_options)
#
# 	# creating a pdf with title "the simple stuff"
# 	with doc.create(Section('The simple stuff')):
# 		doc.append('Some regular text and some')
# 		doc.append(italic('italic text. '))
# 		doc.append('\nAlso some crazy characters: $&#{}')
# 		with doc.create(Subsection('Math that is incorrect')):
# 			doc.append(Math(data=['2*3', '=', 9]))
#
# 		# creating subsection of a pdf
# 		with doc.create(Subsection('Table of something')):
# 			with doc.create(Tabular('rc|cl')) as table:
# 				table.add_hline()
# 				table.add_row((1, 2, 3, 4))
# 				table.add_hline(1, 2)
# 				table.add_empty_row()
# 				table.add_row((4, 5, 6, 7))
#
# 	# making a pdf using .generate_pdf
# 	doc.generate_pdf('full', clean_tex=False)

