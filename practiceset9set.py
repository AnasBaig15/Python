# class Coder:
#     language = "Python"
#     def printLanguages(self):
#         print(f"Out of all the languages here is your language: {self.language}")

# class Programmer(Employee , Coder):
#     company = "ITC Infotech"
#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")

# a = Employee()
# b = Programmer()

# b.show()
# b . printLanguages()
# b.showLanguage()

class Employee:
    a = 1

class Programmer(Employee):
    b = 2
class Manager(Programmer):
    c = 3

o = Employee()
print(o.a)

o = Programmer()
print(o.a , o.b)

o = Manager()
print(o.a , o.b , o.c)

class Employee:
    a = 1

class Programmer(Employee):
    b = 2
class Manager(Programmer):
    c = 3

o = Employee()
print(o.a)

o = Programmer()
print(o.a , o.b)

o = Manager()
print(o.a , o.b , o.c)













