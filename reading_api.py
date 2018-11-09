# reading_api.py
#
# Sensor API script
#
# Authors: Matt Harrison, Nao Hashizume, Set 2B

from manager.pressure_reading_manager import PressureReadingManager
from manager.temperature_reading_manager import TemperatureReadingManager
from readings.pressure_reading import PressureReading
from readings.temperature_reading import TemperatureReading

import json
import datetime

temp_results_file = "data/temperature_results.csv"
press_results_file = "data/pressure_results.csv"

from flask import Flask
from flask import request
app = Flask(__name__)

DEFAULT_SEQ_NUM = 0
TIMESTAMP = "timestamp"
SENSOR_NAME = "sensor_name"
MIN_READING = "min_reading"
AVG_READING = "avg_reading"
MAX_READING = "max_reading"
STATUS = "status"
TEMP_DATE_FORMAT = "%Y-%m-%d %H:%M:%S.%f"
PRESS_DATE_FORMAT = "%Y-%m-%d %H:%M"


@app.route('/sensor/<sensor_type>/add', methods=['POST'])
def add_reading(sensor_type):
    if sensor_type == "pressure":
        press_sensor = PressureReadingManager(press_results_file)
        json_reading = request.get_json()
        timestamp = datetime.datetime.strptime(json_reading[TIMESTAMP], PRESS_DATE_FORMAT)
        new_reading = PressureReading(timestamp, json_reading[SENSOR_NAME], DEFAULT_SEQ_NUM, json_reading[MIN_READING], json_reading[AVG_READING], json_reading[MAX_READING], json_reading[STATUS])
        press_sensor.add_reading(new_reading)

        response = app.response_class(
            response='Reading added successfully',
            status=200,
            mimetype='text/plain'
        )
        return response

    elif sensor_type == "temperature":
        temp_sensor = TemperatureReadingManager(temp_results_file)
        json_reading = request.get_json()
        timestamp = datetime.datetime.strptime(json_reading[TIMESTAMP], TEMP_DATE_FORMAT)
        new_reading = TemperatureReading(timestamp, DEFAULT_SEQ_NUM, json_reading[SENSOR_NAME],
                                      json_reading[MIN_READING], json_reading[AVG_READING], json_reading[MAX_READING],
                                      json_reading[STATUS])
        temp_sensor.add_reading(new_reading)

        response = app.response_class(
            response='Reading added successfully',
            status=200,
            mimetype='text/plain'
        )
        return response


@app.route('/sensor/<sensor_type>/update/<int:seq_num>', methods=['PUT'])
def update_reading(sensor_type, seq_num):
    if sensor_type == "pressure":
        press_sensor = PressureReadingManager(press_results_file)
        json_reading = request.get_json()
        timestamp = datetime.datetime.strptime(json_reading[TIMESTAMP], PRESS_DATE_FORMAT)
        new_reading = PressureReading(timestamp, json_reading[SENSOR_NAME], seq_num, json_reading[MIN_READING],
                                      json_reading[AVG_READING], json_reading[MAX_READING], json_reading[STATUS])
        press_sensor.update_reading(new_reading)

        response = app.response_class(
            response='Reading updated successfully',
            status=200,
            mimetype='text/plain'
        )
        return response

    if sensor_type == "temperature":
        press_sensor = TemperatureReadingManager(temp_results_file)
        json_reading = request.get_json()
        timestamp = datetime.datetime.strptime(json_reading[TIMESTAMP], TEMP_DATE_FORMAT)
        new_reading = TemperatureReading(timestamp, seq_num, json_reading[SENSOR_NAME],
                                         json_reading[MIN_READING], json_reading[AVG_READING],
                                         json_reading[MAX_READING], json_reading[STATUS])
        press_sensor.update_reading(new_reading)

        response = app.response_class(
            response='Reading updated successfully',
            status=200,
            mimetype='text/plain'
        )
        return response


@app.route('/sensor/<sensor_type>/get_reading/<int:seq_num>', methods=['GET'])
def get_reading(sensor_type, seq_num):
    if sensor_type == "pressure":
        press_sensor = PressureReadingManager(press_results_file)
        reading = press_sensor.get_reading(seq_num)
        json_reading = reading.to_json()
        response = app.response_class(
            response=json_reading,
            status=200,
            mimetype='application/json'
        )
        return response

    elif sensor_type == "temperature":
        temp_sensor = TemperatureReadingManager(temp_results_file)
        reading = temp_sensor.get_reading(seq_num)
        json_reading = reading.to_json()
        response = app.response_class(
            response=json_reading,
            status=200,
            mimetype='application/json'
        )
        return response


@app.route('/sensor/<sensor_type>/get_all', methods=['GET'])
def get_all_readings(sensor_type):
    if sensor_type == "pressure":
        press_sensor = PressureReadingManager(press_results_file)
        readings_list = press_sensor.get_all_readings()
        print(readings_list)
        json_readings = json.dumps(readings_list)
        response = app.response_class(
            response=json_readings,
            status=200,
            mimetype='application/json'
        )
        return response

    elif sensor_type == "temperature":
        temp_sensor = TemperatureReadingManager(temp_results_file)
        readings_list = temp_sensor.get_all_readings()
        json_readings = json.dumps(readings_list)
        response = app.response_class(
            response=json_readings,
            status=200,
            mimetype='application/json'
        )
        return response


@app.route('/sensor/<sensor_type>/reading/<int:seq_num>', methods=['DELETE'])
def sensor_delete_reading(sensor_type, seq_num):
    if sensor_type == "temperature":
        temp_sensor = TemperatureReadingManager(temp_results_file)
        json_string = temp_sensor.delete_reading(seq_num)
        response = app.response_class(
            response=json_string,
            status=200,
            mimetype='application/json'
        )
        return response

    elif sensor_type == "pressure":
        press_sensor = PressureReadingManager(press_results_file)
        json_string = press_sensor.delete_reading(seq_num)
        response = app.response_class(
            response=json_string,
            status=200,
            mimetype='application/json'
        )
        return response



if __name__ == "__main__":
    app.run()
