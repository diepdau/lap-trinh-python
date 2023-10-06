from hinhhoc import HinhHoc
from math import pi


class HinhTron(HinhHoc):
    def __init__(self, canh: float):
        super().__init__(canh)
        self.__banKinh = canh
        
    def __str__(self) -> str:
        return super().__str__() + f"Hinh tron co ban kinh {self.__banKinh}"
    
    @property
    def dienTich(self):
        return  pi * pow(int(self.__banKinh),2)