import serial
import DataManager


ser = serial.Serial('/dev/ttyACM0', 9600)
manager = DataManager.DataManager()
manager.readSettings()
i = 0

while True:
    line = ser.readline()
    print(line)
    manager.saveFromSerial(line)