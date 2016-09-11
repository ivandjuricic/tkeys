from tkinter import *

from tkeys.options import validate_kwarg_, set_defaults_


class NumKeyPad:

    def __init__(self, parent, **kwargs):
        set_defaults_(self)
        self.parent = parent
        self.frame = None
        self.widget_list = []

        for key in kwargs:
            validate_kwarg_(key, kwargs[key])  # NAMING CONVENTION?!
            if key in kwargs:
                setattr(self, key, kwargs[key])

        self.widget_bindings()
        self.geometry_manager_change(self.parent)

    @staticmethod
    def geometry_manager_change(parent):
        ordering = "top"
        if not parent.winfo_children():
            raise AttributeError("No child widgets on parent")
        first_widget = parent.winfo_children()[0]
        if first_widget.winfo_manager() == "pack":
            ordering = first_widget.pack_info()["side"]

        children_list = []
        for child in parent.winfo_children():
            child.pack_forget()
            children_list.append(child)
        for i, child in enumerate(children_list):
            if ordering in ["top", "bottom"]:
                child.grid(column=0, row=i)
            else:
                child.grid(row=0, column=i)

    def widget_bindings(self):
        for widget in self.parent.winfo_children():
            if isinstance(widget, Entry):
                widget.bind("<ButtonRelease-1>", lambda w=widget: self.init_keyboard(w.widget))
                self.widget_list.append(widget)
            else:
                widget.bind("<Button-1>", lambda w: self.close_keyboard())

    def init_keyboard(self, widget):
        if self.frame:
            self.frame.destroy()

        width, height = self.parent.winfo_height(), self.parent.winfo_width()
        self.frame = Frame(self.parent, padx=1, pady=1)
        if self.side == "bottom":
            self.frame.grid(row=999, column=0, columnspan=999)
        elif self.side == "right":
            self.frame.grid(column=999, row=0, rowspan=999)

        buttons = [str(x + 1) for x in range(9)] + ["0", "←", "↵"]
        try:
            if self.layout == "grid":
                buttons[9], buttons[10] = buttons[10], buttons[9]
        except AttributeError:
            self.layout = "line"

        for i, text in enumerate(buttons):
            s = Button(self.frame,
                       text=text,
                       width=round(0.005 * width),
                       height=round(0.005 * width),
                       command=lambda name=text, w=widget: self.enter_key(name, w))
            if self.layout in ["line", None]:
                s.pack(side=LEFT, expand=True)
            elif self.layout is "grid":
                r, c = i//3, i % 3
                self.frame.grid_anchor(anchor=CENTER)
                s.grid(row=r, column=c)

    def enter_key(self, value, entry):
        v, e = value, entry
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

    def close_keyboard(self):
        try:
            self.frame.destroy()
        except AttributeError:
            return
        self.frame = None
