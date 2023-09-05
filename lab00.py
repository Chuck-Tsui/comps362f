# File: lab00.py

# Replace the following by your full name and 8-digit student number
student_name = "XU Xiaochi"
student_id = "12556828"

def primes(n):
    ls = []
    for i in range(2, n):
        if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1)):
            ls.append(i)
    return ls

def display_triangle(n):
    for a in range (n):
        print("*"*(a+1))

def goldbach(n):
    if n <= 5:
        return None
    primes_list=primes(n)
    for a in range (len(primes_list)):
        for b in range(len(primes_list)):
            for c in range(len(primes_list)):
                if primes_list[a]+primes_list[b]+primes_list[c]==n:
                    return[primes_list[a],primes_list[b],primes_list[c]]

if __name__ == "__main__":
    display_triangle(12)
    for i in range(100, 110):
        print(i, goldbach(i))
    print(goldbach(4))
    print(goldbach(5))
