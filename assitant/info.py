import speech
import intro



class info:
    """Class nhập thông tin"""
    lastname = ""
    firstname = ""
    qtich = ""
    sdt = ""
    def __init__(self):
        pass
    
    def introo(self):
        intro.playmusic("TVC Quảng cáo giới thiệu khách sạn Mường Thanh chuỗi khách sạn tư nhân lớn nhất Việt Nam")
        while True:
            # self.cmd = speech.phrase().lower()
            self.cmd = input("Nhập:")
            print(self.cmd)
            if self.cmd.find("dừng")!=-1 or self.cmd.find("đặt phòng")!=-1 or self.cmd.find("ngừng")!=-1:
                intro.stopmusic()
                break

    def tentuoi(self):
        # speech.say("Xin chào quý khách, vui lòng cho biết họ và tên.")
        while True:
            # self.cmd = speech.phrase().lower()
            self.cmd = input("Nhập:")
            print(self.cmd)
            if len(self.cmd)!= 0:
                info.lastname = self.cmd[self.cmd.rindex(" ")+1:]
                info.firstname = self.cmd[:self.cmd.rindex(" ")]
                break
            else:
                speech.say("Quý khách xin vui lòng nhắc lại.")
        # speech.say("Địa chỉ của anh {} là gì:".format(info.lastname))
        while True:
            # self.cmd = speech.phrase().lower()
            self.cmd = input("Nhập:")
            print(self.cmd)
            if len(self.cmd)!= 0:
                info.addr=self.cmd
                break
            else:
                speech.say("Quý khách xin vui lòng nhắc lại.")
    
    #quốc tịch, sđt
    def phone(self,lastname):
        # speech.say("anh {} vui lòng cho thêm một số thông tin, cụ thể là quốc tịch.".format(lastname))  
        while True:
            # self.cmd = speech.phrase().lower()
            self.cmd = input("Nhập:")
            print(self.cmd)
            if len(self.cmd) !=0 :
                info.qtich = self.cmd
                # speech.say("Có số điện thoại thì tốt quá")
                while True:
                    # self.cmd = speech.phrase().lower()  
                    self.cmd = input("Nhập:")
                    if len(self.cmd) !=0:
                        for i in range(0,len(self.cmd)):
                            if self.cmd[i].isdigit():
                                info.sdt +=self.cmd[i]
                        print(info.sdt)
                        break
                break
            else:
                speech.say("Quý khách xin vui lòng nhắc lại quốc tịch.")