# HackerRank: Exceptions
# Problem Link: https://www.hackerrank.com/challenges/exceptions/problem

for _ in range(int(input())):
    try:
        a, b = input().split()
        print(int(a) // int(b))
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)
