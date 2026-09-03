# HackerRank: Set .discard(), .remove() & .pop()
# Problem Link: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

"""
Solution for HackerRank: Set .discard(), .remove() & .pop()
Author: Professional Portfolio
Description: Dynamically executes set operations from standard input 
and returns the sum of the remaining elements.
"""

def calculate_set_final_sum() -> int:
    """Reads initial set data and a sequence of commands, applies 
    the operations, and returns the final sum of the set.
    """
    input() # unused number of set elements quantity

    number_set = set(map(int, input().split()))
    
    num_commands = int(input())
    
    for _ in range(num_commands):
        operation = input().split()
        command = operation[0]
        
        # Dispatch the set operation dynamically depending on argument presence
        if len(operation) > 1:
            argument = int(operation[1])
            getattr(number_set, command)(argument)
        else:
            getattr(number_set, command)()
            
    return sum(number_set)

if __name__ == '__main__':
    print(calculate_set_final_sum())

    
    
