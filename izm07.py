# メソッドの種類
"""
・インスタンスメソッド
　いわゆる通常のメソッド。
・クラスメソッド
　クラスをインスタンス化しなくても呼び出すことができるメソッド。
・スタティックメソッド
　クラスをインスタンス化しなくても呼び出すことができるメソッド。またselfやclsなどのインスタンスやクラスを表す変数を必要としない。
"""

class TestClass:
 
    # インスタンスメソッド
    def sample_instancemethod(self, arg_1):
        pass
 
    # クラスメソッド
    @classmethod
    def sample_classmethod(cls, arg_1):
        pass
 
    # スタティックメソッド
    @staticmethod
    def sample_staticmethod(arg_1, arg_2):
        pass


# ファイルの読み書き

# ファイルの読み込み
"""
作業ディレクトリにread.txtというファイル名で、下記内容のテキストファイルを用意している。
open関数の第二引数には読み込み（read）を示すrを渡す。

文字コードを指定してファイルの読み書きを行うのがセオリー。
"""
# open関数でファイルを開く
  # その際、文字コードを「UTF-8」に指定しておくこと
f = open('read.txt', 'r', encoding='UTF-8')
# read関数で、ファイルを全て読み込み、その文字列データに対して処理を行う
data = f.read()
print(data)

print("==========")
# ファイルへの書き込み
  # 書き込みもopen関数を使う。第二引数へ書き込み（write）を示すwを渡すこと。（既に同名のファイルが存在すれば上書きされる）

import datetime
todaydetail = datetime.datetime.today()
year = str(todaydetail.year)
month = str(todaydetail.month)
day = str(todaydetail.day)
hour = str(todaydetail.hour)
minute = str(todaydetail.minute)

f = open('test.txt', 'w', encoding = "utf_8")

f.write(year+"/"+month+"/"+day+" "+hour+":"+minute+' 書き込み完了。')
f.close()

f2 = open('test.txt', 'r', encoding='UTF-8')
data = f2.read()
print(data)

print("==========")