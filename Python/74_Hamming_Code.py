# Hamming Code
def hngCode74(bit):
    # data length is 4, hcode length is 3
    bit = list(str(bit))
    if bit[0]=='0': bit=['0' for _ in range(4)]
    if len(bit)!=4: return print('Input Wroing!')
    # insert p1 bit
    if int(bit[0])^int(bit[1])^int(bit[3])!=0: bit.insert(0, '1')
    else: bit.insert(0, '0')
    # insert p2 bit
    if int(bit[0])^int(bit[1])^int(bit[2])!=0: bit.insert(1, '1')
    else: bit.insert(1, '0')
    # insert p3 bit
    if int(bit[1])^int(bit[2])^int(bit[3])!=0: bit.append('1')
    else: bit.append('0')
    return bit

res=hngCode74(1010)
print('Result of hammingCode is ', end='')
for i in res: print(i, end='')
print('\n')

res2=hngCode74(1111)
print('Result of hammingCode is ', end='')
for j in res2: print(j, end='')
print('\n')

res3=hngCode74(0000)
print('Result of hammingCode is ', end='')
for k in res3: print(k, end='')
print('\n')

res4=hngCode74(11111)