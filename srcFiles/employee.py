from srcFiles.person import Person

class Employee(Person):
        #employeeID and grade are private attributes
        #grade values can be "junior", "senior", "manager", "director"
        def __init__(self, firstName, lastName, personalID, employeeID, grade, salary):
                self.__employeeID = employeeID
                self.__grade = grade
                self.__salary = salary
                super().__init__(firstName, lastName, personalID)
                
        #getters
        def getEmployeeID(self):
                return self.__employeeID
        
        def getGrade(self):
                return self.__grade

        def getSalary(self):
                return self.__salary

        #setters
        def setEmployeeID(self, employeeID):
                self.__employeeID = employeeID

        def setGrade(self, grade):
                self.__grade = grade
                
        #methods 
        def toString(self):
                return (super().toString() + " " + str(self.getEmployeeID()))

