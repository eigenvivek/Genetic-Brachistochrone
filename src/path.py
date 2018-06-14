class Path():
    """A class holding the attributes of an individual path."""

    def __init__(self, external_DNA=None):
        """Initialize the class."""

        # Make a path
        if external_DNA == None:
            self.dna = DNA()
        else:
            self.dna = DNA(external_DNA)


    def evaluate(self):
        """Returns the inverse time required to traverse a path and error estimation."""

        # Differential time as a function of x
        dt = lambda x: sqrt( (1 + self.dna.f2.derivative()(x)**2) / (-self.dna.f2(x)) )

        # Integrate dt over the domain [0,1]
        try:
            T = integrate.quad(dt, a=0, b=1, limit=250)
            T_inv = T[0] ** (-1)
            err = T[1]
            self.valid = True

        except:
            # Exception occurs if f(x)>0 for x in [0,1]
            T = np.inf
            T_inv = T ** (-1)
            err = 0
            self.valid = False

        return T_inv, err

    def visualize(self, title=None):
        """Returns a plot of the interpolated path."""

        # A more granular domain
        xnew = np.linspace(0,1,1001)

        # Plot setup
        plt.plot(self.dna.x, self.dna.y, 'o',         # Original points
                 xnew, self.dna.f2(xnew), '--',       # Interpolated path
                 xnew, [0]*len(xnew),                 # Cutoff line at y=0
                 xnew, interp1d([p1[0],p2[0]],        # Linear
                                [p1[1],p2[1]],
                                kind='linear')(xnew)
                )
        # Plot titles
        if title != None:
            plt.title(title)
        plt.xlabel('x')
        plt.ylabel('y')

        # Render
        plt.show()
