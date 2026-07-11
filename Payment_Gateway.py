class Payment:
    def pay(self, amount):
        pass


class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")


class NetBanking(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Net Banking.")


c = CreditCard()
u = UPI()
n = NetBanking()

c.pay(5000)
u.pay(1200)
n.pay(3000)