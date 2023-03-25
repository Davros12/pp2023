from Domains import Students
from Domains import Courses
import numpy as np
import math

def input_students(st_list):
    no_students = int(input("Enter number of students: "))
    for i in range(no_students):
        id = str(input("Enter student ID: "))
        name = str(input("Enter student name: "))
        dob = str(input("Enter student DoB: "))
        st_list += [Students.Students(id, name, dob)]
            
            
def input_courses(cs_list):
    no_courses = int(input("Enter number of courses: "))
    for i in range(no_courses):
        id = str(input("Enter course ID: "))
        name = str(input("Enter course name: "))
        credits = int(input("Enter course's number of credits: "))
        cs_list += [Courses.Courses(id, name, credits)]
            
def input_marks_all(st_list, cs_list):
    for i in range(len(cs_list)):
        print(f"\n Enter marks for the course {cs_list[i].get_course_name()}: ")
        for j in range(len(st_list)):
            m = input(f"{st_list[j].get_student_name()}: ")
            cs_list[i].add_marks(m)

def calculate_gpa(st_list, cs_list):
    for i in range(len(st_list)):
        student_marks = np.array([])
        credit_list = np.array([])
        for j in range(len(cs_list)):
            m = np.array([cs_list[j].get_course_marks()[i]], dtype=float)
            student_marks = np.concatenate((student_marks, m), axis = None, dtype=float)
            credit_list = np.concatenate((credit_list, [cs_list[j].get_course_no_credits()]), axis = None, dtype = float)
            gpa = math.floor(np.average(student_marks, weights = credit_list) * 10) /10
            st_list[i].set_gpa(gpa)
            
