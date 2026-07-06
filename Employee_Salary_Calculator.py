class Employee:
    def get_data(self, name="", Id=0, salary=None):
            self.name = name
            self.Id = Id
            self.salary = salary

    def calculate_HRA(self):
        self.hra = self.salary*0.20

    def calculate_DA(self):
        self.da = self.salary*0.10

    def gross_salary(self):
        self.gross = self.salary + self.hra + self.da

    def display_details(self):
        print(f"HRA = {self.hra}")
        print(f"DA = {self.da}")
        print(f"Gross Salary = {self.gross}")


Employee1 = Employee()
Employee1.get_data("Adiba", "1234", 1000000)
Employee1.calculate_HRA()
Employee1.calculate_DA()
Employee1.gross_salary()   
Employee1.display_details()