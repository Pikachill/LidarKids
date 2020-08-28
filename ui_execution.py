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

    (udid, mode, d1, t1, d2, t2, threshold, a, f, file_path_name) = pull_val_from_GUI(ui)
    print(udid, mode, d1, t1, d2, t2, threshold, a, f, file_path_name)  # tests if the values has been returned

    #check if the user has input all necessary parameters
    if udid == 'None':
        print ("Please select an intersection.")
    if mode == 'None':
        print ("Please select a data mode.")
    if d1 == 'None':
        print ("Please enter a start date.")
    if d2 == 'None':
        print ("Please enter an end date.")
    if mode == 2 and t1 == 'None':
        print ("Please enter a start time.")
    if mode == 2 and t2 == 'None':
        print ("Please enter an end time.")
    if mode == 2 and a == 'None':
        print ("Please select an aggregation type.")
    if mode == 2 and f == '':
        print ("Please select directions.")

    # executes query functions based on the selected mode
    if udid!= 'None' and mode != 'None' and d1 != 'None' and d2 != 'None':
        if mode == 1:
            mode1_query(udid, d1, d2, threshold, file_path_name)
        elif mode == 2 and t1!= 'None' and t2 != 'None' and a!= 'None' and f != '':
            mode2_query(udid, mode, d1, t1, d2, t2, a, f, file_path_name)
