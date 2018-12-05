# pressure_reading.py
#
# Pressure Reading script
#
# Authors: Nao Hashizume, Matt Harrison, Set 2B

from readings.abstract_reading import AbstractReading
from base import Base
import json


class PressureReading(AbstractReading, Base):
    """ Concrete Implementation of a Pressure Reading """

    __tablename__ = 'pressure_reading'

    def __init__(self, timestamp, model, min_reading, avg_reading, max_reading, status):
        """ Initializes the pressure sensor reading """
        super().__init__(timestamp, model, min_reading, avg_reading, max_reading, status)
