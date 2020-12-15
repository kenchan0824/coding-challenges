Jump Game with Tunnel
===



Given an array of non-negative integers `arr`, first determine the largest element in the array, and then determine whether or not you can reach that same element within the array by moving left or right according to whatever integer is in the current spot. When you reach an edge, you will continue at the opposite edge as if there is an tunnel.

If you can reach the same spot within the array, then your program should output the least amount of jumps it took. 

If it is impossible to end up back at the largest element in the array your program should output `-1`. 



**Examples 1**

```
Input: [2,3,5,6,1]
Output: 2
Expanation: starting at the spot of 6, you jump 6 spaces to the right while looping around the array you end up at the last element, which is 1. Then from here you jump 1 space to the left and you're back where you started.
```



**Example 2**

```
Input: [1,2,3,4,2]
Output: 3
```



**Example 3**

```
Input: [1,7,1,1,1,1]
Output: 2
```



**Constraints**

- `1 <= arr.length <= 5 * 1e4`
- `0 <= arr[i] < 5 * 1e4`
- The largest element will be unique.



#tree 	#breadth-first-search 	#O(n)