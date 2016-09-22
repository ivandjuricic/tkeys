import sys
if sys.version_info[0] == 2:
    from Tkinter import *
else:
    from tkinter import *

def from_pack(parent):
    first_widget = parent.winfo_children()[0]
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
    return "pack"


def from_grid(parent):
    return "grid"


def from_place(parent):
    return "place"


def geometry_manager_change_(parent):
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

def init_container_(cls):
    if cls.keyboard_frame:
        cls.keyboard_frame.destroy()

    cls.keyboard_frame = Frame(cls.parent)

    if "place" in cls.__dict__:
        cls.keyboard_frame.place(relx=cls.place[0], rely=cls.place[1], anchor=cls.place[2])
        return

    if cls.gm in ["pack", "place"]:
        if cls.side == "bottom":
            cls.keyboard_frame.grid(row=999, column=0, columnspan=999)
        elif cls.side == "right":
            cls.keyboard_frame.grid(column=999, row=0, rowspan=999)
    else:
        if cls.side == "bottom":
            cls.keyboard_frame.place(rely=0.98, relx=0.5, anchor=S)
        elif cls.side == "right":
            cls.keyboard_frame.place(rely=0.5, relx=0.98, anchor=E)
