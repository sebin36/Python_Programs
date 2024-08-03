class Course:
    def __init__(self, course_code, course_name, credit):
        self.course_code = course_code
        self.course_name = course_name
        self.credit = credit

    def get_course_info(self):
        pass

class LectureCourse(Course):
    def __init__(self, course_code, course_name, credit, instructor, meeting_time):
        super().__init__(course_code, course_name, credit)
        self.instructor = instructor
        self.meeting_time = meeting_time

    def get_course_info(self):
        return f'{self.course_name}({self.course_code})\nCredits:{self.credit}\nInstructor:{self.instructor}\nMeeting Time:{self.meeting_time}'

class LabCourse(Course):
    def __init__(self, course_code, course_name, credit, lab_instructor, lab_schedule):
        super().__init__(course_code, course_name, credit)
        self.lab_instructor = lab_instructor
        self.lab_schedule = lab_schedule

    def get_course_info(self):
        return f'{self.course_name}({self.course_code})\nCredits:{self.credit}\nLab Instructor:{self.lab_instructor}\nLab schedule:{self.lab_schedule}'

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def get_enrolled_courses(self):
        for course in self.courses:
            print(course.get_course_info())
            print()

    def __str__(self):
        return f'Student ID: {self.student_id}\nName: {self.name}'


lecture_course = LectureCourse("C001", "Introduction to Python", 3, "Dr. Smith", "Mon/Wed 10:00 AM - 11:30 AM")
lab_course = LabCourse("C002", "Python Lab", 1, "Prof. Johnson", "Thu 2:00 PM - 4:30 PM")

student1 = Student("S001", "Alice")
student2 = Student("S002", "Bob")

student1.enroll(lecture_course)
student1.enroll(lab_course)
student2.enroll(lecture_course)

print("Course Information:")
print(lecture_course.get_course_info())
print()
print(lab_course.get_course_info())

print("\nStudent Information:")
print(student1)
print()
print(student2)

print("\nEnrolled Courses:")
print(f'{student1.name} is enrolled in:')
student1.get_enrolled_courses()
print(f'{student2.name} is enrolled in:')
student2.get_enrolled_courses()
