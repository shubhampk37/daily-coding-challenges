# HackerRank: Set .union() Operation
# Problem Link: https://www.hackerrank.com/challenges/py-set-union/problem

if __name__ == '__main__':
    # Number of English subscribers
    n = int(input())
    english = set(map(int, input().split()))
    
    # Number of French subscribers
    b = int(input())
    french = set(map(int, input().split()))
    
    # Print the total number of students with at least one subscription
    print(len(english | french))
    
