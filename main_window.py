from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from home_page import HomePage
from theory_window import TheoryWindow
from analytical_window import AnalyticalWindow
from euler_window import EulerWindow
from modified_euler_window import ModifiedEulerWindow
from navigation_manager import NavigationManager

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Set the title and size of the window
        self.setWindowTitle("Freefall Simulator")
        self.setGeometry(100, 100, 800, 800)

        # Create a stacked widget
        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # Initialise navigation manager
        self.navigation_manager = NavigationManager(self.stacked_widget)

        # Create and add pages to the stacked widget
        self.home_page = HomePage(self.navigation_manager, self)
        self.theory_window = TheoryWindow(self)
        self.analytical_window = AnalyticalWindow(self)
        self.euler_window = EulerWindow(self)
        self.modified_euler_window = ModifiedEulerWindow(self)

        self.stacked_widget.addWidget(self.home_page)
        self.stacked_widget.addWidget(self.theory_window)
        self.stacked_widget.addWidget(self.analytical_window)
        self.stacked_widget.addWidget(self.euler_window)
        self.stacked_widget.addWidget(self.modified_euler_window)

        # NavigationManager register windows
        self.navigation_manager.register_window('home', self.home_page)
        self.navigation_manager.register_window('analytical', self.analytical_window)
        self.navigation_manager.register_window('theory', self.theory_window)
        self.navigation_manager.register_window('euler', self.euler_window)
        self.navigation_manager.register_window('modified_euler', self.modified_euler_window) 

