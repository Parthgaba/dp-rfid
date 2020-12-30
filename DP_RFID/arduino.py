import serial as ser
baudrate = 9600
port = 'COM6' 
msg = 'hello'
serial_ = ser.Serial(port=port, baudrate=baudrate)
print(serial_.is_open)
if serial_.is_open:
    while True:
        data = serial_.read(40)
        print((data))
           
    else:
        print('no data')
else:
    print('serial not open')
ser.write(msg)


    
        
    def store(self,MainWindow):
        name = self.lineEdit.text()
        rfid = self.lineEdit_2.text()
        db = open("db.csv","r")
        data =db.read()
        db.close()
        db = open("db.csv","w")
        db.write(data+'\n'+rfid+','+name)
        db.close()

    def serial_writer_reader(self):

        while True:
            if serial_.is_open:
                while True:
                    data = serial_.read(40)
                    print((data))
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
        if rf[1] in db_data:
            ind = db_data.index(rf[1])
            print("here is my file bhaiyaaa",lis2[ind][1])
        ser.write(lis2[ind][1])

    def getfile(self):
      fname = QFileDialog.getOpenFileName(self, 'Open file', 
         'c:\\',"Image files (*.jpg *.gif)")
      self.le.setPixmap(QPixmap(fname))
		
    def getfiles(self):
      dlg = QFileDialog()
      dlg.setFileMode(QFileDialog.AnyFile)
      dlg.setFilter("Text files (*.txt)")
      filenames = QStringList()
		
      if dlg.exec_():
         filenames = dlg.selectedFiles()
         f = open(filenames[0], 'r')
			
         with f:
            data = f.read()
            self.contents.setText(data)
                    
