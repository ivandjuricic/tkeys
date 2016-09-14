# -*- coding: utf-8 -*-
import sys
from tkeys.options import tk_kwargs
from tkeys.options import validate_kwarg_, set_defaults_
from tkeys.geometry_manipulation import *
import time

if sys.version_info[0] == 2:
    from Tkinter import *
else:
    from tkinter import *


class AlphaNumericKeyPad:
    def __init__(self, parent, **kwargs):
        self.parent = parent
        self.button_options = {}

        set_defaults_(self)
        for key in kwargs:
            validate_kwarg_(key, kwargs[key])  # NAMING CONVENTION?!
            if key in kwargs:
                if key in tk_kwargs:
                    self.button_options[key] = kwargs[key]
                setattr(self, key, kwargs[key])

        self.keyboard_frame = None
        self.widget_list = []
        self.gm = geometry_manager_change_(self.parent)
        self.widget_bindings()
        self.t = None

    def widget_bindings(self):
        for widget in self.parent.winfo_children():
            if isinstance(widget, Entry):
                widget.bind("<ButtonRelease-1>", lambda w=widget: self.init_keyboard(w.widget))
                self.widget_list.append(widget)
            else:
                widget.bind("<Button-1>", self.close_keyboard)

    def init_keyboard(self, widget):
        init_container_(self)
        buttons = [".,?!", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz",
                   "0+-/=", "⇧", "←"]

        for i, text in enumerate(buttons):
            s = Button(self.keyboard_frame,
                       text=text,
                       width=int(self.font[1] * 0.25),
                       command=lambda key=i, w=widget: self.key_press(key, w))
            s.config(self.button_options)
            if self.layout in ["line", None]:
                s.pack(side=LEFT, expand=True)
            elif self.layout is "grid":
                r, c = i // 3, i % 3
                try:
                    self.keyboard_frame.grid_anchor(anchor=CENTER)
                except AttributeError:
                    pass
                s.grid(row=r,
                       column=c)

        s = Button(self.keyboard_frame,
                   text="↵",
                   width=int(self.font[1] * 0.25),
                   command=lambda key=12, w=widget: self.key_press(key, w))
        s.config(self.button_options)
        if self.layout in ["line", None]:
            s.pack(side=LEFT, expand=True)
        elif self.layout is "grid":
            s.grid(row=5, column=0, columnspan=3)

    def key_press(self, value, entry):
        buttons_chars = [".,?!1:;", "abc2", "def3", "ghi4", "jkl5", "mno6",
                        "pqrs7", "tuv8", "wxyz9", "0-_+=/", "⇧", "←", "↵"]
        prev_char = entry.get()[-1:]
        if value >9:
            self.special(entry, value)
            return

        if prev_char == "":
            self.t = time.time()
            next_char = buttons_chars[value][0]
            entry.insert(END, next_char)
        else:
            prev_char_set = [x for x in buttons_chars if prev_char in x][0]

            if buttons_chars[value] == prev_char_set:
                next_char = self.on_same_key(prev_char_set, prev_char)
                if time.time() - self.t < 1.5:
                    new_string = entry.get()[:-1] + next_char
                    entry.delete(0, END)
                    entry.insert(END, new_string)
                    self.t = time.time()
                else:
                    entry.insert(END, buttons_chars[value][0])
                    self.t = time.time()
            else:
                next_char = buttons_chars[value][0]
                entry.insert(END, next_char)
                self.t = time.time()

    @staticmethod
    def on_same_key(all_char, prev):
        if len(all_char) == all_char.find(prev)+1:
            return all_char[0]
        else:
            return all_char[all_char.find(prev)+1]

    def special(self, entry, value):
        if value == 10:
            print("shift")
        elif value == 11:
            nums_till_last = entry.get()[:-1]
            entry.delete(0, END)
            entry.insert(0, nums_till_last)
        else:
            self.on_return_key(entry)


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
