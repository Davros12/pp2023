import math
import numpy as np

class Students:
    def __init__(self, i, n, d):
        self.__sid = i
        self.__sname = n
        self.__dob = d
        self.__gpa = 0
    
    def get_student_id(self):
        return self.__sid
    
    def get_student_name(self):
        return self.__sname
    
    def get_student_dob(self):
        return self.__dob
    
    def get_gpa(self):
        return self.__gpa
    
class Courses:
    def __init__(self, i, n, c):
        self.__cid = i
        self.__cname = n
        self.__no_credits = c
    
    def get_course_id(self):
        return self.__cid
    
    def get_course_name(self):
        return self.__cname
    
    def get_course_no_credits(self):
        return self.__no_credits
    
class Manage:
    def __init__(self):
        self.__no_students = 0
        self.__no_courses = 0
        self.__students_list = []
        self.__courses_list = []
    
    def get_students_list(self):
        return self.__students_list    

    def get_course_list(self):
        return self.__courses_list
    
    def input_students(self):
        n = int(input("Enter number of students: "))
        self.__no_students += n
        for i in range(n):
            id = str(input("Enter student ID: "))
            name = str(input("Enter student name: "))
            dob = str(input("Enter student DoB: "))
            self.__students_list += [Students(id, name, dob)]
            
    def input_courses(self):
        n = int(input("Enter number of courses: "))
        self.__no_courses += n
        for i in range(n):
            id = str(input("Enter course ID: "))
            name = str(input("Enter course name: "))
            credits = int(input("Enter course's number of credits: "))
            self.__courses_list += [Courses(id, name, credits)]
            
    def list_students(self):
        for i in range(self.__no_students):
            print(f"Student ID:  {self.__students_list[i].get_student_id()}")
            print(f"Student name: {self.__students_list[i].get_student_name()}")
            print(f"Student DoB: {self.__students_list[i].get_student_dob()}")
            
    #Need function to validate input natural number
    #Need function to look for cid and sid in list courses and students
    
    
new = Manage()
new.input_students()
new.list_students()
    
            