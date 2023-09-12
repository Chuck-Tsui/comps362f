# File: lab01.py

# Replace the following by your full name and 8-digit student number
student_name = "Xu Xiao Chi"
student_id = "12556828"
import math
from random import random

def palindrome_recur(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return palindrome_recur(s[1:-1])

def myth_value(n):
    count = 0
    for a in range(n):
        x = random()
        y = random()    
        if (x**2+y**2) < 1:
            count+=1
    return count / n*4

# Extras
factorial_recur = lambda n :n*factorial_recur(n-1) if (n>1) else 1

factorial_approx = lambda n : math.sqrt(2*math.pi*n)*(n/math.e)**n

def palindrome_loop(s):
    for a in range(len(s)):
        if s[a] != s [-a-1]:
            return False
    return True

def palindrome_slice(s):
    s_reversed = s[::-1]
    if s == s_reversed:
        return True
    else:
        return False


if __name__ == "__main__":
    print("-------------palindrome_recur----------")
    print("Testing palindrome_recur",palindrome_recur("abba")) 
    print("Testing palindrome_recur",palindrome_recur("abeca")) 
    print("-------------my_value-----------------")
    print("n=10,000 the return value:",myth_value(10000))
    print("n=100,000 the return value:",myth_value(100000))
    print("the resulting mathematical constant is pi")

    print("-----------Extras-------------------")
    print(factorial_recur(5))
    print(factorial_approx(5))
    print("palindrome_slice:",palindrome_slice("abbcbba"))
    print("palindrome_slice:",palindrome_slice("abeca"))
    print("palindrome_loop:",palindrome_loop("abeca"))
    print("palindrome_loop:",palindrome_loop("abbcbba"))