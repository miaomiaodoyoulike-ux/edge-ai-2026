# Day 01 LeetCode
## 1. Two Sum
Link: https://leetcode.cn/problems/two-sum/
## Idea
Use a hash table to store numbers that have already been seen.

For each number `nums[i]`, calculate:
```text
target - nums[i]
```
If this complement already exists in the hash table, then we have found the answer.
## Complexity
- The answer should be indices, not values.
- Do not use the same element twice.
- The hash table should store text target - nums[i]

## 2、Valid Parentheses
Link: https://leetcode.cn/problems/valid-parentheses/
## Idea
Use a stack.
- If the character is a left bracket, push it into the stack.
- If the character is a right bracket, check whether it matches the top of the stack.
- If it matches, pop the stack.
- If it does not match, return false.
- At the end, the stack should be empty.
## Complexity
- Time complexity: O(n)
- Space complexity: O(n)
## Mistakes
s
