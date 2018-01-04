import sys
import logging
logger = logging.getLogger()

from excel.data_table import DataTable
from online.mail import MailManager
from dev import log
from gui import loader

if __name__ == "__main__":
    # Initial parameters
    excel_file = sys.argv[1]
    output_dir = sys.argv[2]

    log.configure()
    loader.load_gui()

    # data_table = DataTable(excel_file, output_dir)
    #
    # data_table.generate_pdfs()
    #
    # mail_query = data_table.build_mail_query()
    #
    # mail_manager = MailManager(mail_query)
    # mail_manager.send_emails()
