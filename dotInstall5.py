#クラスのメソッド（関数）

class User:
    count = 0
    def __init__(self, name):
        User.count += 1
        self.name = name
    # インスタンスメソッド
    def say_hi(self):
        print("hi! {0}"+format(self.name)+".")
    # クラスメソッド
    @classmethod #クラスメソッド使う場合はこれが必要
    def show_info(cls):
        print("{0} instances"+format(cls.count))

tom = User("tom")
bob = User("bob")

User.show_info()