from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QApplication
from home_page import HomePage
from analytical_window import AnalyticalWindow

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
        self.analytical_window = AnalyticalWindow(self)

        self.stacked_widget.addWidget(self.home_page)
        self.stacked_widget.addWidget(self.analytical_window)

        # Connect buttons on the homepage to switch pages
        self.home_page.button1.clicked.connect(self.open_theory)  # Placeholder
        self.home_page.button2.clicked.connect(self.open_analytical_method)
        self.home_page.button3.clicked.connect(self.open_euler_method)  # Placeholder
        self.home_page.button4.clicked.connect(self.open_modified_euler_method)  # Placeholder

    def open_theory(self):
        print("Theory page is not implemented yet")

    def open_analytical_method(self):
        self.stacked_widget.setCurrentWidget(self.analytical_window)
        self.analytical_window.navigation_ribbon.set_active_button("analytical")

    def open_euler_method(self):
        print("Euler Method page is not implemented yet")

    def open_modified_euler_method(self):
        print("Modified Euler Method page is not implemented yet")