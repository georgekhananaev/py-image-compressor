#!/usr/bin/python

# defining given parameters or default parameters for functions
class set_default_values:
    def __init__(self, *args):  # args receives unlimited no. of arguments as an array
        if args[1] is None:
            self.set = args[0]
        else:  # if variable is none, will instead use default value.
            self.set = args[1]
