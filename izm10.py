# with文

"""
with文は、ファイルの自動クローズシステム。
with文を使えば、何らかの処理をしていたファイルを閉じ忘れることを防止できる。
"""

with open('test.txt') as ts:
  """
  何らかの処理
  """
  print(ts.closed) #False
print(ts.closed) #True

# これをさらに発展させた形↓
ts = open('test.txt')

try:
  """
  何らかの処理
  """
  pass
except:
  pass

finally:
  ts.close()


# コンテキストマネージャ

"""
Pythonではwith文で前処理、後処理を行えるようにする場合、そのオブジェクトはコンテキストマネージャである必要がある。

コンテキストマネージャについては、こちら↓に書いてあった。
https://blog.mtb-production.info/entry/2018/04/10/183000
"""

# 特殊メソッド（__enter__,__exit__など）の実装
class ContextManagerTest:
    def __enter__(self):
        print('__enter__')
    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__')
 
with ContextManagerTest():
    print('with')

"""
上記では、__enter__の処理、withブロックの処理、__exit__の処理が順に実行される。
"""

print("==========")
class ContextManagerTest:
    def __enter__(self):
        print('__enter__')
        return 'as obj'
    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__')
 
with ContextManagerTest() as as_obj:
    print(as_obj)
# asで渡されるオブジェクトは「__enter__」の戻り値で指定することができる。

print("==========")

# プロパティ
# プロパティを利用してアクセス制御を行うコード
class Image(object):
    def __init__(self):
        self._width = 300
        self._height = 400

    @property
    def width(self):
        return self._width

    # プロパティの値を設定している
    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    # プロパティの値を設定している
    @height.setter
    def height(self, height):
        self._height = height

    #@は「デコレータ」という
if __name__ == '__main__':
    img = Image()
    img.width = 200
    img.height = 100
    print("width: "+img.width)
    print("height: "+img.height)

print("==========")

# デコレータについてもう一例
def scramble(egg):
    def _scramble():
        return "scramble " + egg() + "!"
    return _scramble

@scramble
def egg():
    return "egg"
"""
要は「親関数の中の子関数の内容」を示す必要がある場合に、その関数がどの親様子の中に存在するものなのかを示すうえで使うのがデコレータ。
"""

if __name__ == '__main__':
    print(egg()) # scramble egg!