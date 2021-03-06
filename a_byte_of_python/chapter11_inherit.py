#/usr/bin/env python3
# -*- coding: utf-8 -*-

class   SchoolMember:
        '''Rspressent any sckool member'''
        def __init__(self, name, age):
            self.name = name
            self.age = age
            print('Initialized Shool Member:      "%s"'%self.name)
        def tell(self):
            '''Tell my details'''
            print('Name:"%s"    Age:"%d"     '%(self.name, self.age))

class Teacher(SchoolMember):
    '''Represent a teach.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print('(Initialized Teacher: %s)'% self.name)

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "%d"'% self.salary)

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print('(Initialized Student: %s)'% self.name)

    def tell(self):
        SchoolMember.tell(self)
        print('Marks, "%d"'% self.marks)

t = Teacher('Mrs. shrivilvye', 40, 30000)
s = Student('Sweroop', 22, 40000)
        
print # Prints a blank line

members = [t,s]
for member in members:
    member.tell() # works for both Teachs and Student.
