# popup_view.py
#
# TODO: Explain about this file
#
# Author:  Nao Hashizume, Matt Harrison Set 2B

import datetime
import tkinter as tk
from tkinter import messagebox as tkMessageBox
import requests

API_ENDPOINT = "http://127.0.0.1:5000/sensor/"
TEMP_READING_SUFFIX = "temperature/reading"
PRES_READING_SUFFIX = "pressure/reading"


class PopupView(tk.Frame):
    """ Popup Window """

    SELECT_OK = "OK"
    SELECT_LOW = "LOW"
    SELECT_HIGH = "HIGH"
    TEMP_PAGE = 1
    PRES_PAGE = 2
    DATE_FORMAT = "%Y-%m-%d %H:%M"


    def __init__(self, parent, close_popup_callback, master):
        """ Initialize the nav bar """
        tk.Frame.__init__(self, parent)
        self._parent = parent
        self._master = master
        self._parent.geometry("500x400")
        # self._parent.title("Add New Reading")
        self._status_var = tk.StringVar(value="OK")
        self._close_popup_callback = close_popup_callback
        self._create_widgets()
        self._selection = "Blar"

    def _create_widgets(self):
        """ Creates the widgets for the nav bar """

        # label - description of popup
        self.label_title = tk.Label(self._parent, text="Please fulfill these entries", width=20, font=("bold, 11"))
        self.label_title.place(x=150, y=10)

        # label - timestamp
        self.timestamp_label = tk.Label(self._parent, text="Timestamp :", width=20)
        self.timestamp_label.place(x=10, y=50)
        # entry - timestamp
        self.timestamp_entry = tk.Entry(self._parent)
        self.timestamp_entry.place(x=150, y=50)
        # label - example of timestamp
        self.timestamp_eg = tk.Label(self._parent, text="eg) 2018-12-01 19:10", width=20)
        self.timestamp_eg.place(x=300, y=50)

        # label2 - model
        self.model_label = tk.Label(self._parent, text="Sensor Model :", width=20)
        self.model_label.place(x=10, y=100)
        # entry - model
        self.model_entry = tk.Entry(self._parent)
        self.model_entry.place(x=150, y=100)
        # label - example of model
        self.model_eg = tk.Label(self._parent, text="eg) ABC Sensor Temp M301A", width=25)
        self.model_eg.place(x=305, y=100)

        # label3 - min_reading
        self.min_label = tk.Label(self._parent, text="Min Reading :", width=20)
        self.min_label.place(x=10, y=150)
        # entry - min_reading
        self.min_entry = tk.Entry(self._parent)
        self.min_entry.place(x=150, y=150)
        # label - example of min_reading
        self.min_eg = tk.Label(self._parent, text="eg) 20.152", width=20)
        self.min_eg.place(x=272, y=150)

        # label4 - avg_reading
        self.avg_label = tk.Label(self._parent, text="Avg Reading :", width=20)
        self.avg_label.place(x=10, y=200)
        # entry - avg_reading
        self.avg_entry = tk.Entry(self._parent)
        self.avg_entry.place(x=150, y=200)
        # label - example of avg_reading
        self.avg_label = tk.Label(self._parent, text="eg) 21.367", width=20)
        self.avg_label.place(x=272, y=200)

        # label5 - max_reading
        self.max_label = tk.Label(self._parent, text="Max Reading :", width=20)
        self.max_label.place(x=10, y=250)
        # entry - avg_reading
        self.max_entry = tk.Entry(self._parent)
        self.max_entry.place(x=150, y=250)
        # label - example of avg_reading
        self.max_eg = tk.Label(self._parent, text="eg) 22.005", width=20)
        self.max_eg.place(x=272, y=250)

        self.status_label = tk.Label(self._parent,
                 text="Choose Status:",
                 width=20).place(x=10, y=300)

        self.radio_ok = tk.Radiobutton(self._parent,
                       text="OK",
                       value="OK",
                       variable=self._status_var).place(x=150, y=300)


        self.radio_high = tk.Radiobutton(self._parent,
                       text="HIGH",
                       value="HIGH",
                       variable=self._status_var).place(x=250, y=300)

        self.radio_low = tk.Radiobutton(self._parent,
                       text="LOW",
                       value="LOW",
                       variable=self._status_var).place(x=350, y=300)

        self._submit_button = tk.Button(self._parent,
                                 text="Submit", command=self.add_reading
                                )
        self._submit_button.place(x=100, y=350)

        self._close_button = tk.Button(self._parent,
                  text="Close",
                  command=self._close_popup_callback)

        self._close_button.place(x=200, y=350)


    def add_reading(self):
        """ Add a reading to the database via the API """
        new_timestamp = self.timestamp_entry.get()
        new_model = self.model_entry.get()
        new_min_reading = float(self.min_entry.get())
        new_avg_reading = float(self.avg_entry.get())
        new_max_reading = float(self.max_entry.get())
        new_status = self._status_var.get()
        if self._master._curr_page == PopupView.TEMP_PAGE:
            post_url = API_ENDPOINT + TEMP_READING_SUFFIX
            headers = {"content-type": "application/json"}
            reading_data = {"timestamp": new_timestamp, "model": new_model, "min_reading": new_min_reading, "avg_reading": new_avg_reading, "max_reading": new_max_reading, "status": new_status}
            response = requests.post(post_url, json=reading_data, headers=headers)
            print(reading_data)
            self._master._temp_sensor_view.update_readings()
        elif self._master._curr_page == PopupView.PRES_PAGE:
            post_url = API_ENDPOINT + PRES_READING_SUFFIX
            headers = {"content-type": "application/json"}
            reading_data = {"timestamp": new_timestamp, "model": new_model, "min_reading": new_min_reading,
                            "avg_reading": new_avg_reading, "max_reading": new_max_reading, "status": new_status}
            response = requests.post(post_url, json=reading_data, headers=headers)
            self._master._pres_sensor_view.update_readings()


    # def add_reading(self):
    #     """ Old method to add a reading to the database using direct access to reading and manager classes"""
    #     new_timestamp = datetime.datetime.strptime(self.entry_1.get(), PopupView.DATE_FORMAT)
    #     new_model = self.entry_2.get()
    #     new_min_reading = self.entry_3.get()
    #     new_avg_reading = self.entry_4.get()
    #     new_max_reading = self.entry_5.get()
    #     new_status = self._status_var.get()
    #     if self._master._curr_page == PopupView.TEMP_PAGE:
    #         new_reading = TemperatureReading(new_timestamp, new_model, new_min_reading, new_avg_reading, new_max_reading, new_status)
    #         temp_manager = TemperatureReadingManager(db_name)
    #         temp_manager.add_reading(new_reading)
    #         self._master._temp_sensor_view.update_readings()
    #     elif self._master._curr_page == PopupView.PRES_PAGE:
    #         new_reading = PressureReading(new_timestamp, new_model, new_min_reading, new_avg_reading,
    #                                          new_max_reading, new_status)
    #         temp_manager = PressureReadingManager(db_name)
    #         temp_manager.add_reading(new_reading)
    #         self._master._pres_sensor_view.update_readings()
