def laSoLe(n):
    if n % 2 ==0:
        return False
    else: 
        return True

def TrungBinhCong(a):
    tong=0
    for i in a:
        tong+= i
    return tong / len(a)
dayso=[2,3,4,5,6,7,8]
daysole = list(filter(laSoLe,dayso))
print(f"Cac so le trong day {dayso} la {daysole}")
print(f"Trung binh cua day so le la : ",TrungBinhCong(daysole))