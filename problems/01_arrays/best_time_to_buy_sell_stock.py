"""
Problem: Best Time To Buy Sell Stock
Topic:   01_arrays
Date:    2026-11-12
Source:  https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Level:   easy (but the O(n) idea is the important lesson)

Description:
    prices[i] is the price of a stock on day i. You may buy on ONE day
    and sell on ONE LATER day. Return the maximum profit you can make.
    If no profit is possible, return 0.

Example:
    Input:  [7, 1, 5, 3, 6, 4]
    Output: 5           # buy on day 1 (price 1), sell on day 4 (price 6)

    Input:  [7, 6, 4, 3, 1]
    Output: 0           # prices only go down, never buy

Hint:
    Level 1: try every (buy day, sell day) pair.  O(n^2).
    Level 2: walk left to right keeping the LOWEST price seen so far.
             On each day, the best profit if you sell today is
             price - lowest_so_far. Keep the best of those.  O(n).
    Do level 2 if you can; compare with find_max.py: it is the same
    "remember the best so far" pattern, with one extra variable.

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
# Run this file with:  python3 problems/01_arrays/best_time_to_buy_sell_stock.py
# ---------------------------------------------------------------------------
TESTS = [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),  # always falling
    ([1, 2, 3, 4, 5], 4),  # always rising
    ([2, 4, 1], 2),  # the lowest price comes AFTER the best sale
    ([3, 3, 3], 0),  # flat
    ([5], 0),  # one day, cannot sell
    ([], 0),  # no days
    ([2, 1, 2, 1, 0, 1, 2], 2),
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
