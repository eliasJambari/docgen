import sys
import os
import operator
import win32com.client

from excel import parser
from excel import tools
from excel import my_constants as cst
from gui import progress


def build_mapping(data_table):
    mapping = {}

    for entry in data_table:
        if len(entry) == 2:
            column = tools.letter_to_index(entry[cst.COLUMN])
            location = tools.check_location(entry[cst.LOCATION])

            # Check if not entry with same column/location
            if any(location in cells for cells in mapping.values()):
                sys.exit("Cannot have multiple entries with '" + location + "'")
            elif column in mapping.keys():
                mapping.get(column).append(location)
            else:
                mapping.update({column: [location]})
        else:
            sys.exit("No possible mapping with more than 2 columns")

    return mapping


def generate_excel_files(data_table, mapping, template_file, output_directory):
    progress.tmp_solution(1, "Generating PDF files", debug="Started PDF files processing")
    template_file = tools.extract_one_sheet(template_file, output_directory, "template")

    columns = sorted(mapping.items(), key=operator.itemgetter(0))
    file_count = 0

    generated_files = []

    o = win32com.client.Dispatch("Excel.Application") # Open excel
    o.Visible = False # Visibility to the user

    wb = o.Workbooks.Open(template_file) # Open Workbook
    wb.WorkSheets("template").Select()  # Sheets to select

    for element in data_table:
        file_count += 1

        pdf_file = os.path.join(output_directory, str(file_count).rjust(3, '0') + ".pdf") # Create file name

        fill_excel_file(wb.ActiveSheet, element, columns) # Fill each file individually

        wb.ActiveSheet.ExportAsFixedFormat(0, pdf_file) # Export as pdf
        generated_files.append(pdf_file)
        progress.tmp_solution(1, "Generating PDF files", debug=("Filling and generating PDF file" + pdf_file))

    wb.Close(True)  # Close program to prevent file from being left opened
    return generated_files


# Fill file individually
def fill_excel_file(ws, content, columns):
    for i in range(len(content)):
        cell_content = content[i]
        location = columns[i]

        for cell in location[cst.LOCATION]:
            ws.Range(cell).Value = cell_content


if __name__ == "__main__":
    file_name = sys.argv[1]
    sheet_name = sys.argv[2]

    sheets_info = {}

    sheets_info.update({sheet_name: [["A", "B"], 2]})

    data_tables = parser.parse_sheets(file_name, sheets_info)

    mapping = build_mapping(data_tables[sheet_name])

    print(mapping)