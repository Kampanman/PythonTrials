# クラス

class Student:
    pass #これで空のクラスができる

ema = Student() #Pythonは「new ～～」とやらないようだ
ema.name = "エマ"
ema.score = str(100) 
"""
文字列と数値はそのままでは共存できない。
だから、数値を文字列に組み込むなら、まずはstr(数値)で文字列化を。
"""

dong = Student() #これらは「インスタンス」と呼ばれる
dong.name = "ドン"
dong.score = str(75)

fill = Student()
fill.name = "フィル"
fill.age = str(4)
# 属性は作るデータに応じて好きに変えることができる

print("『約束のネバーランド』。\n主人公の女の子が、"+ema.name+"。")
print("彼女は毎回、"+ema.score+"%の得点を叩き出している。")
print(fill.name+"の年齢は"+fill.age+"歳。"+ema.name+"とは7つ違う。")

# コンストラクタの作成
class User:
    # クラス変数
    count = 0
    def __init__(self, name):
        User.count += 1
        # インスタンス変数
        self.name = name

print(User.count) #0
chris = User("クリス・ヘプラー")
chris2 = User("クリス・タッカー")
print(User.count) #2

print("どうもこんにちは。"+chris.name+"です。")
print("どうもこんにちは。"+chris2.name+"です。")
print(chris2.count)