from main_window import mainwindow
from PyQt5.QtWidgets import QApplication

import sys

def main():
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()