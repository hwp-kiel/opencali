import numpy as np
import os
import csv
from src.main.funcs import convert_str_to_0or1
from src.main.funcs import log


class Data:
    """
    :type nd: int
    :type ny: int
    :type nx: int
    :type idxd1: int
    :type idxy1: int
    :type idxx1: int
    :type mark: list[bool]
    :type : list()
    :type : list()
    :type : list()
    :type : list()
    :return:
    """
    def __init__(self, parent=None):
        """
        :type self: object
        """
        self._parent = parent
        # length od fields
        self.nrows = 0
        self.nd = 0
        self.ny = 0
        self.nx = 0
        self.ncols = 2 + self.nd + self.ny + self.nx
        # index of 1st element in field
        self.idxd1 = 0
        self.idxy1 = 0
        self.idxx1 = 0
        # contend of cells
        self.mark = []
        self.ignore = []
        self.indx1 = []
        self.indx2 = []
        self.colour = []
        self.label = []
        self.descr = []
        self.yarr = np.zeros((self.nrows, self.ny), dtype=float)
        self.xarr = np.zeros((self.nrows, self.nx), dtype=float)
        self.xtreat = np.zeros((self.nrows, self.nx), dtype=float)
        # header
        self.headerd = []
        self.headery = []
        self.headerx = []
        self.header = []
        self.xvector = np.zeros(self.nx, dtype=float)

    def setRawCellVaue(self, irow: int, icol: int, valu):
        if icol == 0:
            self.mark[irow] = valu
        elif icol == 1:
            self.ignore[irow] = valu
            # self.recalculateIndx1()
        elif icol == 2:
            # self.display[irow] = valu
            pass
        elif icol == 3:
            pass
        elif icol < self.idxy1:
            self.descr[irow][icol-self.idxd1] = valu
        elif icol < self.idxx1:
            myfloat = 0.0
            try:
                myfloat =  np.float64(valu)
            except:
                myfloat = np.NaN
            self.yarr[irow, icol-self.idxy1] = myfloat

    # def recalculateIndx1(self):
    #     print('data.recalculateIndx1:')
    #     self.indx1.clear()
    #     for r in range(self.nrows):
    #         if self.ignore[r] == 0:
    #             self.indx1.append(r)
    #     self.recalculateIndx2()

    def recalculateIndx2(self):
        log('data.recalculateIndx2:' + self._parent.comboBox_select1.currentText())
        self._parent.tablemodeltreated.beginResetModel()
        colname = self._parent.comboBox_select1.currentText()
        selection = [str(x.text()) for x in self._parent.listWidget_select1.selectedItems()]

        self.indx2.clear()
        if colname == 'None':
            for r in range(self.nrows):
                if self.ignore[r] == 0:
                    self.indx2.append(r)
        elif colname == 'Row':
            for r in range(self.nrows):
                if str(r+1) in selection:
                    self.indx2.append(r)
        elif colname in self.headerd:
            idx = self.headerd.index(colname)
            for r in range(self.nrows):
                if self.descr[r][idx] in selection:
                    self.indx2.append(r)
        elif colname in self.headery:
            idx = self.headery.index(colname)
            for r in range(self.nrows):
                if '{:.1f}'.format(self.yarr[r][idx]) in selection:
                    self.indx2.append(r)

        self._parent.tablemodeltreated.endResetModel()
        # self._parent.resetColours()


    def loadSamples(self, filename: str):
        if not os.path.isfile(filename):
            return
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            datalist = list(reader)
        self.convert_list_to_data(datalist)

    def convert_list_to_data(self, datalist):
        if len(datalist) < 2:
            return
        idxm = -1
        idxi = -1
        self.idxd1 = -1
        self.idxy1 = -1
        self.idxx1 = -1
        self.headerd = []
        self.headery = []
        self.headerx = []
        hdr_ign = ''
        hdr_mark = ''

        # ---------- get header information ------------------
        hdr = datalist[0]
        i = -1
        for cll in hdr:
            i += 1
            cllparts = cll.split(sep='|')
            if len(cllparts) > 1:
                if cllparts[1].startswith('m'):
                    idxm = i
                    hdr_mark = cllparts[0]
                elif cllparts[1].startswith('i'):
                    idxi = i
                    hdr_ign = cllparts[0]
                elif cllparts[1].startswith('d'):
                    if self.idxd1 == -1:
                        self.idxd1 = i
                    self.headerd.append(cllparts[0])
                elif cllparts[1].startswith('y'):
                    if self.idxy1 == -1:
                        self.idxy1 = i
                    self.headery.append(cllparts[0])
                elif cllparts[1].startswith('x'):
                    if self.idxx1 == -1:
                        self.idxx1 = i
                    self.headerx.append(cllparts[0])

        hdrleft = ['Mark', 'Ign.', 'Colour', 'Label']
        self.header = hdrleft + self.headerd + self.headery + self.headerx
        self.xvector = np.asfarray(self.headerx)
        self.nd = len(self.headerd)
        self.ny = len(self.headery)
        self.nx = len(self.headerx)
        self.ncols = 2 + self.nd + self.ny + self.nx

        # ---------- get body information ------------------
        self.mark = []
        self.ignore = []
        self.descr = []
        # ----- first get mark, ignore and descriptions
        for iline in range(1,len(datalist)):
            line = datalist[iline]
            if len(line) >= self.ncols:
                self.mark.append(convert_str_to_0or1(line[idxm]))
                self.ignore.append(convert_str_to_0or1(line[idxi]))
                self.descr.append([line[self.idxd1+i] for i in range(self.nd)])
        self.nrows = len(self.mark)
        # ----- next get numpy array for y and x
        self.yarr = np.zeros((self.nrows, self.ny), dtype=float)
        self.xarr = np.zeros((self.nrows, self.nx), dtype=float)
        self.xtreat = np.zeros((self.nrows, self.nx), dtype=float)

        for iline in range(1,len(datalist)):
            r = iline - 1
            line = datalist[iline]
            if len(line) >= self.ncols:
                # convert y variable into float
                for i in range(self.ny):
                    try:
                        self.yarr[r, i] = np.float64(line[self.idxy1+i])
                    except:
                        self.yarr[r, i] = np.float('nan')
                # convert x variable into float
                try:
                    self.xarr[r] = np.asfarray(line[self.idxx1:self.idxx1+self.nx])
                except:
                    print('Error converting to float in line:' + str( iline))
                    for i in range(self.ny):
                        try:
                            self.xarr[r, i] = np.float64(line[self.idxx1+i])
                        except:
                            self.xarr[r, i] = np.float('nan')

        self.ncols = 4 + self.nd + self.ny + self.nx
        self.idxd1 += 2
        self.idxy1 += 2
        self.idxx1 += 2
        self.colour = [''] * self.nrows
        self.label = [''] * self.nrows

        self.xtreat = np.copy(self.xarr)
        # z = np.copy(x)
        # self.recalculateIndx1()

    def treat(self, treatment: str):
        x1 = np.copy(self.xarr)
        x2 = np.copy(self.xarr)
        if treatment == 'None':
            self.xtreat = np.copy(self.xarr)
        elif treatment == 'SNV':
            try:
                mean = np.mean(self.xtreat,axis=1)
                std = np.std(self.xtreat, axis=1)
                for r in np.arange(self.nrows):
                    self.xtreat[r] = self.xtreat[r] - mean[r]
                    self.xtreat[r] = self.xtreat[r] / std[r]
                    x2 = self.xtreat[r]
            except:
                pass
