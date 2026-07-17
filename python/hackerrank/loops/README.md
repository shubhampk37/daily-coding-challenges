# HackerRank: Python Loops

## Problem Link
[HackerRank Python Track: Loops](https://www.hackerrank.com/challenges/python-loops/problem)

## Problem Description
The challenge requires reading an integer $n$ from standard input. For all non-negative integers $i < n$, we must print $i^2$ on a separate line.

## Approach
Using Python's native `range(n)` function allows us to cleanly iterate through all non-negative integers starting from $0$ up to $n-1$. We print the square of each integer using the exponentiation operator (`**`).

## Code
```python
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i ** 2)
```