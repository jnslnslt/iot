import unittest
import DataManager
import pandas as pd

class TestDataManager(unittest.TestCase):

    def setUp(self):
        self.manager = DataManager.Devices()
        self.manager.readSettings('C:/Users/janis/Documents/iot/data_handling/testSettings.json')

    
    def test_readSettings(self):
        device1 = self.manager.devices.get("100")
        self.assertNotEquals(device1, None, "Device 1 not found")
        IOs = device1.getIO()
        self.assertEquals(IOs[0].getCode(), "val1")
        

    def test_saveFromSerial(self):
        for i in range(0,20):
            self.manager.saveFromSerial("100 10.00 nan")
        result = pd.read_hdf('TestName.h5', 'val1')
        self.assertEquals(result[0], 10)


if __name__ == '__main__':
    unittest.main()