import pymysql.cursors
import speech
import myweather

                     
class phong:
    """Đây là class nhập phòng"""
    idphong = ""
    idlphong = ""
    idconv = ""

    def __init__(self, con):
        self.con = con

    def loaiphong(self):
        with self.con.cursor() as cursor:
            # SQL 
            self.sql = "SELECT * FROM loaiPhong " 
            # Thực thi câu lệnh truy vấn (Execute Query).
            cursor.execute(self.sql)
            self.a=cursor.rowcount
            speech.say("Bên khách sạn của chúng tôi có %d loại phòng sau đây" %self.a)
            for row in cursor:
                self.idlp = row['idloaiPhong']
                self.tenloai = row['moTa']
                speech.say("Loại thứ {} là {}".format(self.idlp,self.tenloai))
        speech.say("Không biết quý khách muốn chọn phòng loại nào")
        while True:
            self.aa=0
            # self.cmd = speech.phrase().lower()
            self.cmd = input("Nhập:")
            print(self.cmd)
            if self.cmd.find("loại")!=-1:
                self.tpe= self.cmd[self.cmd.index("loại")+5:]
                with self.con.cursor() as cursor:
                    # SQL 
                    self.sql = "SELECT * FROM phong where idloaiPhong = %s" % self.tpe
                    # Thực thi câu lệnh truy vấn (Execute Query).
                    cursor.execute(self.sql)
                    if cursor.rowcount==0:
                        speech.say("Không có loại phòng này")
                        speech.say("Quý khách xin vui lòng chọn lại.")
                    else:
                        self.a=0
                        for row in cursor:
                            self.tt = row['trangThai']
                            if self.tt=="trống":
                                speech.say("Loại %s có Phòng %s còn trống"%(self.tpe,row['idPhong']))
                                speech.say("Quý khách có muốn chọn loại phòng này không")
                                self.a=1
                                while True:
                                    # self.cmd = speech.phrase().lower()
                                    self.cmd = input("Nhập:")
                                    print(self.cmd)
                                    if self.cmd.find("có")!=-1:
                                        speech.say("Cảm ơn quý khách")
                                        phong.idphong = row['idPhong']
                                        phong.idlphong = self.tpe
                                        self.aa=1
                                        self.sql = "Update phong set trangThai = 'đã đặt' where idPhong = %s " % phong.idphong
                                        cursor.execute(self.sql)
                                        self.con.commit()
                                        break
                                    if self.cmd.find("không")!=-1:
                                        speech.say("vẫn còn sự lựa chọn khác")
                                        break
                    if self.a==0:
                        speech.say("Rất tiếc phòng loại này đã hết.")
                    elif self.aa==0:
                        speech.say("Quý khách có thể chọn phòng khác tùy theo sở thích.")
                    else:
                        break
            else:
                speech.say("Quý khách xin vui lòng nhắc lại.")

    def convenient(self):   
        speech.say("Thêm một thông tin khác " + myweather.completeWeather("Thành phố Hồ Chí Minh"))   
        speech.say("Thời tiết như vậy sẽ rất phù hợp với các dịch vụ sau")   
        with self.con.cursor() as cursor:
            # SQL 
            self.sql = "SELECT * FROM tienich"
            # Thực thi câu lệnh truy vấn (Execute Query).
            cursor.execute(self.sql)
            speech.say("Có tổng cộng %d dịch vụ" % cursor.rowcount)
            for row in cursor:
                self.IDti = row['idtienIch']
                self.tenti = row['name']
                speech.say("Dịch vụ số %d là %s " % (self.IDti, self.tenti))
        speech.say("Với nhiều dịch vụ hấp dẫn như vậy, không biết quý khách muốn chọn dịch vụ nào")

        #chọn tiện ích
        while True:
            # self.cmd = speech.phrase().lower()
            self.cmd = input("Nhập:")
            print(self.cmd)
            if self.cmd.find("số")!=-1:
                self.tpeti = self.cmd[self.cmd.index("số")+3:]
                with self.con.cursor() as cursor:
                    # SQL 
                    self.sql = "SELECT * FROM tienIch where idtienIch = %s" % self.tpeti
                    # Thực thi câu lệnh truy vấn (Execute Query).
                    cursor.execute(self.sql)
                    if cursor.rowcount==0:
                        speech.say("Không có dịch vụ này")
                        speech.say("Quý khách xin vui lòng chọn lại.")
                    else:
                        phong.idconv = self.tpeti
                        speech.say("Quý khách đã chọn dịch vụ này. Xin cảm ơn") 
                        break
            else:
                speech.say("Quý khách xin vui lòng nhắc lại.")  