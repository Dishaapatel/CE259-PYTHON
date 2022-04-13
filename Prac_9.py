#ID:20CS048
#NAME: Disha Patel
class Student: # student class
def init (self, rollNo, name):
  # define roll number and name when the object of studnt is created
self.rollNo = rollNo
# initialize roll number self.name = name # initialize name

def display(self): 
  # display method of student
print(f'Student Roll No: {self.rollNo}') 
# print roll number of student print(f'Student Name: {self.name}') # print name of student


class Exam(Student):
  # exam class
def  init   (self, rollNo, name, subject): 
  # define roll number, name and subject super(). init (rollNo, name) # initialize roll number and name from student class self.subject = subject # initialize subject

def display(self):
  # display method of exam
  
super().display() 
# display roll number and name from student class for i in range(len(self.subject)):
print(f'Subject {i + 1} Marks: {self.subject[i]}') 
# print marks of subject


class Result(Exam):
  # class result total_marks = 0

def   init    (self, rollNo, name, subject):
  # define roll number, name , subject super(). init (rollNo, name, subject) 
  # initialize roll numer, name, subject from
exam class
self.total_marks = sum(subject) # do sum of all marks

def display(self): 
  # display method of result method super().display()
  # display roll number, name and subject print(f'Total Marks: {self.total_marks}')


if  name__ == '  main   ': student = Student(1, 'Prachi') student.display()
print()

exam = Exam(2, 'Shruti', [20, 25, 18]) exam.display()
print()

result = Result(3, 'Disha', [11, 11, 13]) result.display()
print()
