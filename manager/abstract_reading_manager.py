# abstract_reading.py
#
# Abstract Reading script
#
# Authors: Nao Hashizume, Matt Harrison, Set 2B

from readings.abstract_reading import AbstractReading

import csv
import json

class AbstractReadingManager:
    """ Abstract Reading Manager Class """

    # Constants
    FILE_NAME_STR = "File name"
    NEW_READING = "New Reading"
    SEQ_NUM = "Sequence Number"

    def __init__(self, filename):
        """ Initializes the abstract reading manager """
        AbstractReadingManager._validate_input_value(AbstractReadingManager.FILE_NAME_STR, filename)
        self._filename = filename
        self._latest_sequence_num = 0
        self._sensor_readings = []
        self._read_reading_from_file()

    def add_reading(self, new_reading):
        """ Add reading """
        AbstractReadingManager._validate_input_value(AbstractReadingManager.NEW_READING, new_reading)
        if (len(self._sensor_readings) != 0):
            self._latest_sequence_num = self._sensor_readings[-1].get_sequence_num() + 1
            new_reading.set_sequence_num(self._latest_sequence_num)
            self._sensor_readings.append(new_reading)
            self._write_readings_to_file()
        else:
            new_reading.set_sequence_num(self._latest_sequence_num)
            self._sensor_readings.append(new_reading)
            self._write_readings_to_file()

        return new_reading

    def update_reading(self, new_reading):
        """ Update reading"""
        AbstractReadingManager._validate_input_value(AbstractReadingManager.NEW_READING, new_reading)
        for i, reading in enumerate(self._sensor_readings):
            if reading.get_sequence_num() == new_reading.get_sequence_num():
                self._sensor_readings[i] = new_reading
                self._write_readings_to_file()

    def delete_reading(self, seq_num):
        """ Delete reading """
        AbstractReadingManager._validate_int_value(AbstractReadingManager.SEQ_NUM, seq_num)
        for reading in self._sensor_readings:
            if reading.get_sequence_num() == seq_num:
                self._sensor_readings.remove(reading)

            self._write_readings_to_file()

    def get_reading(self, seq_num):
        """Searches _sensor_readings by sequence number and returns the matching AbstractReading object"""
        AbstractReadingManager._validate_int_value(AbstractReadingManager.SEQ_NUM, seq_num)
        for reading in self._sensor_readings:
            if reading.get_sequence_num() == int(seq_num):
                return reading

    def get_all_readings(self):
        """ Returns all readings as a list of JSON objects """
        reading_list = []
        for reading in self._sensor_readings:
            reading_list.append(self._reading_to_dict(reading))
        return reading_list

    def _read_reading_from_file(self):
        """Loads a new readings file into the sensor readings list. Rejects duplicate sequence numbers."""

        with open(self._filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                new_reading = self._load_reading_row(row)
                if new_reading.get_sequence_num() > self._latest_sequence_num:
                    self._sensor_readings.append(new_reading)
                    self._latest_sequence_num = self._sensor_readings[-1].get_sequence_num()


    def _write_readings_to_file(self):
        """ Write readings to a csv file """
        with open(self._filename, 'w', newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            for reading in self._sensor_readings:
                csv_from_reading = self._write_reading_row(reading)
                csv_writer.writerow(csv_from_reading)

    def _reading_to_dict(self, reading):
        reading_dict = {"timestamp": reading.get_timestamp().strftime('%Y/%m/%d %H:%M'), "sensor_name": reading.get_sensor_model(),
             "seq_num": reading.get_sequence_num(), "low_value": reading.get_min_value(),
             "avg_value": reading.get_avg_value(), "max_value": reading.get_max_value(), "range": reading.get_range(),
             "status": reading.get_status()}
        return reading_dict

    def _load_reading_row(self, row):
        """ Private helper to validate that derived class implement abstract class """
        raise NotImplementedError("Child class must implement abstract class")

    def _write_reading_row(self, reading):
        """ Private helper to validate that derived class implement abstract class """
        raise NotImplementedError("Child class must implement abstract class")

    @staticmethod
    def _validate_input_value(display_name, inp_value):
        """ Private helper to validate string values """
        if inp_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if inp_value == "":
            raise ValueError(display_name + " cannot be empty.")

    @staticmethod
    def _validate_int_value(display_name, int_value):
        """ Private helper to validate string values """
        if int_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if int_value == "":
            raise ValueError(display_name + " cannot be empty.")

        if not isinstance(int_value, int):
            raise ValueError(display_name + " must be integer.")

