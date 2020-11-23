# 関数
"""
「return 返り値」とすることで、関数から値を返せます。
返り値には、計算式なども書けます。returnだけだったり、returnせずに終了すると、return Noneと同じようにNoneを返したことになります。
Noneは、特殊な値で何もないことを表します。
"""
# フィボナッチ数列の関数をつくる
def fib(n):
    """n=1000未満のフィボナッチ数列を出力"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

fib(1000)
print()

# 補足：endオプション
"""
print()関数に end を指定しないと、print()は出力最後に「改行文字（'\n'）」を自動で添付します。
endで改行文字以外の文字を指定できます。
"""
print('Hello', end='')
print('World') # HelloWorld
print('Hello', end='@@')
print('World') # Hello@@World
print()

# スコープ
"""
関数外で作成した変数を、グローバル変数といいます。
関数内で作成した変数を、ローカル変数といいます。ローカル変数は、関数ごとにスコープを持ちます。
関数内で、グローバル変数と同名の変数を作成からはじめないで、参照と代入を行うとエラーになります。

ローカル変数として使いたい時：最初に、何らかの初期値で作成してください。
グローバル変数として使いたい時：関数内でグローバル変数を代入することは、不具合の原因になりやすいので、安易にしない方がよいです。
"""

i = 123  # グローバル変数

def func1():
    print(i)
def func2():
    i = 456 #ローカル変数
    print(i)
def func3():
    print(i)

func1()  # 123と出力
func2()  # 456と出力
func3()  # 123と出力
print(i)  # 123と出力

# 引数について
"""
関数の定義時に、n=1000のようにデフォルト値を指定できます。
"""
def func(arg1, arg2=2, arg3=3):
    #これが引数の初期値設定。ユーザーが関数内で引数を設定しなければ、デフォルトでこの数値が適用される
    print(arg1, arg2, arg3)

func(10, 20, 30)  # 10 20 30
func(10, 20)  # 10 20 3
func(arg1=10)  # 10 2 3 （arg=数値、としても同じである模様）
func(10, arg3=30)  # 10 2 30


# 関数の演習
"""
「実引数なし」に対応するためには、デフォルト値を「None」と指定します。
"""
def func(n=None):
    if n is None:
        print("引数を指定してください")
    elif n < 0:
        print("負の値です")
    elif n == 0:
        print("0です")
    else:
        print("正の値です")

func()  # 引数を指定してください
func(0)  # 0です
func(-1)  # 負の値です
func(99)  # 正の値です


# 任意個数の位置引数の定義
# 実引数を何個も指定できる関数は、次のようにしてつくる。
def func(*args):
    print(args) #関数内の同一変数に*をつける必要はない
    for arg in args:
        print(arg, end=' ') #こうすれば改行されずに繋げられる
    print()

func('hello', 'world')
# 1行目に指定した分の引数が、2行目にループ処理で出力した値が表示される


# アンパック
"""
実引数にアスタリスク(*)をつけると、中身を展開してくれます。これをアンパックといいます。
"""
# アンパック前
"""
def func(*args):
    for arg in args:
        print(arg, end=' ')
    print()
"""
# アンパック後（上記と同一の内容）
def func(*args):
    print(*args)
# 引数と引数の間には半角スペースが埋め込まれる模様。

# 任意戸数のキーワード引数
def func(*args, **kwargs):
    print(args, kwargs)

func(1, 2, 3, abc=1, xyz='xyz')
# (1, 2, 3) {'abc': 1, 'xyz': 'xyz'}
"""
**kwargs（他の文字でもOK）という仮引数を作成すると、任意のキーワード引数を任意の個数指定できます。
上記のように、**kwargsを使う場合、仮引数の順番は最後にしなければいけません。
"""


# 辞書からキーワード変数へ

def func(*args, **kwargs):
    print(*args, **kwargs)

func(1, 2, 3, sep='-') # 1-2-3


# print関数のラッパーを作成する
"""
print関数と同じように使えるprint_with_promptを作成するには、どうするか。
（今回は、出力時に先頭に「> 」を出力させる）
"""
def print_with_prompt(*args, **kwargs):
  print('> ', end='') #これで次のprint()と繋げられる
  print(*args, **kwargs)

print_with_prompt("hello", "world", sep=",")
# こうすれば、引数間を,で区切って表示できる。
