# HackerRank: No Idea!
# Problem Link: https://www.hackerrank.com/challenges/no-idea/problem

def happiness_count():
    """
    calculate total happiness based on whether the elements 
    exits in A (+1) or B (-1)
    """
    
    n, m = input().split()
    n, m = int(n), int(m)

    # taking the input of the `n` digits main_array and the sets A and B
    main_array = map(int, input().split())
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))


    # checking in main_array elements exist in sets A and B
    # happiness +1 for array element in A 
    # happiness -1 for array element in B
    happiness = sum((num in A) - (num in B) for num in main_array)

    print(happiness)

if __name__ == '__main__':
    happiness_count()
