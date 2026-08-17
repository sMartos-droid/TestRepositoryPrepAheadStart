from abc import abstractmethod
"""
This class is intended to be the base class for all the test cases.
Inner fields:
    __testCaseName: The name of the test case.
    __testCaseID: The ID of the test case.
    __testCaseDescription: The description of the test case.
    __numberOfSteps: The number of steps in the test case.
Methods:
    getTestCaseName: Returns the name of the test case.
    getTestCaseID: Returns the ID of the test case.
    getTestCaseDescription: Returns the description of the test case.
    getNumberOfSteps: Returns the number of steps in the test case.
    setTestCaseName: Sets the name of the test case.
    setTestCaseID: Sets the ID of the test case.
    setTestCaseDescription: Sets the description of the test case.
    setNumberOfSteps: Sets the number of steps in the test case.
    setupTestCase: Abstract method to setup particular conditions for the test case. This method is called before the test case execution.
    executeTestCase: Abstract method to execute the test case.
    cleanupTestCase: Abstract method to cleanup after the test case execution.
""" 

class TestCaseBase:
    def __init__(self, testCaseName, testCaseID, testCaseDescription, numberOfSteps):
        #inner fields (priavate with __)
        self.__testCaseName = testCaseName
        self.__testCaseID = testCaseID
        self.__testCaseDescription = testCaseDescription
        self.__numberOfSteps = numberOfSteps
    def getTestCaseName(self):
        return self.__testCaseName  
    def getTestCaseID(self):
        return self.__testCaseID
    def getTestCaseDescription(self):
        return self.__testCaseDescription
    def getNumberOfSteps(self):
        return self.__numberOfSteps
    def setTestCaseName(self, name):
        self.__testCaseName = name
    def setTestCaseID(self, idNumber):
        self.__testCaseID = idNumber
    def setTestCaseDescription(self, description):
        self.__testCaseDescription = description
    def setNumberOfSteps(self, steps):
        self.__numberOfSteps = steps
    #Methods
        #setup particular conditions for the test case. 
        #this method is called before the test case execution
    #Parameters:
    #    N/A
    #Returns:
    #(bool): true if the execution was successful, false otherwise
    @abstractmethod
    def setupTestCase(self):
        pass
    #Methods
        #This method is called to execute the test case.
        #All the steps to execute the test case are implemented in this method.
    #Parameters:
    #    N/A
    #Returns:
    #(bool): true if the execution was successful, false otherwise
    @abstractmethod
    def executeTestCase(self):
        pass
    @abstractmethod
    def cleanupTestCase(self):
        pass
    def toString(self):
        return str(self.getTestCaseName() + " " + str(self.getTestCaseID()) + " " + self.getTestCaseDescription())
