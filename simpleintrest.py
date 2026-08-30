#write a program find a simple intrest.

p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time: "))

si = (p * r * t) / 100

print("Simple Interest =", si)
