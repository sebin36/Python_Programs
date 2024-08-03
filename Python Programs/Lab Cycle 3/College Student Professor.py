class College:
    def __init__(self):
        self.students = []
        self.professors = []

    def add_student(self, student):
        self.students.append(student)
        print(f'{student.name} has been enrolled in the College.')

    def add_professor(self, professor):
        self.professors.append(professor)
        print('Professor details added Successfully.')

    def get_student(self, student_id):
        available = False
        for student in self.students:
            if student.student_id == student_id:
                available = True
                print('Student Information:')
                print(f'Name: {student.name}')
                print(f'ID No: {student.student_id}')
                print('Enrolled Courses:')
                for i in student.grades:
                    print(f'- {i}(Grade:{student.grades[i]})')

        if not available:
            print('No Student Details Found.')

    def get_professor(self, employee_id):
       available = False
       for professor in self.professors:
            if professor.employee_id == employee_id:
                available = True
                print('Professor Information:')
                print(f'Name: {professor.name}')
                print(f'ID No: {professor.employee_id}')
                print('Teaching Courses:')
                for i in professor.course_taught:
                    print(f'- {i}')
                    
       if not available:
           print('No Professor Details Found.')

class Student(College):
    def __init__(self, name, student_id):
        super().__init__()
        self.name = name
        self.student_id = student_id
        self.courses = []
        self.grades = {}

    def enroll(self, course):
        self.courses.append(course)
        print('Course added Successfully.')

    def asign_grade(self, course, grade):
        self.grades[course] = grade
        print(f'Grade {grade} assigned to {self.name} for course {course}.')

    def get_grades(self):
        pass

class Professor(College):
    def __init__(self, name, employee_id):
        super().__init__()
        self.name = name
        self.employee_id = employee_id
        self.course_taught = []

    def register_course(self, course):
        self.course_taught.append(course)
        print(f'Course {course} registered by {professor.name}.')

college = College()

while True:
    print('\nMenu')
    print('1.Enroll a student')
    print('2.Register a professor')
    print('3.Enroll a student in a course')
    print('4.Register a course')
    print('5.Display student information')
    print('6.Display professor information')
    print('7.Exit')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        name = input('Enter Student Name: ')
        stud_id = input('Enter Student ID: ')
        student = Student(name,stud_id)
        college.add_student(student)
    elif choice == 2:
        name = input('Enter Professor Name: ')
        prof_id = input('''Enter Professor's Employee ID: ''')
        professor = Professor(name,prof_id)
        college.add_professor(professor)
    elif choice == 3:
        stud_id = input('Enter Student ID: ')
        course = input('Enter Course Name: ')
        grade = input('Enter grade for the course: ')
        for student in college.students:
            if student.student_id == stud_id:
                student.asign_grade(course, grade)
    elif choice == 4:
        prof_id = input('Enter Professor ID: ')
        course = input('Enter course name to register: ')
        for professor in college.professors:
            if professor.employee_id == prof_id:
                professor.register_course(course)
    elif choice == 5:
        stud_id = input('Enter Student ID: ')
        college.get_student(stud_id)
    elif choice == 6:
        prof_id = input('Enter Professor ID: ')
        college.get_professor(prof_id)
    elif choice == 7:
        print('Exiting the College System. Good Bye!')
        break
    else:
        print('Invalid Choice.')
