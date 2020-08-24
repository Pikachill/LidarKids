# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qttest_scrollable.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow():
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(711, 1063)

        self.mainwindow = MainWindow

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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 669, 972))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.Step6Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Step6Label.setObjectName("Step6Label")
        self.gridLayout.addWidget(self.Step6Label, 19, 0, 1, 1)
        self.Step6checkws = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Step6checkws.setObjectName("Step6checkws")
        self.gridLayout.addWidget(self.Step6checkws, 23, 1, 1, 1)
        self.Step6checkwn = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Step6checkwn.setObjectName("Step6checkwn")
        self.gridLayout.addWidget(self.Step6checkwn, 21, 1, 1, 1)
        self.Step3d1Enter = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.Step3d1Enter.sizePolicy().hasHeightForWidth())
        self.Step3d1Enter.setSizePolicy(sizePolicy)
        self.Step3d1Enter.setObjectName("Step3d1Enter")
        self.gridLayout.addWidget(self.Step3d1Enter, 9, 0, 1, 1)
        self.Step6checksw = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Step6checksw.setObjectName("Step6checksw")
        self.gridLayout.addWidget(self.Step6checksw, 24, 0, 1, 1)
        self.Step6checkpednlr = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Step6checkpednlr.setObjectName("Step6checkpednlr")
        self.gridLayout.addWidget(self.Step6checkpednlr, 21, 2, 1, 1)
        self.Step6checkpednrl = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Step6checkpednrl.setObjectName("Step6checkpednrl")
        self.gridLayout.addWidget(self.Step6checkpednrl, 22, 2, 1, 1)
        self.Step5radioButton1 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.Step5radioButton1.setObjectName("Step5radioButton1")
        self.Step5buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.Step5buttonGroup.setObjectName("Step5buttonGroup")
        self.Step5buttonGroup.addButton(self.Step5radioButton1)
        self.gridLayout.addWidget(self.Step5radioButton1, 16, 0, 1, 1)
        self.Step3t1Enter = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Step3t1Enter.sizePolicy().hasHeightForWidth())
        self.Step3t1Enter.setSizePolicy(sizePolicy)
        self.Step3t1Enter.setObjectName("Step3t1Enter")
        self.gridLayout.addWidget(self.Step3t1Enter, 9, 1, 1, 1)
        self.Step6checkes = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Step6checkes.setObjectName("Step6checkes")
        self.gridLayout.addWidget(self.Step6checkes, 26, 1, 1, 1)
        self.Step2radioButtonMode2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.Step2radioButtonMode2.setObjectName("Step2radioButtonMode2")
        self.Step2buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.Step2buttonGroup.setObjectName("Step2buttonGroup")
        self.Step2buttonGroup.addButton(self.Step2radioButtonMode2)
        self.gridLayout.addWidget(self.Step2radioButtonMode2, 6, 0, 1, 1)
        self.Step6checkns = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Step6checkns.setObjectName("Step6checkns")
        self.gridLayout.addWidget(self.Step6checkns, 23, 0, 1, 1)
        self.Step1radioButton1 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.Step1radioButton1.setCheckable(True)
        self.Step1radioButton1.setChecked(True)
        self.Step1radioButton1.setObjectName("Step1radioButton1")
        self.Step1buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.Step1buttonGroup.setObjectName("Step1buttonGroup")
        self.Step1buttonGroup.addButton(self.Step1radioButton1)
        self.gridLayout.addWidget(self.Step1radioButton1, 2, 0, 1, 1)
        self.Step6checkpedwrl = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Step6checkpedwrl.setObjectName("Step6checkpedwrl")
        self.gridLayout.addWidget(self.Step6checkpedwrl, 26, 2, 1, 1)
        self.Step6checkew = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Step6checkew.setObjectName("Step6checkew")
        self.gridLayout.addWidget(self.Step6checkew, 25, 1, 1, 1)
        self.Step5radioButton2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.Step5radioButton2.setObjectName("Step5radioButton2")
        self.Step5buttonGroup.addButton(self.Step5radioButton2)
        self.gridLayout.addWidget(self.Step5radioButton2, 17, 0, 1, 1)
        self.Step6checkse = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Step6checkse.setObjectName("Step6checkse")
        self.gridLayout.addWidget(self.Step6checkse, 25, 0, 1, 1)
        self.Step2Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Step2Label.setObjectName("Step2Label")
        self.gridLayout.addWidget(self.Step2Label, 4, 0, 1, 1)
        self.Step5pedLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Step5pedLabel.setObjectName("Step5pedLabel")
        self.gridLayout.addWidget(self.Step5pedLabel, 20, 2, 1, 1)
        self.Step3tformatLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Step3tformatLabel.setObjectName("Step3tformatLabel")
        self.gridLayout.addWidget(self.Step3tformatLabel, 10, 1, 1, 1)
        self.Step7Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Step7Label.setObjectName("Step7Label")
        self.gridLayout.addWidget(self.Step7Label, 30, 0, 1, 1)
        self.Step6checkpedwlr = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Step6checkpedwlr.setObjectName("Step6checkpedwlr")
        self.gridLayout.addWidget(self.Step6checkpedwlr, 25, 2, 1, 1)
        self.Step3d2Enter = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.Step3d2Enter.sizePolicy().hasHeightForWidth())
        self.Step3d2Enter.setSizePolicy(sizePolicy)
        self.Step3d2Enter.setObjectName("Step3d2Enter")
        self.gridLayout.addWidget(self.Step3d2Enter, 12, 0, 1, 1)
        self.Step3t2Enter = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Step3t2Enter.sizePolicy().hasHeightForWidth())
        self.Step3t2Enter.setSizePolicy(sizePolicy)
        self.Step3t2Enter.setObjectName("Step3t2Enter")
        self.gridLayout.addWidget(self.Step3t2Enter, 12, 1, 1, 1)
        self.Step1radioButton2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.Step1radioButton2.setObjectName("Step1radioButton2")
        self.Step1buttonGroup.addButton(self.Step1radioButton2)
        self.gridLayout.addWidget(self.Step1radioButton2, 3, 0, 1, 1)
        self.Step0titleLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Step0titleLabel.setFont(font)
        self.Step0titleLabel.setObjectName("Step0titleLabel")
        self.gridLayout.addWidget(self.Step0titleLabel, 0, 0, 1, 1)
        self.Step5radioButton4 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.Step5radioButton4.setObjectName("Step5radioButton4")
        self.Step5buttonGroup.addButton(self.Step5radioButton4)
        self.gridLayout.addWidget(self.Step5radioButton4, 17, 1, 1, 1)
        self.Step3dformatLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Step3dformatLabel.setObjectName("Step3dformatLabel")
        self.gridLayout.addWidget(self.Step3dformatLabel, 10, 0, 1, 1)
        self.Step3d2Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Step3d2Label.setObjectName("Step3d2Label")
        self.gridLayout.addWidget(self.Step3d2Label, 11, 0, 1, 1)
        self.Step1toolButtonLayout1 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.Step1toolButtonLayout1.setObjectName("Step1toolButtonLayout1")
        self.gridLayout.addWidget(self.Step1toolButtonLayout1, 2, 1, 1, 1)
        self.Step3t2Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Step3t2Label.setObjectName("Step3t2Label")
        self.gridLayout.addWidget(self.Step3t2Label, 11, 1, 1, 1)
        self.Step4thresholdLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Step4thresholdLabel.setObjectName("Step4thresholdLabel")
        self.gridLayout.addWidget(self.Step4thresholdLabel, 14, 1, 1, 1)
        self.Step3t1Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Step3t1Label.setObjectName("Step3t1Label")
        self.gridLayout.addWidget(self.Step3t1Label, 8, 1, 1, 1)
        self.Step6checkne = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Step6checkne.setObjectName("Step6checkne")
        self.gridLayout.addWidget(self.Step6checkne, 22, 0, 1, 1)
        self.Step6checken = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Step6checken.setObjectName("Step6checken")
        self.gridLayout.addWidget(self.Step6checken, 24, 1, 1, 1)
        self.Step6checksn = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Step6checksn.setObjectName("Step6checksn")
        self.gridLayout.addWidget(self.Step6checksn, 26, 0, 1, 1)
        self.Step3Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Step3Label.setObjectName("Step3Label")
        self.gridLayout.addWidget(self.Step3Label, 7, 0, 1, 1)
        self.Step4thresholdEnter = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.Step4thresholdEnter.setObjectName("Step4thresholdEnter")
        self.gridLayout.addWidget(self.Step4thresholdEnter, 14, 0, 1, 1)
        self.Step4Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Step4Label.setObjectName("Step4Label")
        self.gridLayout.addWidget(self.Step4Label, 13, 0, 1, 2)
        self.Step1toolButtonLayout2 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.Step1toolButtonLayout2.setObjectName("Step1toolButtonLayout2")
        self.gridLayout.addWidget(self.Step1toolButtonLayout2, 3, 1, 1, 1)
        self.Step6checkpederl = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Step6checkpederl.setObjectName("Step6checkpederl")
        self.gridLayout.addWidget(self.Step6checkpederl, 28, 2, 1, 1)
        self.Step6checkwe = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Step6checkwe.setObjectName("Step6checkwe")
        self.gridLayout.addWidget(self.Step6checkwe, 22, 1, 1, 1)
        self.Step5Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Step5Label.setObjectName("Step5Label")
        self.gridLayout.addWidget(self.Step5Label, 15, 0, 1, 1)
        self.Step7radioButtoncsv = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.Step7radioButtoncsv.setObjectName("Step7radioButtoncsv")
        self.Step7buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.Step7buttonGroup.setObjectName("Step7buttonGroup")
        self.Step7buttonGroup.addButton(self.Step7radioButtoncsv)
        self.gridLayout.addWidget(self.Step7radioButtoncsv, 32, 0, 1, 1)
        self.Step1Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Step1Label.setObjectName("Step1Label")
        self.gridLayout.addWidget(self.Step1Label, 1, 0, 1, 1)
        self.Step6checkpedsrl = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Step6checkpedsrl.setObjectName("Step6checkpedsrl")
        self.gridLayout.addWidget(self.Step6checkpedsrl, 24, 2, 1, 1)
        self.Step6checknw = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Step6checknw.setObjectName("Step6checknw")
        self.gridLayout.addWidget(self.Step6checknw, 21, 0, 1, 1)
        self.Step5vehLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Step5vehLabel.setObjectName("Step5vehLabel")
        self.gridLayout.addWidget(self.Step5vehLabel, 20, 0, 1, 1)
        self.Step5radioButton3 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.Step5radioButton3.setObjectName("Step5radioButton3")
        self.Step5buttonGroup.addButton(self.Step5radioButton3)
        self.gridLayout.addWidget(self.Step5radioButton3, 16, 1, 1, 1)
        self.Step7radioButtondisplay = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.Step7radioButtondisplay.setObjectName("Step7radioButtondisplay")
        self.Step7buttonGroup.addButton(self.Step7radioButtondisplay)
        self.gridLayout.addWidget(self.Step7radioButtondisplay, 31, 0, 1, 1)
        self.Step6checkpedslr = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Step6checkpedslr.setObjectName("Step6checkpedslr")
        self.gridLayout.addWidget(self.Step6checkpedslr, 23, 2, 1, 1)
        self.Step6checkpedelr = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Step6checkpedelr.setObjectName("Step6checkpedelr")
        self.gridLayout.addWidget(self.Step6checkpedelr, 27, 2, 1, 1)
        self.Step3d1Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Step3d1Label.setObjectName("Step3d1Label")
        self.gridLayout.addWidget(self.Step3d1Label, 8, 0, 1, 1)
        self.Step8pushButtonConfirmQuery = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Step8pushButtonConfirmQuery.setObjectName("Step8pushButtonConfirmQuery")
        self.gridLayout.addWidget(self.Step8pushButtonConfirmQuery, 33, 0, 1, 1)
        self.Step2radioButtonMode1 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.Step2radioButtonMode1.setObjectName("Step2radioButtonMode1")
        self.Step2buttonGroup.addButton(self.Step2radioButtonMode1)
        self.gridLayout.addWidget(self.Step2radioButtonMode1, 5, 0, 1, 1)
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

        # self.Step1toolButtonLayout1.clicked.connect(self.step1_1clicked)
        # self.Step1toolButtonLayout2.clicked.connect(self.step1_2clicked)
        self.Step8pushButtonConfirmQuery.clicked.connect(self.step8clicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aggregated Data Request"))
        self.Step6Label.setText(_translate("MainWindow", "6. Select Output Items (For Mode 2 Only)"))
        self.Step6checkws.setText(_translate("MainWindow", "West to South"))
        self.Step6checkwn.setText(_translate("MainWindow", "West to North"))
        self.Step6checksw.setText(_translate("MainWindow", "South to West"))
        self.Step6checkpednlr.setText(_translate("MainWindow", "North - L to R"))
        self.Step6checkpednrl.setText(_translate("MainWindow", "North - R to L"))
        self.Step5radioButton1.setText(_translate("MainWindow", "15 minutes"))
        self.Step6checkes.setText(_translate("MainWindow", "East to South"))
        self.Step2radioButtonMode2.setText(_translate("MainWindow", "Custom (Mode 2)"))
        self.Step6checkns.setText(_translate("MainWindow", "North to South"))
        self.Step1radioButton1.setText(_translate("MainWindow", "Bernard Ave and Pandosy St. (#1)"))
        self.Step6checkpedwrl.setText(_translate("MainWindow", "West - R to L"))
        self.Step6checkew.setText(_translate("MainWindow", "East to West"))
        self.Step5radioButton2.setText(_translate("MainWindow", "Hourly"))
        self.Step6checkse.setText(_translate("MainWindow", "South to East"))
        self.Step2Label.setText(_translate("MainWindow", "2. Select Data Mode"))
        self.Step5pedLabel.setText(_translate("MainWindow", "Pedestrian Crosswalks:"))
        self.Step3tformatLabel.setText(_translate("MainWindow", "(HH:MM:SS, e.g. T23:30:00)"))
        self.Step7Label.setText(_translate("MainWindow", "7. Select Output Format"))
        self.Step6checkpedwlr.setText(_translate("MainWindow", "West - L to R"))
        self.Step1radioButton2.setText(_translate("MainWindow", "Bernard Ave and Water St. (#2)"))
        self.Step0titleLabel.setText(_translate("MainWindow", "Aggregated Data Report"))
        self.Step5radioButton4.setText(_translate("MainWindow", "Monthly"))
        self.Step3dformatLabel.setText(_translate("MainWindow", "(YYYY-MM-DD)"))
        self.Step3d2Label.setText(_translate("MainWindow", "End Date: (inclusive)"))
        self.Step1toolButtonLayout1.setText(_translate("MainWindow", "See layout"))
        self.Step3t2Label.setText(_translate("MainWindow", "Time (Mode 2 Only):"))
        self.Step4thresholdLabel.setText(_translate("MainWindow", "veh/hr           (Default: 300)"))
        self.Step3t1Label.setText(_translate("MainWindow", "Time (Mode 2 Only):"))
        self.Step6checkne.setText(_translate("MainWindow", "North to East"))
        self.Step6checken.setText(_translate("MainWindow", "East to North"))
        self.Step6checksn.setText(_translate("MainWindow", "South to North"))
        self.Step3Label.setText(_translate("MainWindow", "3. Enter Range"))
        self.Step4Label.setText(_translate("MainWindow",
                                           "4. Input threshold if you want to obtain # of hours above threshold for each day:"))
        self.Step1toolButtonLayout2.setText(_translate("MainWindow", "See layout"))
        self.Step6checkpederl.setText(_translate("MainWindow", "East - R to L"))
        self.Step6checkwe.setText(_translate("MainWindow", "West to East"))
        self.Step5Label.setText(_translate("MainWindow", "5. Select Aggregation Interval (For Mode 2 Only)"))
        self.Step7radioButtoncsv.setText(_translate("MainWindow", "Store data as  .csv File"))
        self.Step1Label.setText(_translate("MainWindow", "1. Select Location"))
        self.Step6checkpedsrl.setText(_translate("MainWindow", "South - R to L"))
        self.Step6checknw.setText(_translate("MainWindow", "North to West"))
        self.Step5vehLabel.setText(_translate("MainWindow", "Vehicle Directions:"))
        self.Step5radioButton3.setText(_translate("MainWindow", "Daily"))
        self.Step7radioButtondisplay.setText(_translate("MainWindow", "Only display data on screen"))
        self.Step6checkpedslr.setText(_translate("MainWindow", "South - L to R"))
        self.Step6checkpedelr.setText(_translate("MainWindow", "East - L to R"))
        self.Step3d1Label.setText(_translate("MainWindow", "Start Date: (inclusive)"))
        self.Step8pushButtonConfirmQuery.setText(_translate("MainWindow", "Confirm Query"))
        self.Step2radioButtonMode1.setText(_translate("MainWindow", "Summarized (Mode 1)"))

    def step8clicked(self):  # so that when "confirmed query" is pressed GUI window closes
        self.mainwindow.close()

    # def step1_1clicked(self):
    #     image = QtGui.QImage(QtGui.QImageReader("./kalayout.png").read())


# global function to pull values based on GUI input
def pull_val_from_GUI(ui):
    # Step 1 Select Location (UDID) - defines udid
    if ui.Step1radioButton1.isChecked():
        udid = 'BCT_3D_5G_0101001'
    elif ui.Step1radioButton2.isChecked():
        udid = 'BCT_3D_5G_0101002'
    print(udid)

    # Step 2 Select Data Mode - defines mode
    if ui.Step2radioButtonMode1.isChecked():
        mode = 1
    elif ui.Step2radioButtonMode2.isChecked():
        mode = 2

    # Step 3 Enter Date and/or Time Range - defines d1,t1,d2,t2
    d1 = ui.Step3d1Enter.text()  # format: YYYY-MM-DD
    t1 = ui.Step3t1Enter.text()  # format: THH:MM:SS
    d2 = ui.Step3d2Enter.text()
    t2 = ui.Step3t2Enter.text()

    # Step 4 Input Threshold - defines threshold
    if ui.Step4thresholdEnter.text() == "":
        threshold = 300
    else:
        threshold = int(ui.Step4thresholdEnter.text())

    # Step 5 Select Aggregation Interval (Mode 2 Only) - defines a
    if ui.Step5radioButton1.isChecked():
        a = 1
    elif ui.Step5radioButton2.isChecked():
        a = 2
    elif ui.Step5radioButton3.isChecked():
        a = 3
    elif ui.Step5radioButton4.isChecked():
        a = 4
    else:
        a = 0


    # Step 6 Select Output Items (Mode 2 Only) - defines f
    # vehicle directions
    # North
    if ui.Step6checknw.isChecked():
        nw = "nw"
    else:
        nw = ""

    if ui.Step6checkne.isChecked():
        ne = "ne"
    else:
        ne = ""

    if ui.Step6checkns.isChecked():
        ns = "ns"
    else:
        ns = ""
    # South
    if ui.Step6checksw.isChecked():
        sw = "sw"
    else:
        sw = ""

    if ui.Step6checkse.isChecked():
        se = "se"
    else:
        se = ""

    if ui.Step6checksn.isChecked():
        sn = "sn"
    else:
        sn = ""
    # West
    if ui.Step6checkwn.isChecked():
        wn = "wn"
    else:
        wn = ""

    if ui.Step6checkwe.isChecked():
        we = "we"
    else:
        we = ""

    if ui.Step6checkws.isChecked():
        ws = "ws"
    else:
        ws = ""
    # East
    if ui.Step6checken.isChecked():
        en = "en"
    else:
        en = ""

    if ui.Step6checkew.isChecked():
        ew = "ew"
    else:
        ew = ""

    if ui.Step6checkes.isChecked():
        es = "es"
    else:
        es = ""

    # Pedestrian Directions
    if ui.Step6checkpednlr.isChecked():
        nlr = "nlr"
    else:
        nlr = ""

    if ui.Step6checkpednrl.isChecked():
        nrl = "nrl"
    else:
        nrl = ""

    if ui.Step6checkpedslr.isChecked():
        slr = "slr"
    else:
        slr = ""

    if ui.Step6checkpedsrl.isChecked():
        srl = "srl"
    else:
        srl = ""

    if ui.Step6checkpedwlr.isChecked():
        wlr = "wlr"
    else:
        wlr = ""

    if ui.Step6checkpedwrl.isChecked():
        wrl = "wrl"
    else:
        wrl = ""

    if ui.Step6checkpedelr.isChecked():
        elr = "elr"
    else:
        elr = ""

    if ui.Step6checkpederl.isChecked():
        erl = "erl"
    else:
        erl = ""

    selected_dir = [nw, ne, ns, sw, se, sn, wn, we, ws, en, ew, es, nlr, nrl, slr, srl, wlr, wrl, elr, erl]
    f = ",".join(i for i in selected_dir if
                 len(i) > 0)  # a string that contains all the selected directions seperated by comma for API call

    # Step 7 Select Output Format
    if ui.Step7radioButtondisplay.isChecked() == True:
        print_only = True
    elif ui.Step7radioButtoncsv.isChecked() == True:
        print_only = False
    # csv file saving window should pop up here and get file name and location

    # return variables needed for API call
    return (udid, mode, d1, t1, d2, t2, threshold, a, f, print_only)
