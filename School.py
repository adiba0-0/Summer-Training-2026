class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject


class Principal(Teacher):
    def __init__(self, name, age, subject, school_name):
        super().__init__(name, age, subject)
        self.school_name = school_name

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Subject:", self.subject)
        print("School Name:", self.school_name)


p = Principal("Rahul", 45, "Mathematics", "ABC Public School")
p.display()