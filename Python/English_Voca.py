import pymysql

conn=pymysql.connect(host='localhost', user='root', password='root', db='en_voca', charset='utf8')

def save(conn, n):
    curs = conn.cursor(pymysql.cursors.DictCursor)
    n=int(n)
    for i in range(0, n):
        eng=input("Enter voca : ")
        kor=input("voca's mean : ")
        kor=kor.strip()
        count=0
        sql="insert into word(eng, kor, inc_count) values(%s, %s, %s)"
        curs.execute(sql, (eng, kor, count))
        conn.commit()
    return print("Save success.\n")

def slve(conn, n):
    n=int(n)
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql=f"select * from word order by rand() limit {n}"
    curs.execute(sql)
    rows=curs.fetchall()
    for row in rows:
        anw=input(f"{row['eng']} : ")
        anwqmrk=anw
        anw=anw.replace('?','')
        tem=row['kor']
        cmp=tem.replace(' ','')
        if cmp.find(anw.replace(' ',''))!=-1:
            print('You correct :)\n')
            if anwqmrk.find('?')!=-1:
                print(f'Exactly answer is {tem}\n')
        else :
            print("Incorrect :(\n")
            print(f"Right answer is {row['eng']} - {row['kor']}\n")
            count=int(row['inc_count'])+1
            sql=f"update word set inc_count={int(count)} where eng='{row['eng']}'"
            curs.execute(sql)
            conn.commit()

def erse(conn, n):
    n=int(n)
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql=f"select * from word order by inc_count desc limit {n}"
    curs.execute(sql)
    rows=curs.fetchall()
    for row in rows:
        anw=input(f"{row['eng']} : ")
        anwqmrk=anw
        anw=anw.replace('?','')
        tem=row['kor']
        cmp=tem.replace(' ','')
        if cmp.find(anw.replace(' ',''))!=-1 :
            print('You correct :)\n')
            if anwqmrk.find('?')!=-1:
                print(f'Exactly answer is {tem}\n')
        else :
            print("Incorrect :(\n")
            print(f"Right answer is {row['eng']} - {row['kor']}\n")
            count=int(row['inc_count'])+1
            sql=f"update word set inc_count={int(count)} where eng='{row['eng']}'"
            curs.execute(sql)
            conn.commit()

def inputN():
    num=input('Hou many repeat? : ')
    return num

def lkall(conn):
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql='select * from word'
    curs.execute(sql)
    rows=curs.fetchall()
    for row in rows:
        print(f"[ {row['inc_count']} ] [ {row['eng']} - {row['kor']} ]")
    print('\n')

def CrntT(conn):
    curs=conn.cursor(pymysql.cursors.DictCursor)
    sql='select count(eng) from word'
    curs.execute(sql)
    rows=curs.fetchall()
    for row in rows:
        string=(f"There are [{row['count(eng)']}]words.")
    return string

def  Btinc(conn, n):
    curs=conn.cursor(pymysql.cursors.DictCursor)
    sql=f"select * from word order by inc_count desc limit {n}"
    curs.execute(sql)
    rows=curs.fetchall()
    for row in rows:
        anw=input(f"{row['eng']} : ")
        anwqmrk=anw
        anw=anw.replace('?','')
        tem=row['kor']
        cmp=tem.replace(' ','')
        if cmp.find(anw.replace(' ',''))!=-1 :
            print('You correct :)\n')
            if anwqmrk.find('?')!=-1:
                print(f'Exactly answer is {tem}\n')
            if int(row['inc_count'])!=0:
                count = int(row['inc_count']) - 1
                sql = f"update word set inc_count={int(count)} where eng='{row['eng']}'"
                curs.execute(sql)
                conn.commit()
        else :
            print("Incorrect :(\n")
            print(f"Right answer is {row['eng']} - {row['kor']}\n")
            count=int(row['inc_count'])+1
            sql=f"update word set inc_count={int(count)} where eng='{row['eng']}'"
            curs.execute(sql)
            conn.commit()

print('- - - [English Dictionary] made by wonjae to private - - -')
print(CrntT(conn))
while True:
    print('Choose number.\n(1)Save word\n(2)Solve what is in korean\n'
          '(3)Solve error sequence \n(4)Lookup all\n(5)Abate Incorrect count\n(6)Quit\n>', end='')
    num=input(' ')
    if int(num)==1:
        n=inputN()
        save(conn, n)
    elif int(num)==2:
        n=inputN()
        slve(conn, n)
    elif int(num)==3:
        n=inputN()
        erse(conn, n)
    elif int(num)==4:
        lkall(conn)
    elif int(num)==5:
        n=inputN()
        Btinc(conn, n)
    elif int(num)==6:
        quit()
    else :
        print('Wrong number!')