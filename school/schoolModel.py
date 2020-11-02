from school.personal import Personal
from school.group import Group
from school.student import Student
from school.teacher import Teacher

class School:
    def __init__(self, name, groups: list, personals: list):
        self.__name = name
        self.__groups = groups
        self.__personals = personals
        self.__teachers = []
    
    def __str__(self):
        return f'{self.__name}'

    @property
    def group(self):
        return self.__groups

    @property
    def personal(self):
        return self.__personals

    def add_groups(self, group):
        if type(group) == Group:
            self.__groups.append(group)
            return True
        else:
            return False

    def add_personals(self, personal):
        if type(personal) == Personal:
            self.__personals.append(personal)
            return True
        else:
            return False

    def remove_group(self, number):
        for i in self.__groups:
            if i.number == number:
                self.__groups.remove(i)
                return True
        return False

    def remove_personal(self, name, last_name):
        for i in self.__personals:
            if i.name == name and i.last_name == last_name:
                self.__personals.remove(i)
                return True
        return False
#что то тут не так
    def check_groups(self):
        for i in self.__groups:
            print(i.number)
            for j in i.students:
                print(j.name, " ", j.last_name)



    def check_number_of_group(self):
        return len(self.__groups)

s1 = Student("Ivan", "Petrov", 19, 4)
s2 = Student("Petr", "Petrov", 19, 4)
t1 = Teacher("Alex", "Sidorov", 76, 34)
t2 = Teacher("Semen", "Sidorov", 34, 4)
g1 = Group(1, [s1, s2], [t1, t2])
p1 = Personal("Sara", "Vainstein", 35, "Clear rooms")
p2 = Personal("Jack", "Nicolson", 44, "Guard")
personal = [p1, p2]
s3 = Student("Mike", "Lars", 21, 5)
g1.add_student(s3)

s4 = Student("Zina", "Ivanova", 32, 5)
s5 = Student("Masha", "Volkova", 22, 8)
t3 = Teacher("Sergey", "Semenov", 25, 7)
t4 = Teacher("Ivan", "Burov", 44, 9)
p3 = Personal("Valik", "Vetrov", 32, "Cooking")
g2 = Group(2, [s4, s5], [t3, t4])
school1 = School(54, [g1], [personal])
school1.add_groups(g2)
school1.add_personals(p3)

school1.check_groups()

print(school1.check_number_of_group())
