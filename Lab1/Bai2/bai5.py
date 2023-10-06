#Dung de quy:
def KT_Fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return KT_Fibonacci(n-1) + KT_Fibonacci(n-2)

n= int(input("Nhap so thu n :"))
print(f"So Fibonacci thu {n} la {KT_Fibonacci(n)}")

#Khong dung de quy: (DANH DAU CHUA HIEU)
def KT_Fibonacci_KDeQuy(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    
    a=0
    b=1
    for _ in range(2,n+1):
        a,b=b,a+b
    return b

n= int(input("Nhap so thu n :"))
print(f"So Fibonacci thu {n} la {KT_Fibonacci_KDeQuy(n)}")