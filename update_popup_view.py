# update_popup_view.py
#
# Defines the UpdatePopupView class
#
# Author:  Nao Hashizume, Matt Harrison Set 2B

import tkinter as tk
from tkinter import messagebox as tkMessageBox


class UpdatePopupView(tk.Frame):
    """ Update Popup Window """

    TEMP_PAGE = 1
    PRES_PAGE = 2

    def __init__(self, parent, close_popup_callback, master):
        """ Initialize the nav bar """
        tk.Frame.__init__(self, parent)
        self._parent = parent
        self._parent.geometry("500x500")
        self._parent.title("Update Selected Reading")
        self._page = tk.IntVar()
        self._close_popup_callback = close_popup_callback
        self._master = master
        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for the nav bar """

        # label - description of popup
        self.label_title = tk.Label(self._parent, text="Please fulfill these entries", width=20, font=("bold, 11"))
        self.label_title.place(x=150, y=10)

        # label - id of selected row
        self.label_selected_id = tk.Label(self._parent, text="Selected Row id:",width=20)
        self.label_selected_id.place(x=10, y=50)

        self.entry_selected_id = tk.Entry(self._parent)
        self.entry_selected_id.insert(0, self.get_selected_id())
        self.entry_selected_id.config(state=tk.DISABLED)
        self.entry_selected_id.place(x=150, y=50)


        # label - timestamp
        self.label_1 = tk.Label(self._parent, text="Timestamp :", width=20)
        self.label_1.place(x=10, y=100)
        # entry - timestamp
        self.entry_1 = tk.Entry(self._parent)
        self.entry_1.place(x=150, y=100)
        # label - example of timestamp
        self.label_eg_1 = tk.Label(self._parent, text="eg) 2018-12-01 19:10", width=20)
        self.label_eg_1.place(x=300, y=100)

        # label2 - model
        self.label_2 = tk.Label(self._parent, text="Sensor Model :", width=20)
        self.label_2.place(x=10, y=150)
        # entry - model
        self.entry_2 = tk.Entry(self._parent)
        self.entry_2.place(x=150, y=150)
        # label - example of model
        self.label_eg_2 = tk.Label(self._parent, text="eg) ABC Sensor Temp M301A", width=25)
        self.label_eg_2.place(x=305, y=150)

        # label3 - min_reading
        self.label_3 = tk.Label(self._parent, text="Min Reading :", width=20)
        self.label_3.place(x=10, y=200)
        # entry - min_reading
        self.entry_3 = tk.Entry(self._parent)
        self.entry_3.place(x=150, y=200)
        # label - example of min_reading
        self.label_eg_3 = tk.Label(self._parent, text="eg) 20.152", width=20)
        self.label_eg_3.place(x=272, y=200)

        # label4 - avg_reading
        self.label_4 = tk.Label(self._parent, text="Avg Reading :", width=20)
        self.label_4.place(x=10, y=250)
        # entry - avg_reading
        self.entry_4 = tk.Entry(self._parent)
        self.entry_4.place(x=150, y=250)
        # label - example of avg_reading
        self.label_eg_4 = tk.Label(self._parent, text="eg) 21.367", width=20)
        self.label_eg_4.place(x=272, y=250)

        # label5 - max_reading
        self.label_5 = tk.Label(self._parent, text="Max Reading :", width=20)
        self.label_5.place(x=10, y=300)
        # entry - avg_reading
        self.entry_5 = tk.Entry(self._parent)
        self.entry_5.place(x=150, y=300)
        # label - example of avg_reading
        self.label_eg_5 = tk.Label(self._parent, text="eg) 22.005", width=20)
        self.label_eg_5.place(x=272, y=300)

        tk.Label(self._parent,
                 text="Choose Status:",
                 width=20).place(x=10, y=350)

        tk.Radiobutton(self._parent,
                       text="OK/GOOD", # add command=
                       value=1,
                       variable=self._page).place(x=150, y=350)

        tk.Radiobutton(self._parent,
                       text="HIGH", # add command=
                       value=2,
                       variable=self._page).place(x=250, y=350)

        tk.Radiobutton(self._parent,
                       text="LOW", # add command=
                       value=3,
                       variable=self._page).place(x=350, y=350)

        self._update_button = tk.Button(self._parent,
                                 text="Update",

                                )
        self._update_button.place(x=100, y=400)

        self._close_button = tk.Button(self._parent,
                  text="Close",
                  command=self._close_popup_callback)

        self._close_button.place(x=200, y=400)


    def get_selected_id(self):
        """"""
        if self._master._curr_page == UpdatePopupView.TEMP_PAGE:
            row = self._master._temp_sensor_view.displayReadings.focus()
            reading_id = self._master._temp_sensor_view.displayReadings.item(row)["values"][0]
            return reading_id

        elif self._master._curr_page == UpdatePopupView.PRES_PAGE:
            row = self._master._pres_sensor_view.displayReadings.focus()
            reading_id = self._master._pres_sensor_view.displayReadings.item(row)["values"][0]
            return reading_id