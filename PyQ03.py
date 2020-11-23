# リスト
lst = [1, 2, 3, 4]
print('lst:', lst)
  # lst: [1, 2, 3, 4]
print('lst[0]:', lst[0])
  # lst[0]: 1
print('lst[-1]:', lst[-1])
  # lst[-1]: 4
print("\n")

# リストのスライス
lst = [1, 2, 3, 4]
print('lst[1:3]:', lst[1:3])
  #lst[1:3]: [2, 3]
print('lst[1:]:', lst[1:])
  #lst[1:]: [2, 3, 4]
print('lst[1::2]:', lst[1::2])
  #lst[1::2]: [2, 4]
print('lst[:0:-1]:', lst[:0:-1])
  #lst[:0:-1]: [4, 3, 2]
print("\n")

# リストの演算
lst = [1, 2, 3, 4]
print('lst + [5, 6]:', lst + [5, 6])
  #lst + [5, 6]: [1, 2, 3, 4, 5, 6]
print('lst * 2:', lst * 2)
  #lst * 2: [1, 2, 3, 4, 1, 2, 3, 4]
print("\n")

# リストの変更・追加
lst = [1, 2, 3, 4]
print('lst:', lst)
"""
上記のリストを
lst = [10, 20, 30] と
lst = [10, 20, 30, 40] にするためにはどうするか
"""
lst[0] = 10
lst[1:4] = 20, 30 #1番目から4番目手前、という意味なので注意
print('lst:', lst)
# リストの末尾に要素を追加するのなら、コイツを使う
lst.append(40)
print('lst:', lst)
print("\n")

# ここまでの演習
lst = ['A', 'B', 'C', 'D', 'E']
# lstの先頭の要素を出力してください。
print('lstの先頭:', lst[0])
# lstの最後の要素を出力してください。
print('lstの最後:', lst[-1])
# lstの2番目から3番目を出力してください。
print('lstの2番目から3番目:', lst[1:3])
# lstの先頭から最後までを1つ飛ばしで出力してください。
print('lstの先頭から最後までを1つ飛ばしで:', lst[::2])
# lstを逆順に出力してください。
print('lstの逆順:', lst[::-1])
# lstと['F', 'G']を連結したリストを出力してください。
print("lstに['F', 'G']を連結:", lst + ['F', 'G'])

# ここからlstの中身を変える
lst = ['A', 'B', 'C', 'D', 'E']
# lstの出力が、['A', 'B', 'C', 'D', 'E', 'F']になるようにlstに'F'を追加してください。
lst.append('F')
print('lst:', lst)
# lstの出力が、['A', 'C', 'E', 'F']になるように、代入文でlstを修正してください。
lst[1:4] = ['C']
print('lst:', lst)
