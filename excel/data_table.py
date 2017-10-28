from excel import parser
from excel import mapping
from excel import pdf


class DataTable():
    def __init__(self, excel_file, output_dir):
        self.excel_file = excel_file
        self.output_dir = output_dir
        self.generated_files = []

        self.data_mapping = self.build_map(["A", "B"])
        self.data = self.parse_data(2)

    def build_map(self, columns):
        raw_data = parser.parse_sheets(self.excel_file, {"mapping": [columns, 2]}, plain_table=True)
        data_mapping = mapping.build_mapping(raw_data)

        return data_mapping

    def parse_data(self, first_row):
        return parser.parse_sheets(self.excel_file, {"data": [list(self.data_mapping.keys()), first_row]}, plain_table=True)

    def generate_pdfs(self):
        self.generated_files = mapping.generate_excel_files(self.data, self.data_mapping, self.excel_file, self.output_dir)
        pdf.convert_to(self.generated_files)

    def build_mail_query(self):
        pass