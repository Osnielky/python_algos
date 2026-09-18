"""
Problem: Find Max
Topic:   01_arrays
Date:    2026-09-18
Source:  www.codechef.com

Description:
   Given a list of integers, representing height of mountains. Find the height of the tallest mountain.



Example:
    Input:  ...
    Output: ...

My approach:
    (explain your idea BEFORE you code it)

Complexity:
    Time:  O(?)
    Space: O(?)
"""


def solve(data):
    # TODO: write your solution here
    pass


# ---------------------------------------------------------------------------
# Tests: add cases as (input, expected_output)
# Run this file with:  python3 problems/01_arrays/find_max.py
# ---------------------------------------------------------------------------
TESTS = [
    # (input, expected),
]


def run_tests():
    if not TESTS:
        print("No tests yet. Add some to TESTS.")
        return False
    passed = 0
    for i, (data, expected) in enumerate(TESTS, 1):
        result = solve(data)
        if result == expected:
            passed += 1
            print(f"  PASS test {i}")
        else:
            print(f"  FAIL test {i}: input={data!r} expected={expected!r} got={result!r}")
    print(f"{passed}/{len(TESTS)} passed")
    return passed == len(TESTS)


if __name__ == "__main__":
    ok = run_tests()
    raise SystemExit(0 if ok else 1)
