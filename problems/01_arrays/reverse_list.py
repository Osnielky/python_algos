"""
Problem: Reverse List
Topic:   01_arrays
Date:    2026-11-12
Source:  classic (LeetCode 344 is the string version)
Level:   easy

Description:
    Reverse a list IN PLACE, without using reversed(), slicing [::-1]
    or list.reverse(). Return the same list object.

Example:
    Input:  [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1]

Hint:
    Two pointers: one at the start, one at the end. Swap, move both
    inward, stop when they meet. How many swaps for n elements?

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
# Run this file with:  python3 problems/01_arrays/reverse_list.py
# ---------------------------------------------------------------------------
TESTS = [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),  # odd length
    ([1, 2, 3, 4], [4, 3, 2, 1]),  # even length
    ([7], [7]),  # single item
    ([], []),  # empty
    ([2, 2, 2], [2, 2, 2]),  # all the same
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
            print(f"  FAIL test {i}: must reverse in place and return the SAME list object")
        else:
            print(f"  FAIL test {i}: input={data!r} expected={expected!r} got={result!r}")
    print(f"{passed}/{len(TESTS)} passed")
    return passed == len(TESTS)


if __name__ == "__main__":
    ok = run_tests()
    raise SystemExit(0 if ok else 1)
