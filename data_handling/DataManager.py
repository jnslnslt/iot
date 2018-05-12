import pandas as pd
import json
import os
import datetime

TARGET_FILE = "store.h5"

# class to represent one measurement
# values can be added to buffer to prevent continuous
# disk writing
class IO:
    def __init__(self, io, device):
        self.io = io
        self.buffer = {}
        self.filename = device + ".h5"
    # add timestamp-value pair to buffer. If buffer is larger than 10
    #  instances, write to hdfs file and clear buffer
    def addToBuffer(self, value):
        self.buffer[datetime.datetime.now().isoformat()] = value
        if len(self.buffer) >= 10:
            #save to file
            timeSeries = pd.Series(self.buffer)
            timeSeries.to_hdf(self.filename, self.io, mode='a', format='table', append=True)
            #empty buffer
            self.buffer = []

    def getCode(self):
        return self.io
            

# Class for arduino device, contains deviceId
# (which is send via rf) and 1+ IO-objects
class Device:
    def __init__(self, deviceId, deviceName):
        self.deviceId = deviceId
        self.deviceName = deviceName
        self.io = []
    
    # create IO object and add to list
    def addIO (self, io):
        self.io.append(IO(io,self.deviceName))
    
    # return IO objects
    def getIO (self):
        return self.io
    
    def getIOLength(self):
        return len(self.io)



class Devices:
    def __init__(self):
        self.devices = {}

    def readSettings(self, filename='C:/Users/janis/Documents/iot/data_handling/Settings.json'):
        try:
            jsonFile = open(filename)
            data = json.load(jsonFile)
        except FileNotFoundError:
            print("File does not exist")
        except:
            print("File reading failed")

        # loop over all device instances and save to devices-dict
        for device in data[0]["devices"]:
            d = Device(device["deviceId"], device["deviceName"])
            for io in device["IO"]:
                d.addIO(io)
            self.devices[d.deviceId] = d

        # other settings could be handled here

    # function to add values to io buffer
    # including verification and exception handling
    def saveFromSerial(self, message):
        values = message.split(" ")
        # check if message is empty
        if (values.empty()):
            return
        device = self.devices.get(values[0])
        # check if device exists in settings
        if (device == None):
            return
        # check if length of message matches device io number
        elif (len(values)-1 != device.getIOLength()):
            return
        else:
            i = 1 
            for io in device.getIO():
                try:
                    val = float(values[i])
                except ValueError:
                    val = 'nan'
                io.addToBuffer(val)
          

            
        


def main():
    dev = Devices()
    dev.readSettings()
    print("valmis")


main()