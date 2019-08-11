'''	snippet to find the alternate diagnol of a nested list-matrix.
	doesnt use numpy
	numpy arrays have a built in function to return the primary diagnol 
	and the alternate diagnol of the numpy matrices.
	The concept is, alternate diagonal elements are in columns whose value reduce by one for each row.
'''

import math
#create an array or Get it inputted by the user
#----------------------------------------------
array1=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
l=len(array1[1])
#function definition to extract the alternate diagnol elements of the matrix
#----------------------------------------------------------------------------
def alt_diag(array1):
	alt_d=[]
	#length is reduced by one, because the maximum index in the nested list is 0 to 1-the max length
	#-----------------------------------------------------------------------------------------------
	l=len(array1[1])-1
	for i in range(0,4):
		for j in range(0,4):
			if j==l:
				alt_d.append(array1[i][j])
		l-=1
	return alt_d
#function call which passes the array
#------------------------------------
a_d=alt_diag(array1)




#code to find the diagnols of the matrix and the absolute difference between them
#---------------------------------------------------------------------------------
arr=[[1,2,3],[4,5,6],[7,8,9]]
n=3
def diag(arr):
    
    sum1=0
    sum2=0
    list1=[]
    list2=[]
    l=len(arr[1])-1
    for i in range(0,n):
        for j in range(0,n):
            if j==l:
                list2.append(arr[i][j])
        l-=1
    for i in range(0,n):
        for j in range(0,n):
            if i==j:
                list1.append(arr[i][j])
    #find the sum of elements in each diagnol 
	#----------------------------------------
    for i in range(0,len(list1)):
        sum1=sum1+list1[i]
        sum2=sum2+list2[i]
    #Absolute difference between the diagnols(sum of elements)
	#---------------------------------------------------------
    out=abs(sum1-sum2)
    return out
#function call with the array
#----------------------------
out=diag(arr)
