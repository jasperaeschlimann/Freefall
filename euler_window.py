from navigation_ribbon import NavigationRibbon

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)

class EulerWindow(QWidget):
    def __init__(self, parent=None):
        super(EulerWindow, self).__init__(parent)

        # Create a layout
        self.layout = QVBoxLayout(self)

        # Add the navigation ribbon
        self.navigation_ribbon = NavigationRibbon(self)
        self.navigation_ribbon.set_active_button("euler")
        self.layout.addWidget(self.navigation_ribbon)

        # Connect ribbon buttons to NavigationManager
        self.navigation_ribbon.home_button.clicked.connect(lambda: self.parent().parent().navigation_manager.go_to_home())
        self.navigation_ribbon.theory_button.clicked.connect(lambda: self.parent().parent().navigation_manager.go_to_theory())
        self.navigation_ribbon.analytical_button.clicked.connect(lambda: self.parent().parent().navigation_manager.go_to_analytical())
        self.navigation_ribbon.modified_euler_button.clicked.connect(lambda: self.parent().parent().navigation_manager.go_to_modified_euler())

        # Add a title label
        self.title_label = QLabel("Freefall Simulator", self)
        self.title_label.setStyleSheet("font-family: 'Consolas'; font-size: 42px; font-weight: bold;")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        # Add the descriptive text as a separate label
        self.description_label = QLabel("euler bla bla bla", self)
        self.description_label.setWordWrap(True)  # Enable text wrapping
        self.description_label.setStyleSheet("font-size: 16px; margin-top: 10px;")
        self.layout.addWidget(self.description_label)
