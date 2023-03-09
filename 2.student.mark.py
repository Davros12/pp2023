#Define student class
class Students:
    def __init__(self, i, n, d):
        self.sid = i
        self.sname = n
        self.dob = d
    def st_info(self):
        print("Student ID: ", self.sid)
        print("Student name: ", self.sname)
        print("Student DoB: ", self.dob)
    
#Function to input students info
def input_students(n):
    st = []
    for i in range(n):
        id = int(input(f"Enter students {i+1} ID: "))
        name = str(input(f"Enter student {i+1} name: "))
        db = str(input(f"Enter student {i+1} DoB: "))
        st += [Students(id, name, db)]
    return st
        
#Define course class
class Courses:
    def __init__(self, i, n):
        self.cid = i
        self.cname = n
        self.marks = []
    def c_info(self):
        print("Course ID: ", self.cid)
        print("Course name: ", self.cname)
    def set_marks(self, st):
        for i in range(len(st)):
            mk = int(input(f"Enter marks for student {st[i].sid} for the course {self.cname}: "))
            self.marks += [mk]
    
#Function to input courses info
def input_courses(n):
    cs = []
    for i  in range(n):
        id = int(input(f"Enter course {i+1} ID: "))
        name = str(input(f"Enter course {i+1} name: "))
        cs += [Courses(id, name)]
    return cs

#Function to input marks for each student in each course
def input_marks(st, cs):
    for i in range(len(cs)):
        cs[i].set_marks(st)
            
#Function to display students info
def show_st(std):
    for i in range(len(std)):
        std[i].st_info()
        print()
        
#Function to display courses info
def show_cs(css):
    for i in range(len(css)):
        css[i].c_info()
        print()
        
#Function to show students marks for any course
def show_marks(st, cs):
    cid = int(input(f"Enter course ID: "))
    i = 0
    while i in range(len(cs)):
        if cs[i].cid == cid:
            break
        else: 
            i += 1
    print(f"Marks for students in the course {cs[i].cname}: ")
    for j in range(len(st)):
        print(f"{st[j].sname}: {cs[i].marks[j]}")    
    
no_students = int(input(f"Enter number of students: "))
s = input_students(no_students)

no_courses = int(input(f"Enter number of courses: ")) 
c = input_courses(no_courses)

show_st(s)
show_cs(c)
input_marks(s, c)
show_marks(s, c) 

    


