# main_app_controller.py
#
# TODO: Explain about this file
#
# Author:  Nao Hashizume, Matt Harrison Set 2B

import tkinter as tk
import tkinter.ttk
import datetime
from temp_sensor_view import TemperatureSensorView
from top_nav_view import TopNavView

class MainAppController(tk.Frame):
    """ Main Application for GUI """

    def __init__(self,*args, **kwargs):
        """ Initialize Main Application """
        tk.Frame.__init__(self, *args, **kwargs)
        self.lift()
        self.winfo_toplevel().title("Main App Controller")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        topNavBarpage = TopNavView(self)
        topNavBarpage.place(in_=container, relwidth=1, relheight=1, x=0, y=0)
        temperaturePage = TemperatureSensorView(self)
        temperaturePage.place(in_=container, relwidth=1, relheight=1, x=0, y=50)

if __name__ == "__main__":
    root = tk.Tk()
    main = MainAppController(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("750x500")
    root.mainloop()