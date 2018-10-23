import pandas as pd
from svm_model import SVMModel
from naive_bayes_model import NaiveBayesModel


class TextClassificationPredict(object):
    def __init__(self):
        self.predicted = None
        self.proba = None
        self.df_train = None
        self.clf = None

    def get_train_data(self):
        train_data = []
        train_data.append({"feature": u"nhìn bảng", "target": "bang"})
        train_data.append({"feature": u"đọc bảng", "target": "bang"})
        train_data.append({"feature": u"chọn bảng", "target": "bang"})
        train_data.append({"feature": u"bảng", "target": "bang"})

        train_data.append({"feature": u"toàn bộ cơ sở dữ liệu", "target": "csdl"})
        train_data.append({"feature": u"cơ sở dữ liệu", "target": "csdl"})
        train_data.append({"feature": u"toàn bộ", "target": "csdl"})
        train_data.append({"feature": u"hết", "target": "csdl"})
        train_data.append({"feature": u"muốn nhìn hết", "target": "csdl"})
        train_data.append({"feature": u"muốn nhìn toàn bộ", "target": "csdl"})

        train_data.append({"feature": u"thay đổi giá", "target": "gia"})
        train_data.append({"feature": u"đổi giá", "target": "gia"})
        train_data.append({"feature": u"chỉnh giá", "target": "gia"})
        train_data.append({"feature": u"điều chỉnh", "target": "gia"})
        train_data.append({"feature": u"giá", "target": "gia"})
        train_data.append({"feature": u"chỉnh", "target": "gia"})
        
        train_data.append({"feature": u"Tắt đi", "target": "thoat"})
        train_data.append({"feature": u"muốn tắt", "target": "thoat"})
        train_data.append({"feature": u"Nghỉ thôi", "target": "thoat"})
        train_data.append({"feature": u"Không muốn nữa", "target": "thoat"})
        # train_data.append({"feature": u"thoát nha", "target": "thoat"})
        train_data.append({"feature": u"thoát", "target": "thoat"})
        train_data.append({"feature": u"muốn thoát", "target": "thoat"})
        train_data.append({"feature": u"kết thúc", "target": "thoat"})
        train_data.append({"feature": u"bye bye", "target": "thoat"})
        train_data.append({"feature": u"tạm biệt", "target": "thoat"})
        self.df_train = pd.DataFrame(train_data)

    def test(self,name):
        #  test data
        test_data = []
        test_data.append({"feature": name, "target": ""})
        df_test = pd.DataFrame(test_data)
        model = SVMModel()
        # model = NaiveBayesModel()
        self.clf = model.clf.fit(self.df_train["feature"], self.df_train.target)
        self.predicted = self.clf.predict(df_test["feature"])
        self.proba = self.clf.predict_proba(df_test["feature"])


if __name__ == '__main__':
    tcp = TextClassificationPredict()
    tcp.get_train_data()
    while True:
        a = input("Nhập:")
        tcp.test(a)
        print(tcp.predicted[0])
        print (tcp.proba)
