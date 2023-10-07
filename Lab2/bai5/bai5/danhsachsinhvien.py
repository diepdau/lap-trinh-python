from sinhvienchinhquy import SinhVienChinhQuy
from sinhvienphichinhquy import SinhVienPhiCQ
from sinhvien import SinhVien
from datetime import datetime

class DanhSachSV:
    def __init__(self) -> None:
        self.dssv = []
        
    def themSV(self, sv: SinhVien):
        self.dssv.append(sv)
        
    def xuat(self):
        for sv in self.dssv:
            print(sv)
            
    def timSVTheoMs(self, ms: str):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == ms:
                return i
        else:
            return -1

    def timSVTheoLoai(self, loai: str):
        if loai == "chinhquy":
            return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy)]
        return [sv for sv in self.dssv if isinstance(sv, SinhVienPhiCQ)]

    def timSVDiemHon80(self):
        return list(filter(lambda sv: isinstance(sv, SinhVienChinhQuy) and sv.DiemRL >= 80, self.dssv))


    def timSV_CaoDang_SinhTruoc(self):
        return list(filter(lambda sv: isinstance(sv, SinhVienPhiCQ) and sv.TrinhDo == "Cao Đẳng" and sv.ngaySinh < datetime.strptime("15/8/1999", "%d/%m/%Y"), self.dssv))

    def ReadFile(self, path: str) -> None:
        line = ""
        with open(path, "r", encoding="utf8") as fileReader:
            while (line := fileReader.readline()) != "":
                sv = ""
                s = line.split("*")
                if s[0] == "CQ":
                    sv = SinhVienChinhQuy(int(s[1]), s[2], datetime.strptime(
                        s[3], "%d/%m/%Y"), int(s[4]))
                else:
                    sv = SinhVienPhiCQ(int(s[1]), s[2], datetime.strptime(
                        s[3], "%d/%m/%Y"), s[4], float(s[5]))
                self.themSV(sv)
        fileReader.close()
