# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created: Thu May 21 18:57:03 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(451, 531)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setFocusPolicy(QtCore.Qt.TabFocus)
        MainWindow.setStyleSheet("QPushButton {\n"
"   padding: 5px;\n"
"}\n"
"QPushButton:focus {\n"
"    /* border: 1px dotted black; */\n"
"}")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_ships = QtGui.QWidget()
        self.tab_ships.setObjectName("tab_ships")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_ships)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cmb_planets = QtGui.QComboBox(self.tab_ships)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_planets.sizePolicy().hasHeightForWidth())
        self.cmb_planets.setSizePolicy(sizePolicy)
        self.cmb_planets.setObjectName("cmb_planets")
        self.horizontalLayout.addWidget(self.cmb_planets)
        self.btn_get_ships = QtGui.QPushButton(self.tab_ships)
        self.btn_get_ships.setObjectName("btn_get_ships")
        self.horizontalLayout.addWidget(self.btn_get_ships)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.tbl_ships = QtGui.QTableWidget(self.tab_ships)
        self.tbl_ships.setAlternatingRowColors(True)
        self.tbl_ships.setColumnCount(4)
        self.tbl_ships.setObjectName("tbl_ships")
        self.tbl_ships.setColumnCount(4)
        self.tbl_ships.setRowCount(0)
        self.verticalLayout_4.addWidget(self.tbl_ships)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.tab_ships, "")
        self.tab_status = QtGui.QWidget()
        self.tab_status.setObjectName("tab_status")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tab_status)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_get_empire_status = QtGui.QPushButton(self.tab_status)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_get_empire_status.sizePolicy().hasHeightForWidth())
        self.btn_get_empire_status.setSizePolicy(sizePolicy)
        self.btn_get_empire_status.setObjectName("btn_get_empire_status")
        self.verticalLayout_3.addWidget(self.btn_get_empire_status)
        self.txt_status = QtGui.QPlainTextEdit(self.tab_status)
        self.txt_status.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txt_status.setTabChangesFocus(False)
        self.txt_status.setObjectName("txt_status")
        self.verticalLayout_3.addWidget(self.txt_status)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_status, "")
        self.tab_abbrv = QtGui.QWidget()
        self.tab_abbrv.setObjectName("tab_abbrv")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_abbrv)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tbl_abbrv = QtGui.QTableWidget(self.tab_abbrv)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_abbrv.sizePolicy().hasHeightForWidth())
        self.tbl_abbrv.setSizePolicy(sizePolicy)
        self.tbl_abbrv.setAlternatingRowColors(True)
        self.tbl_abbrv.setColumnCount(2)
        self.tbl_abbrv.setObjectName("tbl_abbrv")
        self.tbl_abbrv.setColumnCount(2)
        self.tbl_abbrv.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tbl_abbrv)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab_abbrv, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 451, 25))
        self.menubar.setMouseTracking(True)
        self.menubar.setAcceptDrops(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setMouseTracking(True)
        self.menuFile.setAcceptDrops(True)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setCursor(QtCore.Qt.ArrowCursor)
        self.statusbar.setWhatsThis("")
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionChose_Config_File = QtGui.QAction(MainWindow)
        self.actionChose_Config_File.setObjectName("actionChose_Config_File")
        self.actionChose_Config_Section = QtGui.QAction(MainWindow)
        self.actionChose_Config_Section.setObjectName("actionChose_Config_Section")
        self.actionTest = QtGui.QAction(MainWindow)
        self.actionTest.setObjectName("actionTest")
        self.actionLog_In = QtGui.QAction(MainWindow)
        self.actionLog_In.setObjectName("actionLog_In")
        self.actionConfig_File_Status = QtGui.QAction(MainWindow)
        self.actionConfig_File_Status.setStatusTip("")
        self.actionConfig_File_Status.setObjectName("actionConfig_File_Status")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionLog_Out = QtGui.QAction(MainWindow)
        self.actionLog_Out.setObjectName("actionLog_Out")
        self.actionClear_All_Caches = QtGui.QAction(MainWindow)
        self.actionClear_All_Caches.setObjectName("actionClear_All_Caches")
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionChose_Config_File)
        self.menuFile.addAction(self.actionChose_Config_Section)
        self.menuFile.addAction(self.actionConfig_File_Status)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLog_In)
        self.menuFile.addAction(self.actionLog_Out)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionTest)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionClear_All_Caches)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL("activated()"), MainWindow.close)
        QtCore.QObject.connect(MainWindow, QtCore.SIGNAL("destroyed()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_get_ships.setText(QtGui.QApplication.translate("MainWindow", "Get ships on this planet", None, QtGui.QApplication.UnicodeUTF8))
        self.tbl_ships.setSortingEnabled(False)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ships), QtGui.QApplication.translate("MainWindow", "Ships", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_get_empire_status.setText(QtGui.QApplication.translate("MainWindow", "Get Empire Status", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_status), QtGui.QApplication.translate("MainWindow", "Empire Status", None, QtGui.QApplication.UnicodeUTF8))
        self.tbl_abbrv.setSortingEnabled(True)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_abbrv), QtGui.QApplication.translate("MainWindow", "Abbreviations", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.statusbar.setToolTip(QtGui.QApplication.translate("MainWindow", "status tt", None, QtGui.QApplication.UnicodeUTF8))
        self.statusbar.setStatusTip(QtGui.QApplication.translate("MainWindow", "status st", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionChose_Config_File.setText(QtGui.QApplication.translate("MainWindow", "Chose Config File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionChose_Config_File.setStatusTip(QtGui.QApplication.translate("MainWindow", "Select a non-default config file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionChose_Config_Section.setText(QtGui.QApplication.translate("MainWindow", "Chose Config Section", None, QtGui.QApplication.UnicodeUTF8))
        self.actionChose_Config_Section.setStatusTip(QtGui.QApplication.translate("MainWindow", "Log in using a different account", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTest.setText(QtGui.QApplication.translate("MainWindow", "Test", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTest.setStatusTip(QtGui.QApplication.translate("MainWindow", "Whoops.  I should have removed this.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLog_In.setText(QtGui.QApplication.translate("MainWindow", "Log In", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfig_File_Status.setText(QtGui.QApplication.translate("MainWindow", "Connection Status", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setStatusTip(QtGui.QApplication.translate("MainWindow", "App details and version information", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLog_Out.setText(QtGui.QApplication.translate("MainWindow", "Log Out", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear_All_Caches.setText(QtGui.QApplication.translate("MainWindow", "Clear All Caches", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear_All_Caches.setToolTip(QtGui.QApplication.translate("MainWindow", "Click if you\'re getting old data.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear_All_Caches.setStatusTip(QtGui.QApplication.translate("MainWindow", "Click if you\'re getting old data.", None, QtGui.QApplication.UnicodeUTF8))

