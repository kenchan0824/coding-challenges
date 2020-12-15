Longest Common Subsequence
===



Given two sequences, find the length of longest subsequence present in both of them. Both the strings are of uppercase.



**Example 1:**

```
Input:
X = "ABCDGH", Y = "AEDFHR", m = 6, n = 6
Output: 3
Explanation: LCS for input Sequences "ABCDGH" and "AEDFHR" is "ADH" of length 3.
```



**Example 2:**

```
Input: X = "ABC", Y = "AC", m = 3, n = 2
Output: 2
Explanation: LCS of "ABC" and "AC" is "AC" of length 2.
```



**Your Task:**

Complete the function `lcs()` which takes two strings and their lengths respectively as input parameters and returns the length of the longest subsequence present in both of them.

- Expected Time Complexity: `O(|X| x |Y|)`
- Expected Auxiliary Space: `O(|X| x |Y|)`



**Constraints:**
`1 <= size(X),size(Y) <= 100`



#string 	#dynamic-programming 	#O(m.n)