# HackerRank: String Formatting
# Problem Link: https://www.hackerrank.com/challenges/python-string-formatting/problem

# Format specification:
# {value:alignment width type}
#
# >        : Right-align
# width    : Minimum field width
# d        : Decimal representation
# o        : Octal representation
# X        : Uppercase hexadecimal representation
# b        : Binary representation

def print_formatted(number):
    """
    Print decimal, octal, hexadecimal, and binary representations
    for numbers from 1 to the given number.

    Values are right-aligned based on the binary width of the maximum number.
    """
    
    width = len(format(number, "b"))
    
    for i in range(1, number + 1):
        print(f"{i:>{width}} {i:>{width}o} {i:>{width}X} {i:>{width}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)