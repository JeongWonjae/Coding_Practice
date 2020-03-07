import time

def recordToText(line):
    try:
        f=open('TimeRecord.txt', 'at')
        try:
            f.write(line+"\n")
            print("(+) Recording success line is {}".format(line))
            f.close()
        except:
            print("(+) Recording fail line is {}".format(line))
            print("(!) Quit program by occurred error.")
            exit()
            f.close()
    except FileNotFoundError:
        print("(!) Text File is not exist.")
        print("(!) Quit program by occurred error.")
        exit()

def getDayOfWeek(tm_wday):
    if tm_wday==0: return '월요일'
    elif tm_wday==1: return '화요일'
    elif tm_wday == 2: return '수요일'
    elif tm_wday == 3: return '목요일'
    elif tm_wday == 4: return '금요일'
    elif tm_wday == 5: return '토요일'
    else: return '일요일'

def firstLineToday():
    currentTime = time.localtime(time.time())
    if(currentTime.tm_hour>0 and currentTime.tm_hour<5):
        line="{}년 {}월 {}일".format(currentTime.tm_year, currentTime.tm_mon, currentTime.tm_mday-1)
    else: line="{}년 {}월 {}일".format(currentTime.tm_year, currentTime.tm_mon, currentTime.tm_mday)

    dayOfWeek=getDayOfWeek(currentTime.tm_wday)
    line+=" {}".format(dayOfWeek)
    recordToText(line)

def recordStart():
    startTime = time.localtime(time.time())
    startTime_c= time.time()
    print("(+) [ {} : {} ] Start!".format(startTime.tm_hour, startTime.tm_min))
    line="{} : {} ~".format(startTime.tm_hour, startTime.tm_min)
    print("(+) Enter 'p' if you want pause. Or Enter 'q' if you want quit recording.")
    pauseSec=0
    totalSec=0
    perTenMin = "0"

    while True:
        chk=input()
        if (chk.lower()=='p'):
            pauseStartTime=time.localtime(time.time())
            pauseStartTime_c=time.time()
            print("(+) [ {} : {} ] Paused recording.".format(pauseStartTime.tm_hour, pauseStartTime.tm_min))
            print("(+) Enter 'r' if you want re-start.")
            chk=input()
            if (chk.lower()=='r'):
                pauseStopTime = time.localtime(time.time())
                pauseStopTime_c=time.time()
                pauseSec+=int(pauseStopTime_c-pauseStartTime_c)
                print("(+) [ {} : {} ] Re-start recording.".format(pauseStopTime.tm_hour, pauseStopTime.tm_min))
                print("(+) Enter 'p' if you want pause. Or Enter 'q' if you want quit recording.")
        elif(chk.lower()=='q'):
            stopTime = time.localtime(time.time())
            stopTime_c=time.time()
            print("(+) [ {} : {} ] Stop. Well done!".format(stopTime.tm_hour, stopTime.tm_min))
            totalSec=int(stopTime_c-startTime_c)
            break
        else:
            print("(!) Wrong command.")

        checkTime=time.localtime(time.time())
        checkTime_c=time.time()

        if(int(checkTime_c-startTime_c)/600==0):
            perTenMin=str(int(perTenMin)+1)
            print("(+) [ {} : {} ] Passed {}0 minutes. Great!".format(checkTime.tm_hour, checkTime.tm_min, perTenMin))


    line+=" {} : {} <{}-{}={}> ".format(stopTime.tm_hour, stopTime.tm_min, int(totalSec/60), int(pauseSec/60), int(totalSec/60)-int(pauseSec/60))
    print("(+) Enter content what do you doing at this time > ", end=' ')
    content=input()
    line+=content
    recordToText(line)

def lookup():
    try:
        r=open('TimeRecord.txt', 'rt')
        print(r.read())
    except FileNotFoundError:
        print("(!) Text File is not exist.")
        print("(!) Quit program by occurred error.")
        exit()

if __name__=="__main__":
    print("(+) TimeRecord.py started")

    while True:
        #menu
        menuLine="""
(+) Select number from below.
(1) First open this program today.
(2) Time recording start.
(3) Lookup text file.
(4) Program exit.
>"""
        print(menuLine, end='')
        selected=input()

        if selected=='1': firstLineToday()
        elif selected=='2': recordStart()
        elif selected=='3': lookup()
        elif selected=='4':
            print("(+) Do you want quit? (y/n) > ", end=' ')
            check=input();
            if(check.lower()=='y' or check.lower()=='yes'): exit()
        else: print("\n(!) Wrong selection.")
