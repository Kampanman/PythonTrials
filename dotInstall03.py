# 関数

def Queen():
  print("We will rock you !\n")
Queen()

def favorVoc(artist, group = "ソロアーティスト"):
  #引数を渡すが、事前にデフォルトを設定出来たりもする。
  print("{0} ({1})".format(artist, group))

favorVoc("ジョン・レノン","ビートルズ")
favorVoc("ロバート・プラント","レッド・ツェッペリン")
favorVoc("フレディ・マーキュリー","クイーン")
favorVoc("クレッグ・レイク","キング・クリムゾン")
favorVoc("ジョー・ストラマー","クラッシュ")
favorVoc("ボノ","U2")
favorVoc("クリス・マーティン","コールドプレイ")
# ここからは、アーティスト名（ソロ）で返ってくる
favorVoc("エリック・クラプトン")
favorVoc("デヴィット・ボウイ")
favorVoc("スティング")
favorVoc("ジョージ・マイケル")
print("\n")
# 関数の返り値を使う
def highShout():
  return "Poooooh!"
msg = highShout()
print(msg)
# 関数内でpassを使うと・・・
def scat():
  pass
  # print("Ski Ba Bop Ba Dop Bop")
msg2 = scat()
print(msg2) #Noneが返ってくるはずだ

"""
関数を使う場合、スコープに注意しよう。
関数内で定義した変数は、その関数の中でしか使えない。
（「ローカル変数」と呼ばれる）
関数の内外関わらず使いたい変数は、
def ○○()とやって関数を定義する前に定義しておくように。
（「グローバル変数」と呼ばれる）

但し、次のようにすると関数でもグローバル変数を使える。
"""

msg = "hello" # グローバル変数

def say_hi():
    global msg
    msg = "hello global"
    print(msg)

say_hi()
print(msg)