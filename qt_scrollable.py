# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qttest_scrollable.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(711, 1063)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setLineWidth(-1)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 689, 988))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.Step5LabelVeh = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Step5LabelVeh.setObjectName("Step5LabelVeh")
        self.gridLayout.addWidget(self.Step5LabelVeh, 20, 0, 1, 1)
        self.pushButtonConfirm = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButtonConfirm.setObjectName("pushButtonConfirm")
        self.gridLayout.addWidget(self.pushButtonConfirm, 36, 0, 1, 1)
        self.Step2Mode2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.Step2Mode2.setObjectName("Step2Mode2")
        self.gridLayout.addWidget(self.Step2Mode2, 6, 0, 1, 1)
        self.t2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t2.sizePolicy().hasHeightForWidth())
        self.t2.setSizePolicy(sizePolicy)
        self.t2.setObjectName("t2")
        self.gridLayout.addWidget(self.t2, 12, 1, 1, 1)
        self.labeltimeformat = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labeltimeformat.setObjectName("labeltimeformat")
        self.gridLayout.addWidget(self.labeltimeformat, 10, 1, 1, 1)
        self.checkwlr = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkwlr.setObjectName("checkwlr")
        self.gridLayout.addWidget(self.checkwlr, 25, 3, 1, 1)
        self.Step5Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Step5Label.setObjectName("Step5Label")
        self.gridLayout.addWidget(self.Step5Label, 15, 0, 1, 1)
        self.Step2Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Step2Label.setObjectName("Step2Label")
        self.gridLayout.addWidget(self.Step2Label, 4, 0, 1, 1)
        self.radioButtoncsv = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButtoncsv.setObjectName("radioButtoncsv")
        self.gridLayout.addWidget(self.radioButtoncsv, 32, 0, 1, 1)
        self.aggregation3 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.aggregation3.setObjectName("aggregation3")
        self.gridLayout.addWidget(self.aggregation3, 16, 1, 1, 1)
        self.labeld1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labeld1.setObjectName("labeld1")
        self.gridLayout.addWidget(self.labeld1, 8, 0, 1, 1)
        self.aggregation2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.aggregation2.setObjectName("aggregation2")
        self.gridLayout.addWidget(self.aggregation2, 17, 0, 1, 1)
        self.threshold = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.threshold.setObjectName("threshold")
        self.gridLayout.addWidget(self.threshold, 14, 0, 1, 1)
        self.Step1Intersection1 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.Step1Intersection1.setObjectName("Step1Intersection1")
        self.gridLayout.addWidget(self.Step1Intersection1, 2, 0, 1, 1)
        self.lineEditCSVname = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditCSVname.setObjectName("lineEditCSVname")
        self.gridLayout.addWidget(self.lineEditCSVname, 34, 0, 1, 1)
        self.toolButtonLayout1 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButtonLayout1.setObjectName("toolButtonLayout1")
        self.gridLayout.addWidget(self.toolButtonLayout1, 2, 1, 1, 1)
        self.lineEditPath = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditPath.setObjectName("lineEditPath")
        self.gridLayout.addWidget(self.lineEditPath, 35, 0, 1, 2)
        self.toolButtonLayout2 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButtonLayout2.setObjectName("toolButtonLayout2")
        self.gridLayout.addWidget(self.toolButtonLayout2, 3, 1, 1, 1)
        self.toolButtonExport = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButtonExport.setObjectName("toolButtonExport")
        self.gridLayout.addWidget(self.toolButtonExport, 35, 2, 1, 1)
        self.labelcsv = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelcsv.setObjectName("labelcsv")
        self.gridLayout.addWidget(self.labelcsv, 34, 1, 1, 1)
        self.checksrl = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checksrl.setObjectName("checksrl")
        self.gridLayout.addWidget(self.checksrl, 24, 3, 1, 1)
        self.checknlr = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checknlr.setObjectName("checknlr")
        self.gridLayout.addWidget(self.checknlr, 21, 3, 1, 1)
        self.radioButtondisplay = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButtondisplay.setObjectName("radioButtondisplay")
        self.gridLayout.addWidget(self.radioButtondisplay, 31, 0, 1, 1)
        self.Step4Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Step4Label.setObjectName("Step4Label")
        self.gridLayout.addWidget(self.Step4Label, 13, 0, 1, 2)
        self.checkelr = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkelr.setObjectName("checkelr")
        self.gridLayout.addWidget(self.checkelr, 27, 3, 1, 1)
        self.labelt2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelt2.setObjectName("labelt2")
        self.gridLayout.addWidget(self.labelt2, 11, 1, 1, 1)
        self.Step2Mode1 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.Step2Mode1.setObjectName("Step2Mode1")
        self.gridLayout.addWidget(self.Step2Mode1, 5, 0, 1, 1)
        self.labelTitle = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")
        self.gridLayout.addWidget(self.labelTitle, 0, 0, 1, 1)
        self.checkwn = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkwn.setObjectName("checkwn")
        self.gridLayout.addWidget(self.checkwn, 21, 1, 1, 1)
        self.t1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t1.sizePolicy().hasHeightForWidth())
        self.t1.setSizePolicy(sizePolicy)
        self.t1.setObjectName("t1")
        self.gridLayout.addWidget(self.t1, 9, 1, 1, 1)
        self.Step5LabelPed = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Step5LabelPed.setObjectName("Step5LabelPed")
        self.gridLayout.addWidget(self.Step5LabelPed, 20, 3, 1, 1)
        self.checknrl = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checknrl.setObjectName("checknrl")
        self.gridLayout.addWidget(self.checknrl, 22, 3, 1, 1)
        self.Step1Intersection2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.Step1Intersection2.setObjectName("Step1Intersection2")
        self.gridLayout.addWidget(self.Step1Intersection2, 3, 0, 1, 1)
        self.Step1Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Step1Label.setObjectName("Step1Label")
        self.gridLayout.addWidget(self.Step1Label, 1, 0, 1, 1)
        self.labelt1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelt1.setObjectName("labelt1")
        self.gridLayout.addWidget(self.labelt1, 8, 1, 1, 1)
        self.Step6Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Step6Label.setObjectName("Step6Label")
        self.gridLayout.addWidget(self.Step6Label, 19, 0, 1, 1)
        self.label_threshold = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_threshold.setObjectName("label_threshold")
        self.gridLayout.addWidget(self.label_threshold, 14, 1, 1, 1)
        self.aggregation4 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.aggregation4.setObjectName("aggregation4")
        self.gridLayout.addWidget(self.aggregation4, 17, 1, 1, 1)
        self.d2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.d2.sizePolicy().hasHeightForWidth())
        self.d2.setSizePolicy(sizePolicy)
        self.d2.setObjectName("d2")
        self.gridLayout.addWidget(self.d2, 12, 0, 1, 1)
        self.aggregation1 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.aggregation1.setObjectName("aggregation1")
        self.gridLayout.addWidget(self.aggregation1, 16, 0, 1, 1)
        self.labeldateformat = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labeldateformat.setObjectName("labeldateformat")
        self.gridLayout.addWidget(self.labeldateformat, 10, 0, 1, 1)
        self.Step7Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Step7Label.setObjectName("Step7Label")
        self.gridLayout.addWidget(self.Step7Label, 30, 0, 1, 1)
        self.Step8Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Step8Label.setObjectName("Step8Label")
        self.gridLayout.addWidget(self.Step8Label, 33, 0, 1, 1)
        self.d1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.d1.sizePolicy().hasHeightForWidth())
        self.d1.setSizePolicy(sizePolicy)
        self.d1.setObjectName("d1")
        self.gridLayout.addWidget(self.d1, 9, 0, 1, 1)
        self.Step3Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Step3Label.setObjectName("Step3Label")
        self.gridLayout.addWidget(self.Step3Label, 7, 0, 1, 1)
        self.checknw = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checknw.setObjectName("checknw")
        self.gridLayout.addWidget(self.checknw, 21, 0, 1, 1)
        self.checkslr = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkslr.setObjectName("checkslr")
        self.gridLayout.addWidget(self.checkslr, 23, 3, 1, 1)
        self.labeld2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labeld2.setObjectName("labeld2")
        self.gridLayout.addWidget(self.labeld2, 11, 0, 1, 1)
        self.checkwrl = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkwrl.setObjectName("checkwrl")
        self.gridLayout.addWidget(self.checkwrl, 26, 3, 1, 1)
        self.checkerl = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkerl.setObjectName("checkerl")
        self.gridLayout.addWidget(self.checkerl, 28, 3, 1, 1)
        self.checkne = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkne.setObjectName("checkne")
        self.gridLayout.addWidget(self.checkne, 22, 0, 1, 1)
        self.checkns = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkns.setObjectName("checkns")
        self.gridLayout.addWidget(self.checkns, 23, 0, 1, 1)
        self.checksw = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checksw.setObjectName("checksw")
        self.gridLayout.addWidget(self.checksw, 24, 0, 1, 1)
        self.checkse = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkse.setObjectName("checkse")
        self.gridLayout.addWidget(self.checkse, 25, 0, 1, 1)
        self.checksn = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checksn.setObjectName("checksn")
        self.gridLayout.addWidget(self.checksn, 26, 0, 1, 1)
        self.checkwe = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkwe.setObjectName("checkwe")
        self.gridLayout.addWidget(self.checkwe, 22, 1, 1, 1)
        self.checkws = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkws.setObjectName("checkws")
        self.gridLayout.addWidget(self.checkws, 23, 1, 1, 1)
        self.checken = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checken.setObjectName("checken")
        self.gridLayout.addWidget(self.checken, 24, 1, 1, 1)
        self.checkew = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkew.setObjectName("checkew")
        self.gridLayout.addWidget(self.checkew, 25, 1, 1, 1)
        self.checkes = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkes.setObjectName("checkes")
        self.gridLayout.addWidget(self.checkes, 26, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 711, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aggregated Data Request"))
        self.Step5LabelVeh.setText(_translate("MainWindow", "Vehicle Directions:"))
        self.pushButtonConfirm.setText(_translate("MainWindow", "Confirm Query"))
        self.Step2Mode2.setText(_translate("MainWindow", "Custom (Mode 2)"))
        self.labeltimeformat.setText(_translate("MainWindow", "(HH:MM:SS, e.g. T23:30:00)"))
        self.checkwlr.setText(_translate("MainWindow", "West - L to R"))
        self.Step5Label.setText(_translate("MainWindow", "5. Select Aggregation Interval (For Mode 2 Only)"))
        self.Step2Label.setText(_translate("MainWindow", "2. Select Data Mode"))
        self.radioButtoncsv.setText(_translate("MainWindow", "Store data as  .csv File"))
        self.aggregation3.setText(_translate("MainWindow", "Daily"))
        self.labeld1.setText(_translate("MainWindow", "Start Date:"))
        self.aggregation2.setText(_translate("MainWindow", "Hourly"))
        self.Step1Intersection1.setText(_translate("MainWindow", "Bernard Ave and Pandosy St. (#1)"))
        self.toolButtonLayout1.setText(_translate("MainWindow", "See layout"))
        self.toolButtonLayout2.setText(_translate("MainWindow", "See layout"))
        self.toolButtonExport.setText(_translate("MainWindow", "..."))
        self.labelcsv.setText(_translate("MainWindow", ".csv"))
        self.checksrl.setText(_translate("MainWindow", "South - R to L"))
        self.checknlr.setText(_translate("MainWindow", "North - L to R"))
        self.radioButtondisplay.setText(_translate("MainWindow", "Only display data on screen"))
        self.Step4Label.setText(_translate("MainWindow", "4. Input threshold if you want to obtain # of hours above threshold for each day:"))
        self.checkelr.setText(_translate("MainWindow", "East - L to R"))
        self.labelt2.setText(_translate("MainWindow", "Time (Mode 2 Only):"))
        self.Step2Mode1.setText(_translate("MainWindow", "Summarized (Mode 1)"))
        self.labelTitle.setText(_translate("MainWindow", "Aggregated Data Report"))
        self.checkwn.setText(_translate("MainWindow", "West to North"))
        self.Step5LabelPed.setText(_translate("MainWindow", "Pedestrian Crosswalks:"))
        self.checknrl.setText(_translate("MainWindow", "North - R to L"))
        self.Step1Intersection2.setText(_translate("MainWindow", "Bernard Ave and Water St. (#2)"))
        self.Step1Label.setText(_translate("MainWindow", "1. Select Location"))
        self.labelt1.setText(_translate("MainWindow", "Time (Mode 2 Only):"))
        self.Step6Label.setText(_translate("MainWindow", "6. Select Output Items (For Mode 2 Only)"))
        self.label_threshold.setText(_translate("MainWindow", "veh/hr           (Default: 300)"))
        self.aggregation4.setText(_translate("MainWindow", "Monthly"))
        self.aggregation1.setText(_translate("MainWindow", "15 minutes"))
        self.labeldateformat.setText(_translate("MainWindow", "(YYYY-MM-DD)"))
        self.Step7Label.setText(_translate("MainWindow", "7. Select Output Format"))
        self.Step8Label.setText(_translate("MainWindow", "8. File Name and Location"))
        self.Step3Label.setText(_translate("MainWindow", "3. Enter Range"))
        self.checknw.setText(_translate("MainWindow", "North to West"))
        self.checkslr.setText(_translate("MainWindow", "South - L to R"))
        self.labeld2.setText(_translate("MainWindow", "End Date:"))
        self.checkwrl.setText(_translate("MainWindow", "West - R to L"))
        self.checkerl.setText(_translate("MainWindow", "East - R to L"))
        self.checkne.setText(_translate("MainWindow", "North to East"))
        self.checkns.setText(_translate("MainWindow", "North to South"))
        self.checksw.setText(_translate("MainWindow", "South to West"))
        self.checkse.setText(_translate("MainWindow", "South to East"))
        self.checksn.setText(_translate("MainWindow", "South to North"))
        self.checkwe.setText(_translate("MainWindow", "West to East"))
        self.checkws.setText(_translate("MainWindow", "West to South"))
        self.checken.setText(_translate("MainWindow", "East to North"))
        self.checkew.setText(_translate("MainWindow", "East to West"))
        self.checkes.setText(_translate("MainWindow", "East to South"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

