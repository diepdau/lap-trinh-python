from datetime import datetime
class SinhVien:
    truong="Dai hoc Da Lat"
    
    def _init_(self, maSo:int, hoTen: str, ngaySinh: datetime) -> None:
        self._maSo = maSo
        self._hoTen = hoTen
        self._ngaySinh = ngaySinh
        
            
    @property
    def maSo(self):
        return self._maSo



    @maSo.setter
    def maSo(self, maSo):
        if self.laMaSoHopLe(maso):
            self._maSo = maSo
            
            
    @staticmethod
    def laMaSoHopLe(maso: int):
        return len(str(maso)) == 7


    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong = tenmoi
        
        
    def _str_(self) -> str:
        return (f"{self._maSo}\t{self._hoTen}\t{self._ngaySinh}")


class DanhSachSv:
    def _init_(self) -> None:
        self.dssv = []
        
    def themSinhVien(self, sv:SinhVien):
        self.dssv.append(sv)
    
    def xuat(self):
        for sv in self.dssv:
            print(sv)
    
    def timSvTheoMssv(self, mssv:int):
        return [sv for sv in self.dssv if sv.mssv == mssv]
    
    def timVTSvTheoMssv(self, mssv:int):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == mssv:
                return i
        return -1
    
    
    def xoaSvTheoMSSv(self, maSo:int) -> bool:
        vt = self.timVTSvTheoMssv(maSo)
        if vt!=-1:
            del self.dssv[vt]
            return True
        else:
            return False
    
    def timSvTheoTen(self, ten:str):
        return [sv for sv in self.dssv if ten in sv._hoTen]
    
    def timSvSinhTruocNgay(self, ngay: datetime):
        return [sv for sv in self.dssv if sv._ngaySinh < ngay]
    
    #Sap xep danh sach tang theo ho ten 
    def sapXepTangHoTen(self):
        self.dssv.sort(key=lambda sv: sv._hoTen)
    #Sap xep danh sach giam theo ho ten
    def sapXepGiamHoTen(self):
        self.dssv.sort(key =lambda sv: sv._hoTen, reverse=True)
    
    def docTuFile(self, filename):
        try:
            with open(file,'r') as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split('\t')
                    maSo=int(parts[0])
                    hoTen = parts[1]
                    ngaySinh = datetime.strptime(parts[2], '%Y-%m')
                    sv=SinhVien(maSo, hoTen, ngaySinh)
                    self.themSinhVien(sv)
            print(f"Doc tu file {filename} thanhf cong")
        except FileNotFoundError:
            print ("File khong ton tai")
        except Exception as e:
            print(f"Loi khi doc file {str(e)}")

#Su dung
if __name__ == "__main__":
    dssv = DanhSachSv()
    dssv.docTuFile("dssv.txt")
    
    print("Danh sach truoc khi sap xep:")
    dssv.xuat()
    
    dssv.sapXepTangHoTen()
    print("\nDanh sach sap tang ho ten")
    dssv.xuat()
    
    dssv.sapXepGiamHoTen()
    print("\nDanh sach sap giam ho ten")
    dssv.xuat()
    
    
    
    