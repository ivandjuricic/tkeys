# -*- coding: utf-8 -*-
import sys
from tkeys.options import tk_kwargs
from tkeys.options import validate_kwarg_, set_defaults_
from tkeys.geometry_manipulation import *
if sys.version_info[0] == 2:
    from Tkinter import *
else:
    from tkinter import *


class NumKeyPad:
    def __init__(self, parent, **kwargs):
        self.button_options = {}
        set_defaults_(self)
        for key in kwargs:
            validate_kwarg_(key, kwargs[key])  # NAMING CONVENTION?!
            if key in kwargs:
                if key in tk_kwargs:
                    self.button_options[key] = kwargs[key]
                setattr(self, key, kwargs[key])
        self.parent = parent
        self.keyboard_frame = None
        self.widget_list = []
        self.gm = self.geometry_manager_change(self.parent)
        self.widget_bindings()

    @staticmethod
    def geometry_manager_change(parent):
        if not parent.winfo_children():
            raise AttributeError("No child widgets on parent")

        # Checking geometry manager and sides of packing
        first_widget = parent.winfo_children()[0]
        if first_widget.winfo_manager() == "grid":
            from_grid(parent)
        elif first_widget.winfo_manager() == "pack":
            from_pack(parent)
        else:
            from_place(parent)

    def widget_bindings(self):
        for widget in self.parent.winfo_children():
            if isinstance(widget, Entry):
                widget.bind("<ButtonRelease-1>", lambda w=widget: self.init_keyboard(w.widget))
                self.widget_list.append(widget)
            else:
                widget.bind("<Button-1>", self.close_keyboard)

    def init_container(self):
        if self.keyboard_frame:
            self.keyboard_frame.destroy()

        self.keyboard_frame = Frame(self.parent)

        if self.gm in ["pack", "place"]:
            if self.side == "bottom":
                self.keyboard_frame.grid(row=999, column=0, columnspan=999)
            elif self.side == "right":
                self.keyboard_frame.grid(column=999, row=0, rowspan=999)
        else:
            print self.gm
            if self.side == "bottom":
                self.keyboard_frame.place(rely=0.98, relx=0.5, anchor=S)
            elif self.side == "right":
                self.keyboard_frame.place(rely=0.5, relx=0.98, anchor=E)

    def init_keyboard(self, widget):
        self.init_container()
        buttons = [str(x + 1) for x in range(9)] + ["0", "←", "↵"]
        if self.layout == "grid":
            buttons[9], buttons[10] = buttons[10], buttons[9]

        for i, text in enumerate(buttons):
            s = Button(self.keyboard_frame,
                       text=text,
                       command=lambda name=text, w=widget: self.key_press(name, w))
            s.config(self.button_options)
            if self.layout in ["line", None]:
                s.pack(side=LEFT, expand=True)
            elif self.layout is "grid":
                r, c = i // 3, i % 3
                try:
                    self.keyboard_frame.grid_anchor(anchor=CENTER)
                except AttributeError:
                    pass
                s.grid(row=r, column=c)

    def key_press(self, value, entry):
        if value == "←":
            nums_till_last = entry.get()[:-1]
            entry.delete(0, END)
            entry.insert(0, nums_till_last)
        elif value == "↵":  # enters the value and moves on to other entry widget
            self.on_return_key(entry)
        else:
            entry.insert(END, value)

    def on_return_key(self, widget):
        try:
            next_widget = self.widget_list[self.widget_list.index(widget) + 1]
        except IndexError:
            self.close_keyboard()
            return
        self.parent.nametowidget(next_widget).focus_set()
        self.init_keyboard(next_widget)

    def close_keyboard(self, *args):
        try:
            self.keyboard_frame.destroy()
        except AttributeError:
            return
        self.keyboard_frame = None
