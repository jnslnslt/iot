#import pandas as pd
import json
import os

TARGET_FILE = "store.h5"

# class to represent one measurement
# values can be added to buffer to prevent continuous
# disk writing
class IO:
    def __init__(self, io):
        self.io = io
        self.buffer = []
    def addToBuffer(self, value):
        self.buffer.append(value)
        if len(self.buffer) > 10:
            #todo
            #save to file
            #timeSeries = pd.Serial(self.buffer)
            #timeSeries.to_hdf('store.h5', 'table')
            #empty buffer
            self.buffer = []
            

# Class for arduino device, contains deviceId
# (which is send via rf) and 1+ IO-objects
class Device:
    def __init__(self, deviceId):
        self.deviceId = deviceId
        self.io = []
    
    # create IO object and add to list
    def addIO (self, io):
        self.io.append(IO(io))
    
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
            d = Device(device["deviceId"])
            for io in device["IO"]:
                d.addIO(io)
            self.devices[d.deviceId] = d

        # other settings could be handled here

    # function to add values to io buffer
    # including verification and exception handling
    def saveFromSerial(self, message):
        values = message.split("")
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