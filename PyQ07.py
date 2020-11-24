# リストメソッド
"""
append(item)
　：リストの最後にitemを追加します。
extend(iterable)
　：リストの最後に、イテラブルiterableの要素全てを追加します。
insert(i, item)
　：iの位置の前に、itemを追加します。
remove(item)
　：itemを削除します。
pop([i])
　：iの位置の要素を削除して、その要素を返します。iを省略すると、末尾の要素を削除して返します。
clear()
　：全ての要素を削除します。
index(item[, start[, end]])
　：itemを探し、その位置を返します。見つからなければエラー（ValueError）になります。探索範囲は、startからendの前までで、返り値は[start, end)の範囲になります。省略すると全体を探します。
count(item)
　：itemの出現回数を返します。
sort(key=None, reverse=False)
　：リストをソートします。このように元のデータを変更する演算をインプレース演算といいます。keyで比較の関数を指定できます。reverse=Trueで大きい順にします。
reverse()
　：インプレース演算で逆順にします。
copy()
　：コピーを作成します。

Pythonでは、del 変数とすることで変数を削除できます。
"""

items = ['art', 'box', 'cup']
print("items:", items)

# 末尾に追加
items.append('doll')
print("items.append('doll')")
print("items:", items)

# 途中に追加
items.insert(2, 'doll')
print("items.insert(2, 'doll')")
print("items:", items)

# 計測
result = items.count('doll')
print("items.count('doll'):", result)

# 位置0の要素を削除
del items[0]
print("del items[0]")
print("items:", items)

# 反転
items.reverse()
print("items.reverse()")
print("items:", items)

# 全削除
items.clear()
print("items.clear()")
print("items:", items)
print()

items = [1]
print("items:", items) #[1]

# 末尾にリストを追加
items.extend([2, 5, 3, 4])
print("items.extend([2, 5, 3, 4])")
print("items:", items)

# 要素を削除
items.remove(3)
print("items.remove(3)")
print("items:", items)

# 末尾を削除して取得
result = items.pop()
print("items.pop():", result)
print("items:", items)

# 5の位置を探索
result = items.index(5)
print("items.index(5):", result)

# コピー
items2 = items.copy()
print("items2 = items.copy()")

# 逆順でソート
items.sort(reverse=True)
print("items.sort(reverse=True)")
print("items:", items)
print("items2:", items2)
print()


# 内包表現
# （リストの内包表記、ジェネレーター式、集合の内包表記、辞書の内包表記）

"""
sq = []
for i in range(10):
    sq.append(i**2) #iの2乗

これを、内包表記を使って書くと、次のようになる
"""
sq = [i**2 for i in range(10)]

"""
内包表記は、ネストにしたりifと組み合わせたりできます。
たとえば、2次元座標[0, 0]の上下左右のポイント（[-1, 0], [0, -1], [0, 1], [1, 0]）の取得は下記のように書けます。
"""
pt = [[x, y]
      for x in range(-1, 2)
      for y in range(-1, 2)
      if abs(x - y) == 1]
# absは絶対値を計算する関数
print(pt)
print()

# ログの整理
"""
【問題】
　ログデータ（log）を、「1行が1要素に対応したリスト」にしてください。さらに、各行も「単語ごとのリスト」にして、loglistに代入してください。
　pprint(loglist)で出力してください。
　loglistの要素のうち、要素のリスト中に'晴れ'が含まれる要素だけ、loglist2に代入してください。
　print(loglist2)で出力してください。

　なお、pprintは見やすいように整形して出力する関数です。
"""

"""
【ポイント】
・logを1行1要素のリストにするには、log.splitlines()でできます。
・文字列sを単語ごとのリストにするのは、s.split()でできます。
・リストを元に、条件を満たす要素で別のリストを作成するのは、[it for it in リスト if 条件]でできます。
・「要素のリスト中に'晴れ'が含まれる」か調べるには、'晴れ' in 要素でできます。
"""

from pprint import pprint

log = """\
1/1 晴れ
1/2 晴れ
1/3 曇り
1/4 雨
1/5 雨
1/6 曇り
1/7 晴れ
"""

loglist = [s.split() for s in log.splitlines()]
print('loglist:')
pprint(loglist)
loglist2 = [it for it in loglist if '晴れ' in it]
print('loglist2:', loglist2)

"""
【出力解答】
loglist:
[['1/1', '晴れ'],
 ['1/2', '晴れ'],
 ['1/3', '曇り'],
 ['1/4', '雨'],
 ['1/5', '雨'],
 ['1/6', '曇り'],
 ['1/7', '晴れ']]
loglist2: [['1/1', '晴れ'], ['1/2', '晴れ'], ['1/7', '晴れ']]
"""
