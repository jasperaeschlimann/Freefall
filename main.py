from planets import Planet
from freefall_object import Freefall_object
from analytical_plotter import FreefallPlotter

def main():
    """
    Create instances of the falling object and planet. Then plot the analytical freefall
    """
    falling_object = Freefall_object("Ball", 1000, 0, 0.47, 50, 1)
    Earth = Planet("Earth", 9.81, 1.225)

    plotter = FreefallPlotter(falling_object, Earth)
    plotter.plot_freefall()

if __name__ == "__main__":
    main()