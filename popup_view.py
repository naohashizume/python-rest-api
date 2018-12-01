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
        self.grid(rowspan=2, columnspan=2)

        self._sample_data = ["Test1", "Test2", "Test3", "Test4", "Test5", "Test6", "Test7", "Test8", "Test9", "Test10", "Test11", "Test12"]
        self._list_data = []

        self._close_popup_callback = close_popup_callback
        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for the nav bar """

        self._scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)

        self._listbox = tk.Listbox(self, yscrollcommand=self._scrollbar.set)
        self._scrollbar.config(command=self._listbox.yview)
        self._listbox.grid(row=0, columnspan=2)
        self._scrollbar.grid(row=0, column=3, sticky=tk.N+tk.S+tk.W+tk.E)

        index = 0
        for item in self._sample_data:
            self._listbox.insert(tk.END, item)

        tk.Button(self,
                  text="Delete",
                  command=self._delete).grid(row=1, column=0)
        tk.Button(self,
                  text="Close",
                  command=self._close_popup_callback).grid(row=1, column=1)

    def _delete(self):
        if tkMessageBox.askyesno('Verify', 'Really delete?'):
            # Delete item
            print("Index: " + str(self._listbox.curselection()[0]))
            self._listbox.delete(tk.ANCHOR)
