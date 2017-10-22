import sys
import os
import string
import shutil

from openpyxl.utils import coordinate_from_string
from openpyxl import load_workbook


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


def extract_one_sheet(input_file, output_directory, sheet_to_keep):
    wb = load_workbook(filename=input_file)

    to_remove = []

    to_remove = wb.get_sheet_names()

    to_remove.remove(sheet_to_keep)

    print(to_remove)

    for sheet_name in to_remove:
        sheet_to_delete = wb.get_sheet_by_name(sheet_name)
        wb.remove_sheet(sheet_to_delete)

    output_file = os.path.join(output_directory, sheet_to_keep + ".xlsx")

    wb.save(output_file)

    return output_file


def dupplicate_file(original_file, output_directory, new_file_name):
    new_file_name = os.path.join(output_directory, new_file_name)
    shutil.copy2(original_file, new_file_name)

    return new_file_name