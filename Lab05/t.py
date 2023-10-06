# string= "my home"
# s = string.split()
# s.reverse()
# print(" ".join(s))

# chuoi ="Lop CTK44dlu"
# print(chuoi[::-2])

# def outer_fun(a,b):
#     def inner_fun(c,d):
#         return c**d
#     return inner_fun(a,b)
# res = outer_fun(4,3)
# print(res)

# ds = [1,2,"hello"]
# print(ds is list)

# x =0
# for i in range(5):
#     for j in range(1,10,2):
#         x+=1
# print(x)

# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# my_favorite_fruits = set(fruits[5:])
# my_favorite_fruits.append("peach")

# print(my_favorite_fruits)

# class MyClass:
#     def __init__(self,bien) -> None:
#         self.__var = bien
# def myVar(self):
#     return self.__var
# obj = MyClass()
# print(obj.myVar)
# obj.myVar = 7

# class MyClass:
#     def __init__(self, bien) -> None:
#         self.__var = bien
        
#     def myVar(self):  # Corrected method definition
#         return self.__var

# obj = MyClass(5)  # Pass an argument when creating the object
# print(obj.myVar())  # Corrected method call syntax
# obj.myVar = 7  # This line will cause an AttributeError



# class MyClass:
#     def __init__(self, bien) -> None:
#         self.__var = bien

#     @property
#     def myVar(self):  
#         return self.__var

#     @myVar.setter  
#     def myVar(self, value):
#         self.__var = value

# obj = MyClass(5)
# print(obj.myVar)  # Kết quả: 5

# obj.myVar = 7  # Gán giá trị mới cho myVar
# print(obj.myVar)  # Kết quả: 7

# x=5.6
# print(type(x))

# print(type(()) is set)

# def myfunc(*num):
#     sum =0
#     for i in num:
#         sum+=i
#     return sum
# print(myfunc(20,1,6))

# print('Ben', 25, 'California',sep='--')

# def xuatSoLe(batDau,ketThuc):
#     while batDau < ketThuc:
#         if batDau & 1 != 0:
#             print (batDau)
#         batDau+=1
# xuatSoLe(10,20)

# print('Hôm nay',end=',')
# print('ngày mai',end='//')
# print('ngày kia',end=',')

# chuoi = "DaLat University"
# kq=chuoi[2:7]
# print(kq)

# chuoi="Lop CTK44dlu"
# print(chuoi[7:].upper())

# class MyClass:
#     def __init__(self, bien) -> None:
#         self.__var=bien
#     @property
#     def var(self):
#         return self.__var

# obj=MyClass(1)
# print(obj.var)

# bien_cua_toi =("apple","banana","chery")
# print(type(bien_cua_toi))

# def display(**kwargs):
#     for i in kwargs.values():
#         print(i)
# display(hoten="Nga", mssv="12334",yuu=122)

# def display(**kwargs):
#     print(' '.join(map(str, kwargs.values())))

# display(hoten="Nga", mssv="12334", yuu=122)
# Cái này là hiện thị ra Nga...

# Còn bỏ values() đi là hiện mấy thuộc tính

# chuoi="DaLat University"
# print(chuoi[12:])
# print(chuoi[-4:])
# print(chuoi[-4:len(chuoi)])

# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(set(fruits[-3:]))
my_list=[4,6,9,12,17,18,20,11]
def c1(my_list):
    sum=0
    for i in my_list:
        if i&1 !=0:
            sum+=i
    return sum
print(c1(my_list))
def c2(my_list):
    sum=0;
    for i in my_list:
        if i%2 !=0:
            sum+=i
    return sum
print(c2(my_list))
def c3(my_list):
    newList=[]
    for i in my_list:
        if i&1 !=0:
            newList.append((i))
    return sum(newList)
print(c3(my_list))

print(type(range(10)))


                    
    