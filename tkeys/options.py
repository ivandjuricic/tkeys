valid_kwargs = {"layout": ["grid", "line"],
                "side": ["bottom", "top", "left", "right"]}


def set_defaults_(cls):
    for key in valid_kwargs.keys():
        setattr(cls, key, valid_kwargs[key][0])

def validate_kwarg_(key, value):
    if key not in valid_kwargs:
        raise KeyError("'%s' is not supported keyword argument" % key)
    if value in valid_kwargs[key]:
        return
    else:
        error_string = "'%s' not valid value for '%s' is not valid.\n" \
                       "\t\t\tAvailable arguments: %s" % (value, key, ', '.join(valid_kwargs[key]))
        raise ValueError(error_string)
