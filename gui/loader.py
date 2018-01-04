import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from gui.events import Main
from gui.ui_main import Ui_main_window


def load_gui():
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(window)

    events = Main(app, ui)
    events.add_events()

    window.show()
    sys.exit(app.exec_())