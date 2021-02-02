import functools
from mc import *


class listen:
    def __init__(self, name):
        self.eventname = name
        
    def __call__(self, function):
    
        @functools.wraps(function)
        def wrapped(arg):
            if isinstance(arg, dict): # while pyrunner is passing a dict as argument
                kwargs = arg # explicitly assign keyword arguments so they can be defined out of order.
                return function(**kwargs)
            else: # int typed argument, usually (player*)
                return function(arg)
        setListener(self.eventname, wrapped)
        return wrapped

