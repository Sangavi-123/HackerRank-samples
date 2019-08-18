grades=[73]
newGrades=[]

#for loop for each element in the list
#_____________________________________
 
for i in range(0,len(grades)):
	#if the incoming grade falls between 38 and 100, 38 included
	#____________________________________________________________
	if ((grades[i]>=38) & (grades[i]<100)):
		#rounding to next multiple of 5
		#______________________________
		lastDigit=grades[i]%10
		if lastDigit<5:
			fromFive=lastDigit-5
			newGrade=grades[i]+abs(fromFive)
			#diff less than 3
			#________________
			if (newGrade-grades[i])<3:
				newGrades.append(newGrade)
			else:
				newGrades.append(grades[i])
		else:
			fromTen=lastDigit-10
			newGrade=grades[i]+abs(fromTen)
			#diff less than 3
			#________________
			if (newGrade-grades[i])<3:
				newGrades.append(newGrade)
			else:
				newGrades.append(grades[i])
	#if the number is less than 38
	#_____________________________
	else:
		newGrades.append(grades[i])
newGrades		
		
		
		
		
		 
				
	