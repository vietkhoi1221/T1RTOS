import pymysql.cursors
import speech
from datetime import datetime
class bill:
    """ đây là class xuất phí"""
    def __init__(self, con, fee=0):
        self.con = con
        self.fee = fee

    def tinhphi(self):
        with self.con.cursor() as cursor:
            self.sql = "select * from Bill"
            cursor.execute(self.sql)
            self.a = cursor.rowcount
            self.sql = "select * from Bill where idbill = %s" %self.a
            cursor.execute(self.sql)
            for row in cursor:
                self.fee = float(row['total']) * 1000
            self.con.close()
        return self.fee
    def xam(self):
        with self.con.cursor() as cursor:
            self.sql = "select * from Bill"
            cursor.execute(self.sql)
            self.a = cursor.rowcount
            self.sql = "select * from Bill where idbill = %s" %self.a
            cursor.execute(self.sql)
            for row in cursor:
                self.idphong = row['idPhong']
                self.idti = row['idtienIch']
                self.idkm = row['idkhuyenMai']
                self.idkhach = row['idKhach']
            cursor.execute("select * from datphong where idkhach = %s" % self.idkhach)
            for row in cursor:
                self.date_format = "%Y-%m-%d"
                self.a = datetime.strptime(row['tDen'], self.date_format)
                self.b = datetime.strptime(row['tDi'], self.date_format)
                self.songay = str(self.b-self.a)
                self.songay = int(self.songay[:self.songay.find(" ")])
            cursor.execute("select * from phong where idphong = %s" %self.idphong)
            for row in cursor:
                self.idlp = row['idloaiPhong']
            cursor.execute("select * from loaiphong where idloaiPhong = %s" %self.idlp)
            for row in cursor:
                self.gp = int(row['gia'])*1000
                self.lp = row['moTa']
            cursor.execute("select * from tienich where idtienIch = %s" %self.idti)
            for row in cursor:
                self.gt = row['gia']
                self.ti = row['name']
            if self.idkm is not None:
                cursor.execute("select * from khuyenmai where idkhuyenMai = %s" %self.idkm)
                for row in cursor:
                    self.idgg = row['idgiamGia']
                cursor.execute("select * from giamgia where idgiamgia = %s" %self.idgg)
                for row in cursor:
                    self.gg = row['ten']
                    self.tg = row['tienGiam']
            self.tt = self.songay*(self.gp+self.gt*1000)
        print("Bạn đã đặt phòng " + str(self.idphong) +" thuộc loại " +self.lp + " giá " + str(self.gp) + " đồng một ngày đêm trong vòng " \
            +str(self.songay) + " ngày và sử dụng dịch vụ "+self.ti+" với giá " + str(self.gt*1000) + " đồng. Tổng cộng là " + str(self.tt))
        if self.idkm is not None:
            print("Tuy nhiên bạn đã nhận được khuyến mãi " + self.gg +" với mức giảm " + str(self.tg) + "%.")
    def inform(self):
        speech.say("Quý khách phải trả %.0f đồng" % self.tinhphi())
