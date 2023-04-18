#!/bin/env/python3
import sys
from PyQt5.QtWidgets import QApplication
from gui.mainwindow import MyHealthCareBot
import qdarkstyle

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MyHealthCareBot()
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
	window.show()
	sys.exit(app.exec_())
