from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QApplication
from home_page import HomePage
from theory_window import TheoryWindow
from analytical_window import AnalyticalWindow
from euler_window import EulerWindow
from modified_euler_window import ModifiedEulerWindow

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Set the title and size of the window
        self.setWindowTitle("Freefall Simulator")
        self.setGeometry(100, 100, 800, 800)

        # Create a stacked widget
        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # Create and add pages to the stacked widget
        self.home_page = HomePage(self)
        self.theory_window = TheoryWindow(self)
        self.analytical_window = AnalyticalWindow(self)
        self.euler_window = EulerWindow(self)
        self.modified_euler_window = ModifiedEulerWindow(self)

        self.stacked_widget.addWidget(self.home_page)
        self.stacked_widget.addWidget(self.theory_window)
        self.stacked_widget.addWidget(self.analytical_window)
        self.stacked_widget.addWidget(self.euler_window)
        self.stacked_widget.addWidget(self.modified_euler_window)

        # Connect buttons on the homepage to switch pages
        self.home_page.button1.clicked.connect(self.open_theory)  
        self.home_page.button2.clicked.connect(self.open_analytical_method)
        self.home_page.button3.clicked.connect(self.open_euler_method)  
        self.home_page.button4.clicked.connect(self.open_modified_euler_method)  

        #navigation ribbon buttons disabled
        self.theory_window.navigation_ribbon.set_active_button("theory")
        self.analytical_window.navigation_ribbon.set_active_button("analytical")
        self.euler_window.navigation_ribbon.set_active_button("euler")
        self.modified_euler_window.navigation_ribbon.set_active_button("modified_euler")

    def open_theory(self):
        self.stacked_widget.setCurrentWidget(self.theory_window)

    def open_analytical_method(self):
        self.stacked_widget.setCurrentWidget(self.analytical_window)

    def open_euler_method(self):
        self.stacked_widget.setCurrentWidget(self.euler_window)

    def open_modified_euler_method(self):
        self.stacked_widget.setCurrentWidget(self.modified_euler_window)