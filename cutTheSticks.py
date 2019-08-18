#Library imports/dependencies
#____________________________
import pandas as pd
import numpy as np
import re


#code flow
#_________

#get array from user or default
#______________________________
arr=[1,2, 3, 4, 3, 3, 2, 1]
l=len(arr)

#looping logic
#_____________
while(l!=0):
    count=len(arr)
    print(count)
    mini=min(arr)
    #list comprehension method: employed here to find all occurrences of a minimum value in the  array
    #_________________________________________________________________________________________________
    list1=[i for i in arr if i!=mini]
    arr=list1
    #array to shorten the length of the sticks 
    #_________________________________________
    for i in range(0,len(list1)):
        list2=[]
        newLength=i-mini
        list2.append(newLength)#new list with shortened lengths
    l=len(arr) #for the while loop to be rational



#list comprehension (here, checks for multiple occurences of same element)
#______sample___________________________________________________________________
list1=[]
mini=2
list1=[i for i in arr if i!=mini]

