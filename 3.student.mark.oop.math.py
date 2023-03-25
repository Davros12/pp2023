import math
import numpy as np

class Students:
    def __init__(self, i, n, d):
        self.__id = i
        self.__sname = n
        self.__dob = d
        self.__gpa = None
    
    def get_id(self):
        return self.__id
    
    def get_student_name(self):
        return self.__sname
    
    def get_student_dob(self):
        return self.__dob
    
    def get_gpa(self):
        return self.__gpa
    
    def set_gpa(self, g):
        self.__gpa = g
    
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
    
    def get_course_marks(self):
        return self.__marks
    
    def add_marks(self, m):
        self.__marks += [m]
    
class Manage:
    def __init__(self):
        self.__no_students = 0
        self.__no_courses = 0
        self.__students_list = []
        self.__courses_list = []
        self.__gpa_list = np.array([])
    
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
            print(f"\nStudent ID:  {self.__students_list[i].get_id()} \n"
                  f"Student name: {self.__students_list[i].get_student_name()} \n"
                  f"Student DoB: {self.__students_list[i].get_student_dob()}")
            print()
            
    def list_courses(self):
        for i in range(self.__no_courses):
            print(f"\nCourse ID : {self.__courses_list[i].get_id()} \n"
                  f"Course name: {self.__courses_list[i].get_course_name()} \n"
                  f"Number of credits: {self.__courses_list[i].get_course_no_credits()}")
            print()
            
    def input_marks(self):
        id = input("Enter course ID: ")
        i = get_index(id, self.__courses_list)
        print(f"Enter marks for the course {self.__courses_list[i].get_course_name()}: ")
        for j in range(self.__no_students):
            m = float(input(f"{self.__students_list[j].get_student_name()}: "))
            self.__courses_list[i].add_marks(m)
            
    def input_marks_all(self):
        for i in range(self.__no_courses):
            print(f"\n Enter marks for the course {self.__courses_list[i].get_course_name()}: ")
            for j in range(self.__no_students):
                m = input(f"{self.__students_list[j].get_student_name()}: ")
                self.__courses_list[i].add_marks(m)
                
    def calculate_gpa(self):
        for i in range(self.__no_students):
            student_marks = np.array([])
            credit_list = np.array([])
            for j in range(self.__no_courses):
                m = np.array([self.__courses_list[j].get_course_marks()[i]], dtype=float)
                student_marks = np.concatenate((student_marks, m), axis = None, dtype=float)
                credit_list = np.concatenate((credit_list, [self.__courses_list[j].get_course_no_credits()]), axis = None, dtype = float)
            gpa = math.floor(np.average(student_marks, weights = credit_list) * 10) /10
            self.__students_list[i].set_gpa(gpa)
            
    def list_students_GPA(self):
        for i in range(self.__no_students):
            print(f"\nStudent ID:  {self.__students_list[i].get_id()} \n"
                  f"Student name: {self.__students_list[i].get_student_name()} \n"
                  f"Student DoB: {self.__students_list[i].get_student_dob()} \n"
                  f"GPA: {self.__students_list[i].get_gpa()}")
            print()
            
    def sort_students(self):
        st_gpa = np.array([])
        for i in range(self.__no_students):
            g = np.array([self.__students_list[i].get_gpa()])
            st_gpa = np.concatenate((st_gpa, g), axis = None)
        st_gpa = np.sort(st_gpa, axis = None)
        for i in range(len(st_gpa)):
            for j in range(self.__no_students):
                if self.__students_list[j].get_gpa() == st_gpa[i]:
                    print(f"\nStudent ID: {self.__students_list[j].get_id()} \n"
                          f"Student name: {self.__students_list[j].get_student_name()} \n"
                          f"GPA: {self.__students_list[j].get_gpa()} \n")
                    
    
            
#Need function to validate input natural number
def get_index(id, arr):
    for i in range(len(arr)):
        if arr[i].get_id() == id:
            return arr.index(arr[i])
    
    
new = Manage()
new.input_students()
new.list_students()
new.input_courses()
new.list_courses()
new.input_marks_all()
new.calculate_gpa()
new.list_students_GPA()
new.sort_students()
            