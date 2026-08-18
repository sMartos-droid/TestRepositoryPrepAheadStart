from decoratorsLib import DecoratorsLib
import time


@DecoratorsLib.logDatetime
def myMethod():
    print("myMethod() is called")
    time.sleep(3)

@DecoratorsLib.iterateTwice
def myPrintMessage(message):
    print(message)
    
#Method call to test the decorator functionality
myMethod()
myPrintMessage("Hello Leander")
print("myPrintMessage() __name__ property: ", myPrintMessage.__name__)
print("myPrintMessage() __doc__ property: ", myPrintMessage.__doc__)