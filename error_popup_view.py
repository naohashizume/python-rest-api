# error_popup_view.py
#
# TODO: Explain about this file
#
# Author:  Nao Hashizume, Matt Harrison Set 2B

import tkinter as tk
from tkinter import messagebox as tkMessageBox

class ErrorPopupView(tk.Frame):
    """ Error Popup Window """
    def __init__(self, parent, close_popup_callback):
        """ Initialize the nav bar """
        tk.Frame.__init__(self, parent)
        self._parent = parent
        self.grid(rowspan=2, columnspan=2)

        self._close_popup_callback = close_popup_callback
        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for the nav bar """
        tkMessageBox.showerror("Error", "The input data is invalid, Can you try again?")