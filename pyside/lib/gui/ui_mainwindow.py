# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created: Mon May 18 16:43:01 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(451, 531)
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
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_login = QtGui.QPushButton(self.tab_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy)
        self.btn_login.setObjectName("btn_login")
        self.verticalLayout_4.addWidget(self.btn_login)
        self.btn_logout = QtGui.QPushButton(self.tab_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setObjectName("btn_logout")
        self.verticalLayout_4.addWidget(self.btn_logout)
        self.btn_check_status = QtGui.QPushButton(self.tab_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_check_status.sizePolicy().hasHeightForWidth())
        self.btn_check_status.setSizePolicy(sizePolicy)
        self.btn_check_status.setObjectName("btn_check_status")
        self.verticalLayout_4.addWidget(self.btn_check_status)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem)
        self.btn_quit = QtGui.QPushButton(self.tab_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_quit.sizePolicy().hasHeightForWidth())
        self.btn_quit.setSizePolicy(sizePolicy)
        self.btn_quit.setObjectName("btn_quit")
        self.verticalLayout_4.addWidget(self.btn_quit)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_get_empire_status = QtGui.QPushButton(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_get_empire_status.sizePolicy().hasHeightForWidth())
        self.btn_get_empire_status.setSizePolicy(sizePolicy)
        self.btn_get_empire_status.setObjectName("btn_get_empire_status")
        self.verticalLayout_3.addWidget(self.btn_get_empire_status)
        self.txt_status = QtGui.QPlainTextEdit(self.tab_2)
        self.txt_status.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txt_status.setTabChangesFocus(False)
        self.txt_status.setObjectName("txt_status")
        self.verticalLayout_3.addWidget(self.txt_status)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tbl_abbrv = QtGui.QTableWidget(self.tab_3)
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
        self.tabWidget.addTab(self.tab_3, "")
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
        self.actionConfig_File_Status.setObjectName("actionConfig_File_Status")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionChose_Config_File)
        self.menuFile.addAction(self.actionChose_Config_Section)
        self.menuFile.addAction(self.actionConfig_File_Status)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLog_In)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionTest)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL("activated()"), MainWindow.close)
        QtCore.QObject.connect(self.btn_quit, QtCore.SIGNAL("clicked()"), MainWindow.close)
        QtCore.QObject.connect(MainWindow, QtCore.SIGNAL("destroyed()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btn_login, self.btn_logout)
        MainWindow.setTabOrder(self.btn_logout, self.btn_check_status)
        MainWindow.setTabOrder(self.btn_check_status, self.btn_quit)
        MainWindow.setTabOrder(self.btn_quit, self.btn_get_empire_status)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_login.setText(QtGui.QApplication.translate("MainWindow", "Log in", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_logout.setText(QtGui.QApplication.translate("MainWindow", "Log out", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_check_status.setText(QtGui.QApplication.translate("MainWindow", "Check login status", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_quit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QtGui.QApplication.translate("MainWindow", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_get_empire_status.setText(QtGui.QApplication.translate("MainWindow", "Get Empire Status", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Empire Status", None, QtGui.QApplication.UnicodeUTF8))
        self.tbl_abbrv.setSortingEnabled(True)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Abbreviations", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.statusbar.setToolTip(QtGui.QApplication.translate("MainWindow", "status tt", None, QtGui.QApplication.UnicodeUTF8))
        self.statusbar.setStatusTip(QtGui.QApplication.translate("MainWindow", "status st", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionChose_Config_File.setText(QtGui.QApplication.translate("MainWindow", "Chose Config File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionChose_Config_Section.setText(QtGui.QApplication.translate("MainWindow", "Chose Config Section", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTest.setText(QtGui.QApplication.translate("MainWindow", "Test", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLog_In.setText(QtGui.QApplication.translate("MainWindow", "Log In", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfig_File_Status.setText(QtGui.QApplication.translate("MainWindow", "Config File Status", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

