# temp_sensor_view.py
#
# TODO: Explain about this file
#
# Author:  Nao Hashizume, Matt Harrison Set 2B

import tkinter as tk
import tkinter.ttk
import datetime


class TemperatureSensorView(tk.Frame):
    """ TODO: Explain about this file """
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        # title of readings
        self.label_title = tk.Label(self, text="Temperature Sensor Readings")
        self.label_title.pack()

        # treeview
        self.style = tkinter.ttk.Style()
        self.style.configure("style.Treeview", hightlightthickness=0, bd=0)
        self.style.configure("style.Treeview.Heading", font=("Calibri", 11,"bold"))

        self.displayReadings= tkinter.ttk.Treeview(self, style="style.Treeview")
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
        self.displayReadings.column("timestamp",anchor="center", width=100)
        self.displayReadings.heading("timestamp", text="Timestamp")
        # treeview - model column
        self.displayReadings.column("model", anchor="center", width=110)
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

        self.displayReadings.pack(pady=15)

        self.addButton = tkinter.Button(self, text="Add", width=15)


        self.displayReadings.insert("", "end",
                                    values=[len(self.displayReadings.get_children("")) + 1,
                                            datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                                            "ABC Sensor Temp",
                                            20.152,
                                            21.367,
                                            22.005,
                                            "OK"])


