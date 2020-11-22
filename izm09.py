# ファイル・ディレクトリの存在確認
# os.path.isfile()
import os
src = 'c:/Users/user/Desktop/MemoryLinkers/connect.php'
if os.path.isfile(src):
  print('ファイルが存在しています。')
else:
  print('ファイルは存在していません。')

print('==========')

# ファイル・ディレクトリのコピー
import shutil

movedir = 'C:/Users/user/Desktop/PythonTrials'
if os.path.exists(movedir):
  # ファイル・ディレクトリ問わず存在しているかを確かめるには、こう書く。
  copied = movedir + '/copied'
  # os.makedirs(copied) # ディレクトリが作成される
  # print('フォルダを作成しました')
  shutil.copytree(copied,"../copied2") #相対パスでも行けるようだ
  print('コピーディレクトリを作成しました。')
else:
  print('そもそもディレクトリが存在していませんでした。')
print('==========')

input("ディレクトリごと削除しますか？")
# ルートディレクトリごと削除する方法
rmdir = 'C:/Users/user/Desktop/copied2'
shutil.rmtree(rmdir)
print('ディレクトリごと削除しました。')

