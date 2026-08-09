import sys
from pathlib import Path

script_dir = Path(__file__).resolve().parent
if str(script_dir) not in sys.path:
   sys.path.insert(0, str(script_dir))

from testResults import TestResults


testResultsLastIteration = TestResults("ARRAKIS", "SW.6")
print("Path of the results database:", testResultsLastIteration.get_database_path())