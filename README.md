# Python Algorithms & OOP: Daily Practice

Goal: solve **1–2 problems per day**, typed by hand, each one with tests.

## Project layout

```
python_algos/
├── problems/          # algorithm problems, one folder per topic (in study order)
│   ├── 01_arrays/
│   ├── 02_strings/
│   ├── ...
│   └── 13_dynamic_programming/
├── oop/               # object-oriented programming exercises
├── sandbox/           # free experiments and scratch code (not tested)
├── templates/         # file templates used by new.py
├── new.py             # creates a new problem file and logs it
├── run_all.py         # runs the tests in every problem file
└── PROGRESS.md        # your daily log
```

## Daily routine (about 30–60 minutes)

1. **Pick** the next problem from the roadmap below (or LeetCode / HackerRank).
2. **Create** the file:
   ```bash
   python3 new.py arrays two_sum
   ```
3. **Understand** it: fill in the description, an example, and *your approach in words* before writing any code.
4. **Write tests first.** Add `(input, expected)` pairs to `TESTS`, including edge cases (empty list, one item, negative numbers).
5. **Code** `solve()` and run it:
   ```bash
   python3 problems/01_arrays/two_sum.py
   ```
6. **Analyze** the time and space complexity (Big-O) and write it in the docstring.
7. **Log** it: mark ✅ in `PROGRESS.md` and commit:
   ```bash
   git add . && git commit -m "arrays: two_sum"
   ```

Check that everything still passes with `python3 run_all.py`.

**Stuck for more than 30 minutes?** Read a hint or a solution, then close it and write the code again from memory the next day. Mark it 🔁 in the log.

## Roadmap

Roughly one topic per week. Do a few algorithm problems, then an OOP exercise.

| Week | Topic | Suggested problems |
|------|-------|--------------------|
| 1 | Arrays | max of list (no `max()`), reverse list, second largest, running sum, missing number, two sum, remove duplicates, move zeros, best time to buy/sell stock, rotate array, max subarray (Kadane), product except self |
| 2 | Strings | reverse string, palindrome, count vowels, valid anagram, first unique char, longest common prefix |
| 3 | Hashing (dict/set) | contains duplicate, word frequency, group anagrams, intersection of arrays, top k frequent |
| 4 | Two pointers | valid palindrome, merge sorted arrays, container with most water, 3sum |
| 5 | Sliding window | max sum subarray of size k, longest substring without repeats, min size subarray sum |
| 6 | Stacks & queues | valid parentheses, min stack, implement queue with stacks, daily temperatures |
| 7 | Linked lists | build a `Node`/`LinkedList` class, reverse list, detect cycle, merge two lists, middle node |
| 8 | Recursion | factorial, fibonacci, power, sum of digits, flatten nested list |
| 9 | Sorting & searching | bubble, selection, insertion, merge sort, quick sort, binary search |
| 10 | Trees | build a BST class, traversals (in/pre/post/level), max depth, invert tree, validate BST |
| 11 | Graphs | BFS, DFS, number of islands, flood fill, course schedule |
| 12 | Backtracking | subsets, permutations, combination sum, N-queens |
| 13 | Dynamic programming | climbing stairs, house robber, coin change, longest increasing subsequence |

### OOP track (`python3 new.py oop <name>`)

1. `bank_account`: deposit, withdraw, validation (build on `sandbox/first.py`)
2. `shapes`: base `Shape` with `area()`; `Circle`, `Rectangle` (inheritance and polymorphism)
3. `library_system`: `Book`, `Member`, `Library` working together (composition)
4. `inventory`: `@property`, `__str__`, `__eq__`, `@classmethod` constructors
5. `stack_and_queue_classes`: your own data structures with `__len__` and `__iter__`
6. `parking_lot`: a classic OOP design interview question

## Where to find more problems

- [LeetCode](https://leetcode.com/problemset/): filter by *Easy* and a topic tag
- [NeetCode 150](https://neetcode.io/practice): an ordered list with video explanations
- [HackerRank Python](https://www.hackerrank.com/domains/python)
- [Exercism Python track](https://exercism.org/tracks/python): good for OOP and idiomatic Python
