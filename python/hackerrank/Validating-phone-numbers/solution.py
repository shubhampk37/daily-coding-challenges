# HackerRank: Validating phone numbers
# Problem Link: https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re

def is_valid_mobile_number(number: str) -> bool:
    """Validate if a string represents a 10-digit mobile number starting with 7, 8, or 9."""
    mobile_pattern = re.compile(r"^[789]\d{9}$")
    return bool(mobile_pattern.match(number))


def main() -> None:
    num_cases = int(input())

    for _ in range(num_cases):
        phone_number = input().strip()

        if is_valid_mobile_number(phone_number):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()