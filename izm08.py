# ファイル、ディレクトリの存在チェック

import os

filepath = 'c:/Users/user/Desktop/PythonTrials'
filename = 'c:/Users/user/Desktop/PythonTrials/izm08.py'

if os.path.exists(filepath): 
  #ファイルもしくはディレクトリがあるかをここでチェックしている
    print('指定のファイル、またはディレクトリが存在しています。')   
    if os.path.isfile(filepath):
        print('指定のパスはファイルです。')
        print('==========')
    if os.path.isdir(filepath):
        print('指定のパスはディレクトリです。')
        print('==========')
else:
    print('指定のファイル、またはディレクトリが存在していません。')
    print('==========')

if os.path.exists(filename): 
    print('指定のファイル、またはディレクトリが存在しています。')   
    if os.path.isfile(filename):
        print('指定のパスはファイルです。')
        print('==========')
    if os.path.isdir(filename):
        print('指定のパスはディレクトリです。')
        print('==========')
else:
    print('指定のファイル、またはディレクトリが存在していません。')
    print('==========')

# ディレクトリの作成と削除
import shutil

def show_dir(path):
  # 指定パス以下のディレクトリを全て表示させる関数
    print('==========')
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            print(os.path.join(dirpath, dirname))

tmpdir = 'c:/Users/user/Desktop/PythonTrials'
 
# os.mkdir(tmpdir)
# ↑既に作成されているのならば処理が止まる
movedir = tmpdir+'/mydir/inner1/inner1-1'
os.makedirs(movedir) # ディレクトリが作成される
show_dir(tmpdir)
print('フォルダを作成しました\n==========')
os.rmdir(movedir) # 指定したディレクトリの右端のフォルダorファイルが削除される
show_dir(tmpdir)
print('フォルダを削除しました\n==========')
