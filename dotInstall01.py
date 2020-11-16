# テキスト出力
print("アイーン！")

# 文字列の連結と繰り返し
print("\n何なんだチミはってか？\n何なんだチミはってか！？え！？")
name = "変なおじさん"
print("そうです。\nワダスが"+name+"です。\n")
print(("ア"+name+"だか～ら"+name+"♪\n") * 3)
print("だっふんだ！\n")

# 応用技(with 文字列の複数行纏め)
song = """
カ～ラ～ス～　なぜ鳴くの～
{}でしょ～♪\n"""
song2 = """
ゾ～～さん　ゾ～～さん　お～～鼻が長いのね
そ～～～よ　{}も　な～～がいのヨ～～♪\n"""
print(song.format("カラスの勝手")+song2.format("チ〇チ〇"))

# boolean型の検証
print(True and False) #False
print(True or False) #True
print(not True) #False

# 文字列に値を埋め込む
studentName = "エマ"
score = 100
print("""
生徒氏名：%s ,得点：%f""" % (studentName, score))
studentName_2 = "ノーマン"
score_2 = 100
print("生徒氏名：{0} ,得点：{1}".format(studentName_2, score_2))
studentName_3 = "レイ"
score_3 = 100
print("生徒氏名：{0} ,得点：{1:<10.2f}".format(studentName_3, score_3))
