#
# Authors: Matt Harrison, Nao Hashizume, Set 2B
#
# test_temperature_reading_manager.py
#

from manager.temperature_reading_manager import TemperatureReadingManager
from readings.temperature_reading import TemperatureReading

temp_obj = TemperatureReadingManager('temperature_results.csv')
test_obj = TemperatureReading('2018-09-23 19:56:01.345000','50','ABC Sensasdasdor hiTemp second M301A','20.152','21.367','22.005','OK')
temp_obj.add_reading(test_obj)


# pres_obj_2 = PressureReadingManager('pressure_results_empty.csv')
# test_obj_empty = PressureReading('2018-09-23 21:90:12','ABC Sensor Pres M100','30','100.0','100.0','100.0','HIGH_PRESSURE')
# pres_obj_2.add_reading(test_obj_empty)
