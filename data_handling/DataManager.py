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
        self.buffer[pd.Timestamp.now()] = value
        if len(self.buffer) >= 10:
            #save to file
            timeSeries = pd.Series(self.buffer)
            print("filename: ", self.filename)
            timeSeries.to_hdf(self.filename, self.io, mode='a', format='table', append=True)
            #empty buffer
            self.buffer = {}

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



class DataManager:
    def __init__(self):
        self.devices = {}

    def readSettings(self, filename='Settings.json'):
        try:
            jsonFile = open(filename)
            data = json.load(jsonFile)
        #except FileNotFoundError:
        #    print("File does not exist")
        #    return
        except:
            print("File reading failed")
            return
        # loop over all device instances and save to devices-dict
        for device in data[0]["devices"]:
            d = Device(device["deviceId"], device["deviceName"])
            for io in device["IO"]:
                d.addIO(io["M"])
            self.devices[d.deviceId] = d

        jsonFile.close()

        # other settings could be handled here

    # function to add values to io buffer
    # including verification and exception handling
    def saveFromSerial(self, message):
        values = message.split(" ")
        # check if message is empty
        if (not values):
            print("empty message") #debug
            return
        device = self.devices.get(values[0])
        # check if device exists in settings
        if (device == None):
            print("device ", values[0], " not found") #debug
            return
        # check if length of message matches device io number
        elif (len(values)-1 < device.getIOLength()):
            print("message length does not match") #debug
            return
        else:
            i = 1 
            for io in device.getIO():
                try:
                    val = float(values[i])
                except ValueError:
                    val = 'nan'
                io.addToBuffer(val)
                i = i + 1
          
