# HackerRank: itertools.product()
# Problem Link: https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product


def main() -> None:
    """Read two space-separated lists of integers from input, compute their

    Cartesian product using itertools.product, and print the resulting tuples.
    """
    # Read input lists from standard input
    list_a: list[int] = list(map(int, input().split()))
    list_b: list[int] = list(map(int, input().split()))

    # Compute the Cartesian product
    cartesian_product: list[tuple[int, ...]] = list(product(list_a, list_b))

    # Print the output as space-separated tuples
    print(*(cartesian_product))


if __name__ == "__main__":
    main()