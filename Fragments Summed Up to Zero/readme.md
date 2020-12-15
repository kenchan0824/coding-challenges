Write a function solution that, given an array `A` consisting of `N` integers, returns the number of fragments of `A` whose sum equals `0` (this is, pairs `(P, Q)` such that ` P <= Q ` and the sum `A[P] + A[P+1] + ... + A[Q]` is `0`). The function should return `-1` if this number exceeds `1,000,000,000`.



**Example 1:**
```
Input: A = [2, -2, 3, 0, 4, -7]
Output: 4
Explanation:
  2, -2, 3, 0, 4, -7  
  +---+     +  
         +---------+  
  +----------------+  
```



**Example 2:**

```
Input: A = [0, 0, ..., 0], N = 100,000
Output: -1.
```



**Assumptions:**

- `N` is an integer within the range`[1..100,000]`
- each element of array `A` is an integer within the range `[-10,000 .. 10,000]`



#prefix-sum 	#O(n)