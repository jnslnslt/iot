#import pandas as pd
import json
import os

class device:
    def __init__(self, deviceId):
        self.deviceId = deviceId
        self.io = []
    
    def addIO (self, io):
        self.io.append(io)



class Devices:
    def __init__(self):
        pass

    def readSettings(self, filename='C:/Users/janis/Documents/iot/data_handling/Settings.json'):
        jsonFile = open(filename)
        data = json.load(jsonFile)

        for device in data[0]["devices"]:
            print(device["deviceId"])


def main():
    dev = Devices()
    dev.readSettings()
    print("valmis")


main()