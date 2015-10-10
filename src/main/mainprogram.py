import numpy as np
from src.main.funcs import log, deletelogger
from os import path, getcwd, pardir
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSlot
from src.ui.mainwindow import Ui_MainWindow
from src.ui.mplwidget import MplWidget
from src.main.INIfile import Ini, IniFile
from src.main.data import Data
from src.main.tablemodel_raw import TableModel_Raw
from src.main.tablemodel_treated import TableModel_Treated



class MyMainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        deletelogger()
        log('class MyMainWindow: def __init__')
        self.setupUi(self)
        # ---------- class variables ------------------------
        # -- paths --
        self.pathStart = getcwd()
        self.pathParent = path.abspath(path.join(self.pathStart, pardir))
        self.pathSettings = path.join(self.pathParent, 'settings')
        # -- project stuff --
        self.actModelName = ''
        self.ini = Ini()
        # -- data --
        self.data = Data(self)
        self.tablemodelraw = TableModel_Raw(data=self.data, parent=self)
        self.tablemodeltreated = TableModel_Treated(data=self.data, parent=self)
        # -- add matplotlib widget
        self.mpl = MplWidget(self.tab)
        self.mpl.setObjectName("mpl")
        self.horizontalLayout_5.addWidget(self.mpl)
        # --- initializations ------------------------
        self.initIni()
        self.initFileMenu()
        # self.initPerspectives()
        self.initPerspectives()
        self.iniTreeWidgetProject()
        self.initTableRaw()
        self.initTableTreated()
        self.initTabSelect()
        self.initTabWidget()
        self.initComboSelect1()
        self.initlistWidget_select1()
        # self.resetMplPlot()
        self.initTreatments()
        self.initPlotSettings()

        self.comboBox_select1_seletedItm = ''

    # region  -------------------- Initializations -----------------------------

    def initIni(self):
        iniFile = IniFile()
        iniFile.read(self.pathSettings, self.ini)
        if not path.isfile(self.ini.paths.samples):
            self.ini.paths.samples = path.join(self.pathParent, 'samples')
            iniFile.write(self.pathSettings, self.ini)
        # print('self.pathStart:             ' + self.pathStart)
        # print('self.pathParent:            ' + self.pathParent)
        # print('self.pathSettings:          ' + self.pathSettings)
        # print('self.ini.paths.lastproject: ' + self.ini.paths.lastproject)
        # print('self.ini.paths.projects:    ' + self.ini.paths.projects)
        # print('self.ini.paths.samples:     ' + self.ini.paths.samples)

    def initDockWigets(self):
        self.dockwidget1.setMinimumWidth(300)

    def initTabSelect(self):
        #print('class MyMainWindow: def initTabSelect')
        self.listWidget_select2.setVisible(False)
        self.listWidget_select3.setVisible(False)

    def initTabWidget(self):
        #print('class MyMainWindow: def initTabWidget')
        self.tabwidgetmain.currentChanged.connect(self.tabindex_changed)

    def initTableRaw(self):
        #print('class MyMainWindow: def initTableRaw')
        self.tableView_raw.setModel(self.tablemodelraw)
        self.tableView_raw.setAlternatingRowColors(True)

    def initTableTreated(self):
        self.tableView_treated.setModel(self.tablemodeltreated)
        self.tableView_treated.setAlternatingRowColors(True)

    def initFileMenu(self):
        #print('class MyMainWindow: def initFileMenu')
        self.action_file_project_open.triggered.connect(
            self.onPerspectiveSave_triggered)

    # endregion

    # region -------------------- Class Events --------------------------------

    def showEvent(self, event):
        log('class MyMainWindow: def showEvent')
        self.onPerspectiveOpenLast()

    def closeEvent(self, event):
        print('class MyMainWindow: def closeEvent')
        if self.windowState() != QtCore.Qt.WindowMaximized:
            print('nicht max')
            self.savePerspective(path.join(self.pathSettings, 'last.persp'))

    def tabindex_changed(self):
        print('class MyMainWindow: def tabindex_changed')
        if self.tabwidgetmain.currentIndex() == 2:
            self.resetMplPlot()

    # endregion

    # region -------------------- Tree Widget ---------------------------------

    def iniTreeWidgetProject(self: object):
        # print('class MyMainWindow: def iniTreeWidgetProjec')
        self.treeWidgetProject.setHeaderLabels(['Item', 'Description'])
        self.treeWidgetProject.setColumnWidth(0, 150)
        itm1 = QtGui.QTreeWidgetItem(['Model name', 'Moisture'])
        itm11 = QtGui.QTreeWidgetItem(['selected samples', '1-32'])
        itm12 = QtGui.QTreeWidgetItem(['pre treatment', 'SNV, Derivate gap 2'])
        itm121 = QtGui.QTreeWidgetItem(['SNV', ''])
        itm12.addChild(itm121)
        itm13 = QtGui.QTreeWidgetItem(['validation',
                                       'cross validation 111222333'])
        itm1.addChildren([itm11, itm12, itm13])
        itm2 = QtGui.QTreeWidgetItem(['Model name', 'Protein'])
        itm21 = QtGui.QTreeWidgetItem(['selected samples', '1-35, 7-45'])
        itm22 = QtGui.QTreeWidgetItem(['pre treatment', 'SNV, Derivate gap 4'])
        itm23 = QtGui.QTreeWidgetItem(['validation',
                                       'cross validation 111222333'])
        itm2.addChildren([itm21, itm22, itm23])

        self.treeWidgetProject.addTopLevelItems([itm1, itm2])
        self.treeWidgetProject.currentItemChanged.connect(
                                    self.on_treeWidgetProject_currentItemChanged)

    @pyqtSlot(QtGui.QTreeWidgetItem)
    def on_treeWidgetProject_currentItemChanged(self):
        log('class MyMainWindow: def on_treeWidgetProject_currentItemChanged')
        currentitem = self.treeWidgetProject.currentItem()
        if currentitem:
            currnodes = [currentitem]
            currKeys = [currentitem.text(0)]
            currValus = [currentitem.text(1)]
            parentitem1 = currentitem.parent()
            if parentitem1:
                currnodes.append(parentitem1)
                currKeys.append(parentitem1.text(0))
                currValus.append(parentitem1.text(1))
                parentitem2 = parentitem1.parent()
                if parentitem2:
                    currnodes.append(parentitem2)
                    currKeys.append(parentitem2.text(0))
                    currValus.append(parentitem2.text(1))
            # print(currKeys)
            # print(currKeys[-1])
            if currValus[-1] != self.actModelName:
                self.actModelName = currValus[-1]
                # print('self.actModelName changed into: ' + self.actModelName)
                self.loadSamples()

        # self.tablemodelraw.reset()
        # self.tablemodeltreated.reset()

    def loadSamples(self, filename='Donut.csv'):
        log('class MyMainWindow: def loadSamples')
        self.tablemodelraw.beginResetModel()
        self.tablemodeltreated.beginResetModel()
        self.data.loadSamples(path.join(self.ini.paths.samples, filename))
        # self.resetlistWidget_select1()
        self.resetComboSelect1()
        #self.resetPlotSettings()
        self.tablemodelraw.reset()
        #self.tablemodelraw.endResetModel()
        # self.tablemodeltreated.reset()
        #self.tablemodeltreated.endResetModel()
        #self.formatTableView_raw()
        #self.formatTableView_treated()

    def formatTableView_raw(self):
        log('class MyMainWindow: def formatTableView_raw')
        self.tableView_raw.setColumnWidth(0, 38)
        self.tableView_raw.setColumnWidth(1, 38)
        self.tableView_raw.setColumnHidden(2, True)
        self.tableView_raw.setColumnHidden(3, True)

    def formatTableView_treated(self):
        log('class MyMainWindow: def formatTableView_treated')
        self.tableView_treated.setColumnWidth(0, 38)
        self.tableView_treated.setColumnHidden(1, True)
        self.tableView_treated.setColumnHidden(2, False)
        self.tableView_treated.setColumnHidden(3, False)

    # endregion

    # region -------------------- Perspectives --------------------------------

    def initPerspectives(self):
        #print('class MyMainWindow: def initPerspectives')
        self.action_view_saveCurrentPerspective.triggered.connect(
            self.onPerspectiveSave_triggered)
        self.action_view_ToggleFull_Screen.triggered.connect(
            self.onPerspectiveSave_triggered)
        self.action_view_FactoryPerspective.triggered.connect(
            self.onPerspectiveOpenFactory)

    def onPerspectiveSave_triggered(self):
        #print('class MyMainWindow: def onPerspectiveSave_triggered')
        title = "save perspective"
        direc = self.pathSettings
        filtr = "Perspective settings *.persp(*.persp);;Text *.txt(*.txt)"
        fn = QtGui.QFileDialog.getSaveFileName(self, title, direc, filtr)
        if not fn.upper().endswith('.persp'):
            fn += '.persp'
        self.savePerspective(fn)

    def onPerspectiveOpenFactory(self):
        #print('class MyMainWindow: def onPerspectiveOpenFactory')
        fullpath = path.join(self.pathSettings, 'factory.persp')
        print(fullpath)
        self.onPerspectiveOpen(fullpath)

    def onPerspectiveOpenLast(self):
        #print('class MyMainWindow: def onPerspectiveOpenLast')
        fullpath = path.join(self.pathSettings, 'last.persp')
        self.onPerspectiveOpen(fullpath)

    def savePerspective(self, filename: str):
        #print('class MyMainWindow: def savePerspective')
        settings = QtCore.QSettings(filename, QtCore.QSettings.IniFormat)
        settings.setFallbacksEnabled(False)
        settings.beginGroup("MainWindow")
        settings.setValue('geometry', self.saveGeometry())
        settings.setValue('windowstate', self.saveState())
        settings.endGroup()


    def onPerspectiveOpen(self, fullpath):
        #print('class MyMainWindow: def onPerspectiveOpen')
        if path.isfile((fullpath)):
            settings = QtCore.QSettings(fullpath, QtCore.QSettings.IniFormat)
            settings.setFallbacksEnabled(False)
            settings.beginGroup("MainWindow")
            geom = settings.value('geometry', self.saveGeometry())
            wstate = settings.value('windowstate', self.saveState())
            self.restoreGeometry(geom)
            self.restoreState(wstate)
            settings.endGroup()
        else:
            print(fullpath + ' does not exist')

    # endregion

    # region -------------------- select samples ------------------------------

    def initComboSelect1(self):
        # log('class MyMainWindow: def initComboSelect1')
        self.comboBox_select1.addItem('None')
        self.comboBox_select1.currentIndexChanged.connect(self.onComboSelect1_Changed)

    def resetComboSelect1(self):
        log('class MyMainWindow: def resetComboSelect1')
        self.comboBox_select1.clear()
        self.comboPlot_ColourBy.clear()
        itms = ['None', 'Row']
        for dname in self.data.headerd:
            itms.append(dname)
        for yname in self.data.headery:
            itms.append(yname)
        self.comboBox_select1.addItems(itms)
        self.comboPlot_ColourBy.addItems(itms)
        # self.comboBox_select1.setCurrentIndex(0)

    def onComboSelect1_Changed(self):
        self.resetlistWidget_select1()

    def initlistWidget_select1(self):
        # log('class MyMainWindow: def initlistWidget_select1')
        self.listWidget_select1.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_select1.itemSelectionChanged.connect(self.onListWidget_select1_changed)

    def resetlistWidget_select1(self):
        # log('class MyMainWindow: def resetlistWidget_select1')
        #print('combo1.: ', self.comboBox_select1.currentText())
        self.comboPlot_ColourBy.setCurrentIndex(self.comboBox_select1.currentIndex())
        self.listWidget_select1.clear()
        currText = self.comboBox_select1.currentText()
        if currText != self.comboBox_select1_seletedItm:
            log('class MyMainWindow: def resetlistWidget_select1-')
            self.comboBox_select1_seletedItm = currText
            itms = []
            if currText == 'Row':
                # itms = [str(i + 1) for i in self.data.indx1]
                for r in range(self.data.nrows):
                    if self.data.ignore[r] == 0:
                        itms.append(str(r+1))
            elif currText in self.data.headerd:
                idx = self.data.headerd.index(currText)
                # itms = [self.data.descr[i][idx] for i in self.data.indx]
                for r in range(self.data.nrows):
                    if self.data.ignore[r] == 0:
                        if not self.data.descr[r][idx] in itms:
                            itms.append(self.data.descr[r][idx])
            elif currText in self.data.headery:
                idx = self.data.headery.index(currText)
                # argsort = np.argsort(self.data.yarr[:, idx])
                sortiert = self.data.yarr[:, idx]
                sortiert.sort()
                for x in sortiert:
                    xstr = '{:.1f}'.format(x)
                    if not xstr in itms:
                        itms.append(xstr)

            # mymin = np.floor(np.nanmin(self.data.yarr[:, idx],axis=0))
            # mymax = np.ceil(np.nanmax(self.data.yarr[:, idx],axis=0))
            # mystep = (mymax-mymin) / 5
            # steps = np.arange(mymin, mymax, mystep, dtype=float )
            # for step in steps:
            #     itms.append(str(step) + ' - ' + str(step + mystep))
            self.listWidget_select1.addItems(itms)
            self.data.recalculateIndx2()


    def onListWidget_select1_changed(self):
        log('class MyMainWindow: def onListWidget1 changed')
        self.listWidgetPlot_ColourBy.setCurrentRow(1)


    # endregion

    # region -------------------- treatments ----------------------------------

    def initTreatments(self):
        self.checkBox_treatment_apply.stateChanged.connect(
            self.onCheck_treatment_apply)
        self.listWidget_treatAvailable.addItems(['SNV'])
        self.listWidget_treatAvailable.currentItemChanged.connect(
            self.onlistWidget_treatAvailable_changed)
        self.pushButton_treatment_add.clicked.connect(
            self.onPushButton_treatment_add_clicked)
        self.pushButton_treatment_remove.clicked.connect(
            self.onPushButton_treatment_remove_clicked)
        self.pushButton_treatment_apply.clicked.connect(self.treatmentApply)

    def onCheck_treatment_apply(self):
        self.pushButton_treatment_apply.setEnabled(
            not self.checkBox_treatment_apply.checkState())

    def onlistWidget_treatAvailable_changed(self):
        print(self.listWidget_treatAvailable.currentItem().text())

    def onPushButton_treatment_add_clicked(self):
        self.treatmentAddSelected()

    def treatmentAddSelected(self):
        treat = self.listWidget_treatAvailable.currentItem().text()
        self.listWidget_treatSelected.addItem(QtGui.QListWidgetItem(treat))
        if self.checkBox_treatment_apply.checkState():
            self.treatmentApply()

    def onPushButton_treatment_remove_clicked(self):
        for itm in self.listWidget_treatSelected.selectedItems():
            self.listWidget_treatSelected.takeItem(
                self.listWidget_treatSelected.row(itm))
            if self.checkBox_treatment_apply.checkState():
                self.treatmentApply()

    def treatmentApply(self):
        treatments = []
        if self.listWidget_treatSelected.count() == 0:
            treatments.append('None')
        else:
            treatments.append('Reset')
            for idx in range( self.listWidget_treatSelected.count()):
                treatments.append(self.listWidget_treatSelected.item(idx).text())

        print('apply treatments: ', treatments)
        for treatment in treatments:
            self.data.treat(treatment)
        self.resetColours()
        self.resetMplPlot()


    # endregion

    # region -------------------- Plot ----------------------------------------

    def initPlotSettings(self):
        self.comboPlot_ColourBy.currentIndexChanged.connect(self.resetColours)
        self.coloursY = ['red', 'orange', 'green', 'blue', 'darkviolet']

    def resetPlotSettings(self):
        log('class MyMainWindow: def resetPlotSettings')
        self.comboPlot_ColourBy.clear()
        itms = ['Row']
        for dname in self.data.headerd:
            itms.append(dname)
        for yname in self.data.headery:
            itms.append(yname)
        self.comboPlot_ColourBy.addItems(itms)

    def resetMplPlot(self):
        log('class MyMainWindow: def resetMplPlot')
        if self.tabwidgetmain.currentIndex() != 2:
            return
        ax = self.mpl.canvas.ax
        ax.clear()
        x = self.data.xvector
        for r in range(self.data.nrows):
            if r in self.data.indx2:
                y = self.data.xtreat[r]
                colour = self.data.colour[r]
                label = self.data.label[r]
                if colour == '':
                    colour = 'red'
                    #     self.mpl.canvas.ax.plot(x, y)
                    # else:
                    #     self.mpl.canvas.ax.plot(x, y,  color=colour, label = 'a')
                    #     self.mpl.canvas.ax.le
                    #     plt.legend(handles=[line_up, line_down])
                if label == '':
                    p1, = ax.plot(x, y, color = colour)
                else:
                    p1, = ax.plot(x, y,   label = label, color = colour)
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles, labels)

        self.mpl.canvas.draw()

    def resetColours(self):
        log('class MyMainWindow: def resetColours(self):')
        colourCriterion = self.comboPlot_ColourBy.currentText()
        print('colourCriterion:',colourCriterion)
        icolour = 0
        self.data.colour = [''] * self.data.nrows
        self.data.label = [''] * self.data.nrows
        if colourCriterion == 'Row':
            for r in range(self.data.nrows):
                if r in self.data.indx2:
                    self.data.colour[r] = self.coloursY[icolour % len(self.coloursY)]
                    icolour += 1
        elif colourCriterion in self.data.headerd:
            idx = self.data.headerd.index(colourCriterion)
            key = []
            for r in range(self.data.nrows):
                if r in self.data.indx2:
                    if not self.data.descr[r][idx] in key:
                        key.append(self.data.descr[r][idx])
                        self.data.label[r] = self.data.descr[r][idx]
                    self.data.colour[r] = self.coloursY[
                        key.index(self.data.descr[r][idx]) % len(self.coloursY)]
        elif colourCriterion in self.data.headery:
            idx = self.data.headery.index(colourCriterion)
            argsort = np.argsort(self.data.yarr[:, idx])
             # get min and max
            ymin = 1000000000
            ymax = -ymin
            # find min and max
            for r in range(self.data.nrows):
                if r in self.data.indx2:
                    if self.data.yarr[r,idx] > ymax:
                        ymax = self.data.yarr[r,idx]
                    if self.data.yarr[r,idx] < ymin:
                        ymin = self.data.yarr[r,idx]
            ymin = np.floor(ymin)  # np.floor(np.nanmin(self.data.yarr[:, idx],axis=0))
            ymax = np.ceil(ymax)   # np.ceil(np.nanmax(self.data.yarr[:, idx],axis=0))
            ystep = (ymax-ymin)/len(self.coloursY)
            ysteps = np.arange(ymin, ymax, ystep)
            labels = []
            for r in range(self.data.nrows):
                if r in self.data.indx2:
                    y = self.data.yarr[r,idx]
                    isdone = False
                    for i in range(len(ysteps)):
                        y0 = ysteps[i]

                        if y>11:
                            print(y)

                        if y <= y0 + ystep:
                            if not isdone:
                                isdone = True
                                ystr = str(y0) + ' - ' + str(y0 + ystep)
                                self.data.colour[r] = self.coloursY[i]
                                if not ystr in labels:
                                    labels.append(ystr)
                                    self.data.label[r] = ystr


        self.tablemodeltreated.reset()
        self.resetMplPlot()



    # endregion

    def nix(self):
        pass
