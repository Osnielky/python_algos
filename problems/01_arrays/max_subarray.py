"""
Problem: Max Subarray
Topic:   01_arrays
Date:    2026-11-12
Source:  https://leetcode.com/problems/maximum-subarray/
Level:   medium (Kadane's algorithm, a classic)

Description:
    A subarray is a CONTIGUOUS piece of the list (at least one element).
    Return the largest possible sum of a subarray.

Example:
    Input:  [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Output: 6           # the subarray [4, -1, 2, 1] has sum 6

    Input:  [-3, -1, -2]
    Output: -1          # all negative: the best is the single element -1

Hint:
    Level 1: for every start i and end j, sum data[i..j]. O(n^3), or O(n^2)
             if you keep a running sum while j grows.
    Level 2 (Kadane): walk once. Keep current = best sum of a subarray
             that ENDS here. At each element x:
                 current = max(x, current + x)
             (either extend the previous run, or start fresh at x).
             Keep the best current seen.  O(n) time, O(1) space.
    Bonus: this can also be done divide-and-conquer like findMax(lo, hi),
           in O(n log n). What makes the merge step harder than max()?

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
# Run this file with:  python3 problems/01_arrays/max_subarray.py
# ---------------------------------------------------------------------------
TESTS = [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1], 1),  # single item
    ([5, 4, -1, 7, 8], 23),  # whole list
    ([-3, -1, -2], -1),  # all negative: pick the biggest single element
    ([-1], -1),
    ([2, -1, 2, 3, 4, -5], 10),
    ([0, 0, 0], 0),
    ([3, -4, 5], 5),  # dropping the past beats keeping it
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
