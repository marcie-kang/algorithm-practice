"""
You're going on a trip with some students and it's up to you to keep track of how much money each Student has. A student is defined like this:

class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties
As you can tell, each Student has some fives, tens, and twenties. Your job is to return the name of the student with the most money. If every student has the same amount, then return "all".

Notes:

Each student will have a unique name
There will always be a clear winner: either one person has the most, or everyone has the same amount
If there is only one student, then that student has the most money
"""

def most_money(students):
    if len(students) == 1:
        return students[0].name

    students_total = []

    for student in students:
        total = (student.fives * 5) + (student.tens * 10) + (student.twenties * 20)
        students_total.append([student.name, total])

    students_total.sort(key=lambda x: x[1])

    return students_total[-1][0] if students_total[-1][1] > students_total[0][1] else "all"
