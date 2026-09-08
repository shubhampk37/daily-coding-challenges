# HackerRank: Validating UID
# Problem Link: https://www.hackerrank.com/challenges/validating-uid/problem

import re

def validate_uid(uid: str) -> str:
    """
    Validates an employee Unique Identification Number (UID) based on corporate standards:
    - Exactly 10 characters long.
    - Only alphanumeric characters.
    - No repeating characters.
    - At least 2 uppercase English letters.
    - At least 3 digits.
    """
    # Rule 1: Must be exactly 10 characters long
    if len(uid) != 10:
        return 'Invalid'
    
    # Must contain only alphanumeric characters
    if not uid.isalnum():
        return 'Invalid'
        
    # No character should repeat (sets drop duplicates)
    if len(set(uid)) != 10:
        return 'Invalid'
        
    # Rule 4: Must contain at least 2 uppercase letters
    uppercase_count = sum(1 for char in uid if char.isupper())
    if uppercase_count < 2:
        return 'Invalid'
        
    # Must contain at least 3 digits
    digit_count = sum(1 for char in uid if char.isdigit())
    if digit_count < 3:
        return 'Invalid'
        
    return 'Valid'


if __name__ == '__main__':
    test_case_count = int(input())
    for _ in range(test_case_count):
        uid = input()
        print(validate_uid(uid))