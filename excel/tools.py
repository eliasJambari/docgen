import sys
import string

from openpyxl.utils import coordinate_from_string


def check_location(cell_location):
    try:
        coordinate_from_string(cell_location)
        return cell_location
    except Exception:
       sys.exit("Not a valid cell location '" + cell_location + "'")


def print_table(data_table):
    for i in range(len(data_table)):
        for j in range(len(data_table[i])):
            print(data_table[i][j] + " ", end='')
        print("")


def to_str(cell_content):
    if cell_content is None:
        return ""
    else:
        return str(cell_content)


def empty(line):
    if all(cell == "" for cell in line):
        return True
    else:
        return False


def columns_to_indexes(columns, max_column):
    indexes = []

    for col in columns:
        indexes.append(letter_to_index(col, max_column))

    return sorted(indexes)


def letter_to_index(col, max_column=None):

    index = column_to_num(col)

    if max_column is not None:
        if index <= max_column:
            index = column_to_num(col)
            return index
        else:
            sys.exit("Column '" + col + "' not present in worksheet")
    else:
        return index


def column_to_num(column):
    num = 0

    if isinstance(column, int) and column > 0:
        return column
    elif column != "":
        for char in column:
            if char in string.ascii_letters:
                num = num * 26 + (ord(char.upper()) - ord('A')) + 1
            else:
                sys.exit("Column '" + column + "' is not a column")
    else:
        sys.exit("Empty column is not a column")

    return num