#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QMessageBox, QDesktopWidget)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication 


class Example(QWidget):

	def __init__(self):	
		super().__init__()
		self.initUI()
			
# функция super возвращает родительский объект Example
# с классом

	def initUI(self):
		QToolTip.setFont(QFont('SansSerif', 10))
		
		
		btn = QPushButton('Exit', self)
		btn.clicked.connect(QCoreApplication.instance().quit)
		btn.setToolTip('Fuck <b>Socity</b>')
		
		btn.resize(btn.sizeHint())
		btn.move(125, 125)
		
		self.resize(300,300)
		self.center()
		
		self.setWindowTitle('Tooltips')
		self.setWindowIcon(QIcon('icon.png'))
        
		self.show()
		
	def center(self):
	
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	
	def closeEvent(self, event):
	
		replay = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox. No)
		
		if replay == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())