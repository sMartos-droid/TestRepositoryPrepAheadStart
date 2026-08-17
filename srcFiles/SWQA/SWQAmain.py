import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
srcfiles_dir = project_root / "srcFiles"

for directory in (project_root, srcfiles_dir):
    dir_str = str(directory)
    if dir_str not in sys.path:
        sys.path.insert(0, dir_str)

from srcFiles.SWQA.TestEngine.testReporter import TestReporter

#adding the test results for the iteration SW1.1.5 of the SW6 release
testResultsLastIteration = TestReporter("ARRAKIS", "SW.6", "SW.1.1.5")
testResultsLastIteration.set_result(13245, "SW6-[StartUp](powerConsumption)", "BLOCKED", 135, "re-validation of issue ID: 13543")
testResultsLastIteration.set_result(13246, "SW6-[Actuation](ActiveDischarge)", "PASSED", 1520, "N/A")
testResultsLastIteration.set_result(13247, "SW6-[Acquisition](HvVoltage)", "PASSED", 920, "new test content added to the test suite")
testResultsSingleItem = testResultsLastIteration.fetchTestResults(13247)
print("Test result for test ID 13247:", testResultsSingleItem)
print("Test result for test case name: SW6-[StartUp](powerConsumption):", testResultsSingleItem)
testResultsLastIteration.connection_close()

#adding the test results for the iteration SW1.1.5 of the SW6 release
testResultsLastIteration = TestReporter("ARRAKIS", "SW.6", "SW.1.2.0")
testResultsLastIteration.set_result(13245, "SW6-[StartUp](powerConsumption)", "PASSED", 135, "re-validation of issue ID: 13550")
testResultsLastIteration.set_result(13246, "SW6-[Actuation](ActiveDischarge)", "PASSED", 1520, "regression testing")
testResultsLastIteration.set_result(13247, "SW6-[Acquisition](HvVoltage)", "PASSED", 920, "regression testing")
testResultsLastIteration.set_result(13247, "SW6-[Acquisition](CoreTemperature)", "PASSED", 1300, "new content added to the test suite")
testResultsLastIteration.connection_close()
