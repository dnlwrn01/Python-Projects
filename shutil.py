
import os
import time
import shutil
import datetime


# Path to the file/directory
path =  '/Users/dnlwr/Desktop/filesA/'
destination =  '/Users/dnlwr/Desktop/filesB/'
files = os.listdir(path)

HourDateTime = datetime.datetime.now() - datetime.timedelta(hours = 24)
print(HourDateTime)

for i in files:
    # Both the variables would contain time 
    # elapsed since EPOCH in float
    ti_c = os.path.getctime(path)
    ti_m = os.path.getmtime(path)

    # Converting the time in seconds to a timestamp
    c_ti = time.ctime(ti_c)
    m_ti = time.ctime(ti_m)

    if c_ti < HourDateTime or m_ti < HourDateTime:
        shutil.move(path+i, destination)
        


    
