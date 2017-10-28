import sys

from excel.data_table import DataTable
from online.mail import MailManager

if __name__ == "__main__":
    # Initial parameters
    excel_file = sys.argv[1]
    output_dir = sys.argv[2]
    # email column

    data_table = DataTable(excel_file, output_dir)

    data_table.generate_pdfs()

    # mail_query = data_table.build_mail_query()

    # MailManager(mail_query)
