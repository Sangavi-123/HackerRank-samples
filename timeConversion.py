import math
import pandas as pd
import numpy as np
import datetime
from datetime import datetime
from datetime import time, timedelta

s=input()
s=datetime.strptime(s, '%I:%M:%S%p').strftime('%H:%M:%S')

#without datetime package
s=input()
last=s[-2:]
time=s[:-2]
if last== "PM":
    if s[0:2]=='12':
        print(time)
    else:
        new=str(int(s[0:2])+12)
        full=new+s[2:-2]
        print(full)
elif(s[0:2]<'12'):
    full=time
    print(full)
elif(s[0:2]>='12'):
    new='00'
    full=new+time[2:]
    print(full)
else:
    full='00:00:00'
    print(full)
    
    
#one line code instead of the above logic
    
import datetime
from datetime import date,time,timedelta,datetime
s=input()
s=datetime.strptime(s,"%I:%M:%S%p").strftime("%H:%M:%S")