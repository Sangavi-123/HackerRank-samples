
a=[3,9,6]
b=[36,72]

'''a=[100,99,98,97,96,95,94,93,92,91]
b=[1,2,3,4,5,6,7,8,9,10]
'''
arr1=a
arr2=b
arr1Len=len(arr1)
arr2Len=len(arr2)

list1=[]
list2=[]
count=0


#choosing the range of values in between
minVal=max(arr1)
maxVal=min(arr2)
  
checkBetween=list(range(minVal,maxVal+1))

arr=arr1+arr2
list2=[]
for i in checkBetween:
  list1=[]
  for j in arr:
    if i>=j :
      if i%j==0:
        list1.append(0)
    else:
      if j%i==0 :
        list1.append(0)
  if len(arr)==len(list1):
    count=count+1
    list2.append(i)
count
list2












