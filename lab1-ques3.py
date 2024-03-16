#income tax

income = float(input("enter total annual income: "))
if income < 200000:
 tax=0
elif income < 400000:
 tax=(income-200000)*0.05
elif income < 800000:
 tax=(income-400000)*0.07+10000
else:
 tax=(income-800000)*0.1+38000
print("income tax to pay", tax)
