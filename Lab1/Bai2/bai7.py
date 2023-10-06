import math

def TongCanBacHai(n):
    tong = 0
    for i in range(1, n + 1):
        tong += math.sqrt(i)
    return tong

n = int(input("Nhập số nguyên dương n: "))
print("Tổng căn bậc hai của", n, "số nguyên đầu tiên là:", TongCanBacHai(n))
