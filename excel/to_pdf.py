import win32com.client
import os


def convert_to_pdf(file_name):

    o = win32com.client.Dispatch("Excel.Application")

    o.Visible = False

    wb_path = file_name

    wb = o.Workbooks.Open(wb_path)

    ws_index_list = [1]  # say you want to print these sheets

    file_name, file_extension = os.path.splitext(file_name)

    path_to_pdf = file_name + ".pdf"

    wb.WorkSheets(ws_index_list).Select()

    wb.ActiveSheet.ExportAsFixedFormat(0, path_to_pdf)

    wb.Close(True)

    print("Generated pdf : " + file_name + ".pdf")


def convert_to_pdfs(generated_files):
    for file in generated_files:
        convert_to_pdf(file)