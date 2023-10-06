from bai3 import PhanSo
class DanhSachPhanSo:
    def __init__(self):
        self.ds_phan_so = []
    
    def TimTu(self, x: PhanSo):
        return x.tu

    def TimMau(self, x: PhanSo):
        return x.mau
        
    def themPhanSo(self, phan_so):
        self.ds_phan_so.append(phan_so)
        
    def demPhanSoAm(self):
        return len([ps for ps in self.ds_phan_so if ps.tuSo * ps.mauSo < 0])
    
    def timPhanSoDuongNhoNhat(self):
        ds_phan_so_duong = [ps for ps in self.ds_phan_so if ps.tuSo * ps.mauSo > 0]
        if not ds_phan_so_duong:
            return None
        return min(ds_phan_so_duong, key=lambda ps: ps.tuSo / ps.mauSo)
    
    def timViTriPhanSo(self, x):
        return [i for i, ps in enumerate(self.ds_phan_so) if ps == x]
    
    def tongPhanSoAm(self):
        return sum(ps for ps in self.ds_phan_so if ps.tuSo * ps.mauSo < 0)
    
    def xoaPhanSo(self, x):
        self.ds_phan_so = [ps for ps in self.ds_phan_so if ps != x]
        
    def xoaPhanSoCoTuBangX(self, x):
        self.ds_phan_so = [ps for ps in self.ds_phan_so if ps.tuSo != x]
        
    def SapXepTheoTu(self, condition=False):
        self.ds_phan_so.sort(key=self.TimTu, reverse=condition)
    def SapXepTheoMau(self, condition=False):
        self.ds_phan_so.sort(key=self.TimMau, reverse=condition)
      
    def xuat(self):
        for ps in self.ds_phan_so:
            print(ps)

if __name__ == "__main__":
    ds_phan_so = DanhSachPhanSo()
    
    ds_phan_so.themPhanSo(PhanSo(3, 4))
    ds_phan_so.themPhanSo(PhanSo(-1, 2))
    ds_phan_so.themPhanSo(PhanSo(2, 5))
    ds_phan_so.themPhanSo(PhanSo(5, 6))
    ds_phan_so.xuat()
    ds_phan_so.SapXepTheoTu(False)
    print("Sap xep tang theo tu")
    ds_phan_so.xuat()
