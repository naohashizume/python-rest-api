# abstract_reading.py
#
# Abstract Reading script
#
# Authors: Matt Harrison, Nao Hashizume, Set 2B

from sqlalchemy import Column, Integer, DateTime, String, Float
import json
import datetime

class AbstractReading():
    """ Abstract Reading Class """

    DATE_FORMAT = '%Y-%m-%d %H:%M'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.now, nullable=False)
    model = Column(String(250), nullable=False)
    min_reading = Column(Float, nullable=False)
    avg_reading= Column(Float, nullable=False)
    max_reading = Column(Float, nullable=False)
    status = Column(String(250), nullable=False)

    def __init__(self, date, model, min_reading, avg_reading, max_reading, status):
        """ Initializes the sensor reading """
        self.timestamp = date
        self.model = model
        self.min_reading = min_reading
        self.avg_reading = avg_reading
        self.max_reading = max_reading
        self.status = status

    def to_dict(self):
        """ Convert reading to dictionary """
        reading_data = {
            "id": self.id,
            "timestamp": self.timestamp.strftime(AbstractReading.DATE_FORMAT),
            "model": self.model,
            "min_reading": self.min_reading,
            "avg_reading": self.avg_reading,
            "max_reading": self.max_reading,
            "status": self.status}

        return reading_data