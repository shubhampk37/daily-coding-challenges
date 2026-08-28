# HackerRank: Set .difference() Operation
# Problem Link: https://www.hackerrank.com/challenges/py-set-difference-operation/problem

if __name__ == '__main__':
    # Number of English newspaper subscribers
    n = int(input())
    
    # roll numbers of students having English newspaper
    english = set(map(int, input().split()))
    
    # Number of English newspaper subscribers
    b = int(input())
    
    # roll numbers of students having French newspaper
    french = set(map(int, input().split()))
    
    print(len(english.difference(french)))
    
