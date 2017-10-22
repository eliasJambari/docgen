import sys

from excel import parser
from excel import mapping
from excel import tools

if __name__ == "__main__":
    file_name = sys.argv[1]
    output_directory = sys.argv[2]
    sheets_info = {}

    # Parse and extract mapping information from excel file
    mapping_col = mapping.map_columns_location(parser.parse_sheets(file_name, {"mapping": [["A", "B"], 2]}, plain_table=True))

    print(mapping_col)

    # Parse needed data from excel file
    data = parser.parse_sheets(file_name, {"data": [list(mapping_col.keys()), 1]}, plain_table=True)

    print(data)

    mapping.generate_excel_files(data, mapping_col, file_name, output_directory)
