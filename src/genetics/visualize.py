import numpy as np
import matplotlib.pyplot as plt
from genetics.curves import f_linear, T_linear, x, y, T_cycloid
from genetics.constants import P1, P2

def visualize(path, title=None):
    """Returns a plot of the interpolated path."""

    # A more granular domain
    xnew = np.linspace(P1[0], P2[0], 1001)

    # Plot setup
    plt.plot(path.dna.x, path.dna.y, 'o')
    plt.plot(xnew, path.dna.f(xnew), '--', label='Path')
    plt.plot(xnew, [P1[1]] * len(xnew), label='Cutoff')
    plt.plot(xnew, f_linear(xnew), label='Linear')
    plt.plot(x, y, label='Cycloid')

    # try:
    #     plt.text(0.8, 0, str(path.time))
    # except:
    #     path.evaluate()
    #     plt.text(0.8, 0, str(path.time))
    # plt.text(0.8, -0.5, str(T))

    # Plot titles
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    # plt.legend()

    # Render
    plt.show()
