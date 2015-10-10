import sys
from PyQt4 import QtGui
from src.main import mainprogram


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWindow = mainprogram.MyMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
