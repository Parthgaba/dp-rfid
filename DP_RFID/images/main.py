from PyQt5 import QtCore, QtGui, QtWidgets
from serial import Serial as ser
import numpy as np
import threading
import shutil
import time
import random

serial_ = ser(port='COM6',baudrate=9600)
im = ''
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(949, 688)
        MainWindow.setStyleSheet("background:rgb(47, 47, 47)\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.left = QtWidgets.QFrame(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(-1, -1, 241, 661))
        self.left.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.left.setStyleSheet("background :rgb(70, 70, 212)\n"
"")
        self.left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left.setObjectName("left")
        self.textEdit = QtWidgets.QTextEdit(self.left)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 241, 651))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 10, 541, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 70, 48, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 110, 48, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(370, 70, 133, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(370, 110, 133, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 480, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 160, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 160, 47, 13))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 949, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.store)
        self.pushButton_2.clicked.connect(self.openFile)
        t = threading.Thread(target=self.serial_writer_reader)
        t.start()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.textEdit.setReadOnly(True)
        self.textEdit.append('started')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Some Kind of text will go here about this software</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Name</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">RFID</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "ENTER "))
        self.pushButton_2.setText(_translate("MainWindow", "getImage"))
        self.label_4.setText(_translate("MainWindow", "Image"))
        self.textEdit.append('connecting...')
    
        
    def store(self,MainWindow):
        global im
        name = self.lineEdit.text()
        rfid = self.lineEdit_2.text()
        db = open("db.csv","r")
        self.textEdit.append('connecting with database...')
        data =db.read()
        db.close()
        db = open("db.csv","w")
        db.write(data+'\n'+rfid+','+name)
        self.textEdit.append('writing in database...')
        db.close()
        print(im)
        try: 
            shutil.copyfile(src=im, dst='C:/Users/Parth/Desktop/DP_RFID/images'+rfid+'.png') 
            print("File copied successfully.") 
        except shutil.SameFileError: 
            print("Source and destination represents the same file.")
        except IsADirectoryError: 
            print("Destination is a directory.") 
        except PermissionError: 
            print("Permission denied.") 
        except Exception as e: 
            print("Error occurred while copying file.",e) 
        

    def serial_writer_reader(self):

        while True:
            if serial_.is_open:
                while True:
                    data = serial_.read(33)
                    self.textEdit.append('data retrieving... '+str(data))
                    self.send_db(data)
                    break
                else:
                    print('no data')
            else:
                print('serial not open')

    def send_db(self,com):
        db = open("db.csv","r")
        data = db.read()
        
        lis = data.split("\n")
        
        lis2 = []
        for i in lis:
            lis2.append(i.split(','))
        db_data = []
        
        for i in lis2:
            db_data.append(i[0])
        
        com_data = str(com).split(',')
        rf = com_data[0].split('\'')
        print('com',rf[1])
        self.textEdit.append('RFID... '+rf[1])
        if rf[1] in db_data:
            ind = db_data.index(rf[1])
            self.textEdit.append('sending details... '+lis2[ind][1])
            print("here is my file bhaiyaaa",lis2[ind][1])
            ser.write(serial_,data=lis2[ind][1].encode())

    def openFile(self):
        global im
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        f,_ = QtWidgets.QFileDialog.getOpenFileName()
        im=f
        print(im)
                    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
