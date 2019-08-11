# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 19:03:06 2019

@author: sangavi
"""

#

import datetime
from datetime import datetime
from datetime import timedelta
from datetime import time
d=time(13,3,45)
obj=input()
import time
o=time.strptime(obj,"%H:%M:%S")
hour=o.tm_hour
mini=o.tm_min
sec=o.tm_sec
print(hour,":",mini,":",sec)