import sys
from excel.data_table import CellFactory

if __name__ == "__main__":
    file_name = sys.argv[1]

    input = "al k"

    cell = CellFactory.create_cell(input, file_name)

    print(cell.get_content(1))