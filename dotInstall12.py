# イテレータ - 次の要素を返してくれるデータの集合

scores = [1,2,4,5]
it = iter(scores)
print(next(it)) #1
print(next(it)) #2
print("サァ～ン！")
print(next(it)) #4
print("==========")

for score in scores:
  print(score)
# ループ処理ならば、自動的にイテレーターに変換してくれる
print("==========")

def get_infinite(): # ジェネレーター
  i = 0
  while True:
    yield i * 2
    i += 1

g = get_infinite()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# つまり、コイツを追加した分だけ関数の処理を実行できる
print("==========")

# map(関数, イテレータ)
def triple(n):
  return n * 3

print(list(map(triple, [1,2,3])))

# lambda 引数: 処理
print(list(map(lambda n: n * 3, [4,5,6])))


# filter(関数, イテレータ)
def is_even(n):
  return n % 3 == 0

print(list(filter(is_even, range(29))))
print(list(filter(lambda n: n % 3 == 0, range(30,49))))