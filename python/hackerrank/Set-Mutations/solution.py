# HackerRank: Set Mutations
# Problem Link: https://www.hackerrank.com/challenges/py-set-mutations/problem

def set_mutations() -> int :
    # length set A (of no use)
    input()
    A = set(map(int, input().split()))
    
    # Number of operations
    N = int(input())
    
    for _ in range(N):
        op_name, _ = input().split()
        other_set = set(map(int, input().split()))
        
        # Execute the mutation on set A
        if hasattr(A, op_name):
            getattr(A, op_name)(other_set)
            
    return sum(A)
        
if __name__ == '__main__':
    print(set_mutations())
    
