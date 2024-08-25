# This file includes the main script for my project.
from student_organizer import Student, StudentOrganizer

def main():
    organizer = StudentOrganizer()

    students = [
        Student(f"Student {i+1}", i+1, "Math" if i % 2 == 0 else "Biology")
        for i in range(50)
    ]

    for student in students:
        organizer.add_student(student)

    organizer.show_summary()

if __name__ == "__main__":
    main()
