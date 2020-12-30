from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as con
import xlsxwriter
data_g = ''
import main_2
from datetime import datetime
import requests

class Ui_MainWindow(object):
    def openDash(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = main_2.Ui_MainWindow()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(814, 616)
        MainWindow.setStyleSheet("background-color: rgb(41,54,63);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 811, 601))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 814, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionget_excel = QtWidgets.QAction(MainWindow)
        self.actionget_excel.setObjectName("actionget_excel")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.menuFile.addAction(self.actionget_excel)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionexit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.conn()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.actionget_excel.triggered.connect(self.xcl)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "RFID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Latitude"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Longitude"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionget_excel.setText(_translate("MainWindow", "get excel"))
        self.actionexit.setText(_translate("MainWindow", "go back"))

    def xcl(self):
        global data_g
        try:
           
            name = str(datetime.now())
            name = name.split('.')
            print(name)
            name = name[0][0:10]+' '+name[0][11:13]+'-'+name[0][14:16]+'-'+name[0][17:19]+'.xlsx'
            print(name)
            workbook = xlsxwriter.Workbook(name) 
            worksheet = workbook.add_worksheet()
            for i in range(len(data_g)-1):
                worksheet.write(i, 0, (str(data_g[i][0])))
                worksheet.write(i, 1, (str(data_g[i][1])))
                worksheet.write(i, 2, (str(data_g[i][2])))
                worksheet.write(i, 3, (str(data_g[i][3])))
            workbook.close()
        except Exception as e:
            print(e)

    def conn(self):
        global data_g
        try:
            url = "http://dptestparth.000webhostapp.com/query_get.php?query=select * from rfid_data"
            r = requests.get(url)
            data = r.content
            data = str(data)
            data = data.strip('b\'')
            data = data.split('<br>')
            d= []
            
            for i in range(len(data)):
                d.append(data[i].split(','))
            data = d
            data_g = d
            self.tableWidget.setStyleSheet("color:gray;")
            self.tableWidget.setEnabled(False)
            self.tableWidget.setRowCount(len(data))
            print(data)
            for i in range(len(data)-1):
                 self.tableWidget.setItem(i,0, QtWidgets.QTableWidgetItem(str(data[i][1])))
                 self.tableWidget.setItem(i,1, QtWidgets.QTableWidgetItem(str(data[i][0])))
                 self.tableWidget.setItem(i,2, QtWidgets.QTableWidgetItem(str(data[i][2])))
                 self.tableWidget.setItem(i,3, QtWidgets.QTableWidgetItem(str(data[i][3])))
        except Exception as e:
            print(e)
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
