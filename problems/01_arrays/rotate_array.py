"""
Problem: Rotate Array
Topic:   01_arrays
Date:    2026-11-12
Source:  https://leetcode.com/problems/rotate-array/
Level:   medium

Description:
    Rotate the list to the RIGHT by k steps, in place. Return the same list.
    k can be larger than len(data).

Example:
    Input:  nums = [1, 2, 3, 4, 5, 6, 7], k = 3
    Output: [5, 6, 7, 1, 2, 3, 4]

    Input:  nums = [1, 2], k = 3        # 3 % 2 = 1 real step
    Output: [2, 1]

Hint:
    Level 1: pop the last element and insert it at the front, k times.
             Works, but list.insert(0, x) is O(n), so this is O(n*k).
    Level 2: the "three reversals" trick, O(n) time and O(1) space:
             reverse the whole list, then reverse the first k elements,
             then reverse the rest. Try it on paper with the example
             before coding. You already wrote a reverse in reverse_list.py:
             make a helper reverse(data, lo, hi).
    Don't forget k = k % len(data).

My approach:
    (explain your idea BEFORE you code it)

Complexity:
    Time:  O(?)
    Space: O(?)
"""


def solve(nums, k):
    # TODO: write your solution here
    pass


# ---------------------------------------------------------------------------
# Tests: add cases as ((nums, k), expected_output)
# Run this file with:  python3 problems/01_arrays/rotate_array.py
# ---------------------------------------------------------------------------
TESTS = [
    (([1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 1, 2, 3, 4]),
    (([1, 2], 3), [2, 1]),  # k bigger than n
    (([1, 2, 3], 0), [1, 2, 3]),  # no rotation
    (([1, 2, 3], 3), [1, 2, 3]),  # full turn = no rotation
    (([-1, -100, 3, 99], 2), [3, 99, -1, -100]),
    (([1], 5), [1]),  # single item
    (([], 2), []),  # empty
]


def run_tests():
    passed = 0
    for i, ((nums, k), expected) in enumerate(TESTS, 1):
        original = list(nums)
        result = solve(original, k)
        if result is original and result == expected:
            passed += 1
            print(f"  PASS test {i}")
        elif result is not original:
            print(f"  FAIL test {i}: must rotate in place and return the SAME list object")
        else:
            print(f"  FAIL test {i}: nums={nums!r} k={k} expected={expected!r} got={result!r}")
    print(f"{passed}/{len(TESTS)} passed")
    return passed == len(TESTS)


if __name__ == "__main__":
    ok = run_tests()
    raise SystemExit(0 if ok else 1)
