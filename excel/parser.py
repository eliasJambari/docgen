import sys
import string
from openpyxl import load_workbook


def parse_excel_file(file_name, sheet_name, columns, first_row=0, remove_empty_lines=True):
    wb = load_workbook(filename=file_name, read_only=True)
    ws = wb[sheet_name]

    data = []

    col_indexes = convert_column_indexes(columns, ws)

    for row in ws.iter_rows(row_offset=first_row):
        row_data = []

        current_col = 1
        next = 0
        
        for cell in row:
            if current_col == col_indexes[next]:
                row_data.append(to_str(cell.value))
                next += 1
            current_col += 1

        # Add line if not empty and option selected
        if not(remove_empty_lines and empty(row_data)):
            data.append(row_data)

    return data


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


def convert_column_indexes(columns, ws):
    indexes = []

    for col in columns:
        index = column_to_num(col)
        if index <= ws.max_column:
            indexes.append(index)
        else:
            sys.exit("Column '" + col + "' not present in worksheet")

    return sorted(indexes)


def column_to_num(column):
    num = 0
    for char in column:
        if char in string.ascii_letters:
            num = num * 26 + (ord(char.upper()) - ord('A')) + 1
    return num


if __name__ == "__main__":
    file_name = sys.argv[1]
    sheet_name = sys.argv[2]

    columns = ["A", "B", "C", "E", "D"]

    data_table = parse_excel_file(file_name, sheet_name, columns)

    print_table(data_table)