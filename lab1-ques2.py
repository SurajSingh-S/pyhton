#Emi 
p = float(input("Enter principal amount: "))
R = float(input("Enter annual interest rate: "))
n = int(input("Enter number of months: " ))

# Calculating interest rate per month
r = R/(12*100)

# Calculating Equated Monthly Installment (EMI)
emi = p * r * ((1+r)**n)/((1+r)**n - 1)
print("Monthly EMI = ", emi)

#gst
cost=float(input("enter cost of the products/services: "))
gstPer=float(input("enter the % charged for gst: "))
gst=cost*gstPer/100
amount=cost+gst
print("gst is",gst)
print("amount to pay is ",amount)
