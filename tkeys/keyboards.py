# -*- coding: utf-8 -*-
import sys
import time
from tkeys.validation import *
from tkeys.geometry_manipulation import *
if sys.version_info[0] == 2:
    from Tkinter import *
else:
    from tkinter import *


class NumKeyPad:
    def __init__(self, parent, **kwargs):
        self.parent = parent
        self.button_options = {}

        check_placement_manager_(kwargs)
        set_defaults_(self)
        for key in kwargs:
            validate_kwarg_(key, kwargs[key])  # NAMING CONVENTION?!
            if key in kwargs:
                if key in TK_KWARGS:
                    self.button_options[key] = kwargs[key]
                setattr(self, key, kwargs[key])


        self.keyboard_frame = None
        self.widget_list = []
        self.gm = geometry_manager_change_(self.parent)
        self.widget_bindings()

    def widget_bindings(self):
        for widget in self.parent.winfo_children():
            if isinstance(widget, Entry):
                widget.bind("<ButtonRelease-1>", lambda w=widget: self.init_keyboard(w.widget))
                self.widget_list.append(widget)
            else:
                pass
                widget.bind("<Button>", self.close_keyboard, "+")

    def init_keyboard(self, widget):
        init_container_(self)
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


class AlphaNumericKeyPad:
    def __init__(self, parent, **kwargs):
        self.parent = parent
        self.button_options = {}

        check_placement_manager_(kwargs)
        set_defaults_(self)
        for key in kwargs:
            validate_kwarg_(key, kwargs[key])  # NAMING CONVENTION?!
            if key in kwargs:
                if key in TK_KWARGS:
                    self.button_options[key] = kwargs[key]
                setattr(self, key, kwargs[key])

        self.keyboard_frame = None
        self.widget_list = []
        self.gm = geometry_manager_change_(self.parent)
        self.widget_bindings()
        self.t = None
        self.shift = False

    def widget_bindings(self):
        for widget in self.parent.winfo_children():
            if isinstance(widget, Entry):
                widget.bind("<ButtonRelease-1>", lambda w=widget: self.init_keyboard(w.widget))
                self.widget_list.append(widget)
            else:
                widget.bind_class("<Button>", self.close_keyboard, "+")

    def init_keyboard(self, widget):
        init_container_(self)

        for i, text in enumerate(ALPHANUMERIC_BUTTONS_TEXT):
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
        prev_char = entry.get()[-1:].lower()
        if value > 9:
            self.special(entry, value)
            return

        if prev_char == "":
            self.t = time.time()
            next_char = ALPHANUMERIC_CHARS[value][0]
            #entry.insert(END, next_char)
        else:
            prev_char_set = [x for x in ALPHANUMERIC_CHARS if prev_char in x][0]

            if ALPHANUMERIC_CHARS[value] == prev_char_set:
                next_char = self.on_same_key(prev_char_set, prev_char)
                if time.time() - self.t < 1.5:
                    if self.shift == True:
                        next_char = next_char.upper()
                    prev_string = entry.get()[:-1]
                    entry.delete(0, END)
                    entry.insert(END, prev_string)
                else:
                    next_char = ALPHANUMERIC_CHARS[value][0]
                    self.t = time.time()
            else:
                next_char = ALPHANUMERIC_CHARS[value][0]
        if self.shift == True:
            next_char = next_char.upper()
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
            self.on_shift_key(value)
        elif value == 11:
            nums_till_last = entry.get()[:-1]
            entry.delete(0, END)
            entry.insert(0, nums_till_last)
        else:
            self.on_return_key(entry)

    def on_shift_key(self, value):
        if self.shift is False:
            for button in self.keyboard_frame.winfo_children():
                button.config(text=button["text"].upper())
            self.shift = True
        else:
            for i, button in enumerate(self.keyboard_frame.winfo_children()):
                button.config(text=ALPHANUMERICS_ALL[i])
                self.shift = False

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
