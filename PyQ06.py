# ラムダ式（1つの式からなる小さな名前のない関数）
"""
func = lambda a, b: a + b
print(func(1, 2))

これは以下と同じことである。
"""
def func(a,b):
  return a + b
print(func(1,2)) #3


# ドキュメンテーション文字列

def add(a, b):
    """Add a and b.
    `add(a, b)` is same as `a + b`.
    """
    # 上記がドキュメンテーション文字列。
    return a + b

print(add.__doc__)
"""
Add a and b.
    `add(a, b)` is same as `a + b`.
"""
# ドキュメンテーション文字列は、関数名.__doc__で参照できる。
print(add(5,5)) #10


# ラムダ式とdocstringの演習
"""
docstringは、defの次の行に書きます。
ラムダ式は、lambda 引数の並び: 式のように書きます。
"""
def docst(a,b):
  """Subtract b from a."""
  return b - a

print(docst.__doc__)
"""Subtract b from a."""
print(docst(8,10)) #2