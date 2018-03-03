import logging

logger = logging.getLogger()

from online import mail

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import Qt

from gui.preferences.ui_preferences import Ui_preferences
from gui.preferences import functions
from gui import my_constants as cst


class Preferences():
    def __init__(self):
        self.window = QDialog()
        self.ui = Ui_preferences()

        self.init()

        self.window.show()

    def init(self):
        self.ui.setupUi(self.window)
        self.add_events()

        functions.set_validation_state(self.ui, cst.NOT_VALIDATED)

    def add_events(self):
        # Add events to QDialog preferences
        self.ui.validate_btn.clicked.connect(self.check_auth)
        self.ui.clear_btn.clicked.connect(self.clear_auth)
        self.ui.cancel_btn.clicked.connect(self.window.close)

    def check_auth(self):
        functions.set_validation_state(self.ui, cst.VALIDATING)

        QApplication.setOverrideCursor(Qt.WaitCursor)

        user = self.ui.add_txt.text() + "@gmail.com"
        password = self.ui.pass_txt.text()

        print("User : " + str(user))
        print("Password : " + str(password))
        result = mail.check_auth(user, password)
        print(result)

        if result:
            functions.set_validation_state(self.ui, cst.VALIDATED)
        else:
            functions.set_validation_state(self.ui, cst.INCORRECT_LOGIN)

        QApplication.restoreOverrideCursor()

    def clear_auth(self):
        # Clear input fields
        self.ui.add_txt.setText("")
        self.ui.pass_txt.setText("")

        # Disable options (mode : need validation)
        functions.set_validation_state(self.ui, cst.NOT_VALIDATED)