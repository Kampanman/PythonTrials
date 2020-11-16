# 内包表記

# 0-9を配列化
print([i for i in range(10)]) # i*1が10に達するまでのJ*1の配列
print([j * 3 for j in range(20)]) # j*3が20*3に達するまでのJ*3の数の配列
# mapを使うよりも上記の方がスッキリ書けている。
print([k * 4 for k in range(40) if k % 3 == 0]) # k*4が40*4までのk*4の配列
print(l * 5 for l in range(20) if l % 2 == 0) #ジェネレータ
print({l * 5 for l in range(20) if l % 2 == 0}) #集合型