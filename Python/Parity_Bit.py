#Odd parity
def prtBit(bit):
    bit=list(str(bit))
    count=0
    if len(bit)!=7:
        print('Input Wrong!')
        return
    for j in bit:
        if j=='1': count=count+1
    if count%2==0: bit.append('1')
    elif count%2==1: bit.append('0')
    return bit

res=prtBit(1001101)
print('Result of odd parity is ' ,end='')
for n in res: print(n, end='')