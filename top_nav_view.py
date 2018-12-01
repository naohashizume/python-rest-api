# top_nav_view.py
#
# TODO: Explain about this file
#
# Author:  Nao Hashizume, Matt Harrison Set 2B

import tkinter as tk

class TopNavView(tk.Frame):
    """ TODO: Explain about this file """

    def __init__(self, *args, **kwargs):
        """ Initialize the nav bar """
        tk.Frame.__init__(self, *args, **kwargs)

        # title of readings
        self.label_title = tk.Label(self,
                                    text="Choose a type of sensor:")
        self.label_title.place(x=50, y=10)

        # radio button for temperature sensor
        tk.Radiobutton(self,
                       text="temperature",
                       value=1).place(x=250, y=10)

        # radio button for pressure sensor
        tk.Radiobutton(self,
                       text="pressure",
                       value=2).place(x=450, y=10)
