from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
)

class HomePage(QWidget):
    def __init__(self, navigation_manager, parent=None):
        super(HomePage, self).__init__(parent)

        #Create navigation manager
        self.navigation_manager = navigation_manager

        # Create a layout
        self.layout = QVBoxLayout(self)

        # Add a title label
        self.title_label = QLabel("Freefall Simulator", self)
        self.title_label.setStyleSheet("font-family: 'Consolas'; font-size: 42px; font-weight: bold;")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        # Add the welcome text as a centered label
        self.welcome_label = QLabel("Welcome to the Freefall Simulator!", self)
        self.welcome_label.setStyleSheet("font-size: 16px; margin-top: 10px;")
        self.welcome_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.welcome_label)

        # Add the descriptive text as a separate label
        self.description_label = QLabel(
            "The mechanics of objects in freefall can be difficult to solve as the acceleration of the object "
            "changes due to the varying drag, which is a function of the changing air density over altitutde. " 
            "Because of this, solutions for the mechanics of freefalling objects often involve solving coupled "
            "differential equations of altitude and velocity. This programme calculates the altitude and velocity "
            "mechanics for objects in freefall over time using 3 approaches. The Analytical Method uses derived "
            "predictions to calculate the altitude and velocity over time. The Euler Method solves the first order "
            "differential equations of altitude and velocity by numerical integration. The Modified Euler Method "
            "also solves the first order differential equations by numerical integration over the midpoints. "
            "Click one of the following options to proceed:", self
        )
        self.description_label.setWordWrap(True)  # Enable text wrapping
        self.description_label.setStyleSheet("font-size: 16px; margin-top: 10px;")
        self.layout.addWidget(self.description_label)

        # Add buttons
        self.button1 = QPushButton("Theory", self)
        self.button2 = QPushButton("Analytical Method", self)
        self.button3 = QPushButton("Euler Method", self)
        self.button4 = QPushButton("Modified Euler Method", self)
        self.button1.setStyleSheet("width: 200px; height: 100px; font-size: 18px;")
        self.button2.setStyleSheet("width: 200px; height: 100px; font-size: 18px;")
        self.button3.setStyleSheet("width: 200px; height: 100px; font-size: 18px;")
        self.button4.setStyleSheet("width: 200px; height: 100px; font-size: 18px;")

        # Add buttons to the layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)
        button_layout.addWidget(self.button3)
        button_layout.addWidget(self.button4)
        self.layout.addLayout(button_layout)

        # Connect buttons to navigation manager
        self.button1.clicked.connect(self.navigation_manager.go_to_theory)
        self.button2.clicked.connect(self.navigation_manager.go_to_analytical)
        self.button3.clicked.connect(self.navigation_manager.go_to_euler)
        self.button4.clicked.connect(self.navigation_manager.go_to_modified_euler)
