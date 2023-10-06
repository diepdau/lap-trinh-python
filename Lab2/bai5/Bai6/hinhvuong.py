
from hinhhoc import HinhHoc


class HinhVuong(HinhHoc):
    def __init__(self, canh: float):
        super().__init__(canh)
        self.__canh = canh
        
    def __str__(self) -> str:
        return super().__str__() + f"Hinh vuong canh {self.__canh}"
    
    @property
    def dienTich(self):
        return pow(int(self.canh),2)