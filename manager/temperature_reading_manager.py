# temperature_reading_manager.py
#
# Extends AbstractReadingManager class to handle temperature readings
#
# Author: Matt Harrison, Nao Hashizume, Set 2B

import datetime
from manager.abstract_reading_manager import AbstractReadingManager
from readings.temperature_reading import TemperatureReading

class TemperatureReadingManager(AbstractReadingManager):
    """ Temperature Sensor concrete implementation """

    DATE_FORMAT = "%Y-%m-%d %H:%M"

    def __init__(self, db_name):
        """ Constructor for PressureSensor Class """
        super().__init__(db_name)


    def get_reading(self, id):
        """ Get temperature reading from SQL database"""
        session = self.DBSession()
        reading = session.query(TemperatureReading).filter(TemperatureReading.id == id).first()
        session.close()
        if reading is not None:
            return reading
        else:
            return None


    def get_all_readings(self):
        """ Get all temperature readings from SQL database """
        session = self.DBSession()
        readings = session.query(TemperatureReading).all()
        session.close()
        if readings is not None:
            dict_list = []
            for reading in readings:
                dict_list.append(reading.to_dict())
            return dict_list
        else:
            return None


    def delete_reading(self, id):
        """ Delete a temperature reading from the SQL database by id """
        session = self.DBSession()
        del_reading = session.query(TemperatureReading).filter(TemperatureReading.id == id).first()
        if del_reading is not None:
            session.delete(del_reading)
            session.commit()
            session.close()
            return True
        else:
            return False


    def update_reading(self, id, new_reading):
        """ Update a temperature reading from the SQL database by id"""
        session = self.DBSession()
        update_reading = session.query(TemperatureReading).filter(TemperatureReading.id == id).first()

        if update_reading is not None:
            new_reading_dict = new_reading.to_dict()
            update_reading.timestamp = datetime.datetime.strptime(new_reading_dict["timestamp"], TemperatureReadingManager.DATE_FORMAT)
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