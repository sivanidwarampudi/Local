# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 13:36:24 2019

@author: sivan
"""

"""my_student = {
      'name':'sivani',
      'grades':[10,20,40,60]
}
def avg(student):
        return sum(student['grades'])/len(student['grades'])"""
        
        
"""my_student = {
  'name': 'Rolf Smith',
  'grades': [70, 88, 90, 99]
}

def average_grade(student):
  return sum(student['grades']) / len(student['grades'])
print(average_grade(my_student))"""


"""class WorkingStudent:
    def __init__(self, name, school, salary):
        self.name = name
        self.school = school
        self.marks = []
        self.salary = salary

    def average(self):
        return sum(self.marks) / len(self.marks)


rolf = WorkingStudent("Rolf", "MIT", 15.50)
marks=[5,55]
rolf.marks.append(67)
rolf.marks.append(97)

print(rolf.marks)
print(rolf.average())"""
class Student1:
    def student(self,v1,v2):
        self.v1=v1
        self.v2=v2
        return (v1+v2)
print(student(2,3))