"""
Problem: Find Max
Topic:   01_arrays
Date:    2026-09-18
Source:  www.codechef.com

Description:
   Given a list of integers, representing height of mountains. Find the height of the tallest mountain.



Example:
    Input:  ...
    Output: ...

My approach:
    Im going element by element , every time I find a greater element I will  store it in a variable to be returned after 

Complexity:
    Time:  O(?)
    Space: O(?)
"""


def solve(data):
    # TODO: write your solution here
    bigger = data[0];

    for ele in data:
if (ele > bigger)
bigger = ele;


    return 7

    pass


# ---------------------------------------------------------------------------
# Tests: add cases as (input, expected_output)
# Run this file with:  python3 problems/01_arrays/find_max.py
# ---------------------------------------------------------------------------
TESTS = [
    ([3, 7, 2], 7),           # normal case, max in the middle
    ([4], 4),                 # single item
    ([1, 2, 9], 9),           # max at the end
    ([9, 2, 1], 9),           # max at the start
    ([-5, -1, -9], -1),       # all negatives
    ([5, 5, 5], 5),           # repeated values
]

def run_tests():
    if not TESTS:
        print("No tests yet. Add some to TESTS.")
        return False
    passed = 0
    for i, (data, expected) in enumerate(TESTS, 1):
        result = solve(data)
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
