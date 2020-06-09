#dummy variables
s = ('UDDDUDUU')
count  = 0
mtList = []
valley = []
sumVal = 0
len(s)
#algorithm

for i in range(len(s)):
  if s[i] == 'U':
    mtList.append(1)
  else:
    mtList.append(-1)
i=0  


while i < len(s):
  sumVal = sumVal + mtList[i]
  count += 1
  if sumVal == 0:
    print('i',i)
    print('mtListVal', mtList[i-(count-1)])
    if mtList[i-(count-1)] == -1:
      valley.append(1)
    count = 0
  i += 1
len(valley)
  