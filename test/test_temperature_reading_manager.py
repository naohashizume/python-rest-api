#
# Authors: Matt Harrison, Nao Hashizume, Set 2B
#
# test_temperature_reading_manager.py
#

from manager.temperature_reading_manager import TemperatureReadingManager
from readings.temperature_reading import TemperatureReading

from unittest import TestCase
import inspect
import csv

from unittest.mock import MagicMock
from unittest.mock import patch, mock_open

class TestTemperatureReadingManager(TestCase):
    """ Unit Tests for the Temperature Reading Manager Class """

    TEST_TEMP_READINGS = [
        ["2018-09-23 19:56:01.345", "1", "ABC Sensor Temp M301A", "20.152", "21.367", "22.005", "OK"],
        ["2018-09-23 19:57:02.321", "2", "ABC Sensor Temp M301A", "20.163", "21.435", "22.103", "OK"],
        ["2018-09-23 19:58:01.324", "3", "ABC Sensor Temp M301A", "20.142", "21.528", "21.803", "OK"],
        ["2018-09-23 19:59:03.873", "4", "ABC Sensor Temp M301A", "20.212", "21.641", "22.017", "OK"],
        ["2018-09-23 20:00:01.453", "5", "ABC Sensor Temp M301A", "100.000", "100.000", "100.000", "HIGH_TEMP"],
        ["2018-09-23 20:01:01.111", "6", "ABC Sensor Temp M301A", "21.244", "21.355", "22.103", "OK"],
        ["2018-09-23 20:02:02.324", "7", "ABC Sensor Temp M301A", "21.112", "22.345", "22.703", "OK"],
        ["2018-09-23 20:03:02.744", "8", "ABC Sensor Temp M301A", "20.513", "21.745", "22.105", "OK"],
        ["2018-09-23 20:04:01.123", "9", "ABC Sensor Temp M301A", "20.333", "21.348", "21.943", "OK"],
        ["2018-09-23 20:04:01.999", "10", "ABC Sensor Temp M301A", "20.332", "21.445", "22.013", "OK"],
        ["2018-09-23 20:04:02.001", "11", "ABC Sensor Temp M301A", "-50.000", "-50.000", "-50.000", "LOW_TEMP"]]

    @patch('builtins.open', mock_open(read_data='1'))
    def setUp(self):
        """ Called once, before any tests """
        csv.reader = MagicMock(return_value=TestTemperatureReadingManager.TEST_TEMP_READINGS)
        self.temp_sensor1 = TemperatureReadingManager("data/temperature_results.csv")
        self.logPoint()

    def tearDown(self):
        """ Called once, after all tests, if setUp class successful """
        self.logPoint()

    def logPoint(self):
        """ Utility function used for module functions and class methods """
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))



# temp_obj = TemperatureReadingManager('temperature_results.csv')
# test_obj = TemperatureReading('2018-09-23 19:56:01.345000','50','ABC Sensasdasdor hiTemp second M301A','20.152','21.367','22.005','OK')
# temp_obj.add_reading(test_obj)


# pres_obj_2 = PressureReadingManager('pressure_results_empty.csv')
# test_obj_empty = PressureReading('2018-09-23 21:90:12','ABC Sensor Pres M100','30','100.0','100.0','100.0','HIGH_PRESSURE')
# pres_obj_2.add_reading(test_obj_empty)
