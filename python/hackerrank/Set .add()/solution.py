# HackerRank: Set .add()
# Problem Link: https://www.hackerrank.com/challenges/py-set-add/problem

def count_unique_countries(number_of_stamps): 
    """ Return the unique number of countries """

    countries = set()
    
    for _ in range(number_of_stamps):
        # Remove the leading and trailing whitespaces
        countries.add(input().strip())
        
    return len(countries)
           
if __name__ == "__main__":
    number_of_stamps = int(input())    
    print(count_unique_countries(number_of_stamps))
    
