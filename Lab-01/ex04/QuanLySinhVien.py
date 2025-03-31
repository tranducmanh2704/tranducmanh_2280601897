from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    def generateID(self):
        maxId = 1
        if(self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0].id
            for sv in self.listSinhVien:
                if(maxId < sv.id):
                    maxId = sv.id
            maxId = maxId + 1
        return maxId
    
    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()
    
    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập chuyên ngành sinh viên: ")
        diemTB = float(input("Nhập điểm của sinh viên: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv:SinhVien = self.findByID(ID)
        if(sv != None):
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính sinh viên: ")
            major = input("Nhập chuyên ngành sinh viên: ")
            diemTB = float(input("Nhập điểm của sinh viên: "))    
            sv.name = name
            sv.sex = sex
            sv.major = major
            sv.diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh viên  có ID = {} không tồn tại.".format(ID))

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x.id, reverse = False)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x.name, reverse = False)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x.diemTB, reverse = False)

    def findByID(self, id):
        searchResult = None
        if(self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if(sv.id == id):
                    searchResult = sv
        return searchResult

    def findByName(self, keyword):
        listSV = []
        if(self.soLuongSinhVien() > 0 ):
            for sv in self.listSinhVien:
                if(keyword.upper() in sv.name.upper()):
                    listSV.append(sv)
        return listSV

    def deleteById(self, ID):
        isDelated = False
        sv = self.findByID(ID)
        if(sv != None):
            self.listSinhVien.remove(sv)
            isDelated = True
        return isDelated

    def xepLoaiHocLuc(self, sv:SinhVien):
        if(sv.diemTB >= 8):
            sv.hocluc = "Giỏi"
        elif(sv.diemTB >= 6.5):
            sv.hocluc = "Khá"
        elif(sv.diemTB >= 5):
            sv.hocluc = "Trung Bình"
        else:
            sv.hocluc = "Yếu"

    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8}  {:<8}{:<8} {:<8}".format("ID","Name","Sex","Major","Điểm TB", "Học Lực"))
        if(listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8}  {:<8}{:<8} {:<8}".format(sv.id, sv.name, sv.sex, sv.major, sv.diemTB, sv.hocluc))
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien
                    