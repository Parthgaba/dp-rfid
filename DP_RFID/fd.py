import serial

with serial.Serial(port = 'COM6',baudrate = 9600) as ser:
    ser.baudrate = 9600
    ser.port = 'COM6'
  
    ser.write(b'hello')
