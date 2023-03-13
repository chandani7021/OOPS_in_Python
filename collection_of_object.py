class Customer:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("I am",self.name,"and i am",self.age)

c1 = Customer("Nitish",34)
c2 = Customer("Nikhil",21)
c3 = Customer("Nikita",18)

L = [c1,c2,c3]

for i in L:
   i.intro()
