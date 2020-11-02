from school.student import Student
from school.teacher import Teacher


class Group:
    def __init__(self, number, students: list, teachers: list):
        self.__number = number
        self.__students = students
        self.__teachers = teachers

    def __str__(self):
        return f'{self.__number}, {self.__students}'

    @property
    def students(self):
        return self.__students

    @property
    def teachers(self):
        return self.__teachers

    def add_student(self, student):
        if type(student) == Student:
            self.__students.append(student)
            return True
        else:
            return False

    def remove_student(self, name, last_name):
        for i in self.__students:
            if i.name == name and i.last_name == last_name:
                self.__students.remove(i)
                return True

        return False

    def add_teacher(self, teacher):
        if type(teacher) == Teacher:
            self.__teachers.append(teacher)
            return True
        else:
            return False

    def remove_teacher(self, name, last_name):
        for i in self.__teachers:
            if i.name == name and i.last_name == last_name:
                self.__teachers.remove(i)
                return True

        return False

    def check_students(self):
        return len(self.__students)

    def check_teachers(self):
        return len(self.__teachers)








