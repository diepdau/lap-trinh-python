import math


class PhanSo:
    def __init__(self, tu=0, mau=1):
        self.tu = tu
        self.mau = mau

    def __str__(self):
        return "{}/{}".format(self.tu, self.mau)

    
    def RutGon(self):
        ucln = math.gcd(self.tu, self.mau)
        self.tu //=ucln
        self.mau //=ucln
    
    def __add__(self, other):
        kq = PhanSo()
        kq.tu = self.tu*other.mau+self.mau*other.tu
        kq.mau = self.mau*other.mau
        kq.RutGon()
        return kq

    def __sub__(self, other):
        kq = PhanSo()
        kq.tu = self.tu*other.mau-self.mau*other.tu
        kq.mau = self.mau*other.mau
        # kq.RutGon()
        return kq

    def __mul__(self, other):
        kq = PhanSo()
        kq.tu = self.tu*other.tu
        kq.mau = self.mau*other.mau
        # kq.RutGon()
        return kq

    def __truediv__(self, other):
        kq = PhanSo()
        kq.tu = self.tu*other.mau
        # kq.mau = self.mau*other.tu
        kq.RutGon()
        return kq
a = PhanSo()
a.tu = 2
a.mau = 3

b = PhanSo (3,5)

print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")

# if __name__ == "__main__":
#     phanSo = PhanSo(4,8)
#     print("Phan so truoc khi rut gon", phanSo)
    
#     phanSo.rutGon()
#     print("Phan so sau khi rut gon: ", phanSo)