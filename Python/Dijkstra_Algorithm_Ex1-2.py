#딕스트라 알고리즘 구현
num=6
INF=1000000000 #직접경로가 아닌 노드사이의 거리는 무한대로 표현, 10억

a=[
    [0, 5, INF, 6, 3, INF],
    [5, 0, 3, INF, INF, INF],
    [INF, 3, 0, INF, 2, INF],
    [6, INF, INF, 0, 7, 2],
    [3, INF, 2, 7, 0, 5],
    [INF, INF, INF, 2, 5, 0]
]

d=[0 for i in range(num)] #최종 거리를 출력하기 위함
v=['false' for i in range(num)] #방문했던 노드를 표시함

def getMinNode(): #가장 가까이 있는 노드를 찾음
    min=INF
    index=0
    for i in range(num):
        if(d[i]<min and v[i]=='false'): 
            min=d[i]
            index=i
    return index

def dijkstra(s):
    for i in range(num):
        d[i]=a[s][i] #시작점으로부터 모든 경로를 담아줌
    v[s]='true' #자기 자신은 방문했던 노드로 표시
    for i in range(num-2):
        c=getMinNode() #가까운 노드 탐색
        v[c]='true' #방문했던 노드로 표시함
        for j in range(num):
            if(v[j]=='false'): #방문했던 노드가 아니라면
                if(d[c]+a[c][j] < d[j]): #거쳐간 경로가 거치지 않은 경로보다 작다면
                    d[j]=d[c]+a[c][j] #그 값으로 갱신해준다!
sel=4
dijkstra(sel)

for i in range(num):
    print("[", str(sel+1), "]번째 노드에서 [", str(i+1), "]번 노드까지의 최단거리는 : ", str(d[i]))
