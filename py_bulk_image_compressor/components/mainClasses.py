#!/usr/bin/python

class set_default_values:
    """
    Assigns a default value if the provided argument is None.
    Usage:
        set_default_values(default, provided)
    """
    def __init__(self, *args):
        # args[0] -> default, args[1] -> provided
        if args[1] is None:
            self.set = args[0]
        else:
            self.set = args[1]
        # Allow additional attributes like user_specified
        self.user_specified = None