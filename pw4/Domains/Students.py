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