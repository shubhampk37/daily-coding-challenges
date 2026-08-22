# HackerRank: Symmetric Difference
# Problem Link: https://www.hackerrank.com/challenges/symmetric-difference/problem

def print_symmetric_difference() -> None:
    """Reads two sets from input and prints their symmetric difference in ascending order."""
    
    # disregarding the previous input for set_a & set_b, because it's of no use since we are using sets 
    _, set_a = input(), set(map(int, input().split())) 

    _, set_b = input(), set(map(int, input().split()))

    # Find the symmetric difference
    sym_diff = set_a.symmetric_difference(set_b)

    # Sort the results in ascending order and print them one per line
    for num in sorted(sym_diff):
        print(num)

if __name__ == '__main__':
    print_symmetric_difference()
