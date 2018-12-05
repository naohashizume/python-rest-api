# main_app_controller.py
#
# Main App Controller for GUI
#
# Author:  Nao Hashizume, Matt Harrison Set 2B

import tkinter as tk
from top_navbar_view import TopNavbarView
from temp_sensor_view import TempSensorView
from pres_sensor_view import PressureSensorView
from bottom_navbar_view import BottomNavbarView
from popup_view import PopupView
from update_popup_view import UpdatePopupView


class MainAppController(tk.Frame):
    """ Main Application for GUI """

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        self._top_navbar = TopNavbarView(self, self._temp_page_callback, self._pres_page_callback)
        self._temp_sensor_view = TempSensorView(self, self._temp_page_callback)
        self._pres_sensor_view = PressureSensorView(self,self._pres_page_callback)
        self._bottom_navbar = BottomNavbarView(self,self._page_popup_callback, self._update_popup_callback, self._quit_callback)

        self._top_navbar.grid(row=0, columnspan=4, pady=10)
        self._temp_sensor_view.grid(row=1, columnspan=4, pady=10)
        self.grid_columnconfigure(1, weight=1)
        self._curr_page = TopNavbarView.TEMP_PAGE
        self._bottom_navbar.grid(row=2, columnspan=4, pady=10)

    def _temp_page_callback(self):
        """ Open Temperature Sensor Reading Page """
        if (self._curr_page == TopNavbarView.PRES_PAGE):
            self._pres_sensor_view.grid_forget()
            self._temp_sensor_view.grid(row=1, columnspan=4, pady=10)
            self._curr_page = TopNavbarView.TEMP_PAGE

    def _pres_page_callback(self):
        """ Open Pressure Sensor Reading Page """
        if (self._curr_page == TopNavbarView.TEMP_PAGE):
            self._temp_sensor_view.grid_forget()
            self._pres_sensor_view.grid(row=1, columnspan=4, pady=10)
            self._curr_page = TopNavbarView.PRES_PAGE

    def _page_popup_callback(self):
        """ Open Popup for Adding a Reading """
        self._popup_win = tk.Toplevel(self)
        self._popup = PopupView(self._popup_win, self._close_popup_callback, self)

    def _update_popup_callback(self):
        """ Open Popup for Updating a Reading"""
        self._popup_win = tk.Toplevel()
        self._popup = UpdatePopupView(self._popup_win, self._close_popup_callback, self)

    def _close_popup_callback(self):
        """ Close a Popup Page"""
        self._popup_win.destroy()

    def _quit_callback(self):
        """ Close Main App Controller """
        self.quit()


if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.wm_geometry("800x400")
    root.title("Sensor Reading Manager - v1.0")
    root.mainloop()
