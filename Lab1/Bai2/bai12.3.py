import math

def XuatSNT(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

dayso = [2, 3, 4, 5, 6, 7, 8]
a = list(filter(XuatSNT, dayso))
print(f"Cac so nguyen to cua day trong day {dayso} la :",a)
Max = 0  
for x in a:
    if x > Max:
        Max = x

print(f"Cac so nguyen to lon nhat trong {a} la:", Max)
