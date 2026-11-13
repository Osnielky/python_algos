"""
Problem: Move Zeros
Topic:   01_arrays
Date:    2026-11-12
Source:  https://leetcode.com/problems/move-zeroes/
Level:   easy

Description:
    Move all the 0s to the END of the list IN PLACE, keeping the relative
    order of the non-zero elements. Do it without making a copy of the list.
    Return the same list object.

Example:
    Input:  [0, 1, 0, 3, 12]
    Output: [1, 3, 12, 0, 0]

Hint:
    Same "write / read" pointer idea as remove_duplicates:
    every time read finds a non-zero, put it at write and advance write.
    After the scan, what should fill the slots from write to the end?
    Bonus: can you do it with swaps in one pass instead of filling zeros after?

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
# Run this file with:  python3 problems/01_arrays/move_zeros.py
# ---------------------------------------------------------------------------
TESTS = [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0], [0]),  # single zero
    ([1, 2, 3], [1, 2, 3]),  # no zeros
    ([0, 0, 0], [0, 0, 0]),  # all zeros
    ([0, 0, 1], [1, 0, 0]),  # zeros first
    ([1, 0, 0, 2, 0, 3], [1, 2, 3, 0, 0, 0]),  # order must be kept
    ([], []),  # empty
]


def run_tests():
    passed = 0
    for i, (data, expected) in enumerate(TESTS, 1):
        original = list(data)
        result = solve(original)
        if result is original and result == expected:
            passed += 1
            print(f"  PASS test {i}")
        elif result is not original:
            print(f"  FAIL test {i}: must modify in place and return the SAME list object")
        else:
            print(f"  FAIL test {i}: input={data!r} expected={expected!r} got={result!r}")
    print(f"{passed}/{len(TESTS)} passed")
    return passed == len(TESTS)


if __name__ == "__main__":
    ok = run_tests()
    raise SystemExit(0 if ok else 1)
