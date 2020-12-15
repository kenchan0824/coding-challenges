Rod Cutting
===



Given a rod of length `n` and an array of prices `P[]`, where `P[i]` is the price of a rod of length `i`.

The goal is to determine the **maximum revenue**, obtainable by cutting up the rod and selling the pieces.



**Example:**

```
Input: P = [1, 5, 8, 9], n = 4
Output: 10
Explanation:
If we do not cut the rod, we can earn p[4] = 9.
If we cut it into 4 pieces of length 1, we earn 4 x P[1] = 4.
If we cut it into 2 pieces of length 1 & a piece of length 2, we earn 2 x P[1] + P[2] = 9.
If we cut it into 2 pieces of length 2, we can earn 2 x P[2] = 10.
There are more options, but the maximum revenue is 10.
```



In general, rod of length `n` can be cut in `2^(n-1)` different ways, since we can choose cutting, or not cutting, at all distances `i (1 <= i <= n-1)` from the left end.



#dynamic-programing 	#O(n)