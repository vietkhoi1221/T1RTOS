import pymysql.cursors
import speech
import info
import ngay
import insertdb
import phong
import calucate
import bill
import detect
import change
#cấu hình để truy cập database
con = pymysql.connect(host ='localhost', user = 'root', port = 3306,
                     password = 't0cnhutuyet', db = 'hotel', cursorclass = pymysql.cursors.DictCursor)

class khachsan:
    #hàm khởi tạo
    def __init__(self, con):
        self.con = con
    #hàm xử lí
    def xuli(self):
        a = info.info()
        a.tentuoi()
        a.phone(a.lastname)
        b = ngay.ngay(self.con, a.lastname)
        b.datphong()
        b.nhanphong()
        b.traphong()
        c = phong.phong(self.con)
        c.loaiphong()
        c.convenient()
        d = calucate.cal(self.con, b.dnhan, b.dtra, b.idkhuyenMai, c.idlphong, c.idconv)
        d.charge()
        e = insertdb.insertdb(self.con, a.firstname, a.lastname, a.qtich, a.addr, a.sdt, b.ddat, b.dnhan, b.dtra, c.idphong, c.idconv, b.idkhuyenMai, d.total)
        e.chenkhach()
        e.chendatphong()
        e.chenbill()
        f = bill.bill(self.con)
        f.inform()

    def adact(self):
        g = change.changedb(self.con)
        g.exe()

if __name__ == '__main__':
    test = khachsan(con)
    speech.say("Xác nhận quyền quản trị.")
    while(True):
        cmd = speech.phrase().lower()
        print(cmd)
        if (cmd.find("có")!=-1):
            speech.say("Chuẩn bị quét khuôn mặt.")
            if(detect.recog() == True):
                test.adact()
        elif (cmd.find("không")!=-1):
            test.xuli()
        elif (cmd.find("thoát")!=-1):
            break
        else:
            speech.say("Vui lòng nhắc lại.")