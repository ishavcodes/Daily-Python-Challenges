# Store your name in a variable 'name' and print it.
""" name = "Isha"
print (name) """

# Create two variables x = 15 and y = 5, and print their multiplication.
""" x = 15
y = 5 
print(x*y) """

# Convert the string "25" into an integer and add 5 to it, then print the result.
""" num1 = 25
num2 = int(num1)
print(num2+5) """

# Check if a number stored in n = 10 is even or odd, and print "Even" or "Odd".
""" n = 10
if n%2==0:
    print("even")
else:
    print("odd")     """

# Use a for loop to print numbers from 1 to 5.
""" for i in range(1,6):
    print(i) """

# Use a while loop to print numbers from 1 to 3.
""" i = 1
while i <=3:
    print(i)
    i += 1 """

# Use a loop to print numbers 1 to 5, but stop the loop when the number becomes 3.
""" i = 1
while i <=5:
    if i == 3:
        break
    print(i)
    i += 1 """

# Print numbers from 1 to 5, but skip the number 3 using continue.
""" i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1 """

# Create a list nums = [10, 20, 30, 40] and print the first and last element.
""" nums = [10, 20, 30, 40]
print(nums[0])
print(nums[-1]) """

# Create a list fruits = ["apple", "banana"] and add "mango" to the list, then print the list.
""" fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits) """

# Create a list nums = [5, 10, 15, 20] and remove the value 15, then print the list.
""" nums = [5, 10, 15, 20]
nums.remove(15)
print(nums) """

# Given the list nums = [10, 20, 30, 40, 50], print the slice [20, 30, 40].
""" nums = [10, 20, 30, 40, 50]
print(nums[1:4]) """

# Create a tuple marks = (90, 80, 70) and print the second element.
""" marks = (90, 80, 70)
print(marks[1]) """

# Create a tuple nums = (1, 2, 3) and try to change the value at index 1 to 10.(This should cause an error because tuples are immutable.)
""" nums = (1, 2, 3)
nums[1] = 10
print(nums) """

#Create a dictionary student = {"name": "Isha", "age": 20} Print the value of "name".
""" student = {"name": "Isha", "age": 20}
print(student["name"]) """

# Create a dictionary info = {"city": "Delhi"} Add a new key "country" with value "India", then print the dictionary.
""" info = {"city": "Delhi"}
info["country"] = "India"
print(info) """

# Create a dictionary data = {"a": 1, "b": 2, "c": 3} Remove the key "b" and print the dictionary.
""" data = {"a": 1, "b": 2, "c": 3}
data.pop("b")
print(data) """

# Create a set nums = {1, 2, 3} and add the value 4, then print the set.
""" nums = {1, 2, 3}
nums.add(4)
print(nums) """


# Create a set vals = {10, 20, 30, 40} Remove the value 30 and print the set.
""" vals = {10, 20, 30, 40}
vals.remove(30)
print(vals) """

# Create a set items = {"pen", "book", "pencil"} Check if "book" is present in the set and print True or False.
""" items = {"pen", "book", "pencil"}
if "book" in items:
    print("True")
else:
    print("False")   """  


# Given the string text = "Python", print "Pyt".
""" text = "Python"
print(text[0:3]) """
     
# Given the string s = "hello", print the reversed string.
""" s = "hello"
print(s[::-1]) """


# Given the string msg = "I love Python" Split the string by spaces and print the resulting list.
""" msg = "I love Python"
print(msg.split()) """
