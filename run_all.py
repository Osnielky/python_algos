"""
Run the tests in every problem and OOP file, then print a summary.

Usage:
    python3 run_all.py            # everything
    python3 run_all.py arrays     # only folders whose name contains "arrays"
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent


def main():
    filter_text = sys.argv[1] if len(sys.argv) > 1 else ""
    files = sorted(list((ROOT / "problems").rglob("*.py")) + list((ROOT / "oop").rglob("*.py")))
    files = [f for f in files if filter_text in str(f.relative_to(ROOT))]

    if not files:
        print("No problem files yet. Create one with: python3 new.py arrays two_sum")
        return

    passed, failed = [], []
    for f in files:
        result = subprocess.run([sys.executable, str(f)], capture_output=True, text=True, timeout=30)
        (passed if result.returncode == 0 else failed).append(f.relative_to(ROOT))

    for f in passed:
        print(f"  ✅ {f}")
    for f in failed:
        print(f"  ❌ {f}")
    print(f"\n{len(passed)} passing, {len(failed)} failing, {len(files)} total")


if __name__ == "__main__":
    main()
