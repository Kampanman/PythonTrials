# クラスにアクセス制限をつける場合
class User:
  def __init__(self, name):
    self.__name = name
  # name属性にはクラスの外からアクセスしてほしくないケースを想定
  # nameの前に__をつければよい
  def say_hi(self):
    print("どうもこんにちは。{0}です。".format(self.__name))

chris = User("クリス・ヘプラー")
# print(chris.__name)
print("名前："+chris._User__name)
chris.say_hi()