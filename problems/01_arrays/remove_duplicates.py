"""
Problem: Remove Duplicates
Topic:   01_arrays
Date:    2026-11-12
Source:  https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Level:   easy

Description:
    Given a SORTED list, remove the duplicates IN PLACE so that each value
    appears only once, keeping the order. Return k, the number of unique
    values. The first k slots of the list must hold the unique values;
    what is after position k does not matter.
    Do NOT build a new list, set, or dict: O(1) extra memory.

Example:
    Input:  [1, 1, 2]
    Output: 2,  and the list starts with [1, 2, ...]

    Input:  [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    Output: 5,  and the list starts with [0, 1, 2, 3, 4, ...]

Hint:
    Two pointers again, both moving forward:
      - "write" marks where the next unique value should go
      - "read" scans every element
    Because the list is sorted, a duplicate is always equal to the
    element right before it. When is data[read] worth writing?

My approach:
    (explain your idea BEFORE you code it)

Complexity:
    Time:  O(?)
    Space: O(?)
"""


def solve(data):
    # TODO: write your solution here, return k
    pass


# ---------------------------------------------------------------------------
# Tests: add cases as (input, expected_unique_prefix)
# Run this file with:  python3 problems/01_arrays/remove_duplicates.py
# ---------------------------------------------------------------------------
TESTS = [
    ([1, 1, 2], [1, 2]),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),
    ([1, 2, 3], [1, 2, 3]),  # already unique
    ([5, 5, 5, 5], [5]),  # all the same
    ([7], [7]),  # single item
    ([], []),  # empty
    ([-2, -2, -1, 0, 0], [-2, -1, 0]),  # negatives
]


def run_tests():
    passed = 0
    for i, (data, expected) in enumerate(TESTS, 1):
        arr = list(data)
        k = solve(arr)
        if k == len(expected) and arr[:k] == expected:
            passed += 1
            print(f"  PASS test {i}")
        else:
            print(f"  FAIL test {i}: input={data!r} expected k={len(expected)} prefix={expected!r} got k={k!r} list={arr!r}")
    print(f"{passed}/{len(TESTS)} passed")
    return passed == len(TESTS)


if __name__ == "__main__":
    ok = run_tests()
    raise SystemExit(0 if ok else 1)
