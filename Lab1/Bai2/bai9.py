def TinhGiaThua(n):
    giaithua=1
    if n==0 or n==1 :
        return giaithua
    else:
        for i in range(2, n+1):
            giaithua=giaithua*i
        return giaithua

n= int(input("Nhap n tinh giai thua: "))
print(f"Gia thua cua {n} la : {TinhGiaThua(n)}")