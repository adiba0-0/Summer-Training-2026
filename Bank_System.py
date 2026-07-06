class BankAccount:

    def Account_info(self, Account_Holder_Name="", Account_Number=None, Account_Balance=None):
        self.Account_Holder_Name=Account_Holder_Name
        self.Account_Number=Account_Number
        self.Account_Balance=Account_Balance

    def withdraw(self):
        withdraw=int(input("Enter the amount you want to withdraw: "))
        while(withdraw>self.Account_Balance):
            print("Insufficient Balance! Please try again.")
            withdraw=int(input("Enter the amount you want to withdraw: "))
        self.Account_Balance = self.Account_Balance - withdraw

    def deposit(self):
        deposit=int(input("Enter the amount you want to deposit: "))
        while(deposit<0):
               print("ERROR! The value must be positive!")
               deposit=int(input("Enter the amount you want to deposit: "))
        self.Account_Balance = self.Account_Balance + deposit
        print(f"Balance: {self.Account_Balance}")

    def display_balance(self):
         print(f"Balance: {self.Account_Balance}")

Balance = BankAccount()
Balance.Account_info("Adiba", "1234567890", 10000)
Balance.withdraw()
Balance.deposit()
Balance.display_balance()