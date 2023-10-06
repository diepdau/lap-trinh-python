r=float(input("Nhap ban kinh r: "))
while r<0:
    print("Nhap khong hop le! Vui long nhap lai: ")
    r=float(input("Nhap ban kinh r: "))
def STron(r):
    return 3.14*r*r
print(f"Dien tich hinh trong co ban kinh {r} la :",STron(r))