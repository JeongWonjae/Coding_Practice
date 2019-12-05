import datetime
import pymysql

class direct:
    def time_entry(self):
        time_arr=input("Entry time range. (spilt ~) : ").split("~")
        time_spent=input("Entry spent time to min : ")
        time_spent=time_spent.strip()
        content=input("Content : ")
        if int(time_spent) >=60 :
            time_spent_hour = int(time_spent)/60
            time_spent_min = int(time_spent)%60
            time_spent_hour = f"0{int(time_spent_hour)}"
        else:
            time_spent_hour = "00"
            time_spent_min=time_spent
        if len(str(time_spent_min))==1: time_spent_min=f"0{time_spent_min}"
        time_spent=f"{time_spent_hour} : {time_spent_min}"
        start_time=time_arr[0].strip()
        end_time=time_arr[1].strip()
        string=f" values('{start_time[0:2]} : {start_time[2:4]}','{end_time[0:2]} : {end_time[2:4]}','{time_spent}','{content}')"
        return string

    def date_entry(self):
        date_arr=input("Entry date that you want. (spilt /): ").split("/")
        string=f"insert into date_{date_arr[0].strip()}{date_arr[1].strip()}{date_arr[2].strip()}"
        return string

    def sql(self, string, curs):
        curs.execute(string)

def time():
    timeAry=[]
    s=datetime.datetime.now()
    timeAry.append(s.year)
    timeAry.append(s.month)
    timeAry.append(s.day)
    timeAry.append(s.hour)
    timeAry.append(s.minute)
    timeAry.append(s.second)
    return timeAry

def timeClclt(s, e):
    stcHour=int(s[3])*60
    stcMin=int(s[4])
    etcHour=int(e[3])*60
    etcMin=int(e[4])
    sC=stcHour+stcMin
    eC=etcHour+etcMin
    fctToMin=eC-sC
    fcHour=int(fctToMin/60)
    fcMin=int(fctToMin%60)
    if s[2]!=e[2]:
        fcMin=int(etcMin)+((24*60-sC)%60)
        fcHour=int((24*60-sC)/60)
        if int(fcMin)>=60:
            fcHour=int(fcHour)+int(fcMin)/60
            fcMin=int(fcMin)%60

    time=[]
    time.append(fcHour)
    time.append(fcMin)
    return time

def dbSyn():
    conn=pymysql.connect(host='localhost', user='root', password='root', db='timing', charset='utf8')
    return conn

def enterDate():
    date = []
    print('Input date on which you want lookup.')
    y = input('year : ')
    m = input('month : ')
    d = input('day : ')
    date.append(y)
    date.append(m)
    date.append(d)
    return date

def mktdTable(curs):
    dateis=datetime.datetime.now()
    dateisAry=[]
    dateisAry.append(dateis.year)
    dateisAry.append(dateis.month)
    dateisAry.append(dateis.day)
    if len(str(dateisAry[1]))==1:
        dateisAry[1]=f'0{dateisAry[1]}'
    if len(str(dateisAry[2])) == 1:
        dateisAry[2] = f'0{dateisAry[2]}'
    sql=f'create table date_{dateisAry[0]}{dateisAry[1]}{dateisAry[2]}(startTime varchar(20),' \
        f'endTime varchar(20),Time varchar(20),Content varchar(50))'
    curs.execute(sql)

def instTable(curs, res, stime, etime):
    ctn = input('Input content of this time : ')
    for element in range(0, len(stime)):
        if len(str(stime[element]))==1: stime[element]=f"0{stime[element]}"
    for element in range(0, len(etime)):
        if len(str(etime[element])) == 1: etime[element] = f"0{etime[element]}"
    for element in range(0, len(res)):
        if len(str(res[element]))==1: res[element]=f"0{res[element]}"

    stimeSyntax=f'{stime[3]} : {stime[4]}'
    etimeSyntax=f'{etime[3]} : {etime[4]}'
    resSyntax=f'{res[0]} : {res[1]}'
    if int(res[1])==0 and int(res[0])==0:
        print("Time is null. Don't apply.")
        return
    if int(res[1])<10 and int(res[0])==0:
        print("Time is lack. Don't apply.")
        return
    #for dawn
    if int(stime[3])<=3:
        stime[2]=int(stime[2])-1
        stime[2]=f'0{stime[2]}'
    sql=f"insert into date_{stime[0]}{stime[1]}{stime[2]} values('{stimeSyntax}', '{etimeSyntax}', '{resSyntax}', '{ctn}')"
    curs.execute(sql)
    print('Time applied.\n')

def lookupTable(curs, date):
    if len(date[1])==1: date[1]=f'0{date[1]}'
    if len(date[2])==1: date[2]=f'0{date[2]}'
    try:
        sql=f'select * from date_{date[0]}{date[1]}{date[2]}'
        curs.execute(sql)
        rows=curs.fetchall()
        for row in rows:
            print(f"[ {row['startTime']} ~ {row['endTime']} ] = {row['Time']}  {row['Content']}")
    except pymysql.err.ProgrammingError:
        print("Table doesn't exist")
    print('\n')


def sumDateTime(curs, date):
    if len(date[1])==1: date[1]=f'0{date[1]}'
    if len(date[2])==1: date[2]=f'0{date[2]}'
    try:
        sql=f'select Time from date_{date[0]}{date[1]}{date[2]}'
        curs.execute(sql)
        rows=curs.fetchall()
        sumArrayHour=[]
        sumArrayMin=[]
        for row in rows:
            temp=row['Time'].split(':')
            sumArrayHour.append(int(temp[0]))
            sumArrayMin.append(int(temp[1]))
        total=(sum(sumArrayHour)*60)+sum(sumArrayMin)
        print(f'{date[0]}. {date[1]}. {date[2]}. recorded time is ({total})')
    except pymysql.err.ProgrammingError:
        print("Table doesn't exist")
    print('\n')

''''''

#InterlinkDatabase
conn=dbSyn()
curs=conn.cursor(pymysql.cursors.DictCursor)
#from here is program main
#make table auto
try:
    mktdTable(curs)
    print('Make today table.\n')
    print('[ Check your study time ]')
except pymysql.err.InternalError:
    print('[ Check your study time ]')

while True:
    print('<Select number>\n[1].Time Start & End\n[2].Lookup Table\n[3].Lookup Sum Time\n[4].Direct Entry\n[5].Quit\n>', end='')
    sel=input()
    if sel=='1': #timestart
        stime = time()
        print(f'[Start time is {stime[0]}-{stime[1]}-{stime[2]} {stime[3]}:{stime[4]}:{stime[5]}]\n'
              f'If you want stop the time, input any key.')
        stopEnter=input()
        etime = time()
        print(f'[End time is {etime[0]}-{etime[1]}-{etime[2]} {etime[3]}:{etime[4]}:{etime[5]}]',)
        # studiedTime
        res = timeClclt(stime, etime)
        print(f'Study Time is {res[0]}hours {res[1]}minutes\n')
        instTable(curs, res, stime, etime)
        conn.commit()
    elif sel=='2':
        date=enterDate()
        lookupTable(curs, date)
    elif sel=='3':
        date=enterDate()
        sumDateTime(curs, date)
    elif sel=='4':
        d=direct()
        front_string=d.date_entry()
        while True:
            back_string=d.time_entry()
            string=front_string+back_string
            d.sql(string, curs)
            q=input("add? Enter but N is quit\n")
            conn.commit()
            if q=="N" or q=="n" or q=="ㅜ" or q=="ㅜㅜ":
                break;
    elif sel=='5':
        print('Bye.')
        break
    else: print('Wrong Select. Do it again :)\n')
