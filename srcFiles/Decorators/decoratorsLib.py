from datetime import datetime
import time
import functools
"""
    This file include code to try and understand how decorators work
"""
class DecoratorsLib:
    @staticmethod
    def logDatetime(method):
        """
            log the datetime before and after calling a function
            Parameters:
                (func) the method to be decorated
            Returns:
                (func): the wraper function
        """
        def wrapper():
            print("Date and Time before calling the function: ", datetime.now())
            method()
            print("Date and Time after calling the function: ", datetime.now())
        return wrapper   
    @staticmethod
    def iterateTwice(method):
        """
        Execute a given method twice
        Parameters:
           (func) the method to be decorated 
           **args: the arguments to be passed to the method
           **kwargs: the keyword arguments to be passed to the method
        Returns:
           (func): the wraper function
        """
        #adding addtional decorator to keep atributes of the original method
        @functools.wraps(method)
        def wrapper(*args, **kwargs):
            method(*args, **kwargs)
            method(*args, **kwargs)
            return method(*args, **kwargs)
        return wrapper

    @staticmethod
    def debug(func):
        """Print the function signature and return value
        Parameters:
            (func) the method to be decorated 
        Returns: N/A
        """
        @functools.wraps(func)
        def wrapper_debug(*args, **kwargs):
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)
            print(f"Calling {func.__name__}({signature})")
            value = func(*args, **kwargs)
            print(f"{func.__name__}() returned {repr(value)}")
            return value
        return wrapper_debug
