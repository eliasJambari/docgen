import sys

from excel import parser
from excel import mapping
from excel import tools

if __name__ == "__main__":
    file_name = sys.argv[1]
    sheets_info = {}

    # Parse and extract mapping information from excel file
    mapping = mapping.map_columns_location(parser.parse_sheets(file_name, {"mapping": [["A", "B"], 2]}, plain_table=True))

    print(mapping)

    # Parse needed data from excel file
    data = parser.parse_sheets(file_name, {"data": [list(mapping.keys()), 1]}, plain_table=True)

    tools.print_table(data)
