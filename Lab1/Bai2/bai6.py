#Dung de quy:
def KT_Fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return KT_Fibonacci(n-1) + KT_Fibonacci(n-2)

def TongFibonacci_DeQuy(n):
    tong = 0
    for i in range(1, n + 1):
        tong += KT_Fibonacci(i)
    return tong

n=int(input("Nhap n ,So Fibonacci can tinh tong : ")) 
print(n,"số đầu tiên của dãy số fibonacci: ")
sb = ""
for i in range(0, n):
    sb = sb + str(KT_Fibonacci(i)) + ", "

print(sb)
print("Tổng của", n, "số Fibonacci đầu tiên (đệ quy):", TongFibonacci_DeQuy(n))




#Khong de quy DANH DAU CHUA HIEU
def KT_Fibonacci_KhongDeQuy(n):
    f0 = 0
    f1 = 1
    fn = 1
 
    if n < 0:
        return -1
    elif n == 0 or n == 1:
        return n
    else:
        for i in range(2, n):
            f0 = f1
            f1 = fn
            fn = f0 + f1
        return fn

def TongFibonacci_KhongDeQuy(n):
    tong = 0
    for i in range(1, n + 1):
        tong += KT_Fibonacci_KhongDeQuy(i)
    return tong

n=int(input("Nhap n ,So Fibonacci can tinh tong : ")) 
print(n,"số đầu tiên của dãy số fibonacci: ")

sb = ""
for i in range(0, n):
   sb = sb + str(KT_Fibonacci_KhongDeQuy(i)) + ", "
   
print(sb)
print("Tổng của", n, "số Fibonacci đầu tiên (không đệ quy):", TongFibonacci_KhongDeQuy(n))
