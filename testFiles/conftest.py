from pathlib import Path
import sys

# Add the project root (parent of testFiles) to sys.path so tests can import srcFiles
project_root = Path(__file__).resolve().parents[1]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))
