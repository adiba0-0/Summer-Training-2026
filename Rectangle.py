class Rectangle:
    def get_data(self, length="", breadth=""):
                self.length = length
                self.breadth = breadth
    
    def perimeter(self):
        self.perimeter_value = 2 * (self.length + self.breadth)
    
    def area(self):
        self.area_value = self.length * self.breadth
    
    def check_square(self):
        print(f"Is the given shape a square? ")
        if self.length == self.breadth:
            print("Yes")
        else:
            print("No!")
    
    def display_details(self):
        print(f"Perimeter of the rectangle = {self.perimeter_value}")
        print(f"Area of the rectangle = {self.area_value}")
        self.check_square()
    

Rectangle1 = Rectangle()
length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))
Rectangle1.get_data(length, breadth)
Rectangle1.perimeter()
Rectangle1.area()  
Rectangle1.display_details()