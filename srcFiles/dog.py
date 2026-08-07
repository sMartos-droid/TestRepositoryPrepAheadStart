class Dog:
    def __init__(self, name, legs):
        #inner fields (priavate with __)
        self.__name = name
        self.__nrOflegs = legs
        
    #getters
    def getName(self):
        return self.__name
    def getNrOfLegs(self):
        return self.__nrOflegs
        
    #setters
    def setName(self, name):
        self.__name = name
    def setNrOfLegs(self, legs):
        self.__nrOflegs = legs
            
    #methods
    def seak(self):
        print("guau gau")
        
        
        