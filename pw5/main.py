import input
import output

st = []
cs = []
#input.input_students(st)
input.input_courses(cs)
input.input_marks_all(st, cs)
input.calculate_gpa(st, cs)

st = input.load_st_data()
output.list_students(st)
#output.list_courses(cs)
#output.list_students_GPA(st)
#output.sort_students(st)