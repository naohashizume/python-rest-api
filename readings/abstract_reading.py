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
        #self._sequence_num = seq_num
        self.min_reading = min_reading
        self.avg_reading = avg_reading
        self.max_reading = max_reading
        self.status = status

    def to_json(self):
        """ TODO """
        json_string = json.dumps(self.to_dict())
        return json_string

    def to_dict(self):
        """ TODO """
        reading_data = {
            "id": self.id,
            "timestamp": self.timestamp.strftime(AbstractReading.DATE_FORMAT),
            "model": self.model,
            "min_reading": self.min_reading,
            "avg_reading": self.avg_reading,
            "max_reading": self.max_reading,
            "status": self.status}

        return reading_data

    #
    # def get_timestamp(self):
    #     """ Getter for timestamp """
    #     return self._timestamp
    #
    # def get_sensor_model(self):
    #     """ Getter for sensor model """
    #     return self._sensor_model
    #
    # def get_sequence_num(self):
    #     """ Getter for sequence number """
    #     return self._sequence_num
    #
    # def set_sequence_num(self, new_sequence_num):
    #     """ Setter for sequence number """
    #     self._sequence_num = new_sequence_num
    #
    # def get_min_value(self):
    #     """ Getter for the minimum temperature """
    #     return self._min
    #
    # def get_avg_value(self):
    #     """ Getter for the average temperature """
    #     return self._avg
    #
    # def get_max_value(self):
    #     """ Getter for the maximum temperature """
    #     return self._max
    #
    # def get_range(self):
    #     """ Getter for the temperature range """
    #     return self._max - self._min
    #
    # def get_status(self):
    #     """ Getter for the status message """
    #     return self._status
    #
    # def to_json(self):
    #     """Returns reading as JSON"""
    #     reading_dict = {
    #         "timestamp": self._timestamp.strftime('%Y/%m/%d %H:%M'),
    #         "sensor_name": self._sensor_model,
    #         "seq_num": self._sequence_num,
    #         "min_value": self._min,
    #         "avg_value": self._avg,
    #         "max_value": self._max,
    #         "range": self.get_range(),
    #         "status": self._status
    #     }
    #     return json.dumps(reading_dict, indent=4)
    #
    # def is_error(self):
    #     """ Abstract Method - Is Reading and Error """
    #     raise NotImplementedError("Must be implemented")
    #
    # def get_error_msg(self):
    #     """ Abstract Method - Get Error Readings """
    #     raise NotImplementedError("Must be implemented")
