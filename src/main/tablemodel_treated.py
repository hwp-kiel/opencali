import numpy as np
from PyQt4 import QtCore


class TableModel_Treated(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent):
        # print('class TreatedDataModel: def rowCount() rowcount:', self._data.nrows)
        return len(self._data.indx2)

    def columnCount(self, parent):
        return self._data.ncols

    def flags(self, index):
        if index.column() == 0:
            return  QtCore.Qt.ItemIsEnabled | \
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable
        else:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def data(self, index, role):
        irow = self._data.indx2[index.row()]
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
                if irow < len(self._data.colour):
                    valu = self._data.colour[irow]
                else:
                    valu = None
            elif icol == 3:
                if irow < len(self._data.label):
                    valu = self._data.label[irow]
                else:
                    valu = None
            elif icol < self._data.idxy1:
                valu = self._data.descr[irow][icol-self._data.idxd1]
            elif icol < self._data.idxx1:
                if np.isnan(self._data.yarr[irow, icol-self._data.idxy1]):
                    valu = ''
                else:
                    valu = '{:.2f}'.format(self._data.yarr[irow, icol-self._data.idxy1])
            else:
                valu = '{:.6f}'.format(self._data.xtreat[irow, icol-self._data.idxx1])

            if role == QtCore.Qt.EditRole:
                return valu
            if role == QtCore.Qt.DisplayRole:
                return valu

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                if section < len(self._data.header):
                    return self._data.header[section]
                else:
                    return None # "not implemented"
            else:
                if section < len(self._data.indx2):
                    return '  ' + str(1 + self._data.indx2[section]) + '  '

