#dummy variables

count = 0
dummy = 0
s = ('DDUUUUDD')
i = 0
mtList = []

'''
#looping

while i < len(s)-2:
  dummy = 0
  if s[i] == 'D'  and s[i+1] == 'D':
    while i < len(s)-2 and s[i+1] == 'D':
      dummy += 1
      i += 1
  if dummy>0 and i != len(s)-1:
    mtList.append(1)
    i = i + (dummy)
  else:
    i += 1
  print(i)
len(mtList)    
'''

while i < len(s)-2:
  print(i) 
  if s[i]=='D' and s[i+1] == 'D':
     dummy = 0
     while s[i] != 'U':
       i += 1
       dummy += 1
     if s[i+1] != 'D' and i < len(s)-1:
       mtList.append(1)
       i = dummy+i
   






    
      
    
