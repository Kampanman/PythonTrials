# 辞書とは
"""
【辞書の特徴】
・キーと値のペアの集合です。キーに対応する値を取得できます。
・リテラルは、{'art': 1, 'box': 2}のように{キー1: 値1, キー2: 値2, ...}のように記述します。
・キーは、イミュータブル（変更不可）なものしか指定できません。値は何でも指定できます。
・同じキーは1つだけ持てます。複数追加すると上書きします。
・順序がありませんが、イテラブルとして取得するときの順番は不変です。
・マップや連想配列と呼ぶこともあります。
"""

d = {"art":1, "box":2}

# 追加
d["cup"] = 3

# 参照
print("d['art']:", d["art"])
print("d['cup']:", d["cup"])

# 削除
del d['art']
print("d:",d)
print()

# 辞書の主なメソッド
"""
get(key, default=None)
　：keyに対応する値を取得します。存在しないときは、defaultを返します。
clear()
　：全ての要素を削除します。
copy()
　：コピーを作成します。
pop(key[, default])
　：keyに対応する要素を削除し値を返します。存在しないときは、defaultが指定されていればそれを返し、なければエラー（KeyError）になります。
popitem()
　：何れかの要素を削除し、キーと値のタプルを返します。空だとエラー（KeyError）になります。
setdefault(key, default=None)
　：keyが存在するときは対応する値を返します。存在しないときはkeyをdefaultで設定し、defaultを返します。
update(other)
　：別の辞書otherの要素全てを追加します。
dict.fromkeys(iterable, value=None)
　：iterableの要素をキーに、値をvalueとして辞書を作成します。
"""
print("d = dict.fromkeys(['box', 'cup'], 3)")
d = dict.fromkeys(['box', 'cup'], 3)
print("d:", d)

# 参照
print("d.get('art', -1):", d.get('art', -1))
print("d:", d)
print("d.setdefault('art', 1):", d.setdefault('art', 1))
print("d:", d)

# 更新
d.update({'box': 2})
print("d.update({'box': 2})")
print("d:", d)

# 削除
print("d.pop('art'):", d.pop('art'))
print("d.pop('cup'):", d.pop('cup'))
print("d.popitem():", d.popitem())

# 全削除
d.clear()
print("d.clear()")
print("d:", d)
print()


# イテラブルを返すメソッド
"""
keys()
　：キーを要素とするイテラブルを返します。
values()
　：値を要素とするイテラブルを返します。
items()
　：キーと値のタプルを要素とするイテラブルを返します。
"""
d = {"art":1, "box":2, "cup":3}
print("keys:")
for k in d.keys():
  print(k)
print()

print("values:")
for v in d.values():
  print(v)
print()

print("items:")
for k, v in d.items():
  print(k,v)
print()

# 演習問題：血液型別の人数
"""血液型ごとの被験者の人数を辞書dcに入れてください。"""

"""
【ヒント】
・dc = dict.fromkeys(['A', 'B', 'O', 'AB'], 0)とすると、血液型ごとに0で、辞書dcを初期化できます。
・血液型をbloodとしたとき、dc[blood] += 1とすると、その血液型の人数を1増やせます。
"""

bloods = ['A', 'B', 'O', 'AB', 'A', 'B', 'A']

dc = dict.fromkeys(['A', 'B', 'O', 'AB'], 0)
for blood in bloods:
  dc[blood] += 1

for blood, num in dc.items():
  print(f'{blood:2}: {num}')

"""
【実行結果】
A : 3
B : 2
O : 1
AB: 1
"""