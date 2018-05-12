import unittest
import DataManager
import pandas as pd

class TestDataManager(unittest.TestCase):

    def setUp(self):
        self.manager = DataManager.Devices()
    
    def test_readSettings(self):
        self.manager.readSettings('C:/Users/janis/Documents/iot/data_handling/testSettings.json')
        device1 = self.manager.devices.get("100")
        self.assertNotEquals(device1, None, "Device 1 not found")
        IOs = device1.getIO()
        self.assertEquals(IOs[0].getCode(), "val1")
        

    def test_saveFromSerial(self):
        self.manager.saveFromSerial("888001 10.00 32.00 nan")
        #result = pd.read_hdf('')


if __name__ == '__main__':
    unittest.main()