# if文
x = int(input('数字を入れてください: '))
if x < 0:
    print('負の値です')
elif x == 0:
    print('0です')
else:
    print('正の値です')
# Pythonにはswitchやcaseはないようだ。
print("\n")

# for文
"""
for文の表記のキホンはこうだ。
for 要素 in イテラブル:
    処理
"""
#inの後は変数である必要はない。
#リストでも文字列でも、そのままぶっ込んでいいようだ。
for i in [1, 2, 3]:
    print(i)
print("\n")
for s in 'abc':
    print(s)
print("\n")

# for文での指定回数分繰り返し
for i in range(5):
  print(i) #こうすると自動的に0～5が出力される
print(range(5)) #ただこのように書くと「range(0, 5)」と出る
print(list(range(5))) #こうしないと配列にならない
print("\n")

# breakとcontinue
"""
passは何もしないことを表す文です。
ここでは、修正箇所を示すために用いています。
一般には、Pythonの文法上、文が必要だけど処理がないときに用いられます。
"""
for i in range(5):
    if i == 2:
        break
    print(i) # 0 1
print()  # 空行

for i in range(5):
    if i == 2:
        continue
    print(i) # 0 1 3 4

# for文の演習
lst = ['pine', 'apple', 'orange', 'end', 'no show']

for word in lst:
    if word == 'end':
        break
    print(word) #pine apple orange