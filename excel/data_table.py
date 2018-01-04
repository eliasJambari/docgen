import sys
import os
import logging
logger = logging.getLogger()

from excel import parser
from excel import mapping
from excel import tools
from excel import my_constants as cst


class DataTable():
    def __init__(self, excel_file, output_dir):
        self.excel_file = excel_file
        self.output_dir = output_dir
        self.generated_files = []

        self.data_mapping = self.build_map(["A", "B"])
        self.data = self.parse_data(2)

        logger.debug("DataTable created")

    def build_map(self, columns):
        raw_data = parser.parse_sheets(self.excel_file, {"mapping": [columns, 2]}, plain_table=True)
        data_mapping = mapping.build_mapping(raw_data)

        return data_mapping

    def parse_data(self, first_row):
        return parser.parse_sheets(self.excel_file, {"data": [list(self.data_mapping.keys()), first_row]}, plain_table=True)

    def generate_pdfs(self):
        self.generated_files = mapping.generate_excel_files(self.data, self.data_mapping, self.excel_file, self.output_dir)
        # pdf.convert_to(self.generated_files)

    def build_mail_query(self):
        mapping = self.build_mail_info()
        query = []

        # Build each entry
        for i in range(len(self.data)):
            entry = []
            # Entry array : Recipient, subject, message, attachment
            for element in mapping:
                entry.append(element.get_content(i))
            attachment = os.path.join(self.output_dir, str(str(i+1).rjust(3, '0')) + ".pdf")
            entry.append([attachment])
            query.append(entry)

        return query

    def build_mail_info(self):
        raw_data = parser.parse_sheets(self.excel_file, {"mail": [["A", "B"], 2]}, plain_table=True)

        mapping = []

        if len(raw_data) == 3:
            # Find all email data
            for i in range(len(raw_data)):
                mapping.append(CellFactory.create_cell(raw_data[i][cst.LOCATION], self.excel_file))
        else:
            sys.exit("No possible mapping with more than 3 inputs (subject, address, content)")

        return mapping


class CellFactory():
    def create_cell(content, file_name):
        # Determine type dynamically
        type = CellFactory.cell_type(content)

        # Create the right cell type of cell
        if type == cst.DYNAMIC_CONTENT:
            return DynamicCell(content, file_name)
        elif type == cst.STATIC_CONTENT:
            return StaticCell(content)

    def cell_type(content):
        return content.isalpha()


class AbstractCell():
    def get_content(self, position):
        raise NotImplementedError("Subclass must implement abstract method")


class DynamicCell(AbstractCell):
    def __init__(self, column, file_name):
        self.column = column
        self.data = self.parse_data(file_name)

    def parse_data(self, file_name):
        return parser.parse_sheets(file_name, {"data":[self.column, 2]}, plain_table=True)

    def get_content(self, position):
        tools.is_valid(position, len(self.data))
        return self.data[position][cst.UNIQUE_CELL]


class StaticCell(AbstractCell):
    def __init__(self, content):
        self.static_data = content

    def get_content(self, position):
        return self.static_data