import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://drive.google.com/drive/u/0/my-drive'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

app = QApplication(sys.argv)
QApplication.setApplicationName('Drive')
window = MainWindow()
app.exec_()
