# class Programmer:
#     company = " MIcrosoft"
#     def __init__(self, name, salary , pin):
#         self.name = name
#         self.salary = salary
#         self.pin = pin

# p = programmer("Anas",12000,245000)
# print(p.name,p.salary,p.pin,p.company)
# r = programmer("ALi",123000,245080)
# print(r.name,r.salary,r.pin,r.company)


# class Calculator:
#     def __init__(self , n ):
#         self.n = n
#     def square(self):
#         print(f"The square is {self.n*self.n}")
# def square(self):
#          print(f"The cube is {self.n* self.n* self.n}")
# def square(self):
#          print(f"The squareroot is {self.n**1/2}")
# a = Calculator(4)
# a.square()

class Demo:
    a = 4
    
o = Demo()
print(o.a) # print class attribute because instance attribute is not present
o.a = 0 #instance attribute is set
print(o.a) # prints the instance attribute because instance attribute is present
print(Demo.a) # print class attribute













