Repeated Characters Matching
===



Given an input string (`s`) and a pattern (`p`), implement pattern matching with support for `'+'`, `'$'`,`'*'` and `'{N}'` which is optional where:

- `'+'` matches any single alphabetic character.
- `'$'` matches any number between `[1-9]`.
- `'*'` matches any sequence of the same characters of length 3 unless it is followed by `{N}`.
- `'{N}'` specifies how many characters to repeat for the sequence matched by `'*'`

The matching should cover the **entire** input string (not partial).



**Example 1 **

```
Input: s = "jtggggg", p = "++*{5}"
output: true
Explanation: "++" matches "jt" and "*{5}" matches "ggggg" which legnth is 5.
```

**Example 2**

```
Input: s = "abcdehhhhhh", p = "+++++*"
Output: false
Explanation: "+++++" matches "abcde", but "*" does not match "hhhhhh" because the length is not 3.
```

**Example 3 **

```
Input: s = "9mmmrrrkbb", p = "$**+*{2}"
Output: true
```



**Constraints:**

- `0 <= s.length, p.length <= 2000`
- `1 <= N <= 2000`
- `s` contains only numbers between `[1-9]` and lowercase English letters.
- `p` contains only `'+'`, `'$'`,`'*'` and `'{N}'`.