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
            if self.dssv[i].mssv == ms:
                return i
        else:
            return -1

    def timSVTheoLoai(self, loai: str):
        if loai == "chinhquy":
            return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy)]
        return [sv for sv in self.dssv if isinstance(sv, SinhVienPhiCQ)]

    # Tìm sinh viên có điểm rèn luyện từ 80 trở lên
    def timSVDiemHon80(self):
        return [sv for sv in self.dssv  if sv["DiemRL"] >= 80]

    # Tìm sinh viên có trình độ cao đẳng sinh trước 15/8/1999
    def timSV_CaoDang_SinhTruoc(self):
        if self.timSVTheoLoai("Cao Đẳng"):
            return [sv for sv in self.dssv if sv["ngaySinh"] < "15/08/1999"]
        else:
            return -1
    
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

    def __str__(self):
        s = f"{'MSSV':<16}{'HỌ VÀ TÊN':<24}{'NGÀY SINH':<20}{'TRÌNH ĐỘ (PCQ)':<20}{'RL (CQ)'}{'TGĐT (PCQ)':>15}\n"
        "========================================================================================================\n"
        for sv in self.dssv:
            s += "{}\n".format(sv)
        return s