import math

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def print_primes_up_to(n):
    print(f"Prime numbers between 2 and {n} are:")
    for num in range(2, n + 1):
        if is_prime(num):
            print(num, end=' ')
    print()

try:
    N = int(input("Enter a number (N): "))
    if N < 2:
        print("There are no prime numbers less than 2.")
    else:
        print_primes_up_to(N)
except ValueError:
    print("Please enter a valid integer.")
