# インポート
"""
Pythonのインポートは、自ら作成したモジュールも対象となる。
"""
import testmod_izm04

test_c1 = testmod_izm04.TestClass() # create TestClass
test_c1.test_method("1") # call test_method 1
# fromとimportを両方とも使う場合
from testmod_izm04 import TestClass
test_c2 = TestClass() # create TestClass
test_c2.test_method("2") # call test_method 2

print("==========")
# 別名インポート - as
from testmod_izm04 import TestClass as tc
tc = TestClass()
tc.test_method("サン〇リア！")