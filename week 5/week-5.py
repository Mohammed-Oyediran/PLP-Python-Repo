#Defining a class with attributes and methods

class calculator:
    def __init__(self, inputA, inputB):
        self.inputA = inputA
        self.inputB = inputB

    def add(self):
        return self.inputA + self.inputB
    
    def subtract(self):
        return self.inputA - self.inputB

    def multiply(self):
        return self.inputA * self.inputB
    
    def divide(self):
        return self.inputA / self.inputB

mycalc = calculator(20,4)

print(mycalc.add())
print(mycalc.subtract())
print(mycalc.multiply())
print(mycalc.divide())


# #Encapsulation

class accountBalance:
    def __init__(self):
        self.initial_balance = input("please enter your initial balance: ")
        self.__balance = float(self.initial_balance)  # Private attribute
        self.amountToWithdraw = float(input("please Enter amount to withdraw: "))

    def withdrawAmount(self):
        if (self.__balance > 0 and self.amountToWithdraw <= self.__balance):

            self.__balance -= self.amountToWithdraw
            print(f"The amount {self.amountToWithdraw} has been withdrawn!")
            print(f"The new balance is {self.__balance}")
            if self.__balance == 0 :
                print("Account is empty! 😢")
            
        else:
           
            print(f"Invalid amount entered. \n Please Enter amount below {self.initial_balance}") 


money = accountBalance()
money.withdrawAmount()

# Inheritance

class area_of_parallogram: #base class
    def __init__(self, base, height):
        self.base = base
        self.height = height

    
    def parallelogram_area(self):
        area = self.base * self.height
        return area
    

class area_of_triangle(area_of_parallogram):
    pass

    def triangle_area(self):
        return self.parallelogram_area()/2
    
    
myArea = area_of_triangle(10,20)
print(myArea.triangle_area())
print(myArea.parallelogram_area())
print(myArea.base)
print(myArea.height)

#Polymorphism

class triangle: 
    def area(self, base, height):
        return base * height / 2

class rectangle:
    def area(self, length, width):
        return length * width
    

#Polymorphism in action

for area in [triangle(), rectangle()]:
    print(area.area(10,20))


# Polymorphism challenge 
class car:
    def move(self):
        print("The car is driving.")

class plane:
    def move(self):
        print("The plane is flying.")

class bicycle:
    def move(self):
        print("The bicycle is pedaling.")


for vehicle in [car(), plane(), bicycle()]:
    vehicle.move()