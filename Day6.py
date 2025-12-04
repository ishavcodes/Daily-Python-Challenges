# Find remainder of two numbers
""" a = int(input())
b = int(input())
print(a%b) """


# Convert kilometers to meters
""" km = float(input())
print(km*1000) """


# Check if number is divisible by 5
""" n = int(input())
print("Yes" if n % 5 == 0 else "No") """


# Find smallest of three numbers
""" a = int(input())
b = int(input())
c = int(input())
print(min(a, b, c)) """


# Count total words in a sentence
""" s = input()
print(len(s.split())) """


# Remove all spaces from string
""" s = input()
print(s.replace(" ", "")) """


# Check if character is uppercase or lowercase
""" ch = input()
print("Uppercase" if ch.isupper() else "Lowercase") """


# Print ASCII value of a character
""" ch = input()
print(ord(ch)) """


# Convert string into list of characters
""" s = input()
print(list(s)) """


# Join list elements into a string
""" lst = ['P', 'y', 't', 'h', 'o', 'n']
print("".join(lst)) """


# Print right triangle star pattern
""" n = 5
for i in range(1, n+1):
    print("*" * i) """


# Print inverted star pattern
""" n = 5
for i in range(n, 0, -1):
    print("*" * i) """


# Print full pyramid star pattern
""" n = 5
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i-1)) """


# Print reverse full pyramid star pattern
""" n = 5
for i in range(n, 0, -1):
    print(" "*(n-i) + "*"*(2*i-1)) """


# Print diamond star pattern
""" n = 5
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i-1))
for i in range(n-1, 0, -1):
    print(" "*(n-i) + "*"*(2*i-1)) """


# Print number triangle
""" n = 5
for i in range(1, n+1):
    print(str(i) * i) """


# Print increasing number pyramid
""" n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print() """


# Print 0-1 triangle pattern
""" n = 5
for i in range(1, n+1):
    for j in range(i):
        print((i+j)%2, end="")
    print() """


# Print alphabet triangle pattern
""" n = 5
for i in range(n):
    print(chr(65+i) * (i+1)) """


# Print hollow square star pattern
""" n = 5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print() """


# Find sum of digits of a number
""" n = int(input())
print(sum(int(d) for d in n)) """


# Reverse a given number
""" n = input()
print(n[::-1]) """


# Check if number is Armstrong
""" n = input()
power = len(n)
total = sum(int(d)**power for d in n)
print("Armstrong" if int(n)==total else "Not Armstrong") """


# Count consonants in a string
""" s = input().lower()
v = "aeiou"
count = sum(1 for ch in s if ch.isalpha() and ch not in v)
print(count) """


# Find second largest number in list
""" lst = [10, 50, 20, 40]
lst.sort()
print(lst[-2]) """


# Find missing number from 1 to n
""" lst = [1, 2, 4, 5]
n = 5
print(n*(n+1)//2 - sum(lst)) """


# Count total characters excluding spaces
""" s = input()
print(len(s.replace(" ", ""))) """


# Check if two strings are anagram
""" s1 = input()
s2 = input()
print(sorted(s1) == sorted(s2)) """


# Convert binary to decimal
""" b = input()
print(int(b, 2)) """


# Convert decimal to binary
""" n = int(input())
print(bin(n)[2:]) """
