from tkeys.const import *
from tkinter import Button
from tkinter.font import Font
import warnings


def check_placement_manager_(cls_kwargs):
    if "place" in cls_kwargs and "side" in cls_kwargs:
        raise Exception("Side and place arguments found. Only one manager can be selected")



def set_defaults_(cls):
    font = 0
    for key in VALID_KWARGS.keys():
        setattr(cls, key, VALID_KWARGS[key][0])
        if key is "font":
            font = 1
    if font == 0:
        setattr(cls, "font", ("Ubuntu", 10))


def validate_kwarg_(key, value):
    if key not in VALID_KWARGS:
        if key == "place":
            return
        if key not in TK_KWARGS:
            raise KeyError("'%s' is not supported keyword argument" % key)
        else:
            return
    if VALID_KWARGS[key][0] is None:
        return
    if value in VALID_KWARGS[key]:
        return
    else:
        error_string = "'%s' not valid value for '%s' is not valid.\nAvailable arguments: %s" % (value, key, ', '.join(VALID_KWARGS[key]))
        raise ValueError(error_string)
