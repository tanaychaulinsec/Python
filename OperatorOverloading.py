class Student:
    def __init__(self,marks):
        self.marks=marks
    def __add__(self,graceMarks):
        self.marks+=graceMarks
    def __repr__(self):
        return "I will not print"

#driver
Ram=Student(70)
print(Ram.marks)
Ram + 15
print(Ram.marks)
print (Ram)
