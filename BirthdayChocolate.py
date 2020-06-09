#gifting portion of the cholote bar to friend
#constraint one: continuos pieces should be broken
#constraint two: numbers on the pieces should add up to birthday
#constraint three: number of segments should equal the birth month.




# alternate cleared 4/12 test cases
#running forward in the loop
# but starting somewhere in the left of the array the elements in the front can also be added like a closed loop to bring about the sum and the count?!

#elements=[4 ,1 ,4 ,3 ,3 ,5 ,1 ,2 ,4 ,2 ,5 ,1 ,5 ,1 ,4 ,1 ,3 ,1 ,5 ,2 ,2 ,2 ,1 ,1 ,3 ,2 ,5 ,3 ,1 ,5 ,4 ,5 ,2 ,2 ,1 ,1 ,2, 2 ,4 ,5 ,4 ,1 ,5 ,2 ,1 ,1 ,2 ,2 ,1 ,3 ,2 ,4 ,4 ,1 ,3 ,2 ,2 ,3 ,1 ,5 ,4 ,4 ,1 ,4 ,2 ,1 ,2 ,1 ,5 ,1 ,3 ,3 ,4 ,2 ,1 ,5 ,5 ,4 ,2 ,2 ,3 ,3 ,4 ,3 ,1 ,2 ,1 ,2 ,4 ,3]
elements=[2 ,5 ,1 ,3 ,4 ,4 ,3 ,5 ,1 ,1 ,2 ,1 ,4 ,1 ,3 ,3 ,4 ,2 ,1]
birth_day=18
birth_month=7
count=0
combo=0
sumVal=0 
len(elements)
if len(elements)==1:
  count=count+1
  sumVal=sumVal+elements[0]
  if sumVal==birth_day:
    if count==birth_month:
      combo=combo+1
else:
  for i in range(0, len(elements)-1):
    sumVal=0
    count=0
    for j in range(i,len(elements)-1):
      sumVal=sumVal+elements[j]
      count=count+1
      if sumVal==birth_day: 
        if count==birth_month:
          print(sumVal,count)
          combo=combo+1
        else:
          continue
      else:
        continue


#from the internet
count=0
m=birth_month
d=birth_day
length=len(elements)
for i in range(0,length):
  total=sum(elements[i:m+i])
  print(elements[i:i+m])
  if total==birth_day:
    count=count+1
    
count
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  