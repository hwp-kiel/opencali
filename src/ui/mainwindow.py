# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sun Oct  4 19:18:51 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 719)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabwidgetmain = QtGui.QTabWidget(self.centralwidget)
        self.tabwidgetmain.setTabPosition(QtGui.QTabWidget.South)
        self.tabwidgetmain.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabwidgetmain.setObjectName(_fromUtf8("tabwidgetmain"))
        self.tab_raw_data = QtGui.QWidget()
        self.tab_raw_data.setObjectName(_fromUtf8("tab_raw_data"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tab_raw_data)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.tableView_raw = QtGui.QTableView(self.tab_raw_data)
        self.tableView_raw.setObjectName(_fromUtf8("tableView_raw"))
        self.horizontalLayout_4.addWidget(self.tableView_raw)
        self.tabwidgetmain.addTab(self.tab_raw_data, _fromUtf8(""))
        self.tab_treated_data = QtGui.QWidget()
        self.tab_treated_data.setObjectName(_fromUtf8("tab_treated_data"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.tab_treated_data)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tableView_treated = QtGui.QTableView(self.tab_treated_data)
        self.tableView_treated.setObjectName(_fromUtf8("tableView_treated"))
        self.horizontalLayout.addWidget(self.tableView_treated)
        self.tabwidgetmain.addTab(self.tab_treated_data, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.tabwidgetmain.addTab(self.tab, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabwidgetmain, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockwidget1 = QtGui.QDockWidget(MainWindow)
        self.dockwidget1.setMinimumSize(QtCore.QSize(300, 166))
        self.dockwidget1.setFloating(False)
        self.dockwidget1.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dockwidget1.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockwidget1.setWindowTitle(_fromUtf8("Pro&ject"))
        self.dockwidget1.setObjectName(_fromUtf8("dockwidget1"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.treeWidgetProject = QtGui.QTreeWidget(self.dockWidgetContents)
        self.treeWidgetProject.setFrameShadow(QtGui.QFrame.Plain)
        self.treeWidgetProject.setColumnCount(2)
        self.treeWidgetProject.setObjectName(_fromUtf8("treeWidgetProject"))
        self.treeWidgetProject.headerItem().setText(0, _fromUtf8("1"))
        self.treeWidgetProject.headerItem().setText(1, _fromUtf8("2"))
        self.horizontalLayout_2.addWidget(self.treeWidgetProject)
        self.dockwidget1.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockwidget1)
        self.dockWidget2 = QtGui.QDockWidget(MainWindow)
        self.dockWidget2.setMinimumSize(QtCore.QSize(319, 410))
        self.dockWidget2.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dockWidget2.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget2.setWindowTitle(_fromUtf8("Setti&ngs"))
        self.dockWidget2.setObjectName(_fromUtf8("dockWidget2"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.dockWidgetContents_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tabWidget = QtGui.QTabWidget(self.dockWidgetContents_2)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabSettings_select = QtGui.QWidget()
        self.tabSettings_select.setObjectName(_fromUtf8("tabSettings_select"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabSettings_select)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.comboBox_select1 = QtGui.QComboBox(self.tabSettings_select)
        self.comboBox_select1.setObjectName(_fromUtf8("comboBox_select1"))
        self.verticalLayout_2.addWidget(self.comboBox_select1)
        self.listWidget_select1 = QtGui.QListWidget(self.tabSettings_select)
        self.listWidget_select1.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_select1.setObjectName(_fromUtf8("listWidget_select1"))
        self.verticalLayout_2.addWidget(self.listWidget_select1)
        self.comboBox_select2 = QtGui.QComboBox(self.tabSettings_select)
        self.comboBox_select2.setObjectName(_fromUtf8("comboBox_select2"))
        self.verticalLayout_2.addWidget(self.comboBox_select2)
        self.listWidget_select2 = QtGui.QListWidget(self.tabSettings_select)
        self.listWidget_select2.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_select2.setObjectName(_fromUtf8("listWidget_select2"))
        self.verticalLayout_2.addWidget(self.listWidget_select2)
        self.comboBox_select3 = QtGui.QComboBox(self.tabSettings_select)
        self.comboBox_select3.setObjectName(_fromUtf8("comboBox_select3"))
        self.verticalLayout_2.addWidget(self.comboBox_select3)
        self.listWidget_select3 = QtGui.QListWidget(self.tabSettings_select)
        self.listWidget_select3.setSelectionMode(QtGui.QAbstractItemView.ContiguousSelection)
        self.listWidget_select3.setObjectName(_fromUtf8("listWidget_select3"))
        self.verticalLayout_2.addWidget(self.listWidget_select3)
        self.tabWidget.addTab(self.tabSettings_select, _fromUtf8(""))
        self.tabSettings_treat = QtGui.QWidget()
        self.tabSettings_treat.setObjectName(_fromUtf8("tabSettings_treat"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tabSettings_treat)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_3 = QtGui.QLabel(self.tabSettings_treat)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 1, 1, 1)
        self.pushButton_treatment_add = QtGui.QPushButton(self.tabSettings_treat)
        self.pushButton_treatment_add.setObjectName(_fromUtf8("pushButton_treatment_add"))
        self.gridLayout_2.addWidget(self.pushButton_treatment_add, 3, 0, 1, 1)
        self.listWidget_treatSelected = QtGui.QListWidget(self.tabSettings_treat)
        self.listWidget_treatSelected.setObjectName(_fromUtf8("listWidget_treatSelected"))
        self.gridLayout_2.addWidget(self.listWidget_treatSelected, 4, 1, 1, 1)
        self.label = QtGui.QLabel(self.tabSettings_treat)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.listWidget_treatAvailable = QtGui.QListWidget(self.tabSettings_treat)
        self.listWidget_treatAvailable.setObjectName(_fromUtf8("listWidget_treatAvailable"))
        self.gridLayout_2.addWidget(self.listWidget_treatAvailable, 4, 0, 1, 1)
        self.pushButton_treatment_remove = QtGui.QPushButton(self.tabSettings_treat)
        self.pushButton_treatment_remove.setObjectName(_fromUtf8("pushButton_treatment_remove"))
        self.gridLayout_2.addWidget(self.pushButton_treatment_remove, 3, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.tabSettings_treat)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.checkBox_treatment_apply = QtGui.QCheckBox(self.tabSettings_treat)
        self.checkBox_treatment_apply.setChecked(True)
        self.checkBox_treatment_apply.setObjectName(_fromUtf8("checkBox_treatment_apply"))
        self.gridLayout_2.addWidget(self.checkBox_treatment_apply, 1, 0, 1, 1)
        self.pushButton_treatment_apply = QtGui.QPushButton(self.tabSettings_treat)
        self.pushButton_treatment_apply.setEnabled(False)
        self.pushButton_treatment_apply.setObjectName(_fromUtf8("pushButton_treatment_apply"))
        self.gridLayout_2.addWidget(self.pushButton_treatment_apply, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tabSettings_treat, _fromUtf8(""))
        self.tabSettings_plot = QtGui.QWidget()
        self.tabSettings_plot.setObjectName(_fromUtf8("tabSettings_plot"))
        self.label_4 = QtGui.QLabel(self.tabSettings_plot)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 221, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.comboPlot_ColourBy = QtGui.QComboBox(self.tabSettings_plot)
        self.comboPlot_ColourBy.setGeometry(QtCore.QRect(20, 30, 241, 33))
        self.comboPlot_ColourBy.setObjectName(_fromUtf8("comboPlot_ColourBy"))
        self.listWidgetPlot_ColourBy = QtGui.QListWidget(self.tabSettings_plot)
        self.listWidgetPlot_ColourBy.setGeometry(QtCore.QRect(20, 70, 241, 192))
        self.listWidgetPlot_ColourBy.setObjectName(_fromUtf8("listWidgetPlot_ColourBy"))
        self.tabWidget.addTab(self.tabSettings_plot, _fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.tabWidget)
        self.dockWidget2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget2)
        self.action_file_project_new = QtGui.QAction(MainWindow)
        self.action_file_project_new.setObjectName(_fromUtf8("action_file_project_new"))
        self.action_file_project_open = QtGui.QAction(MainWindow)
        self.action_file_project_open.setObjectName(_fromUtf8("action_file_project_open"))
        self.action_file_project_save = QtGui.QAction(MainWindow)
        self.action_file_project_save.setObjectName(_fromUtf8("action_file_project_save"))
        self.action_file_project_saveas = QtGui.QAction(MainWindow)
        self.action_file_project_saveas.setObjectName(_fromUtf8("action_file_project_saveas"))
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName(_fromUtf8("action"))
        self.action_view_ToggleFull_Screen = QtGui.QAction(MainWindow)
        self.action_view_ToggleFull_Screen.setCheckable(True)
        self.action_view_ToggleFull_Screen.setObjectName(_fromUtf8("action_view_ToggleFull_Screen"))
        self.action_view_LastPerspective = QtGui.QAction(MainWindow)
        self.action_view_LastPerspective.setObjectName(_fromUtf8("action_view_LastPerspective"))
        self.action_view_OpenOtherPerspective = QtGui.QAction(MainWindow)
        self.action_view_OpenOtherPerspective.setObjectName(_fromUtf8("action_view_OpenOtherPerspective"))
        self.action_view_FactoryPerspective = QtGui.QAction(MainWindow)
        self.action_view_FactoryPerspective.setObjectName(_fromUtf8("action_view_FactoryPerspective"))
        self.action_view_saveCurrentPerspective = QtGui.QAction(MainWindow)
        self.action_view_saveCurrentPerspective.setObjectName(_fromUtf8("action_view_saveCurrentPerspective"))
        self.action_file_exit = QtGui.QAction(MainWindow)
        self.action_file_exit.setObjectName(_fromUtf8("action_file_exit"))
        self.menuFile.addAction(self.action_file_project_new)
        self.menuFile.addAction(self.action_file_project_open)
        self.menuFile.addAction(self.action_file_project_save)
        self.menuFile.addAction(self.action_file_project_saveas)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_file_exit)
        self.menuView.addAction(self.action_view_ToggleFull_Screen)
        self.menuView.addSeparator()
        self.menuView.addAction(self.action_view_LastPerspective)
        self.menuView.addAction(self.action_view_OpenOtherPerspective)
        self.menuView.addAction(self.action_view_FactoryPerspective)
        self.menuView.addAction(self.action_view_saveCurrentPerspective)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        self.tabwidgetmain.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QObject.connect(self.action_file_exit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tabwidgetmain.setTabText(self.tabwidgetmain.indexOf(self.tab_raw_data), _translate("MainWindow", "raw data", None))
        self.tabwidgetmain.setTabText(self.tabwidgetmain.indexOf(self.tab_treated_data), _translate("MainWindow", "treated data", None))
        self.tabwidgetmain.setTabText(self.tabwidgetmain.indexOf(self.tab), _translate("MainWindow", "Page", None))
        self.menuFile.setTitle(_translate("MainWindow", "Fi&le", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSettings_select), _translate("MainWindow", "select", None))
        self.label_3.setText(_translate("MainWindow", "selected", None))
        self.pushButton_treatment_add.setText(_translate("MainWindow", "add >", None))
        self.label.setText(_translate("MainWindow", "Pretreatments", None))
        self.pushButton_treatment_remove.setText(_translate("MainWindow", "< remove", None))
        self.label_2.setText(_translate("MainWindow", "available", None))
        self.checkBox_treatment_apply.setText(_translate("MainWindow", "apply immediately", None))
        self.pushButton_treatment_apply.setText(_translate("MainWindow", "apply now", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSettings_treat), _translate("MainWindow", "treatment", None))
        self.label_4.setText(_translate("MainWindow", "colour defined by:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSettings_plot), _translate("MainWindow", "plot", None))
        self.action_file_project_new.setText(_translate("MainWindow", "&new Project", None))
        self.action_file_project_open.setText(_translate("MainWindow", "&open Project", None))
        self.action_file_project_open.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.action_file_project_save.setText(_translate("MainWindow", "&save project", None))
        self.action_file_project_saveas.setText(_translate("MainWindow", "save &project as", None))
        self.action.setText(_translate("MainWindow", "-", None))
        self.action_view_ToggleFull_Screen.setText(_translate("MainWindow", "Toggle Full Screen", None))
        self.action_view_ToggleFull_Screen.setShortcut(_translate("MainWindow", "F12", None))
        self.action_view_LastPerspective.setText(_translate("MainWindow", "last Perspective", None))
        self.action_view_OpenOtherPerspective.setText(_translate("MainWindow", "open other Perspective", None))
        self.action_view_FactoryPerspective.setText(_translate("MainWindow", "Factory Perspective", None))
        self.action_view_saveCurrentPerspective.setText(_translate("MainWindow", "save current Perspective", None))
        self.action_view_saveCurrentPerspective.setShortcut(_translate("MainWindow", "F10", None))
        self.action_file_exit.setText(_translate("MainWindow", "Exit", None))
        self.action_file_exit.setShortcut(_translate("MainWindow", "Alt+X", None))

