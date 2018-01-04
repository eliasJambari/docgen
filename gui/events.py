import sys
import logging
logger = logging.getLogger()

from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QDialog
from gui.ui_preferences import Ui_preferences

from online import mail
from gui import events_fcts as fcts
from gui import my_constants as cst

class Events():
    def __init__(self, app, ui):
        self.app = app
        self.ui = ui
        self.ui_preferences = None
        self.ui.window = None
        # self.ui.central_widget.se

    def add_events(self):
        self.add_menu_events()

        self.ui.generate_btn.clicked.connect(self.test)
        self.ui.input_file_btn.clicked.connect(self.choose_file)
        self.ui.output_dir_btn.clicked.connect(self.choose_dir)

    def add_menu_events(self):
        self.ui.quit_act.triggered.connect(self.quit_app)
        self.ui.preferences_act.triggered.connect(self.open_preferences)

    def test(self):
        print("Test")

    def choose_file(self):
        file_name, extension = QFileDialog.getOpenFileName(self.ui.central_widget, "Choose excel file",
                                            ".", "Excel file (*.xlsx)")

        logger.info("Selected file : " + str(file_name))
        self.ui.input_file_txt.setText(file_name)

    def choose_dir(self):
        output_dir = QFileDialog.getExistingDirectory(self.ui.central_widget, "Choose output folder", ".")

        logger.info("Selected directory : " + str(output_dir))
        self.ui.output_dir_txt.setText(output_dir)

    def open_preferences(self):
        logger.info("Opened Dialog Preferences")
        self.ui.window = QDialog()
        self.ui_preferences = Ui_preferences()
        self.ui_preferences.setupUi(self.ui.window)

        # Add events to QDialog preferences
        self.ui_preferences.validate_btn.clicked.connect(self.check_auth)
        self.ui_preferences.clear_btn.clicked.connect(self.clear_auth)
        fcts.set_validation_state(self.ui_preferences, cst.NOT_VALIDATED)

        self.ui.window.show()

    def check_auth(self):
        fcts.set_validation_state(self.ui_preferences, cst.VALIDATING)

        user = self.ui_preferences.add_txt.text() + "@gmail.com"
        password = self.ui_preferences.pass_txt.text()

        print("User : " + str(user))
        print("Password : " + str(password))
        result = mail.check_auth(user, password)
        print(result)

        if result:
            fcts.set_validation_state(self.ui_preferences, cst.VALIDATED)
        else:
            fcts.set_validation_state(self.ui_preferences, cst.INCORRECT_LOGIN)

    def clear_auth(self):
        # Clear input fields
        self.ui_preferences.add_txt.setText("")
        self.ui_preferences.pass_txt.setText("")

        # Disable options (mode : need validation)
        fcts.set_validation_state(self.ui_preferences, cst.NOT_VALIDATED)

    def quit_app(self):
        # Add app exit when X button is pressed
        logger.info("Exiting application")
        sys.exit(self.app.exec_())