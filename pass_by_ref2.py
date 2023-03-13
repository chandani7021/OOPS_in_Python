##class Customer:
##
##    def __init__(self, name):
##        self.name = name
##
##def greet(customer):
##    print(id(customer))
##    customer.name = "Nitish"
##    print(customer.name)
##    print(id(customer))
##    
##cust = Customer("Nitika")
##print(id(cust))
##
##
##greet(cust)
##
##print(cust.name)


##def Change(L):
##    print(id(L))
##    L.append(5)
##    print(id(L))
##
##
##L1 = [1,2,3,4]
##print(id(L1))
##print(L1)
##Change(L1)
##print(L1)


def Change(L):
    print(id(L))
    L = L+(5,6)
    print(id(L))


L1 = (1,2,3,4)
print(id(L1))
print(L1)
Change(L1)
print(L1)
            
