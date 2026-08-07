from srcFiles.person import Person

class Employee(Person):
        def __init__(self, firstName, lastName, personalID, employeeID):
                self.__employeeID = employeeID
                super().__init__(firstName, lastName, personalID)
                
        #getters
        def getEmployeeID(self):
                return self.__employeeID
        
        #setters
        def setEmployeeID(self, employeeID):
                self.__employeeID = employeeID
                
        #methods 
        def toString(self):
                return (super().toString() + " " + str(self.getEmployeeID()))

