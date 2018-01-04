from PyQt5 import QtGui


def open_file(events):
    print("Open file")
    name = QtGui.QFileDialog.getOpenFileName(self, "Open File")


def choose_dir():
    print("Choose directory")