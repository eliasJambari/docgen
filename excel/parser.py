import sys
from openpyxl import load_workbook


def parse_excel_file(file_name, sheet_name, columns, first_row=0, last_row=None, remove_empty_lines=True):
    wb = load_workbook(filename=file_name, read_only=True)
    ws = wb[sheet_name]

    data = []

    for row in ws.iter_rows(row_offset=first_row):
        row_data = []
        for cell in row:
            row_data.append(to_str(cell.value))

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


if __name__ == "__main__":
    file_name = sys.argv[1]
    sheet_name = sys.argv[2]

    columns = []

    data_table = parse_excel_file(file_name, sheet_name, columns)

    print_table(data_table)