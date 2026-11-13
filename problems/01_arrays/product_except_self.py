"""
Problem: Product Except Self
Topic:   01_arrays
Date:    2026-11-12
Source:  https://leetcode.com/problems/product-of-array-except-self/
Level:   medium

Description:
    Return a new list where result[i] is the product of ALL the elements
    except nums[i]. You must NOT use division (think about zeros), and
    the goal is O(n) time.

Example:
    Input:  [1, 2, 3, 4]
    Output: [24, 12, 8, 6]      # 2*3*4, 1*3*4, 1*2*4, 1*2*3

    Input:  [-1, 1, 0, -3, 3]
    Output: [0, 0, 9, 0, 0]

Hint:
    Level 1: nested loops, multiply everything except i.  O(n^2).
    Level 2: the product except i = (product of everything LEFT of i)
             * (product of everything RIGHT of i).
             Pass 1, left to right: result[i] = product of nums[0..i-1]
             Pass 2, right to left: multiply result[i] by the running
             product of nums[i+1..n-1], kept in ONE variable.
             This is the prefix-sum idea from running_sum.py, with * instead of +.

My approach:
    (explain your idea BEFORE you code it)

Complexity:
    Time:  O(?)
    Space: O(?)   (not counting the output list)
"""


def solve(data):
    # TODO: write your solution here
    pass


# ---------------------------------------------------------------------------
# Tests: add cases as (input, expected_output)
# Run this file with:  python3 problems/01_arrays/product_except_self.py
# ---------------------------------------------------------------------------
TESTS = [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),  # one zero
    ([0, 0, 2], [0, 0, 0]),  # two zeros: everything is 0
    ([2, 3], [3, 2]),  # two items
    ([5], [1]),  # single item: empty product is 1
    ([1, 1, 1, 1], [1, 1, 1, 1]),
    ([-2, -3, 4], [-12, -8, 6]),  # negatives
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
