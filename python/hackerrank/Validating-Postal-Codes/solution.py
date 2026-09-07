# HackerRank: Validating Postal Codes
# Problem Link: https://www.hackerrank.com/challenges/validating-postalcode/problem

import re

def is_valid_mobile_number(number: str) -> bool:
    """Validate if a string represents a 10-digit mobile number starting with 7, 8, or 9."""
    mobile_pattern = re.compile(r"^[789]\d{9}$")
    return bool(mobile_pattern.match(number))


regex_integer_in_range = r"^[1-9][0-9]{5}$"	# # Matches six-digit integers from 100000 to 99999.
regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"	# Finds overlapping patterns. Example: 121, 343


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)