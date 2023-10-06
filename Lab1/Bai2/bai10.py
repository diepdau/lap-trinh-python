
def in_tam_giac_duoi(so_hang):
    for i in range(so_hang-1):
        print('*' + ' ' * (i * 2) + '*')
    for i in range(1, so_hang):
         print('*' + ' ' ,end = '')
    print('*')
      
so_hang = int(input("Nhập số hàng: "))
in_tam_giac_duoi(so_hang)

