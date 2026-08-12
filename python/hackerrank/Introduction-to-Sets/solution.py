# HackerRank: Introduction to Sets
# Problem Link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    unique_plant_heights = set(array)
    return round(sum(unique_plant_heights) / len(unique_plant_heights), 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
