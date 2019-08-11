"""
Created on Thu Aug  8 18:44:08 2019

@author: sangavi
"""



#program is to pass an array and find the min and max values of the sume of exactly (n-1) integers
#-------------------------------------------------------------------------------------------------
#also remember to remove the indentation warning by replacing tab spaces with spacebar
#-------------------------------------------------------------------------------------
#function definition
#-------------------
def miniMaxSum(arr):
    l=len(arr)
    #optional to sort the array
	#--------------------------
	arr.sort()
    #creating empty variables to use them later
	#------------------------------------------
	sum1=0
    list1=[]
    #loop to pop each element of the array
	#every time the loop iterate only the element in index zero is popped and stored
	#-------------------------------------------------------------------------------
	for i in range(0,l):
        pop=arr.pop(0)
        #second for loop to calculate the sum of every (n-1) list's elements
		#-------------------------------------------------------------------
		for j in range(0,l-1):
            sum1=sum1+arr[j]
        list1.append(sum1)
        #add the popped element. this function appends anything to the last of the list
		#------------------------------------------------------------------------------
		arr.append(pop)
        #initialise sum1 variable with the value zero to avoid mis calucation
		#--------------------------------------------------------------------
		sum1=0
    #find the minimum and maximum values in the list and pass them
	#-------------------------------------------------------------
	minVal=min(list1)
    maxVal=max(list1)
    return [minVal,maxVal]
arr=[120,0,71]
out=miniMaxSum(arr)	
