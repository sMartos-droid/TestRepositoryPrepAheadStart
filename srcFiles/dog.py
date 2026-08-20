""" This class models a dog"""
class Dog:
    def __init__(self, name, legs):
        #inner fields (priavate with __)
        self.__name = name
        self.__nrOflegs = legs
        
    #getters
    """
    Returns the name of dog
        Parameters:
            N/A
        Returns:
            (str): dog´s name
    """
    def getName(self):
        return self.__name
    """
    Returns the nr. of legs of the dog
        Parameters:
            N/A
        Returns:
            (str): dog´s name
    """
    def getNrOfLegs(self):
        return self.__nrOflegs
        
    #setters
    """
    set the dog´s name
        Parameters:
            (str): dog´s name
        Returns:
            none
    """
    def setName(self, name):
        self.__name = name
    """
    set the dog´s nr of legs
        Parameters:
            (int): dog´s nr. of legs
        Returns:
            none
    """
    def setNrOfLegs(self, legs):
        self.__nrOflegs = legs
            
    #methods
    def seak(self):
        print("guau gau")
        
        
        