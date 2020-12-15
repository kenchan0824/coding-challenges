Maximum Size of Non-overlapping Segments
==

Located on a line are `N` segments, numbered from `0` to `N − 1`, whose positions are given in arrays `A` and `B`. For each `I` (`0 ≤ I < N`) the position of segment `I` is from `A[I]` to `B[I]` (inclusive). The segments are **sorted by their ends**, which means that `B[K] ≤ B[K + 1]` for `K` such that `0 ≤ K < N − 1`.

Two segments `I` and `J`, such that `I ≠ J`, are **overlapping** if they share *at least one common point*. In other words, `A[I] ≤ A[J] ≤ B[I]` or `A[J] ≤ A[I] ≤ B[J]`.

We say that the set of segments is non-overlapping if it contains no two overlapping segments. The goal is to **find the size of a non-overlapping set containing the maximal number of segments**.

Write a function:

```
def solution(A, B)
```

that, given two arrays `A` and `B` consisting of `N` integers, returns the size of a non-overlapping set containing a maximal number of segments.

**Example 1:**

Input:

```
    A[0] = 1    B[0] = 5
    A[1] = 3    B[1] = 6
    A[2] = 7    B[2] = 8
    A[3] = 9    B[3] = 9
    A[4] = 9    B[4] = 10
```
Output:

```
3
```

Explanation:

The segments are shown in the figure below.

```
    (1)        (3)
    -------     -
(0)         (2) (4)
---------   --- ---
1 2 3 4 5 6 7 8 9 0
```

The size of a non-overlapping set containing a maximal number of segments is 3. For example, possible sets are `{0, 2, 3}`, `{0, 2, 4}`, `{1, 2, 3}` or `{1, 2, 4}`. There is no non-overlapping set with four segments.



Assumptions:

- `N` is an integer within the range `[0..30,000]`
- each element of arrays `A`, `B` is an integer within the range `[0..1,000,000,000]`
- `A[I] ≤ B[I]`, for each `I (0 ≤ I < N)`
- `B[K] ≤ B[K+1]`, for each `K (0 ≤ K < N−1)`.



#greedy #event-scan