

class HinhHoc:
    def __init__(self, canh: float):
        self.__canh = canh
        
    @property
    def canh(self):
        return self.__canh
    
    @canh.setter
    def canh(self, canh: float):
        self.__canh = canh
        
    def dienTich(self):
        pass
    
    def __str__(self) -> str:
        return f"Hinh Hoc:"