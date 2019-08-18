#program to print the time in 24 hours format given a time in 12 hours format
#____________________________________________________________________________
#imports
#-------
import datetime
from datetime import datetime
from datetime import timedelta
from datetime import time
import time
import re




#parse the time object into the time format you want using strptime object
#_________________________________________________________________________
obj=input()
o=time.strptime(obj,"%H:%M:%S")
datetime.strftime(o,"%I")
hour=o.tm_hour
mini=o.tm_min
sec=o.tm_sec
print(hour,":",mini,":",sec)

#checking for AM and PM
#______________________
s=input()
s=list(s)
l=len(s)
s[0:2]=str(int(s[0])+12)
n=''.join(s)
type(s)
l=len(s)
if s[l-1]=='P':
    s[0:2]=str(int(s)+12)


