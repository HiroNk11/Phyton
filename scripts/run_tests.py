import subprocess
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    test_path = root / "08_testing"
    command = [sys.executable, "-m", "unittest", "discover", "-s", str(test_path)]
    return subprocess.call(command, cwd=root)


if __name__ == "__main__":
    raise SystemExit(main())
