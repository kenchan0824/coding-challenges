Given an array A[] of N non-negative integers representing height of blocks at index i as A[i], where the width of each block is 1. Compute how much water can be trapped in between blocks after raining.

Structure is like below:

|o|
|o|
+-+
We can trap 2 units of water in the middle gap.

     |
|oooo|
|oo|o|
|oo|o|
+--+-+
Bars for input {3, 0, 0, 2, 0, 4}
Total trapped water = 3 + 3 + 1 + 3 = 10

Output the total unit of water trapped in between the blocks.

Constraints:
3 <= N <= 10^7
0 <= A[i] <= 10^8