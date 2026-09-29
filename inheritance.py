# class food:# parent
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#         print(f"{self.name} is created from base class")

#     def eat(self):
#         print("eat method from base class")

# class apple(food): # child
#     def __init__(self,name,price,amount):
#        #food.__init__(self,name) # create instance from base class
#        super().__init__(name,price)
#        self.amount=amount
#        print(f"{self.name} is created from derived class and price is {self.price} and amount is {self.amount}")

#     def get_from_tree(self):
#         print("Get from tree from derived class")

# food1=apple("pizza",500,5)
# food1.eat()
# food1.get_from_tree()



#==================================================================================================

#=====================================*{MULTIPLE INHERITANCE}*=====================================



class base1:
    def __init__(self):
        print("Base1")

class base2:
    def __init__(self):
        print("Base2")
    

class derived(base1,base2):
    pass

my_var=derived() # OUTPUT:=> Base1




class Base:
    pass

class derived1(Base):
    pass

class derived2(derived1):
    pass