from PyQt4 import QtCore, QtGui
import numpy as np
from src.main.data import Data


class TableModel_Raw(QtCore.QAbstractTableModel):
    def __init__(self, data=Data(),  parent=None, *args):
        # print('class RawDataModel: def __init__')
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self._data = data
        self.parent = parent

    def rowCount(self, parent):
        # print('class RawDataModel: def rowCount rowcount:', self._data.nrows)
        return self._data.nrows

    def columnCount(self, parent):
        # print('class RawDataModel: def columnCount')
        return self._data.ncols

    def flags(self, index):
        # print('class RawDataModel: def flags')
        if index.column() < 2:
            return  QtCore.Qt.ItemIsEnabled | \
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable
        else:
            return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | \
                QtCore.Qt.ItemIsSelectable

    def data(self, index, role):
        # print('class RawDataModel: def data')
        irow = index.row()
        icol = index.column()
        if not index.isValid():
            return None
        if icol < 2:    # checkboxes
            if role == QtCore.Qt.EditRole:
                return None
            if role == QtCore.Qt.DisplayRole:
                return None
            if role == QtCore.Qt.CheckStateRole:
                if icol == 0:
                    valu = self._data.mark[irow]
                elif icol == 1:
                    valu = self._data.ignore[irow]
                if valu == 0:
                    return QtCore.Qt.Unchecked
                else:
                    return QtCore.Qt.Checked
        else:
            if icol == 2:
                if irow < len(self._data.indx1):
                    valu = self._data.indx1[irow]
                else:
                    valu = None
            elif icol == 3:
                valu = None
            elif icol < self._data.idxy1:
                valu = self._data.descr[irow][icol-self._data.idxd1]
            elif icol < self._data.idxx1:
                if np.isnan(self._data.yarr[irow, icol-self._data.idxy1]):
                    valu = ''
                else:
                    valu = '{:.2f}'.format(self._data.yarr[irow, icol-self._data.idxy1])
            else:
                valu = '{:.6f}'.format(self._data.xarr[irow, icol-self._data.idxx1])

            if role == QtCore.Qt.EditRole:
                return valu
            if role == QtCore.Qt.DisplayRole:
                return valu

    def setData(self, index, value, role = QtCore.Qt.EditRole):
        # print('class RawDataModel: def setData')
        if role == QtCore.Qt.EditRole:
            row = index.row()
            column = index.column()
            self._data.setRawCellVaue(row, column, value)
            self.dataChanged.emit(index, index)
            return True
        if role == QtCore.Qt.CheckStateRole:
            row = index.row()
            column = index.column()
            self._data.setRawCellVaue(row, column, value)
            self.dataChanged.emit(index, index)
            print('icol:', ' irow:', ' value:' )
            print(column, row,value)
            if column == 1:
                self._data.recalculateIndx1()
                idx1 = self.createIndex(0, 2)
                idx2 = self.createIndex(self._data.nrows, 0)
                self.dataChanged.emit(idx1, idx2)
                self.parent.tablemodeltreated.reset()
                self.parent.resetlistWidget_select1()
                # TreatedData.beginResetModel(TreatedData())

            return True

        return False

    def headerData(self, section, orientation, role):
        # print('class RawDataModel: def headerData')
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                if section < len(self._data.header):
                    return self._data.header[section]
                else:
                    return None # "not implemented"
            else:
                return '  ' + str(+section+1) + '  '

    #=====================================================#
    #INSERTING & REMOVING
    #=====================================================#
    def insertRows(self, position, rows, parent = QtCore.QModelIndex()):
        self.beginInsertRows(parent, position, position + rows - 1)
        for i in range(rows):
            defaultValues = [QtGui.QColor("#000000") for i in range(self.columnCount(None))]
            self.__colors.insert(position, defaultValues)
        self.endInsertRows()
        return True

    def insertColumns(self, position, columns, parent = QtCore.QModelIndex()):
        self.beginInsertColumns(parent, position, position + columns - 1)
        rowCount = len(self.__colors)
        for i in range(columns):
            for j in range(rowCount):
                self.__colors[j].insert(position, QtGui.QColor("#000000"))
        self.endInsertColumns()
        return True


