from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton

class NavigationRibbon(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)

        # Create buttons for the ribbon
        self.home_button = QPushButton("Home", self)
        self.theory_button = QPushButton("Theory", self)
        self.analytical_button = QPushButton("Analytical", self)
        self.euler_button = QPushButton("Euler", self)
        self.modified_euler_button = QPushButton("Modified Euler", self)

        # Add buttons to the layout
        layout.addWidget(self.home_button)
        layout.addWidget(self.theory_button)
        layout.addWidget(self.analytical_button)
        layout.addWidget(self.euler_button)
        layout.addWidget(self.modified_euler_button)

        self.setLayout(layout)
    
    def set_active_button(self, active_button: str):
        """
        Disable the button corresponding to the current page.
        """
        # First, enable all buttons
        self.home_button.setEnabled(True)
        self.theory_button.setEnabled(True)
        self.analytical_button.setEnabled(True)
        self.euler_button.setEnabled(True)
        self.modified_euler_button.setEnabled(True)

        # Then, disable the active button
        if active_button == "home":
            self.home_button.setEnabled(False)
        elif active_button == "theory":
            self.theory_button.setEnabled(False)
        elif active_button == "analytical":
            self.analytical_button.setEnabled(False)
        elif active_button == "euler":
            self.euler_button.setEnabled(False)
        elif active_button == "modified_euler":
            self.modified_euler_button.setEnabled(False)
