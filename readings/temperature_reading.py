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

    def __init__(self, date, model, min_reading, avg_reading, max_reading, status):
        """ Initializes the pressure sensor reading """
        super().__init__(date, model, min_reading, avg_reading, max_reading, status)

    # # CONSTANTS
    # HIGH_TEMP_ERROR = "HIGH_TEMP"
    # LOW_TEMP_ERROR = "LOW_TEMP"
    # STATUS_OK = "OK"
    # DEGREE_SIGN = u'\N{DEGREE SIGN}'
    #
    # def __init__(self, date, seq_num, sensor_name, lowest_temp, avg_temp, highest_temp, status):
    #     """ Temperature Reading Constructor """
    #
    #     super().__init__(date, seq_num, sensor_name, lowest_temp, avg_temp, highest_temp, status)
    #
    # def is_error(self):
    #     """ Returns True if there's a there's an error and False if there's no error """
    #     if self._status != TemperatureReading.STATUS_OK:
    #         return True
    #
    #     return False
    #
    # def get_error_msg(self):
    #     """ Returns the error message (or None if not an error) """
    #     status_display = None
    #
    #     reading_display_datetime = self._timestamp.strftime('%Y/%m/%d %H:%M')
    #
    #     reading_seq_num = self._sequence_num
    #
    #     if self._status == TemperatureReading.HIGH_TEMP_ERROR:
    #         status_display = "High Temperature (100%cC) at %s, Sequence: %d" % (TemperatureReading.DEGREE_SIGN, reading_display_datetime, reading_seq_num)
    #     elif self._status == TemperatureReading.LOW_TEMP_ERROR:
    #         status_display = "Low Temperature (-50%cC) at %s, Sequence: %d" % (TemperatureReading.DEGREE_SIGN, reading_display_datetime, reading_seq_num)
    #
    #     return status_display
