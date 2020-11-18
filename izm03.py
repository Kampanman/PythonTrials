# リストに要素を追加
test_list = []
print(test_list)
print("==========")
# 次のようにして空のリストに要素を追加する
test_list.append('パ')
test_list.append('チ')
test_list.append('ン')
test_list.append('コ')
print(test_list)
# インデックスを指定して追加
test_list.insert(4, '玉')
print(test_list)
test_list.insert(4, 'の')
print(test_list)

# 要素の削除 1
test_list.remove('パ')
print(''.join(test_list))
# 要素の削除 2
print(test_list.pop(3)+' を消します') # リストから除く分だけ表示
print(''.join(test_list))

print("==========")
# リスト内での要素数を取得
test_list2 = list("ウコチャヌプコロ")
print(test_list2)
print(test_list2.count("コ")) #2

# 辞書型でValueの取得
test_dict_1 = {'年':'2010', '月':'1', '日':'20'}

print("==========")
print(test_dict_1.get('年')) #2010
print(test_dict_1.get('歳')) #None
# 第二引数で、キーが存在しない場合に出力するものを設定
print(test_dict_1.get('年','ないって。'))
print(test_dict_1.get('歳','ないって。'))