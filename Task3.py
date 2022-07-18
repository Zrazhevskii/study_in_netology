class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        courses = ', '.join(self.courses_in_progress)
        fcourses = ', '.join(self.finished_courses)
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'+\
               f'Средняя оценка за домашние задания: {self.get_avr_grade()}\n'+\
               f'Курсы в процессе изучения: {courses}\n'+\
               f'Завершенные курсы: {fcourses}'

    def __eq__(self, other):
        return self.get_avr_grade() == other.get_avr_grade()

    def __ne__(self, other):
        return self.get_avr_grade() != other.get_avr_grade()

    def __gt__(self, other):
        return self.get_avr_grade() > other.get_avr_grade()

    def __ge__(self, other):
        return self.get_avr_grade() >= other.get_avr_grade()

    def __lt__(self, other):
        return self.get_avr_grade() < other.get_avr_grade()

    def __le__(self, other):
        return self.get_avr_grade() <= other.get_avr_grade()

    def get_avr_grade(self):
        grades_sum = 0
        grades_count = 0
        for course in self.grades.values():
            grades_sum += sum(course)
            grades_count += len(course)
        if grades_count:
            return round(grades_sum/grades_count, 1)
        return 0

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'+\
               f'Средняя оценка за лекции: {self.get_avr_grade()}'

    def __eq__(self, other):
        return self.get_avr_grade() == other.get_avr_grade()

    def __ne__(self, other):
        return self.get_avr_grade() != other.get_avr_grade()

    def __gt__(self, other):
        return self.get_avr_grade() > other.get_avr_grade()

    def __ge__(self, other):
        return self.get_avr_grade() >= other.get_avr_grade()

    def __lt__(self, other):
        return self.get_avr_grade() < other.get_avr_grade()

    def __le__(self, other):
        return self.get_avr_grade() <= other.get_avr_grade()

    def get_avr_grade(self):
        grades_sum = 0
        grades_count = 0
        for course in self.grades.values():
            grades_sum += sum(course)
            grades_count += len(course)
        if grades_count:
            return round(grades_sum/grades_count, 1)
        return 0

class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']
best_student.rate_lect(cool_lecturer, 'Python', 10)
best_student.rate_lect(cool_lecturer, 'Python', 10)
best_student.rate_lect(cool_lecturer, 'Python', 9)

best_student2 = Student('Max', 'Eman', 'your_gender')
best_student2.courses_in_progress += ['Python']
cool_reviewer.rate_hw(best_student2, 'Python', 10)
cool_reviewer.rate_hw(best_student2, 'Python', 10)
cool_reviewer.rate_hw(best_student2, 'Python', 10)

cool_lecturer2 = Lecturer('Den', 'Buggy')
cool_lecturer2.courses_attached += ['Python']
best_student.rate_lect(cool_lecturer2, 'Python', 10)
best_student.rate_lect(cool_lecturer2, 'Python', 10)
best_student.rate_lect(cool_lecturer2, 'Python', 10)

print(best_student.grades)
print(cool_lecturer.grades)
print(best_student)
print(cool_reviewer)
print(cool_lecturer)
print(best_student < best_student2)
print(cool_lecturer < cool_lecturer2)
