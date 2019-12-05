#1번 알고리즘 - 잘못된 뺄셈

def algo(n, k):
    for _ in range(k):
        if(n%10!=0): n=n-1
        else: n=n/10
    return n

print(int(algo(512, 4)))
print(int(algo(1000000000, 9)))
