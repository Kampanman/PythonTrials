# if
score = int(input("得点: "))
#printでなくinputをつけると、ユーザーの入力した値を返してくれる
"""
# Pythonの複数行コメントアウト状態
if score >= 80:
  print("Good!")
elif score > 60:
  print("Ok")
else:
  print("Oops...")
"""
# 以下は上の条件分岐とだいたい同じことを行っている
print("Good!" if score >= 80 else "It's Ok...")
print("\n")
# while

i = 0
while i < 10:
  print(i)
  i += 1
else:
  print("complete!\n")

# for
# 「for 変数 in データの集合:」という記述をする
# for h in range(0, 10):
for h in range(10): # 整数10までの範囲、ということ
  if h == 5:
    break #breakは、その数字の時に処理を打ち切るもの
  print(h)
else:
  print("complete\n")

for g in range(10):
  if g == 3:
    continue #continueは、その数字の時だけ処理を飛ばすもの
  print(g)
else:
  print("complete!\n")