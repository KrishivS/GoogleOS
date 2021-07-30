from PyQt5.QtWebEngineWidgets import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(331, 586)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

app = QApplication(sys.argv)
QApplication.setApplicationName('Google')
window = MainWindow()
app.exec_()
