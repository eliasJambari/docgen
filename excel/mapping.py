import sys

from excel import parser
from excel import tools


def map_col_location(data_table, max_column):
    mapping = {}

    for entry in data_table:
        if len(entry) == 2:
            column = tools.letter_to_index(entry[0], max_column)
            location = tools.check_location(entry[1])

            # Check if not entry with same column/location
            if column in mapping.keys():
                sys.exit("Cannot have multiple entries with '" + column + "'")
            elif location in mapping.values():
                sys.exit("Cannot have multiple entries with '" + location + "'")
            else:
                mapping.update({column: location})

if __name__ == "__main__":
    file_name = sys.argv[1]
    sheet_name = sys.argv[2]

    columns = ["A", "B"]

    data_table, max_column = parser.parse_excel_file(file_name, sheet_name, columns, first_row=2)

    map_col_location(data_table, max_column)

    tools.print_table(data_table)