import serial
import DataManager
import pandas as pd

ser = serial.Serial('/dev/ttyACM0', 9600)
manager = DataManager.DataManager()
manager.readSettings()
i = 0

while True:
    line = ser.readline()
    print(line)
    manager.saveFromSerial(line)
    i +=1
    if i >= 100:
	val = pd.read_hdf('Arduino1 - tempMeasure.h5', 'T01')
	print(val)
	val = pd.read_hdf('Arduino1 - tempMeasure.h5', 'T02')
	print(val)
	val = pd.read_hdf('Arduino1 - tempMeasure.h5', 'H01')
	print(val)
	i = 0
	
