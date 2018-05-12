import unittest
import DataManager
import pandas as pd

class TestDataManager(unittest.TestCase):

    def setUp(self):
        self.manager = DataManager.Devices()
    
    def test_readSettings(self):
        pass
    
    def test_saveFromSerial(self):
        pass


if __name__ == '__main__':
    unittest.main()