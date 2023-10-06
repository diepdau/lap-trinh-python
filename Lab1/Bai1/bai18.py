n=int(input("Nhap so thu 1:"))
b=int(input("Nhap so thu 2:"))
c=int(input("Nhap so thu 3:"))

def TinhTong (n,b,c):
    if n==b and b==c :
        return (n+b+c)*3
    else: return n+b+c
print("Ket qua la: ", TinhTong (n,b,c))
