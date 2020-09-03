import matplotlib.pyplot as plt  # plotting
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from matplotlib.pyplot import figure
import numpy as np  # linear algebra
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    data = pd.read_csv('weblog.csv')
    abnormalData = data
    normalData = data

    # removing unnecessary data
    normalData = normalData[normalData.IP != '[Mon']
    normalData = normalData[normalData.IP != '[Tue']
    normalData = normalData[normalData.IP != '[Wed']
    normalData = normalData[normalData.IP != '[Thu']
    normalData = normalData[normalData.IP != '[Fri']
    normalData = normalData[normalData.IP != '[Sat']
    normalData = normalData[normalData.IP != 'chmod:']
    normalData = normalData[normalData.IP != 'rm:']
    normalData = normalData[normalData.IP != 'sh:']
    normalData = normalData[normalData.IP != 'timeout:']
    normalData = normalData[normalData.IP != 'a.out:']

    # storing unnecessary data
    abnormalData = abnormalData[abnormalData.IP != '10.128.2.1']
    abnormalData = abnormalData[abnormalData.IP != '10.131.0.1']
    abnormalData = abnormalData[abnormalData.IP != '10.130.2.1']
    abnormalData = abnormalData[abnormalData.IP != '10.129.2.1']
    abnormalData = abnormalData[abnormalData.IP != '10.131.2.1']

    pro = data['Protocol'].value_counts()
    urlcom = normalData['URL'].value_counts()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1014, 485)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.abnormalMethodDistribution = QtWidgets.QPushButton(self.centralwidget)
        self.abnormalMethodDistribution.setGeometry(QtCore.QRect(260, 320, 221, 71))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.abnormalMethodDistribution.setFont(font)
        self.abnormalMethodDistribution.setObjectName("abnormalMethodDistribution")
        self.abnormalMethodDistribution.clicked.connect(lambda : self.abMethodDistribution())

        self.abnormalUrlDistribution = QtWidgets.QPushButton(self.centralwidget)
        self.abnormalUrlDistribution.setGeometry(QtCore.QRect(490, 320, 243, 71))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.abnormalUrlDistribution.setFont(font)
        self.abnormalUrlDistribution.setObjectName("abnormalUrlDistribution")
        self.abnormalUrlDistribution.clicked.connect(lambda : self.abUrlDistribution())

        self.abnormalTimeDistribution = QtWidgets.QPushButton(self.centralwidget)
        self.abnormalTimeDistribution.setGeometry(QtCore.QRect(740, 320, 251, 71))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.abnormalTimeDistribution.setFont(font)
        self.abnormalTimeDistribution.setObjectName("abnormalTimeDistribution")
        self.abnormalTimeDistribution.clicked.connect(lambda : self.abTimeDistribution())

        self.abnormalIpDistribution = QtWidgets.QPushButton(self.centralwidget)
        self.abnormalIpDistribution.setGeometry(QtCore.QRect(30, 318, 221, 71))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.abnormalIpDistribution.setFont(font)
        self.abnormalIpDistribution.setObjectName("abnormalIpDistribution")
        self.abnormalIpDistribution.clicked.connect(lambda : self.abIpDistribution())

        self.overallIpDistribution = QtWidgets.QPushButton(self.centralwidget)
        self.overallIpDistribution.setGeometry(QtCore.QRect(31, 246, 221, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.overallIpDistribution.setFont(font)
        self.overallIpDistribution.setObjectName("overallIpDistribution")
        self.overallIpDistribution.clicked.connect(lambda: self.oIpDisrtibution())

        self.normalIpDistribution = QtWidgets.QPushButton(self.centralwidget)
        self.normalIpDistribution.setGeometry(QtCore.QRect(740, 250, 251, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.normalIpDistribution.setFont(font)
        self.normalIpDistribution.setObjectName("normalIpDistribution")
        self.normalIpDistribution.clicked.connect(lambda: self.nIpDistribution())

        self.normalResponseDistriburion = QtWidgets.QPushButton(self.centralwidget)
        self.normalResponseDistriburion.setGeometry(QtCore.QRect(490, 250, 241, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.normalResponseDistriburion.setFont(font)
        self.normalResponseDistriburion.setObjectName("normalResponseDistriburion")
        self.normalResponseDistriburion.clicked.connect(lambda: self.nResponseDistribution())

        self.overallMethodDistribution = QtWidgets.QPushButton(self.centralwidget)
        self.overallMethodDistribution.setGeometry(QtCore.QRect(260, 250, 221, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.overallMethodDistribution.setFont(font)
        self.overallMethodDistribution.setObjectName("overallMethodDistribution")
        self.overallMethodDistribution.clicked.connect(lambda: self.oMethodDistribution())

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1014, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weblog Dataset"))
        self.abnormalMethodDistribution.setText(_translate("MainWindow", "Abnormal Method Distribution"))
        self.abnormalUrlDistribution.setText(_translate("MainWindow", "Abnormal Url Distribution"))
        self.abnormalTimeDistribution.setText(_translate("MainWindow", "Abnormal Time Distribution"))
        self.abnormalIpDistribution.setText(_translate("MainWindow", "Abnormal IP Distribution"))
        self.overallIpDistribution.setText(_translate("MainWindow", "Overall IP Distribution"))
        self.normalIpDistribution.setText(_translate("MainWindow", "Normal IP Distribution"))
        self.normalResponseDistriburion.setText(_translate("MainWindow", "Normal Response Distribution"))
        self.overallMethodDistribution.setText(_translate("MainWindow", "Overall Method Distribution"))

    def oIpDisrtibution(self):
        ip = self.data['IP'].value_counts()
        quality = ip.keys().tolist()
        y_pos = np.arange(len(quality))
        quantity = ip.tolist()

        plt.bar(y_pos, quantity, align='center', alpha=0.5)
        plt.xticks(y_pos, quality)
        plt.xlabel('IP Type', fontsize=14)
        plt.ylabel('No. of IPs', fontsize=14)
        plt.xticks(rotation=45)
        plt.title('Overall IP Distribution', fontsize=16)
        plt.show()

    def oMethodDistribution(self):
        md = self.data['Method'].value_counts()  # useful
        quality = md.keys().tolist()
        y_pos = np.arange(len(quality))
        quantity = md.tolist()

        plt.bar(y_pos, quantity, align='center', alpha=0.5)
        plt.xticks(y_pos, quality)
        plt.xlabel('Method Type', fontsize=14)
        plt.ylabel('No. of Methodss', fontsize=14)
        plt.xticks(rotation=90)
        plt.title('Overall Method Distribution', fontsize=16)
        plt.show()

    def nIpDistribution(self):
        ipcom = self.normalData['IP'].value_counts()  # useful
        # Data to plot Normal IP Distribution
        labels = ipcom.keys().tolist()
        sizes = ipcom.tolist()
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red']
        explode = (0.1, 0.1, 0.1, 0.1, 0.1)  # explode 1st slice

        # Plot
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=60)
        plt.title('Normal IP Distribution', fontsize=18)
        plt.axis('equal')
        plt.show()

    def nResponseDistribution(self):
        rescom = self.normalData['Response'].value_counts()
        # Data to plot
        labels = rescom.keys().tolist()
        sizes = rescom.tolist()
        colors = ['violet', 'blueviolet', 'green', 'yellow', 'orange']
        explode = (0.075, 0.1, 0.2, 0.3, 0.4)  # explode 1st slice

        # Plot
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=180)
        plt.title('Normal Response Distribution', fontsize=18)
        plt.axis('equal')
        plt.gcf().set_size_inches(6, 6)
        plt.show()

    def abMethodDistribution(self):
        mduni = self.abnormalData['Method'].value_counts()
        quality = mduni.keys().tolist()
        y_pos = np.arange(len(quality))
        quantity = mduni.tolist()

        plt.bar(y_pos, quantity, align='center', alpha=0.5)
        plt.xticks(y_pos, quality)
        plt.xlabel('Method Type', fontsize=14)
        plt.ylabel('No. of Requests', fontsize=14)
        plt.xticks(rotation=90)
        plt.title('Abnormal Method Distribution', fontsize=16)
        plt.show()

    def abTimeDistribution(self):
        timeuni = self.abnormalData['Time'].value_counts()  # useful
        quality = timeuni.keys().tolist()
        y_pos = np.arange(len(quality))
        quantity = timeuni.tolist()

        plt.bar(y_pos, quantity, align='center', alpha=0.5)
        plt.xticks(y_pos, quality)
        plt.xlabel('Time Type', fontsize=14)
        plt.ylabel('No. of Requests', fontsize=14)
        plt.xticks(rotation=90)
        plt.title('Abnormal Time Distribution', fontsize=16)
        plt.show()

    def abUrlDistribution(self):
        urluni = self.abnormalData['URL'].value_counts()  # useful
        # Data to plot Abormal IP Distribution
        labels = urluni.keys().tolist()
        sizes = urluni.tolist()
        colors = ['gold', 'yellowgreen', 'blueviolet', 'lightskyblue', 'r', 'g', 'b', 'c']
        explode = (0.05, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6)  # explode 1st slice

        # Plot
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=180)
        plt.title('Abormal URL Distribution', fontsize=18)
        plt.axis('equal')
        plt.gcf().set_size_inches(6, 6)
        plt.show()

    def abIpDistribution(self):
        ipuni = self.abnormalData['IP'].value_counts()  # useful
        # Data to plot Abormal IP Distribution
        labels = ipuni.keys().tolist()
        sizes = ipuni.tolist()
        colors = ['gold', 'yellowgreen', 'blueviolet', 'lightskyblue', 'r', 'g', 'b', 'c', 'm', 'y', 'tomato']
        explode = (0.05, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5)  # explode 1st slice

        # Plot
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=180)
        plt.title('Abormal IP Distribution', fontsize=18)

        plt.axis('equal')
        plt.gcf().set_size_inches(6, 6)
        plt.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
