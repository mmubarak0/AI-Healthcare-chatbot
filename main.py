#!/bin/env/python3
import sys
from PyQt5.QtWidgets import QApplication
from gui.mainwindow import MyHealthCareBot

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyHealthCareBot()
    window.show()
    sys.exit(app.exec_())
