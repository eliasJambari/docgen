import sys

from excel import parser
from excel import mapping
from excel import pdf
from excel import tools

from online import mail

if __name__ == "__main__":
    # file_name = sys.argv[1]
    # output_directory = sys.argv[2]
    #
    # # Parse and extract mapping information from excel file
    # mapping_col = mapping.build_mapping(parser.parse_sheets(file_name, {"mapping": [["A", "B"], 2]}, plain_table=True))
    #
    # print(mapping_col)
    #
    # # Parse needed data from excel file
    # data = parser.parse_sheets(file_name, {"data": [list(mapping_col.keys()), 2]}, plain_table=True)
    #
    # tools.print_table(data)
    #
    # generated_files = mapping.generate_excel_files(data, mapping_col, file_name, output_directory)
    #
    # pdf.convert_to(generated_files)
    #
    #
    # mail.send_mails_w_attachment(emails_to_send)
    pass