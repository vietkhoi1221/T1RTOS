from datetime import datetime
import pymysql.cursors

class cal:
    """Đây là class tính phí"""
    total = ""
    def __init__(self,con,dnhan,dtra,idkm,idlphong,idti):
        self.con = con
        self.dnhan = dnhan
        self.dtra = dtra
        self.idkm = idkm
        self.idlphong = idlphong
        self.idti = idti
    
    def charge(self):
        self.date_format = "%Y-%m-%d"
        self.a = datetime.strptime(self.dnhan, self.date_format)
        self.b = datetime.strptime(self.dtra, self.date_format)
        self.songay = str(self.b - self.a)
        self.songay = int(self.songay[:self.songay.find(" ")])
        with self.con.cursor() as cursor:
            # SQL 
            self.sql = "select * from loaiPhong where idloaiPhong = %s" % (self.idlphong)
            # Thực thi câu lệnh truy vấn (Execute Query).
            cursor.execute(self.sql)
            for row in cursor:
                self.gia = row['gia']
            self.sql = "select * from tienIch where idtienIch = %s " % (self.idti)
            cursor.execute(self.sql)
            for row in cursor:
                self.giati = row['gia']
            if self.idkm is not None:
                self.sql = "select * from khuyenMai where idkhuyenMai = %s " % (self.idkm)
                cursor.execute(self.sql)
                for row in cursor:
                    self.idggia = row['idgiamGia']
                self.sql = "select * from giamgia where idgiamgia = %s " % (self.idggia)
                cursor.execute(self.sql)
                for row in cursor:
                    self.ggia = row['tienGiam']
                cal.total =  self.songay*self.gia-(self.songay*self.gia+self.giati*self.songay)*self.ggia/100 + self.giati*self.songay
            else:
                cal.total =  self.songay*self.gia+self.giati*self.songay