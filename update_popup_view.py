# update_popup_view.py
#
# Defines the UpdatePopupView class
#
# Author:  Nao Hashizume, Matt Harrison Set 2B

import requests
import tkinter as tk
from tkinter import messagebox as tkMessageBox

API_ENDPOINT = "http://127.0.0.1:5000/sensor/"
TEMP_READING_SUFFIX = "temperature/reading/"
PRES_READING_SUFFIX = "pressure/reading/"

class UpdatePopupView(tk.Frame):
    """ Update Popup Window """

    SELECT_OK = "OK"
    SELECT_LOW = "LOW"
    SELECT_HIGH = "HIGH"
    TEMP_PAGE = 1
    PRES_PAGE = 2

    def __init__(self, parent, close_popup_callback, master):
        """ Initialize the nav bar """
        tk.Frame.__init__(self, parent)
        self._parent = parent
        self._parent.geometry("500x500")
        self._parent.title("Update Selected Reading")
        self._status_var = tk.StringVar(value=None)
        self._close_popup_callback = close_popup_callback
        self._master = master
        self._create_widgets()
        self._populate_entry_fields()

    def _create_widgets(self):
        """ Creates the widgets for the nav bar """

        # label - description of popup
        self.label_title = tk.Label(self._parent, text="Please fulfill these entries", width=20, font=("bold, 11"))
        self.label_title.place(x=150, y=10)

        # label - id of selected row
        self.label_selected_id = tk.Label(self._parent, text="Selected Row id:",width=20)
        self.label_selected_id.place(x=10, y=50)

        self.entry_selected_id = tk.Entry(self._parent)
        # self.entry_selected_id.insert(0, self.get_selected_id())
        # self.entry_selected_id.config(state=tk.DISABLED)
        self.entry_selected_id.place(x=150, y=50)


        # label - timestamp
        self.timestamp_label = tk.Label(self._parent, text="Timestamp :", width=20)
        self.timestamp_label.place(x=10, y=100)
        # entry - timestamp
        self.timestamp_entry = tk.Entry(self._parent)
        self.timestamp_entry.place(x=150, y=100)
        # label - example of timestamp
        self.timestamp_eg = tk.Label(self._parent, text="eg) 2018-12-01 19:10", width=20)
        self.timestamp_eg.place(x=300, y=100)

        # label2 - model
        self.model_label = tk.Label(self._parent, text="Sensor Model :", width=20)
        self.model_label.place(x=10, y=150)
        # entry - model
        self.model_entry = tk.Entry(self._parent)
        self.model_entry.place(x=150, y=150)
        # label - example of model
        self.model_eg = tk.Label(self._parent, text="eg) ABC Sensor Temp M301A", width=25)
        self.model_eg.place(x=305, y=150)

        # label3 - min_reading
        self.min_label = tk.Label(self._parent, text="Min Reading :", width=20)
        self.min_label.place(x=10, y=200)
        # entry - min_reading
        self.min_entry = tk.Entry(self._parent)
        self.min_entry.place(x=150, y=200)
        # label - example of min_reading
        self.min_eg = tk.Label(self._parent, text="eg) 20.152", width=20)
        self.min_eg.place(x=272, y=200)

        # label4 - avg_reading
        self.avg_label = tk.Label(self._parent, text="Avg Reading :", width=20)
        self.avg_label.place(x=10, y=250)
        # entry - avg_reading
        self.avg_entry = tk.Entry(self._parent)
        self.avg_entry.place(x=150, y=250)
        # label - example of avg_reading
        self.avg_eg = tk.Label(self._parent, text="eg) 21.367", width=20)
        self.avg_eg.place(x=272, y=250)

        # label5 - max_reading
        self.max_label = tk.Label(self._parent, text="Max Reading :", width=20)
        self.max_label.place(x=10, y=300)
        # entry - avg_reading
        self.max_entry = tk.Entry(self._parent)
        self.max_entry.place(x=150, y=300)
        # label - example of avg_reading
        self.max_eg = tk.Label(self._parent, text="eg) 22.005", width=20)
        self.max_eg.place(x=272, y=300)

        self.status_label = tk.Label(self._parent,
                 text="Choose Status:",
                 width=20).place(x=10, y=350)

        self.radio_ok = tk.Radiobutton(self._parent,
                       text="OK",
                       value="OK",
                       variable=self._status_var).place(x=150, y=350)

        self.radio_high = tk.Radiobutton(self._parent,
                       text="HIGH",
                       value="HIGH",
                       variable=self._status_var).place(x=250, y=350)

        self.radio_low = tk.Radiobutton(self._parent,
                       text="LOW",
                       value="LOW",
                       variable=self._status_var).place(x=350, y=350)

        self._update_button = tk.Button(self._parent,
                                 text="Update", command=self.update_reading)

        self._update_button.place(x=100, y=400)

        self._close_button = tk.Button(self._parent,
                  text="Close",
                  command=self._close_popup_callback)

        self._close_button.place(x=200, y=400)


    def update_reading(self):
        update_timestamp = self.timestamp_entry.get()
        update_model = self.model_entry.get()
        update_min_reading = float(self.min_entry.get())
        update_avg_reading = float(self.avg_entry.get())
        update_max_reading = float(self.max_entry.get())
        update_new_status = self._status_var.get()
        reading_data = {"timestamp": update_timestamp, "model": update_model, "min_reading": update_min_reading,
                        "avg_reading": update_avg_reading, "max_reading": update_max_reading, "status": update_new_status}
        if self._master._curr_page == UpdatePopupView.TEMP_PAGE:
            put_url = API_ENDPOINT + TEMP_READING_SUFFIX + str(self.entry_selected_id.get())
            headers = {"content-type": "application/json"}
            response = requests.put(put_url, json=reading_data, headers=headers)
            self._master._temp_sensor_view.update_readings()
        elif self._master._curr_page == UpdatePopupView.PRES_PAGE:
            put_url = API_ENDPOINT + PRES_READING_SUFFIX + str(self.entry_selected_id.get())
            headers = {"content-type": "application/json"}
            response = requests.put(put_url, json=reading_data, headers=headers)
            self._master._pres_sensor_view.update_readings()


    def _populate_entry_fields(self):
        """ Private method called in __init__ to populate entry fields with reading data"""
        if self._master._curr_page == UpdatePopupView.TEMP_PAGE:
            # Get values from selected row
            row = self._master._temp_sensor_view.displayReadings.focus()
            reading_id = self._master._temp_sensor_view.displayReadings.item(row)["values"][0]
            reading_timestamp = self._master._temp_sensor_view.displayReadings.item(row)["values"][1]
            reading_model = self._master._temp_sensor_view.displayReadings.item(row)["values"][2]
            reading_min_reading = self._master._temp_sensor_view.displayReadings.item(row)["values"][3]
            reading_avg_reading = self._master._temp_sensor_view.displayReadings.item(row)["values"][4]
            reading_max_reading = self._master._temp_sensor_view.displayReadings.item(row)["values"][5]
            reading_status = self._master._temp_sensor_view.displayReadings.item(row)["values"][6]

            # Assign values to entry fields. Locks reading id
            self.entry_selected_id.insert(0, reading_id)
            self.entry_selected_id.config(state=tk.DISABLED)
            self.timestamp_entry.insert(0, reading_timestamp)
            self.model_entry.insert(0, reading_model)
            self.min_entry.insert(0, reading_min_reading)
            self.avg_entry.insert(0, reading_avg_reading)
            self.max_entry.insert(0, reading_max_reading)
            self._status_var.set(reading_status)

        elif self._master._curr_page == UpdatePopupView.PRES_PAGE:
            # Get values from selected row
            row = self._master._pres_sensor_view.displayReadings.focus()
            reading_id = self._master._pres_sensor_view.displayReadings.item(row)["values"][0]
            reading_timestamp = self._master._pres_sensor_view.displayReadings.item(row)["values"][1]
            reading_model = self._master._pres_sensor_view.displayReadings.item(row)["values"][2]
            reading_min_reading = self._master._pres_sensor_view.displayReadings.item(row)["values"][3]
            reading_avg_reading = self._master._pres_sensor_view.displayReadings.item(row)["values"][4]
            reading_max_reading = self._master._pres_sensor_view.displayReadings.item(row)["values"][5]
            reading_status = self._master._pres_sensor_view.displayReadings.item(row)["values"][6]

            # Assign values to entry fields. Locks reading id
            self.entry_selected_id.insert(0, reading_id)
            self.entry_selected_id.config(state=tk.DISABLED)
            self.timestamp_entry.insert(0, reading_timestamp)
            self.model_entry.insert(0, reading_model)
            self.min_entry.insert(0, reading_min_reading)
            self.avg_entry.insert(0, reading_avg_reading)
            self.max_entry.insert(0, reading_max_reading)
            self._status_var.set(reading_status)


    # def get_selected_id(self):
    #     """"""
    #     if self._master._curr_page == UpdatePopupView.TEMP_PAGE:
    #         try:
    #             row = self._master._temp_sensor_view.displayReadings.focus()
    #             reading_id = self._master._temp_sensor_view.displayReadings.item(row)["values"][0]
    #             return reading_id
    #         except (ValueError, IndexError):
    #             tkMessageBox.showerror("Error", "Please select a row to update.")
    #
    #     elif self._master._curr_page == UpdatePopupView.PRES_PAGE:
    #         row = self._master._pres_sensor_view.displayReadings.focus()
    #         reading_id = self._master._pres_sensor_view.displayReadings.item(row)["values"][0]
    #         return reading_id