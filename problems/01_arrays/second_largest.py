"""
Problem: Second Largest
Topic:   01_arrays
Date:    2026-11-12
Source:  classic interview warm-up
Level:   easy

Description:
    Return the second largest DISTINCT value in a list of integers.
    If there is no such value (fewer than 2 distinct numbers) return None.
    Do it in ONE pass, without sorting and without max().

Example:
    Input:  [3, 9, 2, 7, 5, 8, 1, 6]
    Output: 8

    Input:  [5, 5, 5]
    Output: None        # only one distinct value

Hint:
    Keep two variables: first (largest so far) and second.
    When a new element beats first, what happens to the old first?
    Be careful with duplicates of the max: [9, 9, 3] -> 3, not 9.

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
# Run this file with:  python3 problems/01_arrays/second_largest.py
# ---------------------------------------------------------------------------
TESTS = [
    ([3, 9, 2, 7, 5, 8, 1, 6], 8),  # normal case
    ([1, 2], 1),  # two items
    ([2, 1], 1),  # two items, reversed
    ([9, 9, 3], 3),  # duplicate max
    ([5, 5, 5], None),  # one distinct value
    ([4], None),  # single item
    ([], None),  # empty
    ([-3, -1, -2], -2),  # negatives
    ([1, 2, 3, 4, 5], 4),  # increasing
    ([5, 4, 3, 2, 1], 4),  # decreasing
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
