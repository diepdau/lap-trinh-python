from hinhhoc import HinhHoc


class HinhChuNhat(HinhHoc):
    def __init__(self, canh: float, chieuRong: float):
        super().__init__(canh)
        self.__chieuDai = canh
        self.__chieuRong = chieuRong
        
    def __str__(self) -> str:
        return super().__str__() + f"Hinh chu nhat chieu dai: {self.__chieuDai}, chieu rong: {self.__chieuRong}"
    
    @property
    def dienTich(self):
        return int(self.__chieuDai)*int(self.__chieuRong)