import sys

from gui.ui import Ui_main_window
from gui.events import Events
from PyQt5.QtWidgets import QApplication, QMainWindow


def load_gui():
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(window)

    events = Events(app, ui)
    events.add_events()

    window.show()
    sys.exit(app.exec_())