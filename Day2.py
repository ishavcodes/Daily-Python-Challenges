""" Aapko Python syntax follow karte hue apne baare mein 3 variables banana hai:
your_name
your_age
your_city """


""" your_name = "Isha"
your_age = 22
your_city = "Dhanbad" """


""" lucky_number = 4
my_height = 5.4
favorite_food = "Biryani" """


""" num1 = 7
num2 = float(num1)

num3 = 5.7
num4 = int(num3)

num5 = 8
num6 = str(num5) """


""" 
temp = 45
if temp >= 30:
    print("It's Hot")
elif temp >= 20:
    print("Normal Weather")
else:
    print("Cold") """


# Program to print numbers from 1 to 10 using a for loop
""" for i in range(1,11):
    print(i) """

# Program to print numbers from 1 to 10 using while loop
""" count = 1
while count <= 10:
    print(count)
    count +=1 """

# Program to stop loop when number reaches 5
""" count = 1
while count <= 10:
    if count == 5:
        break
    print(count)
    count +=1 """

# Program to skip number 7 in the loop
""" count = 1
while count <=10:
    if count == 7:
        count +=1
        continue
    print(count)
    count +=1  """

# Program to access characters using indexing
""" text = "Python"
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5]) """

# Program to practice string slicing
""" text = "Python"
print(text[0:3])
print(text[3:6])
print(text[1:4]) """


#Given text = "PythonProgramming", print the first 6 characters.

""" text = "PythonProgramming"
print(text[0:6])
print(text[6:12])
print(text[12:17]) """

# Question: Given text = "PythonProgramming", print the reversed string using slicing.

""" text = "PythonProgramming"
print(text[::-1]) """

# Question: Given text = "I love Python programming", split the string into words.

""" text = "I love Python programming"
print(text.split()) """

# Question: Given text = "Python is super easy", split the string into words.

""" text = "Python is super easy"
print(text.split()) """

# Question: Given data = "red,green,blue,yellow", split the string at commas.

""" data = "red,green,blue,yellow"
print(data.split(",")) """

# Question: Given words = ['I', 'love', 'Python'], join the list into a single string with spaces.

""" words = ['I', 'love', 'Python']
print(" ".join(words)) """

""" items = ['red', 'green', 'blue']
print(" ".join(items)) """

""" nums = ['10', '20', '30', '40']
print(" ".join(nums)) """

# Given items = ['sun', 'moon', 'stars'], join them using '-' (hyphen).
""" items = ['sun', 'moon', 'stars']
print("-".join(items)) """

# Given words = ['Python', 'is', 'fun'], join them using space.
""" words = ['Python', 'is', 'fun']
print(" ".join(words)) """

# Given nums = [5, 10, 15, 20, 25], print the element at index 3.
""" nums = [5, 10, 15, 20, 25]
print(nums[3]) """

# Given data = [1, 2, 3, 4], change the element at index 1 to 200.
""" data = [1, 2, 3, 4]
data[1] = 200
print(data) """

# Given items = [10, 20, 30], append 40 and print the updated list.
""" items = [10, 20, 30]
items.append(40)
print(items) """

# Given data = ['a', 'b', 'd'], insert 'c' at index 2.
""" data = ['a', 'b', 'd']
data.insert(2,'c')
print(data) """

# Given t = (5, 10, 15, 20), print the element at index 2.
""" t = (5, 10, 15, 20)
print(t[2]) """

# Given t = ("a", "b", "c", "d"), print the length of the tuple.
""" t = ("a", "b", "c", "d")
print(len(t)) """

# t = ("red", "green", "blue") Tuple ki length print karo.
""" t = ("red", "green", "blue")
print(len(t)) """

# t = (2, 4, 6, 8, 10) 4th index ka element print karo.
""" t = (2, 4, 6, 8, 10)
print(t[4]) """

# Question: What will be the value of key "age" in {"name": "Ria", "age": 18, "city": "Bhopal"}?
""" my_dict =  {"name": "Ria", "age": 18, "city": "Bhopal"}
print(my_dict["age"]) """

# Question: What will be the length of the dictionary {"a":1, "b":2, "c":3, "d":4}?
""" my_dict = {"a":1, "b":2, "c":3, "d":4}
print(len(my_dict)) """

# Question: What will be the dictionary after adding "age": 25 to {"name": "Aarav"}?
""" my_dict = {"name": "Aarav"}
my_dict["age"] = 25
print(my_dict) """

# Question: What will be the dictionary after updating "city" to "Mumbai" in {"city": "Delhi"}?
""" my_dict = {"city": "Delhi"}
my_dict["city"] = "Mumbai"
print(my_dict) """

# Question: What will be the dictionary after deleting key "age" from {"name": "Ria", "age": 20}?
""" my_dict = {"name": "Ria", "age": 20}
del my_dict["age"]
print(my_dict) """

# Question: What will be the dictionary after using pop("b") on {"a":1, "b":2, "c":3}?
""" my_dict = {"a":1, "b":2, "c":3}
my_dict.pop("b")
print(my_dict) """

# Question: What will be the set after adding 40 to {10, 20, 30}?
""" my_set = {10, 20, 30}
my_set.add(40)
print(my_set) """

# Question: What will be the set after removing 3 from {1, 2, 3, 4}?
""" my_set = {1, 2, 3, 4}
my_set.remove(3)
print(my_set) """

# Question: What will be the result of union between {1, 2, 3} and {3, 4, 5}?
""" set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2)) """

# Question: What will be the result of intersection between {10, 20, 30} and {20, 40}?
""" set1 = {10, 20, 30}
set2 = {20, 40}
print(set1.intersection(set2)) """