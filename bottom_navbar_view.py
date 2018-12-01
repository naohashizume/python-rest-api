# bottom_navbar_view.py
#
# TODO: Explain about this file
#
# Author:  Nao Hashizume, Matt Harrison Set 2B

import tkinter as tk

class BottomNavbarView(tk.Frame):
    """ Bottom Navigation Bar """

    def __init__(self, parent, page_popup_callback, quit_callback):
        """ Initialize the nav bar """
        tk.Frame.__init__(self, parent)
        self._parent = parent
        self._page_popup_callback = page_popup_callback
        self._quit_callback = quit_callback
        self._create_widgets()


    def _create_widgets(self):
        """ Creates the widgets for the nav bar """

        # button - add
        self._button_add = tk.Button(self,
                                     text="Add",
                                     fg="blue",
                                     command=self._page_popup_callback)
        self._button_add.grid(row=1, column=1)

        # button - update
        self._button_update = tk.Button(self,
                                     text="Update",
                                     fg="green",
                                     )
        self._button_update.grid(row=1, column=2)

        # button - delete
        self._button_delete = tk.Button(self,
                                        text="Delete",
                                        fg="black",
                                        )
        self._button_delete.grid(row=1, column=3)

        # button - quit
        self._button_quit = tk.Button(self,
                                 text="QUIT",
                                 fg="red",
                                 command=self._quit_callback)
        self._button_quit.grid(row=1, column=4)



