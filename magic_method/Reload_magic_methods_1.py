"""
Перегрузка операторов

__init__() — соответствует конструктору объектов класса, срабатывает при создании объектов.

__del__() — соответствует деструктору объектов класса, срабатывает при удалении объектов.

__str__() — срабатывает при передаче объекта функциям str() и print(), преобразует объект к строке.

__call__() — срабатывает при обращении к экземпляру класса как к функции.

__setattr__() — срабатывает при выполнении операции, присваивания значения атрибуту объекта.

__getitem__() — срабатывает при извлечении элемента по индексу.

"""


class Student:
    def __init__(self, id, name):
        self.id, self.name = id, name

    def __str__(self):
        return f"Student name is {self.name}"

    def __call__(self, *args, **kwargs):
        print("Меня позвали")

student = Student(1, "Ivan")
print(student)
student()

class School:
    def __init__(self, students, grades):
        self.students, self.grades = students, grades

    def __len__(self):
        return len(self.grades)

    def __getitem__(self, index):
        return self.students[index], self.grades[index]

students = [Student(1, "Ivan"), Student(2, "Petya"), Student(3, "Vasya")]
grades = [5, 4, 2]
my_school = School(students, grades)
print(my_school[0])
print(len(my_school))





