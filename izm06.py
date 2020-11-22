# 関数への引数の応用
def test_func(num_1, num_2, oprn=1):
  #引数oprnの初期値には1を設定してある。
    if oprn == 1:
        print('足し算開始')
        print(num_1 + num_2)
    elif oprn == 2:
        print('引き算開始')
        print(num_1 - num_2)
    elif oprn == 3:
        print('掛け算開始')
        print(num_1 * num_2)
    elif oprn == 4:
        print('割り算開始')
        print(num_1 / num_2)
    else:
        print('不明なオペレーション指定です')
         
test_func(100, 10, 1)
test_func(100, 10, 2)
test_func(100, 10, 3)
test_func(100, 10, 4)
test_func(100, 10) # 足し算開始 110

print("==========")

"""
Pythonでは、モジュール内にdefで定義されているものが関数、クラス内にdefで定義されているものがメソッド。
"""
# 関数
def test_func():
  print('This is test_func.')
# メソッド
class TestClass:
  def test_method():
    print('This is test_method.')

test_func()
TestClass.test_method()
print("==========")

# クラスを定義しそれを作成する（インスタンス化）時のルール
class TestClass:
    def __init__(self, best, title, name):
        self.best = best
        self.title = title
        self.name = name
        #selfは、JSのオブジェクト指向のthisにあたるもの

classes = []
classes.append(TestClass(1,'鬼滅の刃','竈門ねず子'))
classes.append(TestClass(2,'魔法陣グルグル','ククリ'))
classes.append(TestClass(3,'約束のネバーランド','エマ'))
classes.append(TestClass(4,'ゴールデンカムイ','アシリパ'))
classes.append(TestClass(5,'エウレカセブン','エウレカ'))
# JSなどのオブジェクト指向でいうところの new Method()
print("思わず惚れた！ 好きな漫画・アニメのヒロイン ベスト５")
# 上記の配列に足していった要素は、次のようにして出力する
for testCls in classes:
  print('第'+str(testCls.best)+'位：『'+testCls.title+'』の '+testCls.name)
print("==========")

# クラス継承
"""
先程作成した「TestClass」を親クラスとして新クラスを作成する。
親クラスの内容をある文法で引き継ぐほかに、子クラスでは新しいクラスを定義する。
"""
class FavChara:
    def __init__(self, title, name):
        self.title = title
        self.name = name

class NeoFavChara(FavChara):
    def __init__(self, title, name, prime):
      super().__init__(title, name)
      self.prime = prime

classes = []
classes.append(NeoFavChara('ドラゴンボール','孫悟飯','孫悟空'))
classes.append(NeoFavChara('ワンピース','ウソップ','ルフィ'))
classes.append(NeoFavChara('ワンパンマン','サイタマ','サイタマ'))
classes.append(NeoFavChara('約束のネバーランド','エマ','エマ'))
classes.append(NeoFavChara('鬼滅の刃','竈門ねず子','竈門炭治郎'))

for eachCls in classes:
  print("『"+eachCls.title+"』で一番好きなキャラ： "+eachCls.name+"（主人公は"+eachCls.prime+"）")