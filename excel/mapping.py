import sys

from excel import parser
from excel import tools
from excel import my_constants as cst


def map_columns_location(data_table):
    mapping = {}

    for entry in data_table:
        if len(entry) == 2:
            column = tools.letter_to_index(entry[cst.COLUMN])
            location = tools.check_location(entry[cst.LOCATION])

            # Check if not entry with same column/location
            if any(location in cells for cells in mapping.values()):
                sys.exit("Cannot have multiple entries with '" + location + "'")
            elif column in mapping.keys():
                mapping.get(column).append(location)
            else:
                mapping.update({column: [location]})
        else:
            sys.exit("No possible mapping with more than 2 columns")

    return mapping

if __name__ == "__main__":
    file_name = sys.argv[1]
    sheet_name = sys.argv[2]

    sheets_info = {}

    sheets_info.update({sheet_name: [["A", "B"], 2]})

    data_tables = parser.parse_sheets(file_name, sheets_info)

    mapping = map_columns_location(data_tables[sheet_name])

    print(mapping)