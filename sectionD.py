

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime Number")
else:
    print("Not Prime Number")

    #2nd
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

num = int(input("Enter a number: "))
print("Factorial is:", factorial(num))

#3rd
def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

print("Simple Interest is:", simple_interest(p, r, t))

#4th

def is_palindrome(num):
    temp = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    return temp == rev

num = int(input("Enter a number: "))
if is_palindrome(num):
    print("Palindrome number")
else:
    print("Not a palindrome number")




