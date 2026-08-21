# HackerRank: Collections.OrderedDict()
# Problem Link: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict


def calculate_net_prices() -> None:

    item_totals = OrderedDict()

    num_records = int(input())

    for _ in range(num_records):
        # Split the input from right to safely handle item names containing spaces
        line = input()
        item_name, price_str = line.rsplit(maxsplit=1)
        net_price = int(price_str)

        # Accumulate the total price for existing items or initialize new ones
        item_totals[item_name] = item_totals.get(item_name, 0) + net_price

    # Output the final aggregated results
    for item_name, net_price in item_totals.items():
        print(f"{item_name} {net_price}")


if __name__ == "__main__":
    calculate_net_prices()
