#
# Authors: Nao Hashizume, Matt Harrison, Set 2B
#
# test_pressure_reading_manager.py
#

from manager.pressure_reading_manager import PressureReadingManager
from readings.pressure_reading import PressureReading
from unittest import TestCase
import inspect
import csv
import datetime

from unittest.mock import MagicMock
from unittest.mock import patch, mock_open

class TestPressureReadingManager(TestCase):
    """ Unit Tests for the Pressure Reading Manager Class """

    TEST_PRES_READINGS = [
        ["2018-09-23 19:56", "ABC Sensor Pres M100", "1", "50.163", "51.435", "52.103", "GOOD"],
        ["2018-09-23 20:00", "ABC Sensor Pres M100", "2", "100.000", "100.000", "100.000", "HIGH_PRESSURE"],
        ["2018-09-23 20:06", "ABC Sensor Pres M100", "3", "0.000", "0.000", "0.000", "LOW_PRESSURE"]
    ]

    @patch('builtins.open', mock_open(read_data='1'))
    def setUp(self):
        """ Called once, before any tests """
        csv.reader = MagicMock(return_value=TestPressureReadingManager.TEST_PRES_READINGS)
        self.temp_sensor = PressureReadingManager("test_results.csv")
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
            self.temp_sensor = PressureReadingManager(None)
            self.temp_sensor = PressureReadingManager("")

    def test_add_reading_valid(self):
        """ 020A - Valid Add Reading """
        new_reading = PressureReading(datetime.datetime.strptime("2018-09-23 20:05", "%Y-%m-%d %H:%M"),
                                        "ABC Sensor Pres M100",
                                        int(1),
                                        float(50.332),
                                        float(51.445),
                                        float(52.013),
                                        "OK")
        added_reading = self.temp_sensor.add_reading(new_reading)
        self.assertEqual(len(self.temp_sensor.get_all_readings()), 4)
        self.assertIsInstance(added_reading, PressureReading)

    def test_add_reading_invalid(self):
        """ 020B - Invalid Add Reading """
        with self.assertRaises(ValueError):
            self.temp_sensor.add_reading(None)
            self.temp_sensor.add_reading("")

    def test_update_reading_valid(self):
        """ 030A - Valid Update Reading """
        new_reading = PressureReading(datetime.datetime.strptime("2018-09-23 19:59", "%Y-%m-%d %H:%M"),
                                        "ABC Sensor Pres M100",
                                         int(2),
                                         float(50.513),
                                         float(51.745),
                                         float(53.105),
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
        self.assertIsInstance(get_reading, PressureReading)

    def test_get_reading_invalid(self):
        """ 050B - Invalid Get Reading """
        with self.assertRaises(ValueError):
            self.temp_sensor.get_reading(None)
            self.temp_sensor.get_reading("")
            self.temp_sensor.get_reading(str(1))

    def test_get_all_readings_valid(self):
        """ 060A - Valid Get All Readings """
        self.assertEqual(len(self.temp_sensor.get_all_readings()), 3)









