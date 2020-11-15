class User:
  def __init__(self, name):
    self.name = name
  def say_hi(self):
    print("どうもこんにちは。{0}です。".format(self.name))

# クラス継承
# Use -> AdminUser
class AdminUser(User):
  def __init__(self, name, me):
    # 親クラスで使われていた関数の引数に新しい引数を加える
    super().__init__(name)
    """ 
    親クラスはsuper()というキーワードで表現できる。
    上記はUserの「self.name = name」の分。
    """
    self.me = me
  def say_yes(self):
    print("そうです。{1}が{0}です。".format(self.name,self.me))

henna = AdminUser("変なおじさん","ワダス")
henna.say_hi()
henna.say_yes()