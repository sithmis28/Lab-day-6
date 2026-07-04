salary=float(input("enter your salary:"))
if salary<=100000:
    bouns=salary*15/100
    
elif 50000<=salary<=99999:
    bouns=salary*10/100
    
else:
    bouns=salary*5/100
    net_salary=bouns+salary
    print("bouns is", bouns)
    print("salary is", net_salary)
