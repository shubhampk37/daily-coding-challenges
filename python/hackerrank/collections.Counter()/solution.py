# HackerRank: collections.Counter()
# Problem Link: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

def solve_shoe_shop():
    # Read the number of shoes (we don't strictly need this value 
    # since Counter handles the inventory dynamically)
    _ = int(input())
    
    # Read the list of available shoe sizes and create a frequency counter
    shoe_sizes = list(map(int, input().split()))
    shoe_inventory = Counter(shoe_sizes)
    
    # Read the total number of customers
    num_customers = int(input())
    
    total_earnings = 0
    
    # Process each customer's request
    for _ in range(num_customers):
        size, price = map(int, input().split())
        
        # Check if the requested shoe size is available in stock
        if shoe_inventory[size] > 0:
            total_earnings += price
            shoe_inventory[size] -= 1  # Decrement the stock count after purchase
            
    # Output the total money earned
    print(total_earnings)

if __name__ == '__main__':
    solve_shoe_shop()