for i in range(1,101):
    if i %2==0:
        print(i)


#2nd
num=int(input("enter the given number"))
if num > 1:
    for i in range (2,num):
        if num %i ==0:
            print("not prime ")
            break
        else:
            print("prime ")

else:
    print("not prime")



#3rd
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial of", num, "is", fact)


#5th

num = int(input("Enter a number: "))
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print("Sum of digits:", sum)
