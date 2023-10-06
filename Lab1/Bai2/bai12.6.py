#Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng

def laSoLe_KhongChiaHetCho3(n):
    if n % 2 ==0:
        return False
    if n % 3 ==0: 
        return False
    return True

def TinhTich(a):
    tich = 1
    for i in a:
       tich*=i
    return tich
dayso=[2,3,4,5,6,7,8,9]
daysole_Khongchiahetcho3 = list(filter(laSoLe_KhongChiaHetCho3,dayso))
print(f"Cac so le va khong chia het cho 3 trong day {dayso} la {daysole_Khongchiahetcho3}")
print(f"Tich cua day so la : ",TinhTich(daysole_Khongchiahetcho3))
