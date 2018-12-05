# abstract_reading.py
#
# Abstract Reading Manager script
#
# Authors: Nao Hashizume, Matt Harrison, Set 2B

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import csv
import json


class AbstractReadingManager():
    """ Abstract Reading Manager Class """

    NEW_READING = "New Reading"

    def __init__(self, db_name):
        """ Initializer for AbstractReadingManager """
        engine = create_engine(db_name)
        self.DBSession = sessionmaker(bind=engine)

    def add_reading(self, new_reading):
        """ Add a new reading to SQL database, TODO: validate"""
        session = self.DBSession()
        AbstractReadingManager._validate_inp_value(AbstractReadingManager.NEW_READING, new_reading)
        session.add(new_reading)
        session.commit()
        session.close()
        return new_reading

    def get_reading(self, id):
        """Abstract method for retrieving a sensor reading"""
        raise NotImplementedError("Child class must implement abstract class")

    def get__all_readings(self):
        """Abstract method for retrieving all sensor readings"""
        raise NotImplementedError("Child class must implement abstract class")

    def delete_reading(self, id):
        """Abstract method for deleting an entry by id number"""
        raise NotImplementedError("Child class must implement abstract class")

    def update_reading(self, id, new_reading):
        """Abstract method for updating a reading by id number"""
        raise NotImplementedError("Child class must implement abstract class")

    @staticmethod
    def _validate_inp_value(display_name, inp_value):
        """ Private helper to validate int values """
        if inp_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if inp_value == "":
            raise ValueError(display_name + " cannot be empty.")

