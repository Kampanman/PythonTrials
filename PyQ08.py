# タプル
# リストとは違って変更不可。()を使って表現する。
"""
index(item[, start[, end]])
　：itemを探し、その位置を返します。見つからなければエラー（ValueError）になります。探索範囲は、startからendの前までで、返り値は[start, end)の範囲になります。省略すると全体を探します。
count(item)
　：itemの出現回数を返します。
"""

items = ('art', 'box', 'cup')
print("items:")  # 各要素
for item in items:
    print('  -', item)
"""
【実行結果】
items:
  - art
  - box
  - cup
items: ('art', 'box', 'cup')
"""

print("items:", items)
result1 = items[2]
print("items[2]:", result1)
  #items[2]: cup

# 個数計測
result2 = items.count('box')
print("items.count('box'):", result2)
  #items.count('box'): 1

# 位置探索
result3 = items.index('cup')
print("items.index('cup'):", result3)
  #items.index('cup'): 2

# タプルの入れ子
items2 = (items, items)
print("items2:", items2)
  #items2: (('art', 'box', 'cup'), ('art', 'box', 'cup'))

print()

# アンパック
"""
タプルは1つのオブジェクトですが、複数の変数に同時に代入できる。これが、アンパック。

(ex) 
items = ('art', 'box', 'cup')
a, b, c = items
  とすると・・・
a == 'art'
b == 'box'
c == 'cup'　・・・となる
"""

items = ('art', 'box', 'cup')
print("items:", items) # items: ('art', 'box', 'cup')
a, b, c = items
print("a, b, c = items")
print("(a,b,c):",(a,b,c)) # (a, b, c): ('art', 'box', 'cup')

"""残りの個数が不明のときには、アスタリスク（*）を使ってアンパックできる。"""
a, *b = items
print("a, *b = items")
print("(a, b):", (a, b))
# (a, b): ('art', ['box', 'cup'])
print()

# forでのアンパック
for i, j in [(1,2), (3,4)]:
  print(i, j)
# 1 2
# 3 4
print()

# 値の交換
"""a, b = b, aとすると、値の交換ができる。"""


# allとany
"""
all（イテラブル）
　：イテラブルの全ての要素が真ならば、Trueを返します。
any（イテラブル）
　：イテラブルのいずれかの要素が真ならば、Trueを返します。
"""
items1 = (True, False, True)
print("items1:", items1)
items2 = (True, True, True)
print("items2:", items2)

# 全ての要素が真かどうか
result_all1 = all(items1)
print("all(items1):", result_all1)

# 全ての要素が真かどうか
result_all2 = all(items2)
print("all(items2):", result_all2)

# 何れかの要素が真かどうか
result_any1 = any(items1)
print("any(items1):", result_any1)


# データの検索
"""
　顧客IDが10以下で、販売額が100円以上のデータを出力してください。

　forでループしてください。
　タプルの要素はインデックスを指定して取得できますし、アンパックして取り出すこともできます。
"""
sales = ((1, 100), (2, 30), (7, 150), (11, 120), (10, 100))

for i in sales:
  if i[0] <= 10 and i[1] >= 100:
  # 配列の要素なので、i[0],i[1]というように記述する
    print(i)