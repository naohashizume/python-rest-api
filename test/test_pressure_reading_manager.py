#
# Authors: Matt Harrison, Nao Hashizume, Set 2B
#
# test_pressure_reading_manager.py
#

from unittest import TestCase
from manager.pressure_reading_manager import PressureReadingManager
from readings.pressure_reading import PressureReading

import datetime

# pres_obj = PressureReadingManager('pressure_results.csv')
# test_obj = PressureReading('2018-09-23 21:90:12','ABC Sensor Pres M100','30','100.0','100.0','100.0','HIGH_PRESSURE')
# pres_obj.add_reading(test_obj)


#pres_obj_2 = PressureReadingManager('pressure_results_empty.csv')
pres_obj_2 = PressureReadingManager('../data/pressure_results.csv')

test_obj_empty = PressureReading(datetime.datetime.strptime('2018-09-25 21:05', '%Y-%m-%d %H:%M'),'Sensor Pres M100 test',30,100.0,100.0,100.0,'HIGH_PRESSURE')
pres_obj_2.add_reading(test_obj_empty)

#pres_obj_2.delete_reading(1)


