# pressure_reading_manager.py
#
# Extends AbstractReadingManager class to handle pressure readings
#
# Author: Matt Harrison, Nao Hashizume, Set 2B


import datetime
from manager.abstract_reading_manager import AbstractReadingManager
from readings.pressure_reading import PressureReading


class PressureReadingManager(AbstractReadingManager):
    """ Pressure Sensor Concrete Implementation """

    # CONSTANTS
    DATETIME_INDEX = 0
    SENSOR_NAME_INDEX = 1
    SEQ_NUM_INDEX = 2
    LOW_INDEX = 3
    AVG_INDEX = 4
    HIGH_INDEX = 5
    STATUS_INDEX = 6

    def __init__(self, filename):
        """ Constructor for PressureSensor Class """
        super().__init__(filename)

    def _load_reading_row(self, row):
        """ Loads list into a PressureReading object """

        reading_datetime = datetime.datetime.strptime(row[PressureReadingManager.DATETIME_INDEX], "%Y-%m-%d %H:%M")

        pressure_reading =  PressureReading(reading_datetime,
                                            row[PressureReadingManager.SENSOR_NAME_INDEX],
                                            int(row[PressureReadingManager.SEQ_NUM_INDEX]),
                                            float(row[PressureReadingManager.LOW_INDEX]),
                                            float(row[PressureReadingManager.AVG_INDEX]),
                                            float(row[PressureReadingManager.HIGH_INDEX]),
                                            row[PressureReadingManager.STATUS_INDEX])

        return pressure_reading

    def _write_reading_row(self, pressure_reading):
        """ Convert reading string and Returns reading list"""
        pres_reading_list = [
                              pressure_reading.get_timestamp().strftime("%Y-%m-%d %H:%M"),
                              pressure_reading.get_sensor_model(),
                              pressure_reading.get_sequence_num(),
                              pressure_reading.get_min_value(),
                              pressure_reading.get_avg_value(),
                              pressure_reading.get_max_value(),
                              pressure_reading.get_status()
                              ]
        return pres_reading_list