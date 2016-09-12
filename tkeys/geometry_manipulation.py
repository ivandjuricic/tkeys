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
