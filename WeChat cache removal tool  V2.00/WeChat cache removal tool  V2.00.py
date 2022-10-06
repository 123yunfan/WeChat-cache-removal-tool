import sys
from PyQt5 import QtWidgets
import win

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindows = QtWidgets.QMainWindow()

    ui = win.Ui_MainWindow()
    ui.setupUi(MainWindows)


    MainWindows.show()
    sys.exit(app.exec_())