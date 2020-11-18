# 文字列の置換
the_word = "ヨードチンキ"
print(the_word)
print(the_word.replace("キ","〇"))
print("==========")

# 文字列を指定文字で分割＆再文字列化
the_word = "きんのたま"
print(the_word.split('の'))
ball = ''.join(the_word.split('の')) #joinメソッドを使う
print(ball)
print("==========")

# （発展）文字列を複数の指定文字で分割
import re
#複数の区切り文字を指定する場合はreモジュールを使用する。
the_word = "ちんすこう"
print(re.split('[すう]',the_word))
sao = ''.join(re.split('[すう]',the_word))
print(sao)
print("==========")

# （発展）文字列を一文字ずつに分割
the_word = "パチンコ"
print(list(the_word)) #["パ","チ","ン","コ"]
print(list(the_word)[-3:]) #後ろから3文字分取り出すのだから...
print("==========")

# 文字列の桁揃え
the_num = "1234"
print(the_num.rjust(5,'0')) # 01234

# 文字列の検索
test_str = 'ウコチャヌプコロ'
# 文字列の先頭が任意の文字であるか見る
print(test_str.startswith('ウコチャ')) #True
print(test_str.startswith('コロ')) #False
# 文字列中に任意の文字が含まれているか
print('ヌ' in test_str) #True
print('ノ' in test_str) #False

# 大文字・小文字変換
test_str = 'Oinarisan'
print(test_str.upper())
print(test_str.lower())

# 先頭・末尾の削除
test_str = "　それは　わたしの　おいなりさんだ！"
print(test_str)
test_str = test_str.lstrip() #左端を削る
# 引数無しの場合は空白を削る
print(test_str)
test_str = test_str.rstrip("！") #右端を削る
print(test_str)
