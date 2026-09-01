# HackerRank: Check Subset
# Problem Link: https://www.hackerrank.com/challenges/py-check-subset/problem

def check_subset(set_a: set, set_b: set) -> bool:
    "Determines if set_a is a subset if set_b"
    return set_a.issubset(set_b)

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        input() # Discard the size of A
        A = set(map(int, input().split()))
        
        input() # Discard the size of B
        B = set(map(int, input().split()))
        print(check_subset(A, B))

    
    
