import sys
from openpyxl import load_workbook

from excel import tools
from excel import my_constants as cst


def parse_sheets(file_name, sheets_info, remove_empty_lines=True, plain_table=False):
    wb = load_workbook(filename=file_name, read_only=True)
    data_tables = {}

    for sheet_name, infos in sheets_info.items():
        ws = wb[sheet_name]

        # Prepare info of each worksheet
        columns = infos[cst.COLUMNS]
        first_row = infos[cst.FIRST_ROW]

        data_table = parse_sheet(ws, columns, first_row, remove_empty_lines)

        data_tables.update({sheet_name: data_table})

    if plain_table :
        if len(data_tables) == 1:
            return list(data_tables.values())[0]
        else:
            sys.exit("Plain table structure is only available when parsing one sheet")
    else:
        return data_tables


def parse_sheet(ws, columns, first_row=1, remove_empty_lines=True):
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

    return data


if __name__ == "__main__":
    file_name = sys.argv[1]
    sheet_name = sys.argv[2]

    sheets_info = {}

    sheets_info.update({sheet_name: [["A", "B", "C", "D", "E"], 1]})

    data_tables = parse_sheets(file_name, sheets_info)

    tools.print_table(data_tables[sheet_name])