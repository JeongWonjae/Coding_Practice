# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup

def RunningMovie():
    
    titleAll=[]
    scoreAll=[]
    attachA=[]
    
    #URL 지정
    html=urlopen("https://movie.naver.com/movie/running/current.nhn")
    bs=BeautifulSoup(html, "html.parser")

    #경로로 찾아와서 배열에 저장
    for title in bs.select("div div div ul li div a img"):
        titleAll.append(title.get("alt"))
    for score in bs.select("div div div ul li dl dd dl dd div a"):
        scoreAll.append((score.find("span", {"class":"num"}).text))

    print("총 ",len(titleAll), '개의 영화가 상영중입니다.')

    for i in range (0, len(titleAll)):
        content="["+str(int(i+1))+"] 영화제목 : "+str(titleAll[i])+" (평점 "+str(scoreAll[i]+") \n")
        print(content)

RunningMovie()

'''
태그 값으로 찾아오기
for a in bs.body.find_all('div', {"class":"thumb"}):
   print(a)
'''
