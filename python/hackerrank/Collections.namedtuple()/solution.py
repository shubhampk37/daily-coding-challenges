# HackerRank: Collections.namedtuple()
# Problem Link: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

def calculate_average_marks():
    # Read the number of students and column headers
    num_students = int(input())
    columns = input().split()
    
    # Dynamically create a namedtuple based on the column names
    Student = namedtuple('Student', columns)
    
    # Collect total marks by reading each student's data
    total_marks = 0
    for _ in range(num_students):
        student_data = input().split()
        student = Student(*student_data)
        total_marks += int(student.MARKS)
        
    # Calculate and print the average formatted to 2 decimal places
    average_marks = total_marks / num_students
    print(f"{average_marks:.2f}")

if __name__ == '__main__':
    calculate_average_marks()
