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