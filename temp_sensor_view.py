# temp_sensor_view.py
#
# Temperature Sensor Reading View
#
# Author:  Nao Hashizume, Matt Harrison Set 2B

import tkinter as tk
import tkinter.ttk
import requests
import datetime
from manager.temperature_reading_manager import TemperatureReadingManager
db_name = "sqlite:///readings.sqlite"

API_ENDPOINT = "http://127.0.0.1:5000/sensor/"
TEMP_READING_SUFFIX = "temperature/reading/all"


class TempSensorView(tk.Frame):
    """ Temperature Sensor Reading View """

    def __init__(self, parent, page_callback):
        """ Initialize Temperature Sensor Reading View """
        tk.Frame.__init__(self, parent)
        self._parent = parent
        self._page_callback = page_callback
        self._create_widgets()
        self.update_readings()

    def _create_widgets(self):
        """ Creates the widgets for Temperature Sensor Page """

        # title of readings
        self.label_title = tk.Label(self, text="Temperature Sensor Readings")
        self.label_title.pack()

        # treeview - style
        self.style = tkinter.ttk.Style()
        self.style.configure("style.Treeview", hightlightthickness=0, bd=0)
        self.style.configure("style.Treeview.Heading", font=("Calibri", 11, "bold"))

        # treeview
        self.displayReadings = tkinter.ttk.Treeview(self, style="style.Treeview")
        self.displayReadings["columns"] = ("id",
                                           "timestamp",
                                           "model",
                                           "min_reading",
                                           "avg_reading",
                                           "max_reading",
                                           "status")
        self.displayReadings["show"] = "headings"

        # treeview - id column
        self.displayReadings.column("id", anchor="center", width=50)
        self.displayReadings.heading("id", anchor="center", text="Id")
        # treeview - timestamp column
        self.displayReadings.column("timestamp", anchor="center", width=100)
        self.displayReadings.heading("timestamp", text="Timestamp")
        # treeview - model column
        self.displayReadings.column("model", anchor="center", width=150)
        self.displayReadings.heading("model", text="Model")
        # treeview - min_reading column
        self.displayReadings.column("min_reading", anchor="center", width=100)
        self.displayReadings.heading("min_reading", text="Min Reading")
        # treeview - avg_reading column
        self.displayReadings.column("avg_reading", anchor="center", width=100)
        self.displayReadings.heading("avg_reading", text="Avg Reading")
        # treeview - max_reading column
        self.displayReadings.column("max_reading", anchor="center", width=100)
        self.displayReadings.heading("max_reading", text="Max Reading")
        # treeview - status column
        self.displayReadings.column("status", anchor="center", width=100)
        self.displayReadings.heading("status", text="status")
        # treeview - position
        self.displayReadings.pack(side="left")

        # treeview - scroll bar
        self.scrollbar = tkinter.ttk.Scrollbar(self, orient="vertical", command=self.displayReadings.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.displayReadings.configure(yscrollcommand=self.scrollbar.set)

    def update_readings(self):
        """ Refreshes the display of all temperature readings """
        if len(self.displayReadings.get_children()) != 0:
            item_list = self.displayReadings.get_children()
            for item in item_list:
                self.displayReadings.delete(item)
        get_all_url = API_ENDPOINT + TEMP_READING_SUFFIX
        response = requests.get(get_all_url)
        temp_readings = response.json()
        for reading in temp_readings:
            self.displayReadings.insert("", "end", values=[reading["id"], reading["timestamp"], reading["model"], reading["min_reading"], reading["avg_reading"], reading["max_reading"], reading["status"]])