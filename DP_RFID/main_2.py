from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
import mysql.connector as con
import shutil
import database
import requests
import serial as ser
import threading
import serial.tools.list_ports


comlist = serial.tools.list_ports.comports()
connected = []
for element in comlist:
    connected.append(element.device)
class Ui_MainWindow(object):
    
    def openDash(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = database.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(965, 683)
        font = QtGui.QFont()
        font.setFamily("Meiryo")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background:rgb(41,54,63)\n")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.left = QtWidgets.QFrame(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(-1, -1, 291, 711))
        self.left.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.left.setStyleSheet("background :rgb(98, 221, 154);\n")
        self.left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left.setObjectName("left")
        self.textEdit = QtWidgets.QTextEdit(self.left)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 291, 741))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color:white")
        self.textEdit.setReadOnly(True)
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 10, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 80, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 150, 48, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(350, 420, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(340, 210, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(460, 260, 272, 40))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(460, 320, 272, 40))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(460, 80, 272, 40))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(460, 140, 272, 40))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(465, 85, 261, 31))
        self.lineEdit.setStyleSheet("border:none;color:white;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(465, 145, 261, 31))
        self.lineEdit_2.setStyleSheet("border:none;color:white;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(465, 265, 261, 31))
        self.lineEdit_3.setStyleSheet("border:none;color:white;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(465, 325, 261, 31))
        self.lineEdit_4.setStyleSheet("border:none;color:white;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(670, 210, 47, 13))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(340, 270, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(340, 330, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 410, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(590, 420, 47, 13))
        self.label_13.setObjectName("label_13")
        self.label_13.setStyleSheet("color:white;")
        self.label_13.clear()
        self.label_13.setText("no image selected")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(350, 510, 151, 31))
        self.lineEdit_5.setStyleSheet("border:none;color:white;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(460, 200, 272, 40))
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(470, 210, 241, 21))
        self.lineEdit_6.setStyleSheet("border:none;")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setStyleSheet("border:none;color:white;")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(860, 600, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 965, 21))
        self.menubar.setObjectName("menubar")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(350, 510, 151, 31))
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 510, 151, 31))
        self.pushButton_3.setStyleSheet("background-color: rgba(255, 0, 0, 0);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setMenuBar(self.menubar)
        textentry = QPixmap("textedit_entry.png")
        self.label_6.setPixmap(textentry)
        self.label_7.setPixmap(textentry)
        self.label_8.setPixmap(textentry)
        self.label_9.setPixmap(textentry)
        self.label_9.setPixmap(textentry)
        #self.label_15.setPixmap(textentry)
        dashbutton = QPixmap("dash.png")
        self.label_14.setPixmap(dashbutton)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.textEdit.append("started app...")
        self.pushButton_3.clicked.connect(self.conn)
        self.pushButton.setStyleSheet("color:white;")
        self.pushButton_2.setStyleSheet("color:white;")
        self.pushButton.clicked.connect(self.openFile)
        self.pushButton_2.clicked.connect(self.openDash)
        t = threading.Thread(target=self.serial_read)
        t.start()
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Delhi Police RFID</span></p><p><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Name</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">RFID</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Image</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">location</span></p><p><br/></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">latitude</span></p><p><br/></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">longitude</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "image"))
        self.label_13.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "database"))

    def store(self):
        global im
        try: 
            shutil.copyfile(src=im, dst='C:/Users/Parth/Desktop/DP_RFID/images/'+self.lineEdit_2.text()+'.png') 
            print("File copied successfully.") 
        except shutil.SameFileError: 
            print("Source and destination represents the same file.")
        except IsADirectoryError: 
            print("Destination is a directory.") 
        except PermissionError: 
            print("Permission denied.") 
        except Exception as e: 
            print("Error occurred while copying file.",e) 
        self.textEdit.append('written succesfully')


    def conn(self):
        self.textEdit.append("trying to connect with the database...")
        if self.lineEdit.text()=='' or self.lineEdit_2.text()=='' or self.lineEdit_3.text()=='' or self.lineEdit_4.text()=='':
            self.textEdit.append('cannot accept your request, first fill all the arguements required!!!')
            return
        
        if not (self.lineEdit_2.text().isnumeric()):
            self.textEdit.append('You cannot enter any character value in rfid field')
            return
        
        if (self.lineEdit_3.text().isnumeric()):
            self.textEdit.append('You can enter decimal value in latitude field')
            return

        if (self.lineEdit_4.text().isnumeric()):
            self.textEdit.append('You can enter decimal value in longitude field')
            return

        try:
            url = "http://dptestparth.000webhostapp.com/insert.php"
            query = "insert into rfid_data values("+self.lineEdit_2.text()+",\""+self.lineEdit.text()+"\","+self.lineEdit_3.text()+","+self.lineEdit_4.text()+");"
            PARAMS = {'query':query}
            r = requests.get(url,params=PARAMS)
            data = r.content
            self.store()
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.textEdit.append("new entry written")
            
        except Exception as e:
            print(e)
            error = e
    def serial_read(self):
        new = ''
        
        
        while True:
            try:
                serial_ = ser.Serial(port='COM4',baudrate=9600)
                print(serial_)
                if serial_.is_open:
                    if self.lineEdit_2.text()=="":
                        while True:
                            data = str(serial_.read(14))
                            print('data',data)
                            if data=="":
                                continue
                            self.textEdit.append('data retrieving... '+str(data))
                            new = data.split('\'')
                            self.lineEdit_2.setText(str(new[1][:10]))
                            serial_.close()
                            break
                        else:
                            print('no data')
                serial_.close()
            except Exception as e:
                print(e)

        
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
