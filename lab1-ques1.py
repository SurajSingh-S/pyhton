#simple interest
p=float(input("p: "))
r=float(input("r: "))
t=float(input("t: "))
si=(p*r*t)/100
print(si)


#compound interest
p=float(input("p: "))
r=float(input("r: "))
n=float(input("n: "))
ci=p*(1+r/100)**n-p
print(ci)
