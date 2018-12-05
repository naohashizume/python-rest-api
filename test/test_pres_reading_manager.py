# test_pres_reading_manager.py
#
#  Unit test for Pressure Reading Manager
#
# Authors: Nao Hashizume, Matt Harrison, Set 2B
#
from manager.pressure_reading_manager import PressureReadingManager
from readings.pressure_reading import PressureReading
from unittest import TestCase
import inspect
import datetime
import os
import sqlite3


class TestPressureReadingManager(TestCase):
    """ Unit Tests for the Pressure Reading Manager Class """

    # Constants
    DROP_TABLE_STATEMENT = "DROP TABLE pressure_reading"
    DATABASE_NAME = "sqlite:///test_pres_reading.sqlite"
    TEST_TIMESTAMP = "2018-12-03 8:30"
    TEST_MODEL = "ABC Sensor Press M100"
    TEST_MIN_VALUE = 49.213
    TEST_AVG_VALUE = 50.111
    TEST_MAX_VALUE = 52.567
    TEST_STATUS = "GOOD"
    DATE_FORMAT = "%Y-%m-%d %H:%M"

    def setUp(self):
        """ Called once, before any tests """
        conn = sqlite3.connect("test_pres_reading.sqlite")
        c = conn.cursor()
        c.execute('''
                  CREATE TABLE pressure_reading
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
        self.test_pres_manager = PressureReadingManager(TestPressureReadingManager.DATABASE_NAME)
        test_pres_reading = PressureReading(datetime.datetime.strptime(TestPressureReadingManager.TEST_TIMESTAMP, TestPressureReadingManager.DATE_FORMAT),
                                            TestPressureReadingManager.TEST_MODEL,
                                            TestPressureReadingManager.TEST_MIN_VALUE,
                                            TestPressureReadingManager.TEST_AVG_VALUE,
                                            TestPressureReadingManager.TEST_MAX_VALUE,
                                            TestPressureReadingManager.TEST_STATUS)
        self.test_pres_manager.add_reading(test_pres_reading)
        self.logPoint()

    def tearDown(self):
        """ Called once, after all tests, if setUp class successful """
        self.test_pres_manager = None
        os.remove("test_pres_reading.sqlite")
        self.logPoint()

    def logPoint(self):
        """ Utility function used for module functions and class methods """
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_init_valid(self):
        """ 010A - Valid Construction Parameters """
        self.assertIsNotNone(PressureReadingManager(TestPressureReadingManager.DATABASE_NAME))

    def test_init_invalid(self):
        """ 010B - Invalid Construction Parameters"""
        with self.assertRaises(ValueError):
            PressureReadingManager(None)
            PressureReadingManager("")

    def test_add_reading_valid(self):
        """ 020A - Valid Add Reading """
        new_reading = PressureReading(datetime.datetime.strptime(TestPressureReadingManager.TEST_TIMESTAMP, TestPressureReadingManager.DATE_FORMAT),
                                      TestPressureReadingManager.TEST_MODEL,
                                      TestPressureReadingManager.TEST_MIN_VALUE,
                                      TestPressureReadingManager.TEST_AVG_VALUE,
                                      TestPressureReadingManager.TEST_MAX_VALUE,
                                      TestPressureReadingManager.TEST_STATUS)
        added_reading = self.test_pres_manager.add_reading(new_reading)
        self.assertEqual(new_reading, added_reading)
        rows = len(self.test_pres_manager.get_all_readings())
        self.assertEqual(rows, 2)

    def test_add_reading_invalid(self):
        """ 020B - Invalid Add Reading """
        with self.assertRaises(ValueError):
            self.test_pres_manager.add_reading(None)
            self.test_pres_manager.add_reading("")

    def test_update_reading_valid(self):
        """ 030A - Valid Update Reading """
        new_reading = PressureReading(datetime.datetime.strptime("2018-09-23 19:59", "%Y-%m-%d %H:%M"),
                                      "ABC Sensor New Pres M100",
                                      float(50.513),
                                      float(51.745),
                                      float(53.105),
                                      "GOOD")
        updated_reading = self.test_pres_manager.update_reading(1, new_reading)
        self.assertTrue(updated_reading)

    def test_update_reading_invalid(self):
        """ 030B - Invalid Update Reading """
        new_reading = PressureReading(datetime.datetime.strptime("2018-09-23 19:59", "%Y-%m-%d %H:%M"),
                                      "ABC Sensor New Pres M100",
                                      float(50.513),
                                      float(51.745),
                                      float(53.105),
                                      "GOOD")

        with self.assertRaises(ValueError):
            self.test_pres_manager.update_reading(None, None)
            self.test_pres_manager.update_reading(1, None)
            self.test_pres_manager.update_reading(None, new_reading)
            self.test_pres_manager.update_reading("", "")
            self.test_pres_manager.update_reading(1, "")
            self.test_pres_manager.update_reading("", new_reading)

    def test_delete_reading_valid(self):
        """ 040A - Valid Delete Reading """
        deleted_reading = self.test_pres_manager.delete_reading(1)
        self.assertTrue(deleted_reading)

    def test_delete_reading_invalid(self):
        """ 040B - Invalid Delete Reading """
        with self.assertRaises(ValueError):
            self.test_pres_manager.delete_reading(None)
            self.test_pres_manager.delete_reading("")

    def test_get_reading_valid(self):
        """ 050A - Valid Get Reading """
        get_reading = self.test_pres_manager.get_reading(1)
        self.assertIsInstance(get_reading, PressureReading)

    def test_get_reading_invalid(self):
        """ 050B - Invalid Get Reading """
        with self.assertRaises(ValueError):
            self.test_pres_manager.get_reading(None)
            self.test_pres_manager.get_reading("")
            self.test_pres_manager.get_reading(str(1))

    def test_get_all_readings_valid(self):
        """ 060A - Valid Get All Readings """
        self.assertEqual(len(self.test_pres_manager.get_all_readings()), 1)



