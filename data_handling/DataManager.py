#import pandas as pd
import json
import os

# class to represent one measurement
# values can be added to buffer to prevent continuous
# disk writing
class IO:
    def __init__(self, io):
        self.io = io
        self.buffer = []
    def addToBuffer(
        self, value):
        self.buffer.append(value)
        if len(self.buffer) > 10:
            #todo
            #save to file
            #empty buffer
            pass

# Class for arduino device, contains deviceId
# (which is send via rf) and 1+ IO-objects
class Device:
    def __init__(self, deviceId):
        self.deviceId = deviceId
        self.io = []
    
    # create IO object and add to list
    def addIO (self, io):
        self.io.append(IO(io))
    
    # return IO object
    def getIO (self):
        return self.io



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
            print(d.deviceId)
            print(d.getIO())
        

        # other settings could be handled here

    def saveFromSerial(self, message):
        measureList = message.split(" ")
        IOList = self.devices.get(measureList[0]).getIO()
        i = 1
        for io in IOList:
            # todo: error handling/verification
            io.addToBuffer(measureList[i])





def main():
    dev = Devices()
    dev.readSettings()
    print("valmis")


main()