# HackerRank: The Captain's Room
# Problem Link: https://www.hackerrank.com/challenges/py-the-captains-room/problem

from collections import Counter

def find_captains_room(group_size: int, room_numbers: list[int]) -> int:
    room_counts = Counter(room_numbers)
    
    for room, count in room_counts.items():
        if count == 1:
            return room
    
    raise ValueError("Captain's room not found in the given data.")

if __name__ == '__main__':
    # Number of members per group 
    K = int(input())
    all_room_numbers = list(map(int, input().split()))
    
    captains_room = find_captains_room(K, all_room_numbers)
    print(captains_room)

    
    
