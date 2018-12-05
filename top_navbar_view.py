# top_navbar_view.py
#
# Top Navigation Bar View
#
# Author:  Nao Hashizume, Matt Harrison Set 2B

import tkinter as tk


class TopNavbarView(tk.Frame):
    """ Top Navigation Bar """

    TEMP_PAGE = 1
    PRES_PAGE = 2

    def __init__(self, parent, temp_page_callback, pres_page_callback):
        """ Initialize the nav bar """
        tk.Frame.__init__(self, parent)
        self._parent = parent

        self._temp_page_callback = temp_page_callback
        self._pres_page_callback = pres_page_callback
        self._page = tk.IntVar()
        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for the nav bar """
        tk.Label(self,
                 text="Select type of sensor:").grid(row=0, column=0)

        tk.Radiobutton(self,
                       text="temperature",
                       variable=self._page,
                       command=self._temp_page_callback,
                       value=1).grid(row=0, column=1)

        tk.Radiobutton(self,
                       text="pressure",
                       variable=self._page,
                       command=self._pres_page_callback,
                       value=2).grid(row=0, column=2)


        self._page.set(1)

