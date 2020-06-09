# breaking records
scores=[3 ,4 ,21 ,36 ,10 ,28 ,35 ,5 ,24 ,42]
length=len(scores)


#step 1 : set the first scores as max and min
score_max=scores[0]
score_min=scores[0]

#step 2: compare each element in the list with max and min
max_index=[]
min_index=[]


for i in scores:
  if i>score_max:
    max_index.append(0)
    score_max=i
  elif i == score_max:
    continue
  elif i<score_min:
    score_min=i
    min_index.append(1)
    print(i)
  else:
    continue
  
len(max_index)
len(min_index)
