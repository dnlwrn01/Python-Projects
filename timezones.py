from datetime import datetime
import pytz

##NEW YORK Current Time
tzNYC = pytz.timezone('America/New_York')
timeNYC = datetime.now(tzNYC)
#format NYC time
nHour = timeNYC.strftime("%H")
nMin = timeNYC.strftime("%M")
nPeriod = timeNYC.strftime("%p")

##PORTLAND Current Time
tzPORT = pytz.timezone('Etc/GMT+7')
timePORT = datetime.now(tzPORT)
#format NYC time
pHour = timePORT.strftime("%H")
pMin = timePORT.strftime("%M")
pPeriod = timePORT.strftime("%p")

##LONDON Current Time
tzLOND = pytz.timezone('Europe/London')
timeLOND = datetime.now(tzLOND)
#format NYC time
lHour = timeLOND.strftime("%H")
lMin = timeLOND.strftime("%M")
lPeriod = timeLOND.strftime("%p")

if int(pHour) > 9 and int(pHour) < 17:
    print("The time is {} : {} {}. Our Portland location is OPEN.".format(pHour, pMin, pPeriod))
else:
    print("Our Portland location is currently CLOSED.")
    
if int(lHour) > 9 and int(lHour) < 17:
    print("The time is {} : {} {}. Our London location is OPEN.".format(lHour, lMin, lPeriod))
else:
    print("Our London location is currently CLOSED.")
    
if int(nHour) > 9 and int(nHour) < 17:
    print("The time is {} : {} {}. Our New York location is OPEN.".format(nHour, nMin, nPeriod))
else:
    print("Our New York location is currently CLOSED.")
    





