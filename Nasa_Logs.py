import matplotlib.pyplot as plt  # plotting
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np  # linear algebra
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    data = pd.read_csv('data.csv', delimiter=',')
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))



        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(30, 180, 561, 91))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        self.url = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.url.setFont(font)
        self.url.setObjectName("url")
        self.url.clicked.connect(lambda: self.urlDistribution())

        self.method = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.method.setFont(font)
        self.method.setObjectName("method")
        self.method.clicked.connect(lambda: self.metnodDistribution())

        self.Responce = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.Responce.setFont(font)
        self.Responce.setObjectName("Responce")
        self.Responce.clicked.connect(lambda: self.responseDistribution())

        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(30, 300, 561, 101))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")

        self.ResVsMed = QtWidgets.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.ResVsMed.setFont(font)
        self.ResVsMed.setObjectName("ResVsMed")
        self.ResVsMed.clicked.connect(lambda: self.responseVsMethod())

        self.MetVsUrl = QtWidgets.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.MetVsUrl.setFont(font)
        self.MetVsUrl.setObjectName("MetVsUrl")
        self.MetVsUrl.clicked.connect(lambda: self.methodVsUrl())

        self.ResVsUrl = QtWidgets.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.ResVsUrl.setFont(font)
        self.ResVsUrl.setObjectName("ResVsUrl")
        self.ResVsUrl.clicked.connect(lambda: self.responseVsUrl())

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nasa Logs"))
        self.url.setText(_translate("MainWindow", "URL Distribution"))
        self.method.setText(_translate("MainWindow", "Method Distribution"))
        self.Responce.setText(_translate("MainWindow", "Responce Distribution"))
        self.ResVsMed.setText(_translate("MainWindow", "Responce Vs Methods"))
        self.MetVsUrl.setText(_translate("MainWindow", "Method Vs Url"))
        self.ResVsUrl.setText(_translate("MainWindow", "Responce Vs Url"))

    def metnodDistribution(self):
        md = self.data['method'].value_counts()  # useful
        quality = md.keys().tolist()
        y_pos = np.arange(len(quality))
        quantity = md.tolist()

        plt.bar(y_pos, quantity, align='center', alpha=0.5)
        plt.xticks(y_pos, quality)
        plt.xlabel('Method Type', fontsize=14)
        plt.ylabel('No. of Methods', fontsize=14)
        plt.xticks(rotation=90)
        plt.title('Method Distribution', fontsize=16)
        plt.gcf().set_size_inches(5, 15)
        plt.show()

    def urlDistribution(self):
        url = self.data['url'].value_counts()  # useful
        quality = url.keys().tolist()
        y_pos = np.arange(len(quality))
        quantity = url.tolist()

        plt.bar(y_pos, quantity, align='center', alpha=0.5)
        plt.xticks(y_pos, quality)
        plt.xlabel('URL Type', fontsize=14)
        plt.ylabel('No. of Urls', fontsize=14)
        plt.xticks(rotation=90)
        plt.title('Url Distribution', fontsize=16)
        plt.gcf().set_size_inches(75, 15)
        plt.show()

    def responseDistribution(self):
        res = self.data['response'].value_counts()
        quality = res.keys().tolist()
        y_pos = np.arange(len(quality))
        quantity = res.tolist()

        plt.bar(y_pos, quantity, align='center', alpha=0.5)
        plt.xticks(y_pos, quality)
        plt.xlabel('Response Type', fontsize=14)
        plt.ylabel('No. of Respones', fontsize=14)
        plt.title('Response Distribution', fontsize=16)
        plt.gcf().set_size_inches(5, 15)
        plt.show()

    def responseVsMethod(self):
        plt.scatter(self.data['response'], self.data['method'], color='green')
        plt.title('Response Vs Method', fontsize=14)
        plt.xlabel('Response', fontsize=14)
        plt.ylabel('Method', fontsize=14)
        plt.grid(True)
        plt.show()

    def responseVsUrl(self):
        plt.scatter(self.data['response'], self.data['url'], color='green')
        plt.title('Responce Vs Url', fontsize=16)
        plt.ylabel('Url', fontsize=16)
        plt.xlabel('Responce', fontsize=16)
        plt.xticks(rotation=90)
        plt.grid(True)
        plt.gcf().set_size_inches(5, 100)
        plt.show()

    def methodVsUrl(self):
        plt.scatter(self.data['method'], self.data['url'], color='red')
        plt.title('Method vs Url', fontsize=14)
        plt.xlabel('Method', fontsize=14)
        plt.ylabel('url', fontsize=14)
        plt.xticks(rotation=90)
        plt.grid(True)
        plt.gcf().set_size_inches(2, 100)
        plt.show()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
