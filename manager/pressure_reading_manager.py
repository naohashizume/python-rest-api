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
    DB_NAME = "Database Name"
    ID = "ID"
    NEW_READING = "New Reading"

    def __init__(self, db_name):
        """ Constructor for PressureReadingManager class """
        PressureReadingManager._validate_str_value(PressureReadingManager.DB_NAME, db_name)
        super().__init__(db_name)

    def get_reading(self, id):
        """ Get a reading from the SQL database by id """
        session = self.DBSession()
        PressureReadingManager._validate_int_value(PressureReadingManager.ID, id)
        reading = session.query(PressureReading).filter(PressureReading.id == id).first()
        session.close()
        if reading is not None:
            return reading
        else:
            return None


    def get_all_readings(self):
        """ Get all readings from the SQL database """
        session = self.DBSession()
        readings = session.query(PressureReading).all()
        session.close()
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
        PressureReadingManager._validate_int_value(PressureReadingManager.ID, id)
        del_reading = session.query(PressureReading).filter(PressureReading.id == id).first()
        if del_reading is not None:
            session.delete(del_reading)
            session.commit()
            session.close()
            return True
        else:
            return False


    def update_reading(self, id, new_reading):
        """ Update reading in the SQL database by id"""
        session = self.DBSession()
        PressureReadingManager._validate_int_value(PressureReadingManager.ID, id)
        update_reading = session.query(PressureReading).filter(PressureReading.id == id).first()
        PressureReadingManager._validate_inp_value(PressureReadingManager.NEW_READING, new_reading)
        if update_reading is not None:
            new_reading_dict = new_reading.to_dict()
            update_reading.timestamp = datetime.datetime.strptime(new_reading_dict["timestamp"], PressureReadingManager.DATE_FORMAT)
            update_reading.model = new_reading_dict["model"]
            update_reading.min_reading = new_reading_dict["min_reading"]
            update_reading.avg_reading = new_reading_dict["avg_reading"]
            update_reading.max_reading = new_reading_dict["max_reading"]
            update_reading.status = new_reading_dict["status"]
            session.commit()
            session.close()
            return True
        else:
            return False

    @staticmethod
    def _validate_str_value(display_name, str_value):
        """ Private helper to validate string values """
        if str_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if str_value == "":
            raise ValueError(display_name + " cannot be empty.")

        if not isinstance(str_value, str):
            raise ValueError(display_name + " must be string.")

    @staticmethod
    def _validate_int_value(display_name, int_value):
        """ Private helper to validate integer values """
        if int_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if int_value == "":
            raise ValueError(display_name + " cannot be empty.")

        if not isinstance(int_value, int):
            raise ValueError(display_name + " must be integer.")

    @staticmethod
    def _validate_inp_value(display_name, inp_value):
        """ Private helper to validate input values """
        if inp_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if inp_value == "":
            raise ValueError(display_name + " cannot be empty.")





