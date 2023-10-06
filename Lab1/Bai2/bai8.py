import math

def Tinh(a,b,c):
    delta= b**2 - 4*a*c
    if delta > 0:
        x1=(-b + math.sqrt(delta)) / (2*a)
        x2=(-b - math.sqrt(delta)) / (2*a)
        return x1, x2
    elif delta ==0:
        x= -b / (2*a)
        return x
    else:
        return None

a= float(input("Nhap a:"))
b= float(input("Nhap b:"))
c= float(input("Nhap c:"))

kq = Tinh(a,b,c)

if kq:
    if len(kq) == 2:
        x1,x2 = kq
        print("Phuong trinh co hai nghien x1, x2 lan luot la :",x1,x2)
    else:
        x = kq[0]
        print("Phuong trinh co nghien kep",x)
else:
    print("Phuong trinh vo nghiem")