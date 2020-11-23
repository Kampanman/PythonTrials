# 文字列の確認用メソッド
"""
isalpha()
：全ての文字がalphabeticかどうかを返します。アルファベットや漢字、平仮名、カタカナなどがalphabeticです。

isdigit()
：全ての文字が数字かどうかを返します（全角の数字も含みます）。

islower()
：大文字と小文字の区別のある文字が含まれていて、その全てが小文字かどうかを返します。

isupper()
：大文字と小文字の区別のある文字が含まれていて、その全てが大文字かどうかを返します。

lower()
：大文字と小文字の区別のある文字を小文字に変換して返します。そうでない文字はそのままです。全角の大文字は、全角の小文字になります。

upper()
：大文字と小文字の区別のある文字を大文字に変換して返します。そうでない文字はそのままです。全角の小文字は、全角の大文字になります。
"""

print("'abc'.isalpha():", 'abc'.isalpha()) #'abc'.isalpha(): True
print("'ab3'.isalpha():", 'ab3'.isalpha()) #'ab3'.isalpha(): False
print("'12'.isdigit():", '12'.isdigit()) #'12'.isdigit(): True
print("'abc'.islower():", 'abc'.islower()) #'abc'.islower(): True
print("'ABC'.isupper():", 'ABC'.isupper()) #'ABC'.isupper(): True
print("'Abc'.isupper():", 'Abc'.isupper()) #'Abc'.isupper(): False
print("'Abc'.lower():", 'Abc'.lower()) #'Abc'.lower(): abc
print("'Abc'.upper():", 'Abc'.upper()) #'Abc'.upper(): ABC
print("\n")

# 探索用メソッド
"""
count(sub[, start[, end]])
：[start, end)の範囲で、subの出現回数を返します。

find(sub[, start[, end]])
：[start, end)の範囲で、subの最初の出現位置を返します。返り値の位置は[start, end)の範囲に入ります。見つからないと-1を返します。

index(sub[, start[, end]])
：[start, end)の範囲で、subの最初の出現位置を返します。返り値の位置は[start, end)の範囲に入ります。見つからないとエラー（ValueError）を返します。

endswith(suffix[, start[, end]])
：[start, end)の範囲で、suffixで終わるかどうかを返します。

startswith(prefix[, start[, end]])
：[start, end)の範囲で、prefixで始まるかどうかを返します。
"""
print("'ABCAB'.count('AB'):", 'ABCAB'.count('AB'))
  #'ABCAB'.count('AB'): 2
print("'ABC'.find('X'):", 'ABC'.find('X'))
  #'ABC'.find('X'): -1
print("'ABC'.index('B'):", 'ABC'.index('B'))
  #'ABC'.index('B'): 1
print("'ABC'.endswith('BC'):", 'ABC'.endswith('BC'))
  #'ABC'.endswith('BC'): True
print("'ABC'.startswith('AB'):", 'ABC'.startswith('AB'))
  #'ABC'.startswith('AB'): True
print("'ABC'.startswith('BA'):", 'ABC'.startswith('BA')) 
  #'ABC'.startswith('BA'): False
print("'ABC'.startswith(('AB', 'BA')):", 'ABC'.startswith(('AB', 'BA')))
  #'ABC'.startswith(('AB', 'BA')): True
print("\n")

# 文字列の主な変換用メソッド
"""
join(iterable)
：iterableの要素をセパレーターをはさんで連結して文字列を作成します。要素は文字列でなければいけません。セパレーターは文字列自身です。

replace(old, new, count=-1)
：oldをnewで置換した文字列を返します。置換の最大回数はcountです。countが-1のときは全て置換します。

split(sep=None, maxsplit=-1)
：sepを区切るための文字列として、リストに分割します。リストは['Alice', 'Bob', 'Carol']のように表されるデータ構造です。次のクエストで学びます。sepは取り除かれます。最大分割数はmaxsplitです。maxsplitが-1のときは全て分割します。

splitlines( keepends=False)
：改行文字を区切りにリストに分割します。keepends=Falseの場合、区切りの改行文字は削除されます。空文字列のとき[]になります。

strip(chars=None)	文字列の先頭または末尾に、文字集合charsに含まれる文字があれば削除した文字列を返します。文字集合が指定されないと空白文字（スペース、タブ、改行など）を対象とします。

lstrip(chars=None)
：文字列の先頭に、文字集合charsに含まれる文字があれば削除した文字列を返します。文字集合が指定されないと空白文字（スペース、タブ、改行など）を対象とします。

rstrip(chars=None)
：文字列の末尾に、文字集合charsに含まれる文字があれば削除した文字列を返します。文字集合が指定されないと空白文字（スペース、タブ、改行など）を対象とします。
"""
print("'...'.splitlines()", """\
Alice
Bob
Carol""".splitlines())
  #'...'.splitlines() ['Alice', 'Bob', 'Carol']
print("'abcd'.replace('bc', '-'):", 'abcd'.replace('bc','-'))
  #'abcd'.replace('bc', '-'): a-d
print("'1 2 3'.split():", '1 2 3'.split())
  #'1 2 3'.split(): ['1', '2', '3']
print("'1<>2<><><3'.split('<>'):", '1<>2<><><3'.split('<>'))
  #'1<>2<><><3'.split('<>'): ['1', '2', '', '<3']
print("'--abc--'.strip('-'):", '--abc--'.strip('-'))
  #'--abc--'.strip('-'): abc
print("'--abc--'.rstrip('-'):", '--abc--'.rstrip('-'))
  #'--abc--'.lstrip('-'): abc--
print("'--abc--'.lstrip('-'):", '--abc--'.lstrip('-'))
  #'-'.join('1 2 3'.split()): 1-2-3
print("'-'.join('1 2 3'.split()):", '-'.join('1 2 3'.split()))
print("\n")

# 上記の演習
s1 = '1234-567 89-00'
s2 = """\
1234
567
89"""
items = ['12', '345', '6789']

print(s1.replace('-',''))
  #1234567 8900
print(s1.split('-'))
  #['1234', '567 89', '00']（「-」で区切られた配列に置き換わる）
print(s2.splitlines())
  #['1234', '567', '89']（行で区切られた配列に置き換わる）
print(''.join(items))
  #123456789
