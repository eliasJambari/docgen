import sys
import os
import string
import shutil
import logging
logger = logging.getLogger()

from openpyxl.utils import coordinate_from_string


# Validates if cell location is valid
def check_location(cell_location):
    logger.debug("Checking location for " + str(cell_location))

    try:
        coordinate_from_string(cell_location)
        return cell_location
    except Exception:
        logger.error("Not a valid cell location '" + str(cell_location) + "'")
        sys.exit()


# Prints 2D table
def print_table(data_table):
    for i in range(len(data_table)):
        for j in range(len(data_table[i])):
            print(data_table[i][j] + " ", end='')
        print("")


# Converts cell value to string
def to_str(cell_content):
    if cell_content is None:
        return ""
    else:
        return str(cell_content)


# Verifies if a line (array) is empty
def empty(line):
    if all(cell == "" for cell in line):
        return True
    else:
        return False


# Converts columns (alpha) to indexes (integers)
def columns_to_indexes(columns, max_column):
    logger.debug("Converting columns " + str(columns) + " to indexes")
    indexes = []

    # Iterate over each column
    for col in columns:
        indexes.append(letter_to_index(col, max_column))

    logger.debug("Columns converted to " + str(indexes))
    return sorted(indexes)


# Converts a letter to its corresponding index (and checks if below max)
def letter_to_index(col, max_column=None):
    index = column_to_num(col)

    if max_column is not None:
        if index <= max_column:
            index = column_to_num(col)
            return index
        else:
            logger.error("Column '" + str(col) + "' not present in worksheet")
            sys.exit()
    else:
        return index


# Converts a letter to its corresponding index (low level implementation)
def column_to_num(column):
    num = 0

    if isinstance(column, int) and column > 0:
        return column
    elif column != "":
        for char in column:
            if char in string.ascii_letters:
                num = num * 26 + (ord(char.upper()) - ord('A')) + 1
            else:
                logger.error("Column '" + str(column) + "' is not a column")
                sys.exit()
    else:
        logger.error("An empty column is not a valid column")
        sys.exit()

    return num


# REMOVE and RENAME this function
def extract_one_sheet(input_file, output_directory, sheet_to_keep):
    # wb = load_workbook(filename=input_file)
    #
    # to_remove = []
    #
    # to_remove = wb.get_sheet_names()
    #
    # to_remove.remove(sheet_to_keep)
    #
    # for sheet_name in to_remove:
    #     sheet_to_delete = wb.get_sheet_by_name(sheet_name)
    #     wb.remove_sheet(sheet_to_delete)

    output_file = os.path.join(output_directory, sheet_to_keep + ".xlsx")

    # wb.save(output_file)

    return dupplicate_file(input_file, output_directory, sheet_to_keep + ".xlsx")


# Copies a file to an output directory with new file name
def dupplicate_file(original_file, output_directory, new_file_name):
    new_file_name = os.path.join(output_directory, new_file_name)
    shutil.copy2(original_file, new_file_name)

    logger.info("Copied file '" + str(original_file) + "' to '" + str(new_file_name) + "'")
    return new_file_name


# Checks if a value is an integer and below the maximum value
def is_valid(value, max):
    if not isinstance(value, int):
        logger.error("Value '" + str(value) + "' is not a numeric value")
        sys.exit()

    if 0 <= value < max:
        return
    else:
        logger.error("Value '" + str(value) + "' is out of range (max : " + str(max) + " excluded)")
        sys.exit()

