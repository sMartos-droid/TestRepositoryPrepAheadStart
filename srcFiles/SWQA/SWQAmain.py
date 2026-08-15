import sys
from pathlib import Path

script_dir = Path(__file__).resolve().parent
if str(script_dir) not in sys.path:
   sys.path.insert(0, str(script_dir))

from testResults import TestResults

#adding the test results for the iteration SW1.1.5 of the SW6 release
testResultsLastIteration = TestResults("ARRAKIS", "SW.6", "SW.1.1.5")
testResultsLastIteration.set_result(13245, "SW6-[StartUp](powerConsumption)", "BLOCKED", 135, "re-validation of issue ID: 13543")
testResultsLastIteration.set_result(13246, "SW6-[Actuation](ActiveDischarge)", "PASSED", 1520, "N/A")
testResultsLastIteration.set_result(13247, "SW6-[Acquisition](HvVoltage)", "PASSED", 920, "new test content added to the test suite")
testResultsLastIteration.connection_close()
print("Path of the results database:", testResultsLastIteration.get_database_path())

#adding the test results for the iteration SW1.1.5 of the SW6 release
testResultsLastIteration = TestResults("ARRAKIS", "SW.6", "SW.1.2.0")
testResultsLastIteration.set_result(13245, "SW6-[StartUp](powerConsumption)", "PASSED", 135, "re-validation of issue ID: 13550")
testResultsLastIteration.set_result(13246, "SW6-[Actuation](ActiveDischarge)", "PASSED", 1520, "regression testing")
testResultsLastIteration.set_result(13247, "SW6-[Acquisition](HvVoltage)", "PASSED", 920, "regression testing")
testResultsLastIteration.set_result(13247, "SW6-[Acquisition](CoreTemperature)", "PASSED", 1300, "new content added to the test suite")
testResultsLastIteration.connection_close()
print("Path of the results database:", testResultsLastIteration.get_database_path())