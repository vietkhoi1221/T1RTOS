import pymysql.cursors
import speech
import text_classification_predict
#cấu hình để truy cập database
# con = pymysql.connect(host ='localhost', user = 'root', port = 3306,
#                      password = 't0cnhutuyet', db = 'hotel', cursorclass = pymysql.cursors.DictCursor)

class changedb:
    def __init__(self, con):
        self.con = con
        
    def showdb(self):
        with self.con.cursor() as cursor:
            # SQL 
            self.sql = "show tables"
            # Thực thi câu lệnh truy vấn (Execute Query).
            cursor.execute(self.sql)
            i=1
            for row in cursor:
                print(str(i) +". "+row['Tables_in_hotel'])
                i+=1

    def showtable(self):
        while(True):
            try:
                # self.cmd = speech.phrase().lower()
                # if self.cmd.find("thoát")!=-1:
                    # break
                # self.cmd = int(self.cmd[self.cmd.index("số")+3:])
                self.cmd = input("Bảng muốn in bảng số mấy:")
                if self.cmd.find("thoát")!=-1:
                    break
                self.cmd = int(self.cmd[self.cmd.index("số")+3:])
                print(self.cmd)
                with self.con.cursor() as cursor:
                    # SQL 
                    self.sql = "show tables"
                    # Thực thi câu lệnh truy vấn (Execute Query).
                    cursor.execute(self.sql)
                    i=[]
                    for row in cursor:
                        i.append(row['Tables_in_hotel'])
                    self.sql = "select * from %s" %i[self.cmd-1]
                    # Thực thi câu lệnh truy vấn (Execute Query).
                    cursor.execute(self.sql)
                    for row in cursor:
                        print(str(row))
            except:
                print("Lỗi")
                speech.say("Lỗi mất rồi, xem thử có đọc đúng không.")
            
    def changeprice(self):
        while(True):
            try:
                self.i = 0
                self.index = 0
                self.price = 0
                self.cmd = speech.phrase().lower()
                print(self.cmd)
                # self.cmd = input("Nhập:")
                if self.cmd.find("thoát")!=-1:
                    break
                elif self.cmd.find("phòng")!=-1 or self.cmd.find("dịch vụ")!=-1 or self.cmd.find("tiện ích")!=-1:
                    if self.cmd.find("phòng")!=-1:
                        self.i=0
                    if self.cmd.find("dịch vụ")!=-1 or self.cmd.find("tiện ích")!=-1:
                        self.i=1
                    with self.con.cursor() as cursor:
                        if self.i == 0:
                            self.sql ="select * from loaiphong"
                            cursor.execute(self.sql)
                            speech.say("Mời xem danh sách sau.")
                            print("Mời xem danh sách sau.")
                            for row in cursor:
                                print("Phòng loại "+ str(row['idloaiPhong']) +" là " + row['moTa'] + " có giá " + str(row['gia']))
                            speech.say("Vui lòng nhập loại phòng cần sửa và giá mới.")
                            print("Vui lòng nhập loại phòng cần sửa và giá mới.")
                            self.index = input("Nhập loại phòng:")
                            self.price = input("Nhập giá mới:")
                            self.sql = "Update loaiphong set gia = '%s' where idloaiphong = %s " %(self.price, self.index)
                            cursor.execute(self.sql)
                        elif self.i == 1:
                            self.sql ="select * from tienich"
                            cursor.execute(self.sql)
                            speech.say("Mời xem danh sách sau.")
                            print("Mời xem danh sách sau.")
                            for row in cursor:
                                print(row)
                            speech.say("Vui lòng nhập loại tiện ích cần sửa và giá mới.")
                            print("Vui lòng nhập loại tiện ích cần sửa và giá mới.")
                            self.index = input("Nhập loại tiện ích:")
                            self.price = input("Nhập giá mới:")
                            self.sql = "Update tienich set gia = '%s' where idtienich = %s " %(self.price, self.index)
                            cursor.execute(self.sql)
                        # SQL
                        self.con.commit() 
                else:
                    speech.say("Vui lòng nói to và rõ hơn.")
                    print("Vui lòng nói to và rõ hơn.")
            except:
                print("Lỗi")
         
    def exe(self):
        speech.say("Hiện nay đã có 3 tính năng đọc cơ sở dữ liệu, đọc bảng và thay đổi giá. Anh muốn sử dụng chức năng nào.")
        print("Hiện nay đã có 3 tính năng đọc cơ sở dữ liệu, đọc bảng và thay đổi giá. Anh muốn sử dụng chức năng nào.")
        tcp = text_classification_predict.TextClassificationPredict()
        tcp.get_train_data()

        while(True):
            # self.cmd = speech.phrase().lower()
            self.cmd = input("Nhập vào tính năng bạn chọn:")
            print(self.cmd)
            if(len(self.cmd)!=0):
                tcp.test(self.cmd)
                if tcp.predicted[0] == 'csdl' and tcp.proba[0][1] > 0.65:
                    print("Đang in CSDL.")
                    self.showdb()
                elif tcp.predicted[0] == 'bang' and tcp.proba[0][0] > 0.65:
                    print("Chuẩn bị in bảng.")
                    self.showtable()
                elif tcp.predicted[0] == 'gia' and tcp.proba[0][2] > 0.65 :
                    print("Đang tiến hành thay đổi giá.")
                    self.changeprice()
                elif tcp.predicted[0] == 'thoat' and tcp.proba[0][3] > 0.65:
                    print("Thoát đây, BYE BYE.")
                    break
                else:
                    speech.say("Không biết tiếng Việt à.")
