"""
Create a Python file named lab_8-4.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Write a function count_a(word) that takes in a string word and returns the number of a's in the word. 
The function should count both lowercase (a) and uppercase (A)
"""

def count_a(word):
    wordl = word.lower()
    a= word.find("a")
    i = 0
    while a > -1:
        a = wordl.find("a")
        wordl.lower()
        wordl = wordl[a+1:]
        i = i + 1
    if i <= 0:
        print (0)
    else:
        print (i - 1)
    
count_a("aA")
"""
Create a Python file named lab_8-5.py

Write a function factorial(num) that takes in a number num 
and returns the product of all numbers from 1 up to and including num
"""
def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    print("The factorial of ", num, " is ", fact)
factorial (10)

"""
Create a Python file named lab_8-6.py

Write a function is_palindrome(word) that takes in a string word 
and returns the true if the word is a palindrome, false otherwise. 

A palindrome is a word that is spelled the same forwards and backwards.
"""
def is_palindrome(word):
    wordl = word.lower()
    word2 = wordl[::-1]
    if word2 == wordl:
        print ("true")
    else:
        print ("false")
is_palindrome("Racecar")