# HackerRank: Validating Email Addresses With a Filter
# Problem Link: https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem

import re
def fun(email: str) -> bool:
    """Validates whether a given string is a properly formatted email address.

    Rules:
    - Username: Letters, digits, dashes, and underscores.
    - Website name: Letters and digits only.
    - Extension: Letters only, with a maximum length of 3.
    """
    pattern = r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$"
    return bool(re.match(pattern, email))

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)