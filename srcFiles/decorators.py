from datetime import datetime
import time

"""
    This file include code to try and understand how decorators work
"""

"""
    This decorator method include functionality to log the date and time that the method is called 
"""
def logDatetime(method):
    def wrapper():
        print("Date and Time before calling the function: ", datetime.now())
        method()
        print("Date and Time after calling the function: ", datetime.now())
    return wrapper

@logDatetime
def myMethod():
    print("myMethod() is called")
    time.sleep(3)
    
#Method call to test the decorator functionality
myMethod()