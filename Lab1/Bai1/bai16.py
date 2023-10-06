n=int(input("Nhap n:"))

def Hieu2So(n:int):
    if n>17: 
         return 2*(n-17)
    else:
        return 17-n

print("Ket qua:",Hieu2So(n))