import pymysql

while True:
    conn=pymysql.connect(host='localhost', user='root', password='root', db='webhackTest', charset='utf8')
    curs=conn.cursor(pymysql.cursors.DictCursor)
    test=input('ID를 입력해주세요. >')
    with curs:
        sql ="select * from users where id=%s"
        curs.execute(sql, test)
        rows = curs.fetchall()
        for row in rows:
            print(row)


