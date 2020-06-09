#imports
#_______
import datetime
from datetime import datetime
from datetime import date
from datetime import timedelta
import pandas as pd
import numpy as np

#samples
#_______
now=datetime.now()
now
type(now) #datetime.datetime  object

now.year #returns the year contained in the datetime object
now.minute #returns the minute component contained in the datetime object
now.month #returns the month contained in the datetime object

now1=datetime.now()
now2=datetime.now()
now3=datetime.now()

timeObjects=[now1,now2,now3]
years=np.zeros(len(timeObjects))


timeObjects[0].year

#printing the year componen
for i in timeObjects:
    print (i.year)

