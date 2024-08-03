class Person:
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name

class Student(Person):
    def __init__(self, student_id, name):
        super().__init__(student_id, name)

    def get_info(self):
        return f"Student ID: {self.person_id}, Name: {self.name}"

class Course:
    def __init__(self, course_name):
        self.course_name = course_name

    def get_info(self):
        return f"{self.course_name}"

class Attendance:
    def __init__(self):
        self.attendance_dict = {}

    def mark_attendance(self, date, students):
        if date not in self.attendance_dict:
            self.attendance_dict[date] = []
        self.attendance_dict[date].extend(students)

    def get_attendance(self, date):
        return self.attendance_dict.get(date, [])

    def get_total_attendance(self):
        total_attendance = 0
        for date in self.attendance_dict:
            total_attendance += len(self.attendance_dict[date])
        return total_attendance


alice = Student("S001", "Alice")
bob = Student("S002", "Bob")
charlie = Student("S003", "Charlie")

math_course = Course("Mathematics")
physics_course = Course("Physics")

math_attendance = Attendance()
physics_attendance = Attendance()

math_attendance.mark_attendance("2023-11-01", [alice, bob])
math_attendance.mark_attendance("2023-11-03", [alice, charlie])

physics_attendance.mark_attendance("2023-11-01", [alice, bob, charlie])
physics_attendance.mark_attendance("2023-11-02", [bob, charlie])

print("Attendance for Mathematics:")
for date in math_attendance.attendance_dict:
    print(f"{date}: {[student.get_info() for student in math_attendance.get_attendance(date)]}")

print("Attendance for Physics:")
for date in physics_attendance.attendance_dict:
    print(f"{date}: {[student.get_info() for student in physics_attendance.get_attendance(date)]}")

print("\nTotal Attendance:")
print(f"{math_course.get_info()}: {math_attendance.get_total_attendance()}")
print(f"{physics_course.get_info()}: {physics_attendance.get_total_attendance()}")
