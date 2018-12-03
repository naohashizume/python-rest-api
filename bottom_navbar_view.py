# bottom_navbar_view.py
#
# TODO: Explain about this file
#
# Author:  Nao Hashizume, Matt Harrison Set 2B

import tkinter as tk
from tkinter import messagebox as tkMessageBox
from manager.temperature_reading_manager import TemperatureReadingManager
from manager.pressure_reading_manager import PressureReadingManager

class BottomNavbarView(tk.Frame):
    """ Bottom Navigation Bar """

    TEMP_PAGE = 1
    PRES_PAGE = 2
    db_name = "sqlite:///readings.sqlite"

    def __init__(self, parent, page_popup_callback, update_popup_callback, quit_callback):
        """ Initialize the nav bar """
        tk.Frame.__init__(self, parent)
        self._parent = parent
        self._page_popup_callback = page_popup_callback
        self._update_popup_callback = update_popup_callback
        self._quit_callback = quit_callback
        self._create_widgets()


    def _create_widgets(self):
        """ Creates the widgets for the nav bar """

        # button - add
        self._button_add = tk.Button(self,
                                     text="Add",
                                     fg="blue",
                                     command=self._page_popup_callback)
        self._button_add.grid(row=1, column=1, padx=5)

        # button - update
        self._button_update = tk.Button(self,
                                     text="Update",
                                     fg="green",
                                     command=self._update_popup_callback)
        self._button_update.grid(row=1, column=2, padx=5)

        # button - delete
        self._button_delete = tk.Button(self,
                                        text="Delete",
                                        fg="black",
                                        command=self.delete_entry
                                        )
        self._button_delete.grid(row=1, column=3, padx=5)

        # button - quit
        self._button_quit = tk.Button(self,
                                 text="QUIT",
                                 fg="red",
                                 command=self._quit_callback)
        self._button_quit.grid(row=1, column=4, padx=5)


    def delete_entry(self):
        try :
            if tkMessageBox.askyesno('Verify', 'Do you really want to delete?'):
                # Delete item
                if self._parent._curr_page == BottomNavbarView.TEMP_PAGE:
                    row = self._parent._temp_sensor_view.displayReadings.focus()
                    reading_id = self._parent._temp_sensor_view.displayReadings.item(row)["values"][0]
                    temp_sensor = TemperatureReadingManager(BottomNavbarView.db_name)
                    temp_sensor.delete_reading(reading_id)
                    self._parent._temp_sensor_view.update_readings()
                elif self._parent._curr_page == BottomNavbarView.PRES_PAGE:
                    row = self._parent._pres_sensor_view.displayReadings.focus()
                    reading_id = self._parent._pres_sensor_view.displayReadings.item(row)["values"][0]
                    pres_sensor = PressureReadingManager(BottomNavbarView.db_name)
                    pres_sensor.delete_reading(reading_id)
                    self._parent._pres_sensor_view.update_readings()
        except (IndexError,ValueError):
            tkMessageBox.showerror("Error", "Please select a row to delete.")




