# リスト型

scores = [60,70,80]
"""
print(scores[0]) #60
scores[0] = 65
print(len(scores)) #2
scores.append(100)
print(scores)
"""

for score in scores:
  print(str(score)+"点") # 60,70,80

for i, score in enumerate(scores):
  print("{0}番: {1}点".format(str(i+1), str(score)))


# タプル型 -リスト型と異なり値変更ができない
items = (50,"apple",32.5)
print(items[1]) #apple
"""
items[1] = "orange" #書き換えられないのでエラーになる
"""

print(list((1,3,5))) #タプルをリストにする（変更可能になる）
print(tuple([1,3,5])) #リストをタプルにする

# スライス（部分的リストの作成機能）
scores = [55,60,70,80,85]
print(scores[1:4]) #60,70,80 (1から数えて4未満のもの)
print(scores[:2]) #55,60（0から数えて2未満のもの）
print(scores[3:]) #80,85（0から数えて3以降のもの）
print(scores[-3:]) #70,80,85（末尾から数えて3つ分）

s = "hello"
print(s[1:4]) # ell

# セット（集合型）- 順番がなく且つ値の重複を認めない
a = {1,1,9,5}
print(a)
#その要素がセットの中にあるかを検索するときは次のを使う
print(5 in a) #あればTrueで返ってくる
a.add(2) #2が追加される
a.remove(9) #9が削除される
print(a)
print(len(a)) #要素の数を示してくれる

b = {1,3,5,8}
c = {3,5,8,9}
print(b | c) #和集合
print(b & c) #積集合
print(b - c) #差集合


# 辞書型

scores = {"Tanjiro": 85, "Zenitsu": 65, "Inosuke":25}
print(scores["Tanjiro"])
scores["Zenitsu"] = 60 #要素「Zenitsu」の書き換え
scores["Kanao"] = 90 #要素「Kanao」を追加
del(scores["Inosuke"]) #要素「Inosuke」を削除
print(scores)

scores["Nedsuko"] = 70
scores["Inosuke"] = 35
# 次のようにすると、要素をループで取り出す事ができる
for key, value in scores.items():
  print("{0}'s score: {1}".format(key, value))
