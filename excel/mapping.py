import sys

from excel import parser
from excel import tools


def map_col_location(data_table):
    mapping = {}

    for entry in data_table:
        if len(entry) == 2:
            column = tools.letter_to_index(entry[0])
            location = tools.check_location(entry[1])

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

    columns = ["A", "B"]

    data_table = parser.parse_excel_file(file_name, sheet_name, columns, first_row=2)

    mapping = map_col_location(data_table)

    print(mapping)

    # tools.print_table(data_table)