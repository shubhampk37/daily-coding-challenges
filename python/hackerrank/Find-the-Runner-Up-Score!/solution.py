# HackerRank: Find the Runner-Up Score!
# Problem Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    
    # Use a set to eliminate duplicate scores in O(n) time
    scores = set(map(int, input().split()))
    
    # Remove top score to find the runner-up
    scores.remove(max(scores))
    print(max(scores))