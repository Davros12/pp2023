from Domains import Students
from Domains import Courses
import numpy as np
import math

def list_students(st_list):
    for i in range(len(st_list)):
        print(f"\nStudent ID:  {st_list[i].get_id()} \n"
              f"Student name: {st_list[i].get_student_name()} \n"
              f"Student DoB: {st_list[i].get_student_dob()}")
        print()
            
def list_courses(cs_list):
    for i in range(len(cs_list)):
        print(f"\nCourse ID : {cs_list[i].get_id()} \n"
              f"Course name: {cs_list[i].get_course_name()} \n"
              f"Number of credits: {cs_list[i].get_course_no_credits()}")
        print()
        
def list_students_GPA(st_list):
    for i in range(len(st_list)):
        print(f"\nStudent ID:  {st_list[i].get_id()} \n"
              f"Student name: {st_list[i].get_student_name()} \n"
              f"Student DoB: {st_list[i].get_student_dob()} \n"
              f"GPA: {st_list[i].get_gpa()}")
        print()
        
def sort_students(st_list):
    st_gpa = np.array([])
    for i in range(len(st_list)):
        g = np.array([st_list[i].get_gpa()])
        st_gpa = np.concatenate((st_gpa, g), axis = None)
    st_gpa = np.sort(st_gpa, axis = None)
    for i in range(len(st_gpa)):
        for j in range(len(st_list)):
            if st_list[j].get_gpa() == st_gpa[i]:
                print(f"\nStudent ID: {st_list[j].get_id()} \n"
                        f"Student name: {st_list[j].get_student_name()} \n"
                        f"GPA: {st_list[j].get_gpa()} \n")