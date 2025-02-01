class Student:
    """
    A class to represent a student.
    Attributes
    ----------
    name : str
        The name of the student.
    roll : str
        The roll number of the student.
    marks : list
        A list of marks obtained by the student.
    Methods
    -------
    setName(name):
        Sets the name of the student.
    setRoll(roll):
        Sets the roll number of the student.
    setMarks(marks):
        Sets the marks of the student.
    getName():
        Returns the name of the student.
    getRoll():
        Returns the roll number of the student.
    getMarks():
        Returns the marks of the student.
    getStudent():
        Prints the details of the student.
    avg():
        Returns the average of the marks obtained by the student.
    """
    def __init__(self, name='', roll='', marks=[]):
        self.name = name
        self.roll = roll
        self.marks = marks
    
    def setName(self, name):
        self.name = name
    def setRoll(self, roll):
        self.roll = roll
    def setMarks(self, marks):
        self.marks = marks
    
    def getName(self):
        return self.name
    def getRoll(self):
        return self.roll
    def getMarks(self):
        return self.marks
    
    def getStudent(self):
        print('Student name:', self.getName())
        print('Roll number:', self.getRoll())
        print('Marks:')
        for i in range(len(self.getMarks())):
            print(f'Quiz{i+1}:', self.getMarks()[i])
    
    def avg(self):
        return sum(self.getMarks()) / len(self.getMarks())

# Define 5 Student type instances and initialize all instance attributes with appropriate values
student1 = Student('Alice', '001', [85, 90, 88])
student2 = Student('Bob', '002', [78, 82, 80])
student3 = Student('Charlie', '003', [92, 95, 94])
student4 = Student('David', '004', [70, 75, 72])
student5 = Student('Eve', '005', [88, 85, 90])

# Print consolidated/complete info for each student
students = [student1, student2, student3, student4, student5]
for student in students:
    student.getStudent()
    print(f'Average marks: {student.avg():.3f}')
    print()

# Print average marks for each quiz
for i in range(3):
    total_marks = sum(student.getMarks()[i] for student in students)
    avg_marks = total_marks / len(students)
    print(f'Average marks for Quiz{i+1}: {avg_marks}')