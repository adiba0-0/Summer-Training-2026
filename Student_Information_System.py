class Student:
    def get_data(self, name="", roll_number=0, marks=None):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def calculate_percentage(self):
        total = sum(self.marks)
        return (total/300)*100

    def display_data(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Percentage: {self.calculate_percentage()} %")

student1 = Student()
student1.get_data("Adiba", "005", [99, 100, 99.50])
student1.display_data()