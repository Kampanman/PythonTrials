# 集合のメソッド（追加等）
"""
add(item)
　：itemを追加します。
update(iterable)
　：イテラブルiterableの要素全てを追加します。
clear()
　：全ての要素を削除します。
pop()
　：何れかの要素を削除し返します。
remove(item)
　：itemを削除します。itemが存在しないとエラー（KeyError）になります。
discard(item)
　：itemを削除します。itemが存在しなくてもエラーになりません。
"""

items = {'art'}
print("items:", items)

# 1要素を削除
result = items.pop()
print("items.pop():", result)
print("items:", items)

# リストを追加
items.update(['egg', 'fog'])
print("items.update(['egg', 'fog'])")
print("items:", items)

# 全削除
items.clear()
print("items.clear()")
print("items:", items)

# 追加
items.add('doll')
print("items.add('doll')")
print("items:", items)

# 削除
items.remove('doll')
print("items.remove('doll')")
print("items:", items)
print()

# 集合のメソッド（判定等）

# 判定とコピー
"""
isdisjoint(other)
　：otherと共通する要素がなければTrueです。
issubset(other)
　：otherの部分集合であればTrueです。
issuperset(other)
　：otherが部分集合であればTrueです。
copy()
　：コピーを返す。
"""
# 演算子を用いる方法
"""
s1 <= s2
　：s1.issubset(s2)あるいは、s2.issuperset(s1)と同じです。
s1 < s2
　：s1 <= s2かつs1 != s2と同じです。
s1 == s2
　：s1 <= s2かつs1 >= s2と同じです。
item in s1
　：itemがs1に含まれればTrueです。
"""
items = {3, 4}
print("items:", items)

# 共通する要素がないか
result1 = items.isdisjoint({1, 2})
print("items.isdisjoint({1, 2}):", result1)

# 部分集合か
result2 = items.issubset({1, 3, 4})
print("items.issubset({1, 3, 4}):", result2)

# 引数が部分集合か
result3 = items.issuperset({4})
print("items.issuperset({4}):", result3)
print()

# 集合のメソッド（演算）
"""
difference(other)
　：otherの要素を削除した集合を返します。差集合といいます。
difference_update(other)
　：difference(other)を演算して置き換えます。
intersection(other)	otherと共通の集合を返します。積集合といいます。
intersection_update(other)
　：intersection(other)を演算して置き換えます。
symmetric_difference(other)
　：片方にしか含まれない要素の集合を返します。対称差といいます。
symmetric_difference_update(other)
　：symmetric_difference(other)を演算して置き換えます。
union(other)
　：otherの要素を追加した集合を返します。和集合といいます。
"""
# 演算子を用いる場合
"""
s1 - s2
　：s1.difference(s2)と同じです。
s1 & s2
　：s1.intersection(s2)と同じです。
s1 ｜ s2
　：s1.union(s2)と同じです。
s1 ^ s2
　：s1.symmetric_difference(s2)と同じです。
"""
s1 = set('ab')
s2 = set('bc')
print("s1:", s1)
print("s2:", s2)

# 差集合
result1 = s1.difference(s2)
print("s1.difference(s2):", result1)

# 積集合
result2 = s1.intersection(s2)
print("s1.intersection(s2):", result2)

# 対称差
result3 = s1.symmetric_difference(s2)
print("s1.symmetric_difference(s2):", result3)

# 和集合
result4 = s1.union(s2)
print("s1.union(s2):", result4)


# 日付の集合演算
"""
【問題】
Aさん、Bさん、Cさんの3人で新年会をすることにしました。ただし、Cさんは、辞退の可能性があります。
それぞれの可能な日付がa, b, cに入っています。
　・a = {'1/1', '1/2', '1/4'}
　・b = {'1/2', '1/4', '1/7', '1/8'}
　・c = {'1/3', '1/4', '1/7', '1/8'}
以下を計算し、出力してください。

・3人とも出席できる日付
・AさんとBさんが出席できて、Cさんが出席できない日付
"""
# 3つの集合の積集合は、set.intersection(集合1, 集合2, 集合3)とすることができる。

# 3人とも出席できる日付
result1 = set.intersection(a,b,c)
print('3人とも出席できる日付:', result1)

# AさんとBさんが出席できて、Cさんが出席できない日付
result2 = a.intersection(b).difference(c)
print('AさんとBさんが出席できて、Cさんが出席できない日付:', result2)
