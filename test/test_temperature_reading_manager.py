#
# Authors: Nao Hashizume, Matt Harrison, Set 2B
#
# test_temperature_reading_manager.py
#

from manager.temperature_reading_manager import TemperatureReadingManager
from manager.pressure_reading_manager import AbstractReadingManager
from readings.temperature_reading import TemperatureReading

from unittest import TestCase
import inspect
import csv
import datetime

from unittest.mock import MagicMock
from unittest.mock import patch, mock_open

class TestTemperatureReadingManager(TestCase):
    """ Unit Tests for the Temperature Reading Manager Class """

    TEST_TEMP_READINGS = [
        ["2018-09-23 19:59:01.873", "1", "ABC Sensor Temp M301A", "20.212", "21.641", "22.017", "OK"],
        ["2018-09-23 20:00:02.453", "2", "ABC Sensor Temp M301A", "100.000", "100.000", "100.000", "HIGH_TEMP"],
        ["2018-09-23 20:00:03.563", "3", "ABC Sensor Temp M301A", "-50.000", "-50.000", "-50.000", "LOW_TEMP"]
    ]

    @patch('builtins.open', mock_open(read_data='1'))
    def setUp(self):
        """ Called once, before any tests """
        csv.reader = MagicMock(return_value=TestTemperatureReadingManager.TEST_TEMP_READINGS)
        self.temp_sensor = TemperatureReadingManager("test_results.csv")
        csv.writer = MagicMock()
        self.logPoint()

    def tearDown(self):
        """ Called once, after all tests, if setUp class successful """
        self.logPoint()

    def logPoint(self):
        """ Utility function used for module functions and class methods """
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_init_valid(self):
        """ 010A - Valid Construction Parameters """
        self.assertIsNotNone(self.temp_sensor)

    def test_init_invalid(self):
        """ 010B - Invalid Construction Parameters"""
        with self.assertRaises(ValueError):
            self.temp_sensor = TemperatureReadingManager(None)
            self.temp_sensor = TestTemperatureReadingManager("")

    def test_add_reading_valid(self):
        """ 020A - Valid Add Reading """
        new_reading = TemperatureReading(datetime.datetime.strptime("2018-09-23 19:59:01.873", "%Y-%m-%d %H:%M:%S.%f"),
                                         int(1),
                                         "ABC Sensor Temp M301A",
                                         float(20.212),
                                         float(21.641),
                                         float(22.017),
                                         "OK")
        added_reading = self.temp_sensor.add_reading(new_reading)
        self.assertEqual(len(self.temp_sensor.get_all_readings()), 4)
        self.assertIsInstance(added_reading, TemperatureReading)

    def test_add_reading_invalid(self):
        """ 020B - Invalid Add Reading """
        with self.assertRaises(ValueError):
            self.temp_sensor.add_reading(None)
            self.temp_sensor.add_reading("")

    def test_update_reading_valid(self):
        """ 030A - Valid Update Reading """
        new_reading = TemperatureReading(datetime.datetime.strptime("2018-09-23 19:59:01.873", "%Y-%m-%d %H:%M:%S.%f"),
                                         int(2),
                                         "ABC Sensor Temp M301A",
                                         float(20.212),
                                         float(21.641),
                                         float(22.017),
                                         "OK")
        self.temp_sensor.update_reading(new_reading)
        updated_reading = self.temp_sensor.get_reading(2)
        self.assertEqual(new_reading, updated_reading)

    def test_update_reading_invalid(self):
        """ 030B - Invalid Update Reading """
        with self.assertRaises(ValueError):
            self.temp_sensor.update_reading(None)
            self.temp_sensor.update_reading("")

    def test_delete_reading_valid(self):
        """ 040A - Valid Delete Reading """
        self.temp_sensor.delete_reading(1)
        self.assertEqual(len(self.temp_sensor.get_all_readings()), 2)

    def test_delete_reading_invalid(self):
        """ 040B - Invalid Delete Reading """
        with self.assertRaises(ValueError):
            self.temp_sensor.delete_reading(None)
            self.temp_sensor.delete_reading("")
            self.temp_sensor.delete_reading(str(1))

    def test_get_reading_valid(self):
        """ 050A - Valid Get Reading """
        get_reading = self.temp_sensor.get_reading(1)
        self.assertIsInstance(get_reading, TemperatureReading)

    def test_get_reading_invalid(self):
        """ 050B - Invalid Get Reading """
        with self.assertRaises(ValueError):
            self.temp_sensor.get_reading(None)
            self.temp_sensor.get_reading("")
            self.temp_sensor.get_reading(str(1))

    def test_get_all_readings_valid(self):
        """ 060A - Valid Get All Readings """
        self.assertEqual(len(self.temp_sensor.get_all_readings()), 3)






