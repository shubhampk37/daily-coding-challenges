# HackerRank: Find Angle MBC
# Problem Link: https://www.hackerrank.com/challenges/find-angle/problem

import math

def find_angle_mbc():
    
    ab = int(input())
    bc = int(input())
    
    # Calculate angle MBC (which is equal to angle ACB)
    angle_radians = math.atan2(ab, bc)
    angle_degrees = math.degrees(angle_radians)
    
    # Use chr(176) for the degree symbol
    degree_symbol = chr(176)
    
    # Print rounded result with the degree symbol
    print(f"{round(angle_degrees)}{degree_symbol}")

if __name__ == '__main__':
    find_angle_mbc()
