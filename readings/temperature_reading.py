# pressure_reading.py
#
# Temperature Reading script
#
# Authors: Nao Hashizume, Matt Harrison, Set 2B

from readings.abstract_reading import AbstractReading
from base import Base


class TemperatureReading(AbstractReading, Base):
    """ Concrete Implementation of a Temperature Reading """

    __tablename__ = 'temperature_reading'

    def __init__(self, timestamp, model, min_reading, avg_reading, max_reading, status):
        """ Initializes the pressure sensor reading """
        super().__init__(timestamp, model, min_reading, avg_reading, max_reading, status)

