# リスト型

scores = [60,70,80]
"""
print(scores[0]) #60
scores[0] = 65
print(len(scores)) #2
scores.append(100)
print(scores)
"""

for score in scores:
  print(str(score)+"点") # 60,70,80

for i, score in enumerate(scores):
  print("{0}番: {1}点".format(str(i+1), str(score)))