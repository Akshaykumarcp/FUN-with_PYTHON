""" def do_twice(func):
    def wrapper_do_twice(*args, **kwargs): # accepts any number of arguments and passes them on to the function it decorates
        func(*args, **kwargs)
        # func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice """

import functools

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice