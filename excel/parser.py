from openpyxl import load_workbook


def parse_excel_file(file_name, sheet, columns, first_row=0, last_row=None):
    wb = load_workbook(filename=file_name, read_only=True)
    ws = wb[sheet]

    for row in ws.rows:
        for cell in row:
            print(cell.value)