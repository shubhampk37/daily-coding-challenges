# HackerRank: Set .symmetric_difference() Operation
# Problem Link: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

if __name__ == '__main__':
    # Number of students who are English newspaper subscribers
    # But, we don't care about storing this value, since it's of no use to us
    input()

    # Student roll numbers subscribed to English newspaper
    english_subs = set(map(int, input().split()))
    
    # Similar for, total Frensh newspaper subscriber count
    input()
    # Student roll numbers subscribed to French newsp
    french_subs = set(map(int, input().split()))
    
    # Number of students subscribed to exactly only one newspaper
    print(len(english_subs ^ french_subs))
    
