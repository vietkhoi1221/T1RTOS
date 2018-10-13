import pymysql.cursors
import speech

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
    
    def inform(self):
        speech.say("Quý khách phải trả %.0f đồng" % self.tinhphi())
