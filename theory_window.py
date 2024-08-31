from navigation_ribbon import NavigationRibbon

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)

class TheoryWindow(QWidget):
    def __init__(self, parent=None):
        super(TheoryWindow, self).__init__(parent)

        # Create a layout
        self.layout = QVBoxLayout(self)

        # Add the navigation ribbon
        self.navigation_ribbon = NavigationRibbon(self)
        self.layout.addWidget(self.navigation_ribbon)

        # Connect ribbon buttons to methods
        self.navigation_ribbon.home_button.clicked.connect(self.go_to_home)
        self.navigation_ribbon.analytical_button.clicked.connect(self.go_to_analytical_window)
        self.navigation_ribbon.euler_button.clicked.connect(self.go_to_euler_window)
        self.navigation_ribbon.modified_euler_button.clicked.connect(self.go_to_modified_euler_window)

        # Add a title label
        self.title_label = QLabel("Freefall Simulator", self)
        self.title_label.setStyleSheet("font-family: 'Consolas'; font-size: 42px; font-weight: bold;")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        # Add the descriptive text as a separate label
        self.description_label = QLabel("theory bla bla bla", self)
        self.description_label.setWordWrap(True)  # Enable text wrapping
        self.description_label.setStyleSheet("font-size: 16px; margin-top: 10px;")
        self.layout.addWidget(self.description_label)

    def go_to_home(self):
        self.parent().setCurrentIndex(0)  # Switch back to the home page

    def go_to_analytical_window(self):
        self.parent().setCurrentWidget(self.parent().parent().analytical_window)  # Switch to the Analytical Window

    def go_to_euler_window(self):
        self.parent().setCurrentWidget(self.parent().parent().euler_window)  # Switch to the Analytical Window

    def go_to_modified_euler_window(self):
        self.parent().setCurrentWidget(self.parent().parent().modified_euler_window)  # Switch to the Analytical Window