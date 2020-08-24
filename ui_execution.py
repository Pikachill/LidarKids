from PyQt5 import QtCore, QtGui, QtWidgets
from qt_scrollable import *
from query import mode1_query, mode2_query

# open GUI window and assign values to variables based on user input
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()

    (udid, mode, d1, t1, d2, t2, threshold, a, f, print_only) = pull_val_from_GUI(ui)
    print(udid, mode, d1, t1, d2, t2, threshold, a, f, print_only)  # tests if the values has been returned

    # executes query functions based on the selected mode
    if mode == 1:
        mode1_query(udid, d1, d2, threshold, print_only)
    elif mode == 2:
        mode2_query(udid, mode, d1, t1, d2, t2, a, f, print_only)
