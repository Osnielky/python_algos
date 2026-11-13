"""
Problem: Missing Number
Topic:   01_arrays
Date:    2026-11-12
Source:  https://leetcode.com/problems/missing-number/
Level:   easy

Description:
    A list contains n DISTINCT numbers taken from the range 0..n
    (so there are n+1 possible values but only n of them appear).
    Return the one number that is missing.

Example:
    Input:  [3, 0, 1]          # n = 3, range is 0..3, 2 is missing
    Output: 2

    Input:  [0, 1]             # n = 2, range is 0..2
    Output: 2

Hint:
    Level 1: build a set of what you have, loop 0..n and find the gap.
             That costs O(n) extra memory.
    Level 2: the sum 0+1+...+n is n*(n+1)/2. What is (that sum) minus
             (sum of the list)? That is O(1) extra memory.
    Try level 1 first, then level 2. Write both complexities down.

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
# Run this file with:  python3 problems/01_arrays/missing_number.py
# ---------------------------------------------------------------------------
TESTS = [
    ([3, 0, 1], 2),
    ([0, 1], 2),  # the last one is missing
    ([1], 0),  # zero is missing
    ([0], 1),
    ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    ([], 0),  # n = 0, range is 0..0
]


def run_tests():
    passed = 0
    for i, (data, expected) in enumerate(TESTS, 1):
        result = solve(list(data))
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
