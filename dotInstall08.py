# クラスの多重継承
# A,B -> C

class A:
  def say_yes(self):
    print("はい")
  def strong(self):
    print("！")
class B:
  def say_no(self):
    print("いいえ")
  def strong(self):
    print("（断言）")

class C(A,B):
  pass

c = C()
c.say_yes()
c.say_no()
c.strong() # 「class C(B,A):」にすると（断言）と返ってくる