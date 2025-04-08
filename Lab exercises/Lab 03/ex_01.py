"""
Develop a student class that has the following functions:
• To take input name , roll_number, email_address from user
• To take the count of courses and name of each course from user
• To calculate GPA of the individual courses
• To calculate CGPA of particular semester
"""

class Student:
    def details(self):
        self.name = input("Enter your name: ")
        self.roll_number = input("Enter your roll number: ")
        self.email_address = input("Enter your email address: ")
    
    def courses(self):
        self.count = int(input("Enter the number of courses: "))
        self.course = []
        for i in range(self.count):
            self.course.append(input(f"Enter the name of course {i+1}: "))
    
    def gpa(self):
        self.gpa = []
        for i in range(self.count):
            self.gpa.append(float(input(f"Enter the GPA of course {self.course[i]}: ")))
    
    def cgpa(self):
        self.cgpa = sum(self.gpa) / self.count
        print(f"CGPA of {self.name} is {self.cgpa}")

student = Student()
student.details()
student.courses()
student.gpa()
student.cgpa()