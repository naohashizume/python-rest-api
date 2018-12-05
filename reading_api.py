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

db_name = "sqlite:///readings.sqlite"

from flask import Flask
from flask import request
app = Flask(__name__)

TIMESTAMP = "timestamp"
MODEL = "model"
MIN_READING = "min_reading"
AVG_READING = "avg_reading"
MAX_READING = "max_reading"
STATUS = "status"
DATE_FORMAT = "%Y-%m-%d %H:%M"

SUCCESS_RESPONSE_CODE = 200
FAILURE_RESPONSE_CODE = 400

@app.route('/sensor/<string:sensor_type>/reading', methods=['POST'])
def add_reading(sensor_type):
    """API call to add a new sensor reading to the reading manager"""
    try:
        if sensor_type == "temperature":
            temp_sensor = TemperatureReadingManager(db_name)
            json_reading = request.get_json()
            timestamp = datetime.datetime.strptime(json_reading[TIMESTAMP], DATE_FORMAT)
            new_reading = TemperatureReading(timestamp, json_reading[MODEL],
                                             json_reading[MIN_READING], json_reading[AVG_READING], json_reading[MAX_READING],
                                             json_reading[STATUS])
            temp_sensor.add_reading(new_reading)
            response = app.response_class(
                response='Reading added successfully',
                status=SUCCESS_RESPONSE_CODE,
                mimetype='text/plain'
            )
            return response

        elif sensor_type == "pressure":
            press_sensor = PressureReadingManager(db_name)
            json_reading = request.get_json()
            timestamp = datetime.datetime.strptime(json_reading[TIMESTAMP], DATE_FORMAT)
            new_reading = PressureReading(timestamp, json_reading[MODEL], json_reading[MIN_READING], json_reading[AVG_READING], json_reading[MAX_READING], json_reading[STATUS])
            press_sensor.add_reading(new_reading)
            response = app.response_class(
                response='Reading added successfully',
                status=SUCCESS_RESPONSE_CODE,
                mimetype='text/plain'
            )
            return response

        else:
            response = app.response_class(
                response="Bad Request",
                status=FAILURE_RESPONSE_CODE,
                mimetype='application/json'
            )
            return response

    except (KeyError, ValueError):
        response = app.response_class(
            response="Bad Request",
            status=FAILURE_RESPONSE_CODE,
            mimetype='application/json'
            )
        return response

@app.route('/sensor/<string:sensor_type>/reading/<int:id>', methods=['PUT'])
def update_reading(sensor_type, id):
    """API call to update a reading in the reading manager"""
    try:
        if sensor_type == "temperature":
            press_sensor = TemperatureReadingManager(db_name)
            json_reading = request.get_json()
            timestamp = datetime.datetime.strptime(json_reading[TIMESTAMP], DATE_FORMAT)
            new_reading = TemperatureReading(timestamp, json_reading[MODEL],
                                             json_reading[MIN_READING], json_reading[AVG_READING],
                                             json_reading[MAX_READING], json_reading[STATUS])
            press_sensor.update_reading(id, new_reading)
            response = app.response_class(
                response='Reading updated successfully',
                status=SUCCESS_RESPONSE_CODE,
                mimetype='text/plain'
            )
            return response

        elif sensor_type == "pressure":
            press_sensor = PressureReadingManager(db_name)
            json_reading = request.get_json()
            timestamp = datetime.datetime.strptime(json_reading[TIMESTAMP], DATE_FORMAT)
            new_reading = PressureReading(timestamp, json_reading[MODEL], json_reading[MIN_READING],
                                          json_reading[AVG_READING], json_reading[MAX_READING], json_reading[STATUS])
            press_sensor.update_reading(id, new_reading)
            response = app.response_class(
                response='Reading updated successfully',
                status=SUCCESS_RESPONSE_CODE,
                mimetype='text/plain'
            )
            return response

        else:
            response = app.response_class(
                response="Bad Request",
                status=FAILURE_RESPONSE_CODE,
                mimetype='application/json'
            )
            return response

    except(AttributeError, KeyError, ValueError):
        response = app.response_class(
            response="Bad Request",
            status=FAILURE_RESPONSE_CODE,
            mimetype='application/json'
        )
        return response

@app.route('/sensor/<string:sensor_type>/reading/<int:id>', methods=['GET'])
def get_reading(sensor_type, id):
    """API call to retrieve a reading from the reading manager using sequence number"""
    try:
        if sensor_type == "temperature":
            temp_sensor = TemperatureReadingManager(db_name)
            reading = temp_sensor.get_reading(id)
            json_reading = reading.to_json()
            response = app.response_class(
                response=json_reading,
                status=SUCCESS_RESPONSE_CODE,
                mimetype='application/json'
            )
            return response

        elif sensor_type == "pressure":
            press_sensor = PressureReadingManager(db_name)
            reading = press_sensor.get_reading(id)
            json_reading = reading.to_json()
            response = app.response_class(
                response=json_reading,
                status=SUCCESS_RESPONSE_CODE,
                mimetype='application/json'
            )
            return response

        else:
            response = app.response_class(
            response="Bad Request",
            status=FAILURE_RESPONSE_CODE,
            mimetype='application/json'
            )
        return response
    except AttributeError:
        response = app.response_class(
            response="Bad Request",
            status=FAILURE_RESPONSE_CODE,
            mimetype='application/json'
        )
        return response

@app.route('/sensor/<string:sensor_type>/reading/all', methods=['GET'])
def get_all_readings(sensor_type):
    """API call to retrieve all readings from the reading manager"""
    if sensor_type == "temperature":
        temp_sensor = TemperatureReadingManager(db_name)
        readings_list = temp_sensor.get_all_readings()
        json_readings = json.dumps(readings_list)
        response = app.response_class(
            response=json_readings,
            status=200,
            mimetype='application/json'
        )
        return response

    elif sensor_type == "pressure":
        press_sensor = PressureReadingManager(db_name)
        readings_list = press_sensor.get_all_readings()
        json_readings = json.dumps(readings_list)
        response = app.response_class(
            response=json_readings,
            status=SUCCESS_RESPONSE_CODE,
            mimetype='application/json'
        )
        return response

    else:
        response = app.response_class(
            response="Bad Request",
            status=FAILURE_RESPONSE_CODE,
            mimetype='application/json'
        )
        return response

@app.route('/sensor/<string:sensor_type>/reading/<int:id>', methods=['DELETE'])
def delete_reading(sensor_type, id):
    """API call to delete a reading from the reading manager using sequence number"""
    try:
        if sensor_type == "temperature":
            temp_sensor = TemperatureReadingManager(db_name)
            temp_sensor.delete_reading(id)
            response = app.response_class(
                response='Reading deleted successfully',
                status=SUCCESS_RESPONSE_CODE,
                mimetype='application/json'
            )
            return response

        elif sensor_type == "pressure":
            press_sensor = PressureReadingManager(db_name)
            press_sensor.delete_reading(id)
            response = app.response_class(
                response='Reading deleted successfully',
                status=SUCCESS_RESPONSE_CODE,
                mimetype='application/json'
            )
            return response

        else:
            response = app.response_class(
                response="Bad Request",
                status=FAILURE_RESPONSE_CODE,
                mimetype='application/json'
            )
            return response
    except AttributeError:
        response = app.response_class(
            response="Bad Request",
            status=FAILURE_RESPONSE_CODE,
            mimetype='application/json'
        )
        return response


if __name__ == "__main__":
    app.run()
