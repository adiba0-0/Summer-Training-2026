from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def display(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

    def display(self):
        print("Full Time Employee")
        print("Name:", self.name)
        print("Salary:", self.calculate_salary())


class PartTimeEmployee(Employee):
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate

    def display(self):
        print("Part Time Employee")
        print("Name:", self.name)
        print("Salary:", self.calculate_salary())


f = FullTimeEmployee("Amit", 50000)
p = PartTimeEmployee("Riya", 40, 500)

f.display()
print()

p.display()