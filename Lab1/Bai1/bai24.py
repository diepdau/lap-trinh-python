import math

x= int(input("Nhap x= "))
y= int(input("Nhap y= "))
def Tinh(x,y):
    return math.pow((x+y), 2)

print(f"Ket qua ({x}+{y})^2= ",Tinh(x,y))