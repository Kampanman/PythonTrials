# 日付の取得

import datetime #日付取得のためにはこれが必要

today = datetime.date.today()
todaydetail = datetime.datetime.today()

print("==========")
# 今日の日付
print(today)
print(todaydetail)

print("==========")
# 今日の日付のそれぞれの値
print(today.year)
print(today.month)
print(today.day)
# 「todaydetail.year～second」合わせてみると・・・
year = str(todaydetail.year)
month = str(todaydetail.month)
day = str(todaydetail.day)
hour = str(todaydetail.hour)
minute = str(todaydetail.minute)
second = str(todaydetail.second)

print(year+"/"+month+"/"+day+" "+hour+":"+minute+":"+second)
print("==========")
# 関数を使えば以下のようにできる
def get_today():
  today = today = datetime.date.today()
  value = (today.year, today.month, today.day)

  return value

getIt = get_today()
print(getIt)
print(getIt[0]) #year
print(getIt[1]) #month
print(getIt[2]) #day

print("==========")
# 日付の計算
print(today + datetime.timedelta(days=1)) # 明日の日付

# 特定の日付からの計算
newyear = datetime.datetime(2020, 1, 1)
# 一週間後
print(newyear + datetime.timedelta(days=7)) # 2020-1-1から7日後