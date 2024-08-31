from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from planets import Planet
from freefall_object import Freefall_object
from analytical_plotter import FreefallPlotter
from navigation_ribbon import NavigationRibbon

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
QDialog,
QLabel,
QVBoxLayout,
QWidget
)

class AnalyticalWindow(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Set the title and size of the window
        self.setWindowTitle("Analytical Method")
        self.setGeometry(100, 100, 800, 600)

        # Create a layout
        self.layout = QVBoxLayout()

        # Add the navigation ribbon
        self.navigation_ribbon = NavigationRibbon(self)
        self.layout.addWidget(self.navigation_ribbon)

        # Connect ribbon buttons to methods
        self.navigation_ribbon.home_button.clicked.connect(self.go_to_home)
        #self.navigation_ribbon.theory_button.clicked.connect(self.go_to_theory)
        self.navigation_ribbon.analytical_button.clicked.connect(self.show)  # Stay on this window
        #self.navigation_ribbon.euler_button.clicked.connect(self.go_to_euler)
        #self.navigation_ribbon.modified_euler_button.clicked.connect(self.go_to_modified_euler)

        # Add a title label
        self.title_label = QLabel("Freefall Simulator", self)
        self.title_label.setStyleSheet("font-family: 'Consolas'; font-size: 42px; font-weight: bold;")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        # Add the descriptive text as a separate label
        self.description_label = QLabel(
            "bla bla bla", self
        )
        self.description_label.setWordWrap(True)  # Enable text wrapping
        self.description_label.setStyleSheet("font-size: 16px; margin-top: 10px;")
        self.layout.addWidget(self.description_label)

        #Create a Matplotlib figure and canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        #initialise plotter
        falling_object = Freefall_object("Ball", 1000, 0, 0.47, 50, 1)
        Earth = Planet("Earth", 9.81, 1.225)
        self.plotter = FreefallPlotter(falling_object, Earth)

        self.plot_freefall()
        self.setLayout(self.layout)

    def plot_freefall(self):
        ax1 = self.figure.add_subplot(111)
        ax2 = ax1.twinx() # Create a secondary y-axis for velocity

        self.plotter.plot_freefall(ax1,ax2)
        self.canvas.draw()

    def go_to_home(self):
        self.hide()
        self.parent().show()
    



