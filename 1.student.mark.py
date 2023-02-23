#define function to input number of students
#and their info
def student_info():
    no_student = int(input("Enter number of students: "))
    while no_student <=0:
        no_student = int(input("Enter a valid number of students: "))
    liststudent = [[0 for i in range(3)] for j in range(no_student)]
    for i in range(no_student):
        liststudent[i][0] = int(input("Enter student ID: "))
        liststudent[i][1] = str(input("Enter student name: "))
        liststudent[i][2] = str(input("Enter student date of birth: "))
    return liststudent

#define a function to input number of course 
#and course info
def course_info():
    no_course = int(input("Enter number of courses: "))
    while no_course <=0:
        no_course = int(input("Enter a valid number of courses: "))
    listcourse = [[0 for i in range(2)] for j in range(no_course)]
    for i in range(no_course):
        listcourse[i][0] = int(input("Enter course ID: "))
        listcourse[i][1] = str(input("Enter course name: "))
    return listcourse

#define a function to input marks of students for each course
def marks(c, st):
    mark = [[0 for i in range(len(st))] for j in range(len(c))]
    for i in range(len(c)):
        for j in range(len(st)):
            print("Enter mark for course", c[i][0], "of student", st[j][0], ": ")
            mark[i][j] = int(input())
    return mark

#define a function to display list of courses
def list_courses():
    print("List of courses:")
    for i in range(len(courses)):
        print("Course ID:", courses[i][0])
        print("Course name:", courses[i][1])

#define a function to display list of students
def list_students():
    print("List of students: ")
    for i in range(len(students)):
        print("Student ID:", students[i][0])
        print("Student name:", students[i][1])
        print("Date of birth:", students[i][2])

#Define a function to show marks of students
#for any course
def show_marks():
    cid = int(input("Enter course ID:"))
    for i in range(len(courses)):
        if courses[i][0] == cid:
            print("Students mark for the subject", courses[i][1], ": ")
            for j in range(len(students)):
                print(students[i][1],":", student_mark[i][j])
        else: 
            i+=1
        if i>len(courses):
            print("Invalid course ID!")
            
#define a list of student info
students = student_info()
            
#define a list of course info
courses = course_info()
       
print("Select: ")
print("1. Input marks for each courses.")
print("2. List courses.")
print("3. List students.")
print("4. Show students marks for any course.")
op = int(input("Your choice: "))
match op:
    case 1:
        student_mark = marks(courses, students)
    case 2: 
        list_courses()
    case 3: 
        list_students()
    case 4: 
        show_marks() 
    case _:
        print("Invalid choice")
        
        