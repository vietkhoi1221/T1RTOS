import pymysql.cursors

class insertdb:
    """Class này chèn dữ liệu vào CSDL"""
    def __init__(self, con, ho, ten, qtich, addr, phone, dat, den, di, idphong, idti, idkhuyenmai, total):
        self.con = con
        self.ho = ho
        self.ten = ten
        self.qtich = qtich
        self.addr = addr
        self.phone = phone 
        self.dat = dat
        self.den = den
        self.di = di
        self.idphong = idphong
        self.idti = idti
        self.idkhuyenmai = idkhuyenmai
        self.total = total
    
    def chenkhach(self):
        with self.con.cursor() as cursor:
            # SQL 
            self.sql = "insert into khach(idKhach, hoTenDem, ten, quocTich, diaChi, SDT) values (DEFAULT,'%s','%s','%s','%s','%s') "\
            %(self.ho, self.ten, self.qtich, self.addr, self.phone)
            # Thực thi câu lệnh truy vấn (Execute Query).
            cursor.execute(self.sql)
            self.con.commit()
    
    def chendatphong(self):
        with self.con.cursor() as cursor:
            # SQL 
            cursor.execute("SELECT * FROM khach where SDT = %s" % self.phone)
            for row in cursor:
                self.idkhach = row['idKhach']
            self.sql = "insert into datPhong(idDatPhong, tDat, tDen, tDi, Comment, idKhach, idPhong, idTienIch) values (DEFAULT,'%s','%s','%s','','%s','%s','%s') "\
            %(self.dat, self.den, self.di, self.idkhach, self.idphong, self.idti)
            # Thực thi câu lệnh truy vấn (Execute Query).
            cursor.execute(self.sql) 
            self.con.commit()

    def chenbill(self):
        with self.con.cursor() as cursor:
            # SQL 
            cursor.execute("SELECT * FROM khach where SDT = %s" % self.phone)
            for row in cursor:
                self.idkhach = row['idKhach']
            if self.idkhuyenmai is not None:
                self.sql = "insert into Bill(idBill, idKhach, idPhong, idtienIch, idkhuyenMai, mota, total) values (DEFAULT,'%s','%s','%s','%s','',%s)" % (self.idkhach, self.idphong, self.idti, self.idkhuyenmai, self.total)
                cursor.execute(self.sql)
            else:
                self.sql = "insert into Bill(idBill, idKhach, idPhong, idtienIch, idkhuyenMai, mota, total) values (DEFAULT,'%s','%s','%s',NULL,'',%s) " %(self.idkhach, self.idphong, self.idti, self.total)
                cursor.execute(self.sql)
            # Thực thi câu lệnh truy vấn (Execute Query).
            self.con.commit() 
