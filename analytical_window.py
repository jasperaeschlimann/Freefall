from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from planets import Planet
from freefall_object import Freefall_object
from analytical_plotter import FreefallPlotter
from navigation_ribbon import NavigationRibbon

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QDoubleSpinBox,
    QVBoxLayout
)

class AnalyticalWindow(QWidget):
    def __init__(self, parent=None):
        super(AnalyticalWindow, self).__init__(parent)

        # Create a layout
        self.layout = QVBoxLayout(self)

        # Add the navigation ribbon
        self.navigation_ribbon = NavigationRibbon(self)
        self.layout.addWidget(self.navigation_ribbon)

        # Connect ribbon buttons to methods
        self.navigation_ribbon.home_button.clicked.connect(self.go_to_home)
        self.navigation_ribbon.theory_button.clicked.connect(self.go_to_theory_window)
        self.navigation_ribbon.euler_button.clicked.connect(self.go_to_euler_window)
        self.navigation_ribbon.modified_euler_button.clicked.connect(self.go_to_modified_euler_window)

        # Add a title label
        self.title_label = QLabel("Freefall Simulator", self)
        self.title_label.setStyleSheet("font-family: 'Consolas'; font-size: 42px; font-weight: bold;")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        # Add the descriptive text as a separate label
        self.description_label = QLabel("bla bla bla", self)
        self.description_label.setWordWrap(True)  # Enable text wrapping
        self.description_label.setStyleSheet("font-size: 16px; margin-top: 10px;")
        self.layout.addWidget(self.description_label)

        # Add a spin box for start height adjustment
        self.start_height_spinbox = QDoubleSpinBox(self)
        self.start_height_spinbox.setRange(0.01, 50000)  # Set the range from 0 to 50,000 meters
        self.start_height_spinbox.setValue(1000)  # Default value
        self.start_height_spinbox.setPrefix("Start Height (m): ")
        self.start_height_spinbox.valueChanged.connect(self.update_start_height)
        self.layout.addWidget(self.start_height_spinbox)

        # Add a spin box for drag coefficient adjustment
        self.drag_coefficient_spinbox = QDoubleSpinBox(self)
        self.drag_coefficient_spinbox.setRange(0.01, 50000)  # Set the range
        self.drag_coefficient_spinbox.setValue(0.47)  # Default value
        self.drag_coefficient_spinbox.setPrefix("Drag Coefficient: ")
        self.drag_coefficient_spinbox.valueChanged.connect(self.update_drag_coefficient)
        self.layout.addWidget(self.drag_coefficient_spinbox)

        # Add a spin box for mass adjustment
        self.mass_spinbox = QDoubleSpinBox(self)
        self.mass_spinbox.setRange(0.01, 50000)  # Set the range
        self.mass_spinbox.setValue(50)  # Default value
        self.mass_spinbox.setPrefix("Mass (kg): ")
        self.mass_spinbox.valueChanged.connect(self.update_mass)
        self.layout.addWidget(self.mass_spinbox)

        # Add a spin box for cross sectional area adjustment
        self.cross_sectional_area_spinbox = QDoubleSpinBox(self)
        self.cross_sectional_area_spinbox.setRange(0.01, 50000)  # Set the range
        self.cross_sectional_area_spinbox.setValue(1)  # Default value
        self.cross_sectional_area_spinbox.setPrefix("Cross Sectional Area (m^2): ")
        self.cross_sectional_area_spinbox.valueChanged.connect(self.update_cross_sectional_area)
        self.layout.addWidget(self.cross_sectional_area_spinbox)

        # Create a Matplotlib figure and canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        # Initialize plotter
        self.falling_object = Freefall_object("Ball", self.start_height_spinbox.value(), 0, self.drag_coefficient_spinbox.value(), self.mass_spinbox.value(), self.cross_sectional_area_spinbox.value())
        self.planet = Planet("Earth", 9.81, 1.225)
        self.plotter = FreefallPlotter(self.falling_object, self.planet)

        self.plot_freefall()

    def update_start_height(self, value):
        """
        Update the start height of the falling object and replot the graph.
        """
        self.falling_object.start_height = value
        self.plot_freefall()

    def update_drag_coefficient(self, value):
        """
        Update the drag coefficient of the falling object and replot the graph.
        """
        self.falling_object.drag_coefficient = value
        self.plot_freefall()

    def update_mass(self, value):
        """
        Update the mass of the falling object and replot the graph.
        """
        self.falling_object.mass = value
        self.plot_freefall()

    def update_cross_sectional_area(self, value):
        """
        Update the cross sectional area of the falling object and replot the graph.
        """
        self.falling_object.cross_sectional_area = value
        self.plot_freefall()

    def plot_freefall(self):
        self.figure.clear()  # Clear the previous plot
        ax1 = self.figure.add_subplot(111)
        ax2 = ax1.twinx()  # Create a secondary y-axis for velocity

        self.plotter.plot_freefall(ax1, ax2)
        self.canvas.draw()

    def go_to_home(self):
        self.parent().setCurrentIndex(0)  # Switch back to the home page

    def go_to_theory_window(self):
        self.parent().setCurrentWidget(self.parent().parent().theory_window)  # Switch to the TheoryWindow

    def go_to_euler_window(self):
        self.parent().setCurrentWidget(self.parent().parent().euler_window)  # Switch to the Analytical Window

    def go_to_modified_euler_window(self):
        self.parent().setCurrentWidget(self.parent().parent().modified_euler_window)  # Switch to the Analytical Window
