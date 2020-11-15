# 例外処理

class MyException(Exception):
  pass

def div(a,b):
  try:
    if(b<0):
      raise MyException("Don't put minus")
    print(a/b)
  except ZeroDivisionError:
    print("Not by zero!")
  except MyException as e:
    print(e)
  else:
    print("Ohh...")
  finally:
    print("-- end --")

div(10,0)