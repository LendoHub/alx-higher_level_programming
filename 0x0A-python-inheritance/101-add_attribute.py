ble File  10 lines (8 sloc)  303 Bytes

#!/usr/bin/python3
"""this module defines a function that adds attributes to objects"""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
