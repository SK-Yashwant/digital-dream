emp_name=input("enter employe name:")
emp_id=input("enter employe id:")rk
basic_salary=float(input("enter basic salary:"))
hra=0.20*basic_salary
da=0.10*basic_salary
pf=0.12*basic_salary
net_salary=basic_salary+hra+da-pf

print("salary summary:")
print(f"employe name:",emp_name)
print(f"employe id:",emp_id)
print(f"basic salary:",basic_salary)
print(f"hra(20%)",hra)
print(f"da(10%)",da)
print(f"pf(12%)",pf)
print(" net salary:",net_salary)