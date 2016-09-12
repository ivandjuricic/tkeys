valid_kwargs = {"layout": ["grid", "line"],
                "side": ["bottom", "top", "left", "right"],
                }

tk_kwargs = ["activebackground", "activeforeground", "background", "bg", "bd", "borderwidth",
             "cursor", "disabledforeground", "font", "foreground", "fg", "highlightbackground",
             "highlightcolor", "highlightthickness", "overrelief", "relief", "underline"]


def set_defaults_(cls):
    for key in valid_kwargs.keys():
        setattr(cls, key, valid_kwargs[key][0])


def validate_kwarg_(key, value):
    if key not in valid_kwargs:
        if key not in tk_kwargs:
            raise KeyError("'%s' is not supported keyword argument" % key)
        else:
            return
    if valid_kwargs[key][0] is None:
        return
    if value in valid_kwargs[key]:
        return
    else:
        error_string = "'%s' not valid value for '%s' is not valid.\n" \
                       "\t\t\tAvailable arguments: %s" % (value, key, ', '.join(valid_kwargs[key]))
        raise ValueError(error_string)
