# Print hello world message

""" print("Hello, World!") """

# Add two fixed numbers

""" a = 5 
b = 7
print(a+b) """

# Take 2 numbers from user and print sum

""" a = int(input())
b = int(input())
print(a+b) """

# Check if number is even or odd
""" n = int(input())
print("Even" if n % 2 == 0 else "Odd") """

# Swap values of a and b
""" a,b = 3,8
a,b = b,a 
print(a,b) """

# Find factorial using loop
""" n = int(input())
fact = 1
for i in range (1, n+1):
    fact *= i
print(fact) """


# Print first n Fibonacci numbers
""" n = int(input())
a,b = 0,1
for _ in range(n):
    print(a, end=" ")
    a,b = b, a + b """

# Check if number is prime
""" n = int(input())
if n <= 1:
    print("Not prime")
else:
    prime = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            prime = False
            break
    print("Prime" if prime else "Not prime") """


# Reverse the given string
""" s = input()
print(s[::-1]) """


# Check if string is palindrome
""" s = input()
print("Palindrome" if s == s[::-1] else "Not palindrome") """


# Count vowels in a string
""" s = input().lower()
vowels = "aeiou"
count = sum(ch in vowels for ch in s)
print(count) """


# Find sum of all elements in list

""" lst = [2, 5, 1, 8]
print(sum(lst)) """


# Find maximum without using max()

""" lst = [3, 9, 1, 7]
mx = lst[0]
for x in lst:
    if x > mx:
        mx = x
print(mx) """


# Calculate average of 3 numbers

""" a = float(input())
b = float(input())
c = float(input())
print((a + b + c) / 3) """


# Remove duplicates while keeping order
""" lst = [1, 2, 2, 3, 1]
seen = set()
res = []
for x in lst:
    if x not in seen:
        seen.add(x)
        res.append(x)
print(res) """


# Sort a list in ascending order

""" lst = [4, 1, 3]
lst.sort()
print(lst) """


# Create list of squares from 1 to 5
""" squares = [x*x for x in range(1, 6)]
print(squares) """

# Count frequency of each character
""" s = "apple"
d = {}
for ch in s:
    d[ch] = d.get(ch, 0) + 1
print(d) """

# Convert lowercase to uppercase and vice versa
""" s = "Hello"
print(s.swapcase()) """


# Pair elements from two lists using zip
""" for a, b in zip([1, 2], ['a', 'b']):
    print(a,b) """


# Print length of string
""" s = "hello"
print(len(s)) """


# Define a function to greet user
""" def greet(name):
    print("Hello,", name)
greet("Isha") """


# Square a number using lambda
""" square = lambda x: x*x
print(square(6)) """


# Count how many even numbers in the list
""" lst = [1, 2, 3, 4, 5, 6]
count = sum(1 for x in lst if x % 2 == 0)
print(count) """