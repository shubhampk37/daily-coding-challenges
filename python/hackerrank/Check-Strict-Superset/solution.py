# HackerRank: Check Strict Superset
# Problem Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem

def check_superset(primary_set: set, candidate_sets: list[set[int]]) -> bool:
    """Determines if the primary_set is a strict superset of all candidate sets."""
    return all(primary_set > candidate_set for candidate_set in candidate_sets)
    
    
if __name__ == '__main__':
    
    primary_set = set(map(int, input().split()))
    
    set_count = int(input())
    candidate_sets = [set(map(int, input().split())) for _ in range(set_count)]
    
    print(check_superset(primary_set, candidate_sets))

    
    
