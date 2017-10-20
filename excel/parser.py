import sys
import string
from openpyxl import load_workbook

from excel import tools


def parse_excel_file(file_name, sheet_name, columns, first_row=1, remove_empty_lines=True):
    wb = load_workbook(filename=file_name, read_only=True)
    ws = wb[sheet_name]

    data = []

    col_indexes = tools.columns_to_indexes(columns, ws.max_column)

    for row in ws.iter_rows(row_offset=first_row-1):
        row_data = []

        current_col = 1
        next = 0

        for cell in row:
            if current_col == col_indexes[next]:
                row_data.append(tools.to_str(cell.value))
                next += 1
            current_col += 1

        # Add line if not empty and option selected
        if not(remove_empty_lines and tools.empty(row_data)):
            data.append(row_data)

    return data, ws.max_column


if __name__ == "__main__":
    file_name = sys.argv[1]
    sheet_name = sys.argv[2]

    columns = ["A", "B", "C", "D", "E"]

    data_table = parse_excel_file(file_name, sheet_name, columns)

    tools.print_table(data_table)