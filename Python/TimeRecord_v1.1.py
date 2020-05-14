import time

def recordToText(line):
    try:
        f=open('TimeRecord.txt', 'at')
        try:
            f.write(line+"\n")
            print("(+) 기록에 성공하였습니다. {}".format(line))
            f.close()
        except:
            print("(+) 기록에 실패하였습니다.. {}".format(line))
            print("(!) 오류로 인해 프로그램을 종료합니다.")
            exit()
            f.close()
    except FileNotFoundError:
        print("(!) 기록 파일을 찾을 수 없습니다.")
        print("(!) 오류로 인해 프로그램을 종료합니다.")
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
        line="----- {}년 {}월 {}일".format(currentTime.tm_year, currentTime.tm_mon, currentTime.tm_mday-1)
    else: line="----- {}년 {}월 {}일".format(currentTime.tm_year, currentTime.tm_mon, currentTime.tm_mday)

    dayOfWeek=getDayOfWeek(currentTime.tm_wday)
    line+=" {} -----".format(dayOfWeek)
    recordToText(line)

def recordStart():
    startTime = time.localtime(time.time())
    startTime_c= time.time()
    print("(+) [ {} : {} ] 시작!".format(startTime.tm_hour, startTime.tm_min))
    line="[ 시작시간 = {} : {}, ".format(startTime.tm_hour, startTime.tm_min)
    print("(+) 중지를 위해 'p'를 입력하거나 종료를 위해 'q'를 입력해주세요.")
    pauseSec=0
    totalSec=0
    perTenMin = "0"

    while True:
        chk=input()
        if (chk.lower()=='p'):
            pauseStartTime=time.localtime(time.time())
            pauseStartTime_c=time.time()
            print("(+) [ {} : {} ] 중지 시작.".format(pauseStartTime.tm_hour, pauseStartTime.tm_min))
            print("(+) 다시 시작을 위해 'r'을 입력해주세요.")
            chk=input()
            if (chk.lower()=='r'):
                pauseStopTime = time.localtime(time.time())
                pauseStopTime_c=time.time()
                pauseSec+=int(pauseStopTime_c-pauseStartTime_c)
                print("(+) [ {} : {} ] 다시 시작.".format(pauseStopTime.tm_hour, pauseStopTime.tm_min))
                print("(+) 중지를 위해 'p'를 입력하거나 종료를 위해 'q'를 입력해주세요.")
        elif(chk.lower()=='q'):
            stopTime = time.localtime(time.time())
            stopTime_c = time.time()
            print("(+) [ {} : {} ] 종료.".format(stopTime.tm_hour, stopTime.tm_min))
            print("(+) 결과시간을 기록하시겠습니까? (y/n) >", end='')
            chk_r=input()

            if(chk_r.lower=='y'):
                totalSec = int(stopTime_c - startTime_c)
            elif(chk_r.lower=='n'):
                totalSec = 0

            break
        else:
            print("(!) 잘못된 명령어입니다.")

        checkTime=time.localtime(time.time())
        checkTime_c=time.time()

    line+="종료시간 = {} : {}, 총 지난시간 = {}, 중지시간 = {}, 결과시간 = {}, ".format(stopTime.tm_hour, stopTime.tm_min, int(totalSec/60), int(pauseSec/60), int(totalSec/60)-int(pauseSec/60))
    if(pauseSec>0):
        line+="중지 시작시간 = {} : {}, 중지 종료시간 = {} : {}, ".format(pauseStartTime.tm_hour, pauseStartTime.tm_min, pauseStopTime.tm_hour, pauseStopTime.tm_min)
    print("(+) 내용을 입력해주세요. > ", end=' ')
    contentLabel="내용 = "
    content=input()
    line+=contentLabel+content+" ]"
    recordToText(line)

def lookup():
    try:
        r=open('TimeRecord.txt', 'rt')
        print(r.read())
    except FileNotFoundError:
        print("(!) 기록파일을 찾을 수 없습니다.")
        print("(!) 오류로 인해 프로그램을 종료합니다.")
        exit()

if __name__=="__main__":
    print("(+) TimeRecord 프로그램이 시작되었습니다.")

    while True:
        #menu
        menuLine="""
(+) 아래 보기 메뉴 중 선택해주세요.
(1) 날짜 기입
(2) 시간 기록 시작
(3) 기록 조회
(4) 프로그램 종료
>"""
        print(menuLine, end='')
        selected=input()

        if selected=='1': firstLineToday()
        elif selected=='2': recordStart()
        elif selected=='3': lookup()
        elif selected=='4':
            print("(+) 정말 프로그램을 종료하시겠습니까? (y/n) > ", end=' ')
            check=input();
            if(check.lower()=='y' or check.lower()=='yes'): exit()
        else: print("\n(!) 잘못된 선택입니다.")