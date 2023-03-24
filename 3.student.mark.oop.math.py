import math
import numpy as np

class Students:
    def __init__(self, i, n, d):
        self.__id = i
        self.__sname = n
        self.__dob = d
        self.__gpa = 0
    
    def get_id(self):
        return self.__id
    
    def get_student_name(self):
        return self.__sname
    
    def get_student_dob(self):
        return self.__dob
    
    def get_gpa(self):
        return self.__gpa
    
class Courses:
    def __init__(self, i, n, c):
        self.__id = i
        self.__cname = n
        self.__no_credits = c
        self.__marks = []
    
    def get_id(self):
        return self.__id
    
    def get_course_name(self):
        return self.__cname
    
    def get_course_no_credits(self):
        return self.__no_credits
    
    def add_marks(self, m):
        self.__marks += [m]
    
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
            print(f"Student ID:  {self.__students_list[i].get_id()} \n"
                  f"Student name: {self.__students_list[i].get_student_name()} \n"
                  f"Student DoB: {self.__students_list[i].get_student_dob()}")
            print()
            
    def list_courses(self):
        for i in range(self.__no_courses):
            print(f"Course ID : {self.__courses_list[i].get_id()} \n"
                  f"Course name: {self.__courses_list[i].get_course_name()} \n"
                  f"Number of credits: {self.__courses_list[i].get_course_no_credits()}")
            print()
            
    def input_marks(self):
        id = input("Enter course ID: ")
        i = get_index(id, self.__courses_list)
        print(f"Enter marks for the course {self.__courses_list[i].get_course_name()}: ")
        for j in range(self.__no_students):
            m = input(f"{self.__students_list[j].get_student_name()}: ")
            self.__courses_list[i].add_marks(m)
            
            
    #Need function to validate input natural number
    #Need function to look for cid and sid in list courses and students
def get_index(id, arr):
    for i in range(len(arr)):
        if arr[i].get_id() == id:
            return arr.index(arr[i])
    
    
new = Manage()
new.input_students()
new.list_students()
new.input_courses()
new.list_courses()
new.input_marks()
            