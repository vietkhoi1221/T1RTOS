import pymysql.cursors
import speech
import time


class ngay:
    """Đây là class nhập ngày"""
    ddat = ""
    dtra = ""
    dnhan = ""
    idkhuyenMai = ""
    
    def __init__(self, con, lastname):
        self.con = con
        self.lastname = lastname

    def datphong(self):
        # speech.say("Không biết anh {} muốn đặt phòng vào ngày nào.".format(self.lastname))
        while True:
            # self.cmd = speech.phrase().lower()
            self.cmd = input("Nhập:")
            print(self.cmd)
            try:
                if self.cmd.find("ngày") !=-1 and self.cmd.find("tháng") !=-1 and self.cmd.find("năm") !=-1 :
                    self.date = self.cmd[self.cmd.index("ngày")+5:self.cmd.index("tháng")-1]
                    print(self.date)
                    self.month = self.cmd[self.cmd.index("tháng")+6:self.cmd.rindex("năm")-1]
                    print(self.month)
                    self.year = self.cmd[self.cmd.rindex("năm")+4:]
                    print(self.year)
                    ngay.ddat= self.year+"-"+self.month+"-"+self.date
                    """
                    Làm cmj đó"""
                    break
                else:
                    speech.say("Quý khách xin vui lòng nhắc lại.")
            except:
                speech.say("Quý khách xin vui lòng nhắc lại.")

    def nhanphong(self):
        # speech.say("Không biết anh {} muốn nhận phòng vào ngày nào.".format(self.lastname))
        while True:
            # cmd = speech.phrase().lower()
            self.cmd = input("Nhập:")
            print(self.cmd)
            try:
                if self.cmd.find("ngày") !=-1 and self.cmd.find("tháng") !=-1 and self.cmd.find("năm") !=-1 :
                    self.date = self.cmd[self.cmd.index("ngày")+5:self.cmd.index("tháng")-1]
                    print(self.date)
                    self.month = self.cmd[self.cmd.index("tháng")+6:self.cmd.rindex("năm")-1]
                    print(self.month)
                    self.year = self.cmd[self.cmd.rindex("năm")+4:]
                    print(self.year)
                    ngay.dnhan= self.year+"-"+self.month+"-"+self.date
                    break
                else:
                    speech.say("Quý khách xin vui lòng nhắc lại.")
            except:
                speech.say("Quý khách xin vui lòng nhắc lại.")

        #so sánh
        with self.con.cursor() as cursor:    
            # SQL 
            self.sql = "SELECT * FROM khuyenMai " 
            # Thực thi câu lệnh truy vấn (Execute Query).
            cursor.execute(self.sql)
            for row in cursor:  
                if time.strptime(ngay.dnhan,"%Y-%m-%d") > time.strptime(str(row['ngayBatDau']),"%Y-%m-%d") \
                    and time.strptime(ngay.dnhan,"%Y-%m-%d") < time.strptime(str(row['ngayKetThuc']),"%Y-%m-%d"):         
                    ngay.idkhuyenMai = row['idkhuyenMai']
                    self.idgiamGia= row['idgiamGia']
                    self.kmstart = row['ngayBatDau']
                    self.kmstop = row['ngayKetThuc']
                    self.sql = "SELECT * FROM giamgia where idgiamGia = %d " %(self.idgiamGia)
                    # Thực thi câu lệnh truy vấn (Execute Query).
                    cursor.execute(self.sql)
                    for self.row in cursor:
                        self.getMa = self.row['ten']
                        self.discount = self.row['tienGiam']
                    speech.say("Anh đã nhận được mã {} có hạn từ {} đến {} , giảm {} phần trăm".format(self.getMa, self.kmstart, self.kmstop, self.discount))
                else:
                    ngay.idkhuyenMai = None
    #trả phòng
    def traphong(self):
        # speech.say("Không biết anh {} muốn trả phòng vào ngày nào.".format(self.lastname))
        while True:
            try:
                # self.cmd = speech.phrase().lower()
                self.cmd = input("Nhập:")
                print(self.cmd)
                if self.cmd.find("ngày") !=-1 and self.cmd.find("tháng") !=-1 and self.cmd.find("năm") !=-1 :
                    self.date = self.cmd[self.cmd.index("ngày")+5:self.cmd.index("tháng")-1]
                    print(self.date)
                    self.month = self.cmd[self.cmd.index("tháng")+6:self.cmd.rindex("năm")-1]
                    print(self.month)
                    self.year = self.cmd[self.cmd.rindex("năm")+4:]
                    print(self.year)
                    ngay.dtra= self.year+"-"+self.month+"-"+self.date
                    break
                else:
                    speech.say("Quý khách xin vui lòng nhắc lại.")
            except:
                speech.say("Quý khách xin vui lòng nhắc lại.")
