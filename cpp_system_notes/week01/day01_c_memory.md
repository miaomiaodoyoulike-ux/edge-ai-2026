# DAY 01 - C memory notes
## Program
File: 'array_sum.c'
This program calculates the sum of an integer array and prints the memory addression of 'num[0]' and 'num[1]'
## Output 
```text
sum = 15
address nums[0] = 000000000062FE00
address nums[1] = 000000000062FE04
 and performance optimization.

```
##  Observation
The address of nums[1] is 4 bytes larger than the address of nums[0]
##  Understanding
- An int usually takes 4 bytes on my current environment.
- Array elements are stored continuously in memory.
- &nums[0] means the address of the first element.
- &nums[1] means the address of the second element.
- This memory layout is important for understanding C, embedded systems, image data, and performance optimization.