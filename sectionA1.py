num=int(input("enter the number to check :"))
if num>0:
    print("positive number")
elif num<0:
    print("negative number")
else :
    print("zero number")


#check number is even or odd
num=int(input("enter tha number"))
if num % 2 ==0:
    print("even number")
else:
    print("odd number")

    #3rd
a=9
b=5
c=30
if a >= b and a>=c:
    print("a is greater")
elif b>=a and b>=c:
    print("b is greater")
else:
    print("c is greater")

    #4th

    year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")
