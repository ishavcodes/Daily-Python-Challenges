# Function to return greeting message
""" def greet(name):
    text = "Hello " + name
    return text


text2 = greet("Isha")

print(text2) """


# Function to return square of a number
""" def square(num):
    text = num*num
    return text

text2 = square(4)
print(text2) """


# Class with a brand attribute and printing it using an object
""" class car:
    brand = "tata"

c1 = car()
print(c1.brand) """


# Student class with course attribute and printing a message
""" class Student:
    course = "Python"
    
s1 = Student()
print("I am Studying",s1.course) """



# Person class with constructor to set name and city
""" class Person:
    def __init__(self,name,city):
        self.name = name
        self.city = city

p1 = Person("Isha","Bhopal")
print(p1.name)
print(p1.city)  """       


# Car class with constructor to set brand and price
"""  class Car:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

c1 = Car("Tata", 800000)
print(c1.brand,"car costs",c1.price)  """


# Dog class with bark method
""" class Dog:
    def __init__(self,name):
        self.name = name

        
    def bark(self):
        print("Dog is Barking")

d1 = Dog("Tommy")
d1.bark() """


# Student class with show method
""" class Student:
    def __init__(self,name,course):
        self.name = name 
        self.course = course

    def show(self):
        print("I am", s1.name,"and I am studying",s1.course)    

s1 = Student("Isha","Python")
s1.show() """


# Handling invalid integer conversion using try-except
""" try:
    num = int("hello")
except:
    print("Invalid Input!") """


# divide with try-except-finally
""" num1 = int(input())
num2 = int(input())
try:
    result = num1/num2
    print(result)
except:
    print("Connot divide!")
finally:
    print("Program finished")  """


# Using else block to validate number input
""" try:
    num = int(input("Enter a number: "))
except:
    print("Invalid number!")
else:
    print("Valid number!")  """




# Custom exception for negative age input
""" try:
    age = int(input())
    if age < 0:
        raise Exception("Age cannot be negative")
except:
    print("Error: Age cannot be negative") """
