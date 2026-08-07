class Person:
    def __init__(self, firstName, lastName, personalID):
        #inner fields (priavate with __)
        self.__firstName = firstName
        self.__lastName = lastName
        self.__personalID = personalID
        
    #getters
    def getFirstName(self):
        return self.__firstName
    
    def getLastName(self):
        return self.__lastName
    
    def getPersonalID(self):
        return self.__personalID
    
    #setters
    def setFirstName(self, name):
        self.__firstName = name
    
    def setLastName(self, surname):
        self.__lastName = surname
    
    def setPersonalID(self, idNumber):
        self.__personalID = idNumber
        
    #Methods
    def toString(self):
        return str(self.getFirstName() + " " + self.getLastName() + " " + str(self.getPersonalID()))
    