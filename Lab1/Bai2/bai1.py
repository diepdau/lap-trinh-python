import math
a=float(input("Nhap a: "))
b=float(input("Nhap b: "))

def TinhTong(a,b):
    return a+b

def TinhHieu(a,b):
    return (a/b)

def TinhMu(a,b):
    return pow(a,b)

print(f"{a}+{b}=",TinhTong(a,b))
print(f"{a}/{b}=",TinhHieu(a,b))
print(f"{a}^{b}=",TinhMu(a,b))