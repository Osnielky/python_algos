"""
Create a new problem file from the template and log it in PROGRESS.md.

Usage:
    python3 new.py <topic> <name>
    python3 new.py arrays two_sum
    python3 new.py oop bank_account

Topic can be a short name ("arrays", "dp") or the full folder name ("01_arrays").
"""
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
PROBLEMS = ROOT / "problems"
PROGRESS = ROOT / "PROGRESS.md"

ALIASES = {"dp": "dynamic_programming", "stack": "stacks_queues", "queue": "stacks_queues",
           "sorting": "sorting_searching", "searching": "sorting_searching",
           "hash": "hashing", "linked_list": "linked_lists", "tree": "trees", "graph": "graphs"}


def find_topic_dir(topic):
    if topic == "oop":
        return ROOT / "oop"
    topic = ALIASES.get(topic, topic)
    for folder in sorted(PROBLEMS.iterdir()):
        if folder.is_dir() and (folder.name == topic or folder.name.split("_", 1)[1] == topic):
            return folder
    return None


def next_number():
    count = sum(1 for line in PROGRESS.read_text().splitlines() if line.startswith("| ") and line[2].isdigit())
    return count + 1


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        print("Topics:", ", ".join(f.name.split("_", 1)[1] for f in sorted(PROBLEMS.iterdir()) if f.is_dir()), "+ oop")
        sys.exit(1)

    topic, name = sys.argv[1], sys.argv[2].lower().replace("-", "_").replace(" ", "_")
    folder = find_topic_dir(topic)
    if folder is None:
        print(f"Unknown topic '{topic}'. Run `python3 new.py` to see the list.")
        sys.exit(1)

    path = folder / f"{name}.py"
    if path.exists():
        print(f"{path.relative_to(ROOT)} already exists.")
        sys.exit(1)

    template = (ROOT / "templates" / ("oop.py" if topic == "oop" else "problem.py")).read_text()
    rel = path.relative_to(ROOT)
    today = date.today().isoformat()
    path.write_text(
        template.replace("{title}", name.replace("_", " ").title())
        .replace("{topic}", folder.name)
        .replace("{date}", today)
        .replace("{path}", str(rel))
    )

    n = next_number()
    with PROGRESS.open("a") as f:
        f.write(f"| {n} | {today} | {folder.name} | [{name}]({rel}) | 🟡 in progress | |\n")

    print(f"Created {rel}  (problem #{n})")
    print(f"Run it with: python3 {rel}")


if __name__ == "__main__":
    main()
