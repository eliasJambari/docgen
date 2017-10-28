import win32com.client
import os


def convert(file_name):
    o = win32com.client.Dispatch("Excel.Application") # Open excel
    o.Visible = False # Visibility to the user

    wb = o.Workbooks.Open(file_name) # Open Workbook

    file_name, file_extension = os.path.splitext(file_name) # Get file name
    path_to_pdf = file_name + ".pdf" # Rename file to pdf

    wb.WorkSheets([1]).Select() # Sheets to select
    wb.ActiveSheet.ExportAsFixedFormat(0, path_to_pdf) # Export as pdf
    wb.Close(True) # Close program to prevent from file from being left opened

    print("Generated pdf : " + file_name + ".pdf")


def convert_to(generated_files):
    for file in generated_files:
        convert(file)