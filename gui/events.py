import logging
import sys

logger = logging.getLogger()

from PyQt5.QtWidgets import QFileDialog
from gui.preferences.events import Preferences
from gui.generation import DocumentGeneration, Parameters
from gui import progress

class Main():
    def __init__(self, app, ui):
        self.app = app
        self.ui = ui
        self.preferences = None
        self.doc_gen = None

    def add_events(self):
        self.add_menu_events()

        self.ui.generate_btn.clicked.connect(self.generate)
        self.ui.input_file_btn.clicked.connect(self.choose_file)
        self.ui.output_dir_btn.clicked.connect(self.choose_dir)

    # Menu bar
    def add_menu_events(self):
        self.ui.quit_act.triggered.connect(self.quit_app)
        self.ui.preferences_act.triggered.connect(self.open_preferences)

    def generate(self):

        parameters = Parameters(self.ui.input_file_txt.text(), self.ui.output_dir_txt.text())

        self.doc_gen = DocumentGeneration(parameters)

        # print(self.doc_gen.parameters.input_file)
        # print(self.doc_gen.parameters.output_dir)

        n_elements = 2
        self.ui.generation_pbr.setMaximum(2+3*n_elements)
        self.ui.generation_pbr.setValue(0)

        progress.n_tasks = 2+3*n_elements
        print(str(progress.n_tasks) + " tasks")

        # Link functions for progress and termination
        self.doc_gen.step_completed.connect(self.update_progress)
        self.doc_gen.finished.connect(self.completed)

        self.doc_gen.start()

        # Activate buttons for stopping the generation
        self.ui.cancel_btn.setEnabled(True)
        self.ui.cancel_btn.clicked.connect(self.doc_gen.terminate)

        self.ui.generate_btn.setEnabled(False)

    def update_progress(self, weight, step, debug = None):
        self.ui.generation_pbr.setValue(self.ui.generation_pbr.value() + weight)
        self.ui.status_bar.showMessage(str(step))

        if debug is not None:
            logger.debug(debug)

    def completed(self):
        pass

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

        self.preferences = Preferences()

        # self.ui.w_preferences = self.preferences.window

    def quit_app(self):
        # Add app exit when X button is pressed
        logger.info("Exiting application")
        sys.exit(self.app.exec_())