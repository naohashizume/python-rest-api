# popup_view.py
#
# TODO: Explain about this file
#
# Author:  Nao Hashizume, Matt Harrison Set 2B

import tkinter as tk
from tkinter import messagebox as tkMessageBox


class PopupView(tk.Frame):
    """ Popup Window """

    def __init__(self, parent, close_popup_callback):
        """ Initialize the nav bar """
        tk.Frame.__init__(self, parent)
        self._parent = parent
        self._parent.geometry("500x400")
        # self._parent.title("Add New Reading")
        self._close_popup_callback = close_popup_callback
        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for the nav bar """

        # label - description of popup
        self.label_title = tk.Label(self._parent, text="Please fulfill these entries", width=20, font=("bold, 11"))
        self.label_title.place(x=150, y=10)

        # label - timestamp
        self.label_1 = tk.Label(self._parent, text="Timestamp :", width=20)
        self.label_1.place(x=10, y=50)
        # entry - timestamp
        self.entry_1 = tk.Entry(self._parent)
        self.entry_1.place(x=150, y=50)
        # label - example of timestamp
        self.label_eg_1 = tk.Label(self._parent, text="eg) 2018-12-01 19:10", width=20)
        self.label_eg_1.place(x=300, y=50)

        # label2 - model
        self.label_2 = tk.Label(self._parent, text="Sensor Model :", width=20)
        self.label_2.place(x=10, y=100)
        # entry - model
        self.entry_2 = tk.Entry(self._parent)
        self.entry_2.place(x=150, y=100)
        # label - example of model
        self.label_eg_2 = tk.Label(self._parent, text="eg) ABC Sensor Temp M301A", width=25)
        self.label_eg_2.place(x=305, y=100)

        # label3 - min_reading
        self.label_3 = tk.Label(self._parent, text="Min Reading :", width=20)
        self.label_3.place(x=10, y=150)
        # entry - min_reading
        self.entry_3 = tk.Entry(self._parent)
        self.entry_3.place(x=150, y=150)
        # label - example of min_reading
        self.label_eg_3 = tk.Label(self._parent, text="eg) 20.152", width=20)
        self.label_eg_3.place(x=272, y=150)

        # label4 - avg_reading
        self.label_4 = tk.Label(self._parent, text="Avg Reading :", width=20)
        self.label_4.place(x=10, y=200)
        # entry - avg_reading
        self.entry_4 = tk.Entry(self._parent)
        self.entry_4.place(x=150, y=200)
        # label - example of avg_reading
        self.label_eg_4 = tk.Label(self._parent, text="eg) 21.367", width=20)
        self.label_eg_4.place(x=272, y=200)

        # label5 - max_reading
        self.label_5 = tk.Label(self._parent, text="Max Reading :", width=20)
        self.label_5.place(x=10, y=250)
        # entry - avg_reading
        self.entry_5 = tk.Entry(self._parent)
        self.entry_5.place(x=150, y=250)
        # label - example of avg_reading
        self.label_eg_5 = tk.Label(self._parent, text="eg) 22.005", width=20)
        self.label_eg_5.place(x=272, y=250)

        tk.Label(self._parent,
                 text="Choose Status:",
                 width=20).place(x=10, y=300)

        tk.Radiobutton(self._parent,
                       text="OK", # add command=
                       value=1).place(x=150, y=300)

        tk.Radiobutton(self._parent,
                       text="HIGH", # add command=
                       value=2).place(x=250, y=300)

        tk.Radiobutton(self._parent,
                       text="LOW", # add command=
                       value=3).place(x=350, y=300)

        self._button = tk.Button(self._parent,
                                 text="Submit", # add command=
                                )
        self._button.place(x=200, y=350)