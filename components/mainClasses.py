#!/usr/bin/python
class set_default_values:  # defining car class
    def __init__(self, *args):  # args receives unlimited no. of arguments as an array
        if args[1] is None:
            self.set = args[0]
        else:
            self.set = args[1]