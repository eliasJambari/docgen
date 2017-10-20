import sys
import string
# Add tools here


def check_location(cell_location):
    if ():
        pass
    else:
        sys.exit("Invalid cell location " + cell_location)


    try:
        ws["A3"]
        print("Valid cell location")
    except ValueError:
        sys.exit("Not a valid cell location")


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


def letter_to_index(col, max_column):
    index = column_to_num(col)
    if index <= max_column:
        index = column_to_num(col)
        return index
    else:
        sys.exit("Column '" + col + "' not present in worksheet")


def column_to_num(column):
    num = 0
    for char in column:
        if char in string.ascii_letters:
            num = num * 26 + (ord(char.upper()) - ord('A')) + 1
    return num