from Domains import Students
from Domains import Courses
import input
import output
import numpy as np
import math


st = []
cs = []
input.input_students(st)
input.input_courses(cs)
input.input_marks_all(st, cs)
input.calculate_gpa(st, cs)

output.list_students(st)
output.list_courses(cs)
output.list_students_GPA(st)
output.sort_students(st)