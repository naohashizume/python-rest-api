# test_temp_reading_manager.py
#
#  Unit test for Temperature Reading Managaer
#
# Authors: Nao Hashizume, Matt Harrison, Set 2B
#
from manager.temperature_reading_manager import TemperatureReadingManager
from readings.temperature_reading import TemperatureReading
from unittest import TestCase
import inspect
import datetime
import os
import sqlite3


class TestTemperatureReadingManager(TestCase):
    """ Unit Tests for the Temperatyre Reading Manager Class """

    DROP_TABLE_STATEMENT = "DROP TABLE pressure_reading"
    DATABASE_NAME = "sqlite:///test_temp_reading.sqlite"
    TEST_TIMESTAMP = "2018-12-03 8:30"
    TEST_MODEL = "ABC Sensor Temp M100"
    TEST_MIN_VALUE = 20.000
    TEST_AVG_VALUE = 21.000
    TEST_MAX_VALUE = 22.000
    TEST_STATUS = "OK"
    DATE_FORMAT = "%Y-%m-%d %H:%M"

    def setUp(self):
        """ Called once, before any tests """
        conn = sqlite3.connect("test_temp_reading.sqlite")
        c = conn.cursor()
        c.execute('''
                  CREATE TABLE temperature_reading
                  (id INTEGER PRIMARY KEY ASC,
                   timestamp DATETIME NOT NULL,
                   model VARCHAR(250) NOT NULL,
                   min_reading NUMBER NOT NULL,
                   avg_reading NUMBER NOT NULL,
                   max_reading NUMBER NOT NULL,
                   status VARCHAR(250) NOT NULL
                  )
                  ''')
        conn.commit()
        conn.close()
        self.test_pres_manager = TemperatureReadingManager(TestTemperatureReadingManager.DATABASE_NAME)
        test_temp_reading = TemperatureReading(datetime.datetime.strptime(TestTemperatureReadingManager.TEST_TIMESTAMP, TestTemperatureReadingManager.DATE_FORMAT),
                                               TestTemperatureReadingManager.TEST_MODEL,
                                               TestTemperatureReadingManager.TEST_MIN_VALUE,
                                               TestTemperatureReadingManager.TEST_AVG_VALUE,
                                               TestTemperatureReadingManager.TEST_MAX_VALUE,
                                               TestTemperatureReadingManager.TEST_STATUS)
        self.test_temp_manager.add_reading(test_temp_reading)
        self.logPoint()

    def tearDown(self):
        """ Called once, after all tests, if setUp class successful """
        self.test_temp_manager = None
        os.remove("test_temp_reading.sqlite")
        self.logPoint()

    def logPoint(self):
        """ Utility function used for module functions and class methods """
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_init_valid(self):
        """ 010A - Valid Construction Parameters """
        self.assertIsNotNone(TestTemperatureReadingManager(TestTemperatureReadingManager.DATABASE_NAME))

    def test_init_invalid(self):
        """ 010B - Invalid Construction Parameters"""
        with self.assertRaises(ValueError):
            TemperatureReadingManager(None)
            TemperatureReadingManager("")

    def test_add_reading_valid(self):
        """ 020A - Valid Add Reading """
        new_reading = TemperatureReading(datetime.datetime.strptime(TestTemperatureReadingManager.TEST_TIMESTAMP, TestTemperatureReadingManager.DATE_FORMAT),
                                         TestTemperatureReadingManager.TEST_MODEL,
                                         TestTemperatureReadingManager.TEST_MIN_VALUE,
                                         TestTemperatureReadingManager.TEST_AVG_VALUE,
                                         TestTemperatureReadingManager.TEST_MAX_VALUE,
                                         TestTemperatureReadingManager.TEST_STATUS)
        added_reading = self.test_temp_manager.add_reading(new_reading)
        self.assertEqual(new_reading, added_reading)
        rows = len(self.test_temp_manager.get_all_readings())
        self.assertEqual(rows, 2)

    def test_add_reading_invalid(self):
        """ 020B - Invalid Add Reading """
        with self.assertRaises(ValueError):
            self.test_temp_manager.add_reading(None)
            self.test_temp_manager.add_reading("")

    def test_update_reading_valid(self):
        """ 030A - Valid Update Reading """
        new_reading = TemperatureReading(datetime.datetime.strptime("2018-09-23 19:59", "%Y-%m-%d %H:%M"),
                                      "ABC Sensor New Temp M100",
                                      float(21.000),
                                      float(22.000),
                                      float(23.000),
                                      "OK")
        updated_reading = self.test_temp_manager.update_reading(1, new_reading)
        self.assertTrue(updated_reading)

    def test_update_reading_invalid(self):
        """ 030B - Invalid Update Reading """
        new_reading = TemperatureReading(datetime.datetime.strptime("2018-09-23 19:59", "%Y-%m-%d %H:%M"),
                                      "ABC Sensor New Temp M100",
                                      float(21.000),
                                      float(22.000),
                                      float(23.000),
                                      "OK")
        with self.assertRaises(ValueError):
            self.test_temp_manager.update_reading(None, None)
            self.test_temp_manager.update_reading(1, None)
            self.test_temp_manager.update_reading(None, new_reading)
            self.test_temp_manager.update_reading("", "")
            self.test_temp_manager.update_reading(1, "")
            self.test_temp_manager.update_reading("", new_reading)

    def test_delete_reading_valid(self):
        """ 040A - Valid Delete Reading """
        deleted_reading = self.test_temp_manager.delete_reading(1)
        self.assertTrue(deleted_reading)

    def test_delete_reading_invalid(self):
        """ 040B - Invalid Delete Reading """
        with self.assertRaises(ValueError):
            self.test_temp_manager.delete_reading(None)
            self.test_temp_manager.delete_reading("")

    def test_get_reading_valid(self):
        """ 050A - Valid Get Reading """
        get_reading = self.test_temp_manager.get_reading(1)
        self.assertIsInstance(get_reading, TemperatureReading)

    def test_get_reading_invalid(self):
        """ 050B - Invalid Get Reading """
        with self.assertRaises(ValueError):
            self.test_temp_manager.get_reading(None)
            self.test_temp_manager.get_reading("")
            self.test_temp_manager.get_reading(str(1))

    def test_get_all_readings_valid(self):
        """ 060A - Valid Get All Readings """
        self.assertEqual(len(self.test_temp_manager.get_all_readings()), 1)



