# HackerRank: Nested Lists
# Problem Link: https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        students.append([name, score])
    
    # With the help of `set` sorting the grades
    grades = sorted(list(set([student[1] for student in students])))
    
    # Finding the second lowest grade
    second_lowest_grade = grades[1]
    
    # Finding the students with the second lowest grade
    second_lowest_students = sorted([student[0] for student in students if student[1] == second_lowest_grade])
    
    for student in second_lowest_students:
        print(student)