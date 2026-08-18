import sys
from pathlib import Path

# Agregar el directorio padre al path antes de importar TestEngine
sys.path.insert(0, str(Path(__file__).parent.parent))

import time
from TestEngine.testCaseBase import TestCaseBase
from TestEngine.testReporter import TestReporter
from TestEngine.testReporter import TestStatus


class TC_ID26345(TestCaseBase):
    def __init__(self):
          super().__init__("SW.6[StartUp](LV current consumption)", 26345, "current consumption at start up", 3)
          #object to report the test results
          self.testReporter = TestReporter("ARRAKIS", "SW.6", "SW.1.3.0")
    def setupTestCase(self):
        super().setupTestCase()
        print("Setting up the test case: " + self.getTestCaseName() + " executing the setupTestCase() step")
        #setup particular conditions for the test case. 
        #this method is called before the test case execution
        return True
    def executeTestCase(self):
        print("Executing the test case: " + self.getTestCaseName() + " executing the executeTestCase() step")
        #All the steps to execute the test case are implemented in this method.
        #Wait 5 seconds to check the test time measurement feature
        time.sleep(5)
        return True
    def cleanupTestCase(self):
        super().cleanupTestCase()
        print("Cleaning up the test case: " + self.getTestCaseName() + " executing the cleanupTestCase() step")
        #cleanup after the test case execution
        #Report of test results
        self.testReporter.setResult(self.getTestCaseID(), self.getTestCaseName(), TestStatus.PASSED, self.getTestTime(), "LV current consumption at start up is inside the expected range")
        sys.path.insert(0, str(Path(__file__).parent.parent))
        #close the connection to the database
        self.testReporter.connection_close()
        return True