class Phone:
    def __init__(self, price, brand, camera):
        print("Inside constructor")
        self.price = price
        self.__brand = brand
        self.camera = camera


    def buy(self):
        print("Buying a phone")


class Smartphone(Phone):
    def buy(self):
        print("Buying a Smartphone")

s = Smartphone(20000,"apple",13)

s.buy()
