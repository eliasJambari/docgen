from PyQt5.QtCore import QThread, pyqtSignal
from excel.data_table import DataTable
from online.mail import MailManager


class DocumentGeneration(QThread):
    step_completed = pyqtSignal(int, str, str)
    finished = pyqtSignal()

    def __init__(self, parameters):
        QThread.__init__(self)
        self.parameters = parameters

    def __del__(self):
        self.wait()

    def do_task(self, i):
        self.sleep(i)
        return i

    def run(self):
        data_table = DataTable(self.parameters.excel_file, self.parameters.output_dir)

        data_table.generate_pdfs()

        mail_query = data_table.build_mail_query()

        mail_manager = MailManager(mail_query)
        mail_manager.send_emails()

        # self.step_completed.emit(weight, step, debug)

        self.finished.emit()


class Parameters():
    def __init__(self, excel_file, output_dir):
        self.excel_file = excel_file
        self.output_dir = output_dir