# from functools import reduce
# name = input("Enter Your name:")
# marks = int(input("Enter your Marks:"))
# number = int(input("Enter your number :"))

# s = " The name of the student is {} , his marks are {} and phone number is {}".format(name,marks,number)

# print(s)


# table = [7*i for i in range(1,11)]
# s = "\n" .join(table)

# print(s)

# def divisible5(n):
#     if(n%5 == 0):
#         return True
#     return False
# a = [1,2,3,5465,53,45,]
# f = list(filter(divisible5,a))
# print(f)

# a = [1,2,3,5465,53,45,]

# def greater(a,b):
#     if(a>b):
#         return a 
#     return b
# print(reduce(greater,1))
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()


