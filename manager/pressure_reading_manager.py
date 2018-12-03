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

    DATE_FORMAT = '%Y-%m-%d %H:%M'

    def __init__(self, db_name):
        """ Constructor for PressureReadingManager class """
        super().__init__(db_name)


    def get_reading(self, id):
        """ Get a reading from the SQL database by id """
        session = self.DBSession()
        reading = session.query(PressureReading).filter(PressureReading.id == id).first()
        if reading is not None:
            return reading
        else:
            return None


    def get_all_readings(self):
        """ Get all readings from the SQL database """
        session = self.DBSession()
        readings = session.query(PressureReading).all()
        if readings is not None:
            dict_list = []
            for reading in readings:
                dict_list.append(reading.to_dict())
            return dict_list
        else:
            return None


    def delete_reading(self, id):
        """ Delete reading from the SQL database by id """
        session = self.DBSession()
        del_reading = session.query(PressureReading).filter(PressureReading.id == id).first()
        if del_reading is not None:
            session.delete(del_reading)
            session.commit()
            return True
        else:
            return False


    def update_reading(self, id, new_reading):
        """ Update reading in the SQL database by id"""
        session = self.DBSession()
        update_reading = session.query(PressureReading).filter(PressureReading.id == id).first()

        if update_reading is not None:
            new_reading_dict = new_reading.to_dict()
            update_reading.timestamp = datetime.datetime.strptime(new_reading_dict["timestamp"], PressureReadingManager.DATE_FORMAT)
            update_reading.model = new_reading_dict["model"]
            update_reading.min_reading = new_reading_dict["min_reading"]
            update_reading.avg_reading = new_reading_dict["avg_reading"]
            update_reading.max_reading = new_reading_dict["max_reading"]
            update_reading.status = new_reading_dict["status"]
            session.commit()
            return True
        else:
            return False

    # # CONSTANTS
    # DATETIME_INDEX = 0
    # SENSOR_NAME_INDEX = 1
    # SEQ_NUM_INDEX = 2
    # LOW_INDEX = 3
    # AVG_INDEX = 4
    # HIGH_INDEX = 5
    # STATUS_INDEX = 6
    #
    # def __init__(self, filename):
    #     """ Constructor for PressureSensor Class """
    #     super().__init__(filename)
    #
    # def _load_reading_row(self, row):
    #     """ Loads list into a PressureReading object """
    #
    #     reading_datetime = datetime.datetime.strptime(row[PressureReadingManager.DATETIME_INDEX], "%Y-%m-%d %H:%M")
    #
    #     pressure_reading =  PressureReading(reading_datetime,
    #                                         row[PressureReadingManager.SENSOR_NAME_INDEX],
    #                                         int(row[PressureReadingManager.SEQ_NUM_INDEX]),
    #                                         float(row[PressureReadingManager.LOW_INDEX]),
    #                                         float(row[PressureReadingManager.AVG_INDEX]),
    #                                         float(row[PressureReadingManager.HIGH_INDEX]),
    #                                         row[PressureReadingManager.STATUS_INDEX])
    #
    #     return pressure_reading
    #
    # def _write_reading_row(self, pressure_reading):
    #     """ Prepares a pressure reading to be written to the csv file """
    #     pres_reading_list = [
    #                           pressure_reading.get_timestamp().strftime("%Y-%m-%d %H:%M"),
    #                           pressure_reading.get_sensor_model(),
    #                           pressure_reading.get_sequence_num(),
    #                           pressure_reading.get_min_value(),
    #                           pressure_reading.get_avg_value(),
    #                           pressure_reading.get_max_value(),
    #                           pressure_reading.get_status()
    #                           ]
    #     return pres_reading_list