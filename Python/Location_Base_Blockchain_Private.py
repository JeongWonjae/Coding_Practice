import hashlib
import datetime as dt
import pymysql

#SYN Mysql
def db_Syn():
    conn=pymysql.connect(host='localhost', user='root', password='root', db='auto_test', charset='utf8')
    return conn
conn = db_Syn()
curs=conn.cursor(pymysql.cursors.DictCursor)

#Regist Mysql
def db_add_block(conn, curs, blockarr):
    sql=f"insert into block values({blockarr[0]},'{blockarr[1]}','{blockarr[2]}','{blockarr[3]}','{blockarr[4]}',{blockarr[5]},{blockarr[6]})"
    curs.execute(sql)
    conn.commit()

#Block Object
class Block(object):
    def __init__(self, index, timestamp, data, previous_hash, latitude, longitude):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
        self.latitude = latitude
        self.longitude = longitude

    #block hash
    def hash_block(self):
        sha = hashlib.sha256()
        new_str_bin = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        sha.update(new_str_bin.encode())
        return sha.hexdigest()

#Make First block
def first_block():
    return Block(0, dt.datetime.now(), data='this is fisrt block', previous_hash="0", latitude='0.000000', longitude='0.000000')

#Make Next block
def next_block(last_block, data, la, lo):

    return Block(index = last_block.index+1,
                 timestamp = dt.datetime.now(),
                 data = f"{data} {last_block.index+1}",
                 previous_hash = last_block.hash,
                 latitude=la,
                 longitude=lo
                 )

def add_blockarr(block):
    blockarr=[]
    blockarr.append(block.index)
    blockarr.append(block.timestamp)
    blockarr.append(block.data)
    blockarr.append(block.previous_hash)
    blockarr.append(block.hash)
    blockarr.append(block.latitude)
    blockarr.append(block.longitude)
    return blockarr

#Blockchain
#Define previous block
blockchain_net = [first_block()]
p_block = blockchain_net[-1]

#main
while True:
    information=input("Entry the data/latitude/longitude\n>").split("/")
    newblock=next_block(p_block, information[0], information[1], information[2])
    blockchain_net.append(newblock)
    p_block=blockchain_net[-1]
    #for save Mysql
    blockarr=add_blockarr(p_block)
    db_add_block(conn, curs, blockarr)
    print(f"{p_block.data} location is {p_block.latitude} / {p_block.longitude}")
    print(f"Block {p_block.index} added to blockchain")
    print(f"hash value is {p_block.hash}")
    n=input("")
    if n=='exit':
        break;
    if n=='lookup':
        print(blockchain_net)
