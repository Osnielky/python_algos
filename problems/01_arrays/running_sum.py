"""
Problem: Running Sum
Topic:   01_arrays
Date:    2026-11-12
Source:  https://leetcode.com/problems/running-sum-of-1d-array/
Level:   easy

Description:
    Given a list nums, return a NEW list where result[i] is the sum of
    nums[0] + nums[1] + ... + nums[i].
    This is called a "prefix sum" and is a building block for many
    harder array problems (range sums, subarray sums, etc.).

Example:
    Input:  [1, 2, 3, 4]
    Output: [1, 3, 6, 10]      # 1, 1+2, 1+2+3, 1+2+3+4

Hint:
    result[i] = result[i-1] + nums[i]. You only need the previous total,
    not a nested loop. A nested loop would be O(n^2): can you do O(n)?

My approach:
    (go 1 by one , save the actual to be added to the next one , manage edge cases. )

Complexity:
    Time:  O(?)
    Space: O(?)   (does the output list count? say what you decided)
"""


def solve(data):
    if len(data) == 0:
        return None
    if len(data) == 1:
        return data

    for index, ele in data:
        data[index +1 ] += data [index]



# ---------------------------------------------------------------------------
# Tests: add cases as (input, expected_output)
# Run this file with:  python3 problems/01_arrays/running_sum.py
# ---------------------------------------------------------------------------
TESTS = [
    ([1, 2, 3, 4], [1, 3, 6, 10]),
    ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
    ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
    ([5], [5]),  # single item
    ([], []),  # empty
    ([2, -3, 4, -1], [2, -1, 3, 2]),  # negatives
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
