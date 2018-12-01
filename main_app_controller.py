# main_app_controller.py
#
# TODO: Explain about this file
#
# Author:  Nao Hashizume, Matt Harrison Set 2B

import tkinter as tk
from top_navbar_view import TopNavbarView
from temp_sensor_view import TempSensorView
from pres_sensor_view import PressureSensorView
from bottom_navbar_view import BottomNavbarView
from popup_view import PopupView


class MainAppController(tk.Frame):
    """ Main Application for GUI """

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        self._top_navbar = TopNavbarView(self, self._page_callback)
        self._temp_sensor_view = TempSensorView(self, self._page1_submit_callback)
        self._pres_sensor_view = PressureSensorView(self, self._page2_submit_callback)
        self._bottom_navbar = BottomNavbarView(self,self._page_popup_callback, self._quit_callback)

        self._top_navbar.grid(row=0, columnspan=4, pady=10)
        self._temp_sensor_view.grid(row=1, columnspan=4, pady=10)
        self.grid_columnconfigure(1, weight=1)
        self._curr_page = TopNavbarView.TEMP_PAGE
        self._bottom_navbar.grid(row=2, columnspan=4, pady=10)

    def _page_callback(self):
        """ Handle Switching Between Pages """
        if (self._curr_page == TopNavbarView.TEMP_PAGE):
            self._temp_sensor_view.grid_forget()
            self._pres_sensor_view.grid(row=1, columnspan=4)
            self._curr_page = TopNavbarView.PRES_PAGE
        elif (self._curr_page == TopNavbarView.PRES_PAGE):
            self._pres_sensor_view.grid_forget()
            self._temp_sensor_view.grid(row=1, columnspan=4)
            self._curr_page = TopNavbarView.TEMP_PAGE

    def _page_popup_callback(self):
        self._popup_win = tk.Toplevel()
        self._popup = PopupView(self._popup_win, self._close_popup_callback)

    def _close_popup_callback(self):
        self._popup_win.destroy()

    def _page1_submit_callback(self):
        print("Submit Page 1")
        # print(self._page1.get_form_data())

    def _page2_submit_callback(self):
        print("Submit Page 2")
        # print(self._page2.get_form_data())

    def _add_callback(self):
        """ """

    def _quit_callback(self):
        self.quit()

if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.wm_geometry("800x500")
    root.mainloop()
