# defining the students and the studentOrganizer class

class Student:
    def __init__(self, name, student_id, interest):
        self.name = name
        self.student_id = student_id
        self.interest = interest

    def __str__(self):
        return f"{self.name} (ID: {self.student_id}) - Interest: {self.interest}"
      
class StudentOrganizer:
    def __init__(self):
        self.math_students = []
        self.biology_students = []

    def add_student(self, student):
        if student.interest == "Math":
            self.math_students.append(student)
        elif student.interest == "Biology":
            self.biology_students.append(student)
        else:
            print(f"Unknown interest for {student.name}")

    def show_summary(self):
        print(f"Math Students ({len(self.math_students)}):")
        for student in self.math_students:
            print(student)

        print(f"\nBiology Students ({len(self.biology_students)}):")
        for student in self.biology_students:
            print(student)
  
