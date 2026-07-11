class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    def verify_pin(self, pin):
        return pin == self.__pin

    def deposit(self, pin, amount):
        if self.verify_pin(pin):
            self.__balance += amount
            print("Amount Deposited Successfully")
        else:
            print("Invalid PIN")

    def withdraw(self, pin, amount):
        if self.verify_pin(pin):
            if amount <= self.__balance:
                self.__balance -= amount
                print("Amount Withdrawn Successfully")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid PIN")

    def display_balance(self, pin):
        if self.verify_pin(pin):
            print("Balance =", self.__balance)
        else:
            print("Invalid PIN")

    def change_pin(self, old_pin, new_pin):
        if self.verify_pin(old_pin):
            self.__pin = new_pin
            print("PIN Changed Successfully")
        else:
            print("Invalid Old PIN")


atm = ATM(1234, 10000)

atm.display_balance(1234)
atm.deposit(1234, 2000)
atm.withdraw(1234, 3000)
atm.change_pin(1234, 4321)
atm.display_balance(4321)