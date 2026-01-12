num=int(input("enter the number"))
for i in range(1,num+1):
    print(i)


#2nd 
num=int(input("enter the number"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)


#3rd
num=int(input("enter the number"))
sum= 0
for i in range(1,num+1):
    sum +=i
print("sum=",sum)

#4th

num = int(input("Enter a number: "))
count = 0

if num == 0:
    count = 1
else:
    while num != 0:
        num = num // 10
        count += 1

print("Number of digits:", count)







