"""
Problem: Two Sum
Topic:   01_arrays
Date:    2026-11-12
Source:  https://leetcode.com/problems/two-sum/
Level:   easy (the most famous interview question)

Description:
    Given a list of integers and a target, return the INDICES [i, j]
    (i < j) of the two numbers that add up to target.
    You may assume exactly one solution exists, and you cannot use the
    same element twice.

Example:
    Input:  nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]          # 2 + 7 = 9

Hint:
    Level 1 (arrays week): two nested loops, try every pair.  O(n^2) time.
    Level 2 (hashing week, come back later): one pass with a dict that
            remembers value -> index. For each x, is target - x already
            in the dict?  O(n) time, O(n) space.
    Do level 1 now. Mark the file 🔁 to redo it with a dict in week 3.

My approach:
    (explain your idea BEFORE you code it)

Complexity:
    Time:  O(?)
    Space: O(?)
"""


def solve(nums, target):
    # TODO: write your solution here
    pass


# ---------------------------------------------------------------------------
# Tests: add cases as ((nums, target), expected_output)
# Run this file with:  python3 problems/01_arrays/two_sum.py
# ---------------------------------------------------------------------------
TESTS = [
    (([2, 7, 11, 15], 9), [0, 1]),
    (([3, 2, 4], 6), [1, 2]),  # the answer is not the first element
    (([3, 3], 6), [0, 1]),  # same value twice, different indices
    (([1, 5, 9, 13], 22), [2, 3]),  # both at the end
    (([-1, -2, -3, -4, -5], -8), [2, 4]),  # negatives
    (([0, 4, 3, 0], 0), [0, 3]),  # zeros
]


def run_tests():
    passed = 0
    for i, ((nums, target), expected) in enumerate(TESTS, 1):
        result = solve(list(nums), target)
        if result is not None and sorted(result) == expected:
            passed += 1
            print(f"  PASS test {i}")
        else:
            print(f"  FAIL test {i}: nums={nums!r} target={target!r} expected={expected!r} got={result!r}")
    print(f"{passed}/{len(TESTS)} passed")
    return passed == len(TESTS)


if __name__ == "__main__":
    ok = run_tests()
    raise SystemExit(0 if ok else 1)
