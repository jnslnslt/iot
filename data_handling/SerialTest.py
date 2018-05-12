import serial
import pandas as pd
import datetime

#store = pd.HDFStore('store.h5')
#store['s'] = pd.Series()#(0, index=datetime.datetime.now().isoformat())

dict = {}

ser = serial.Serial('/dev/ttyACM0',9600)
s = [0]
i = 0


while True:
    i = i + 1
    read_serial = ser.readline()
    print(read_serial)
    str = read_serial.split(" ")
    dict[datetime.datetime.now().isoformat()] = str[0]
    if i > 10:
        i = 0
        timeseries = pd.Series(dict)
        #timeseries.to_hdf('store.h5', 'table', append=True)
	timeseries.to_hdf('test.h5', 'temp1', mode='a', format='table', append=True)
        dict = {}
	#print(pd.read_hdf('store.h5', 'table'))
	print("")
	print(pd.read_hdf('test.h5', 'temp1'))