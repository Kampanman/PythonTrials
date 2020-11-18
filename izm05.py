# パスの結合

import os
 
PROJECT_DIR = 'C:¥python-izm'
SETTINGS_FILE = 'settings.ini'
 
print(os.path.join(PROJECT_DIR, SETTINGS_FILE))
# 次のようにすれば、結合したもの（両方とも変数）の間に文字列を挟む事が出来る
print(os.path.join(PROJECT_DIR, 'settings_dir', SETTINGS_FILE)) 

print("==========")
# if文のpass - 「何もしない」という意味
value_1 = 'python'
value_2 = 'izm'
if value_1 == 'Python':
    pass #何もしない
elif value_1 == 'python' and value_2 == 'izm':
    print('2番目の条件式がTrue')
elif value_1 == "IZM" or value_2 == "PYTHON":
    print('3番目の条件式がTrue')

print("==========")
# 例外処理
# try, except, finally
def exception_test(value_1, value_2):
    print('＝＝＝＝計算開始＝＝＝＝')
    result = 0 #まずは初期値を設定する必要がある
 
    try:
        result = value_1 + value_2
    except:
        print('！計算出来ません！')
    finally:
        print('計算完了')
 
    return result
     
print(exception_test(100, 200)) #計算完了 300
print(exception_test(100, '200')) #！計算出来ません！

# raise
"""呼び出し元にエラーを上げ、そのエラー処理を任せた方が良いケースで使われる。"""
def exception_test(value_1, value_2):
    print('＝＝＝＝計算開始＝＝＝＝')
    result = 0
    try:
        result = value_1 + value_2
    except:
        print('！計算出来ません！')
    finally:
        print('計算完了')

try:
    print(exception_test(100, 100)) #計算完了 300
    print(exception_test(200, 200)) #計算完了 400
    print(exception_test(300, '300'))
    #！計算出来ません！ 計算完了 エラーを受け取りました
except:
    print('エラーを受け取りました')

# エラー内容（スタックトレース）の取得
import sys
import traceback
 
def exception_test(value_1, value_2):
    print('＝＝＝＝計算開始＝＝＝＝')
    result = 0
    try:
        result = value_1 + value_2
    except:
        print('！計算出来ません！')
    finally:
        print('計算完了')
 
    return result
     
try:
    print(exception_test(100, '200'))
except:
    print('---------------------------------------')
    print(traceback.format_exc(sys.exc_info()[2]))
    print('---------------------------------------')

# こうすることで、計算結果（計算不能）の後でこういうメッセージが出る
"""
---------------------------------------
Traceback (most recent call last):
  File "test.py", line 27, in 
    print exception_test(100,"200")
  File "test.py", line 14, in exception_test
    result = value_1 + value_2
TypeError: unsupported operand type(s) for +: 'int' and 'str'

---------------------------------------
"""