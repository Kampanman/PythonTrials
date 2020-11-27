# 様々なループ用の関数
"""
enumerate(iterable, start=0)
　：startからの通し番号とiterableで繰り返される値のタプルを要素とするイテレーターを返します。
zip(*iterables)
　：それぞれのイテラブルから要素を集めたイテレータを返します。
sorted(iterable, *, key=None, reverse=False)
　：iterableを小さい順にソートしたリストを返します。keyで比較関数を指定できます。reverse=Trueとすると大きい順になります。
reversed(seq)
　：seqを逆順にしたイテレーターを返します。
"""

items = ('cup', 'art', 'box')
print('items:', items)

print('enumerate:')
print(list(enumerate(items)))

print('zip:')
print(list(zip(range(3), items)))

print('sorted:')
print(sorted(items))

print('reversed:')
print(list(reversed(items)))

"""
上記の実行結果
items: ('cup', 'art', 'box')
enumerate:
[(0, 'cup'), (1, 'art'), (2, 'box')]
zip:
[(0, 'cup'), (1, 'art'), (2, 'box')]
sorted:
['art', 'box', 'cup']
reversed:
['box', 'art', 'cup']
"""


# 様々な条件の書き方
"""
not 条件
　：bool(条件)の否定です。条件には、任意のオブジェクトが使えます。not Trueは、Falseです。
条件1 and 条件2
　：条件1と条件2の両方が真のとき真になります。ただし、評価結果が True/False を返すとは限りません（後述の補足参照）。
条件1 or 条件2
　：条件1と条件2のどちらかが真のとき真になります。ただし、評価結果が True/False を返すとは限りません（後述の補足参照）。
式1 is 式2
　：式1と式2が同一のオブジェクトかどうかを返します。1 is 1や'abc' is 'abc'はTrueです。[1] == [1]はTrueですが[1] is [1]はFalseになります。
要素 in コンテナ
　：要素がコンテナに含まれるかどうかを返します。コンテナとは要素を管理するオブジェクトでリストやタプルや集合や辞書などです。
式1 if 条件 else 式2
　：条件が真のとき式1になり、そうでないとき式2になります。条件式あるいは三項演算子とよばれます。

- 様々な比較の書き方
Pythonでは比較の条件を連結して記述できます。

0 <= x <= 1は、0 <= x and x <= 1を意味します。
0 <= x < y <= 1は、0 <= x and x < y and y <= 1を意味します。
a == b <= cは、a == b and b <= cを意味します。
"""

result1 = 'is' not in 'this'
print("'is' not in 'this':", result1)

result2 = 'OK' and None
print("'OK' and None:", result2)

result3 = 'OK' or None
print("'OK' or None:", result3)

val = 'OK'
result4 = val is None
print("val is None:", result4)

result5 = 'OK' if 'OK' else None
print("'OK' if 'OK' else None:", result5)

x = 1
result6 = 0 <= x <= 1
print("0 <= x <= 1:", result6)

"""
上記の実行結果
'is' not in 'this': False
'OK' and None: None
'OK' or None: OK
val is None: False
'OK' if 'OK' else None: OK
0 <= x <= 1: True
"""


# シーケンス同士の比較
"""Boolean型で返ってくる"""
result1 = [0, 1, 2] < [0, 1, 3]
print("[0, 1, 2] < [0, 1, 3]:", result1)
result2 = [0, [0, 1, 2]] < [0.0, [0, 1, 3]]
print("[0, [0, 1, 2]] < [0.0, [0, 1, 3]]:", result2)
result3 = 'abc' < 'abd'
print("'abc' < 'abd':", result3)

"""
実行結果
[0, 1, 2] < [0, 1, 3]: True
[0, [0, 1, 2]] < [0.0, [0, 1, 3]]: True
'abc' < 'abd': True
"""


# 練習問題 - 「購買ログの解析」
"""
2種類の購買ログがあります。

log1：レジごとの購入者のIDのリストです。
log2：レジごとの「購入商品のIDのタプル」のリストです。
log1とlog2は対応しています。購入者log1[i]の購入した商品はlog2[i]です。

問題
「商品IDが100の商品を購入している購入者」のIDをソートして出力してください。
"""
log1 = [6, 1, 3, 5, 2, 4]
log2 = [(100, ), (115, 110, 180), (120, 100), (120, 131), (115, 100), (100, 115, 119)]

print(sorted([i1 for i1, i2 in zip(log1, log2) if 100 in i2]))

"""
実行結果
[2, 3, 4, 6]
"""