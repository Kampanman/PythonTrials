# 文字列の結合
num = 123
text = "abc"  # 行の途中からコメント
print(num, text)  # 123 abc (間にスペースがつくのは注意)
print("\n")

# 四則演算
print(2 * (1 + 3)) #8（積）
print(5 / 2) #2.5（商）
print(5 // 2) #2（商の整数分）
print(5 % 2) #1（余り）
print(5 ** 2) #25（乗数）
print("\n")

# 文字列の出力のされ方の違い
s = 'pine' 'apple'
print(s) #pineapple
s = ('pine'
     'apple')
print(s) #pineapple
print('Yes' * 3) #YesYesYes
print('is' in 'this') #True
print("\n")

# 文字列のインデックス指定とスライス
s = 'ABCD'

print('インデックス： s[0] =', s[0]) #インデックス： s[0] = A

print('スライス： s[1:3] =', s[1:3]) #スライス： s[1:3] = BC
print('スライス： s[:3] =', s[:3]) #スライス： s[:3] = ABC
print('スライス： s[1:] =', s[1:]) #スライス： s[1:] = BCD

print('ステップ： s[::2] =', s[::2]) #ステップ： s[::2] = AC
print('ステップ： s[::-1] =', s[::-1]) #ステップ： s[::-1] = DCBA

print('長さ： len(s) =', len(s)) #長さ： len(s) = 4
print("\n")

# ここまでの演習
s = 'Python'

print(11 // 3)  # 11 を 3 で割った商を出力
print(11 % 3)  # 11 を 3 で割った余りを出力
print(2 ** 3)  # 2 の 3乗を出力

print(s * 3)  # sを3回繰り返し出力
print(s[::-1])  # sを逆順にして出力
print(s[2:5])  # sの3文字目から5文字目までを出力
print(s[:2])  # sの2文字目までを出力

print("\n")