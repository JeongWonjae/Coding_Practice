# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import string

def CurrentRunningMovie():
    titleAll=[]
    scoreAll=[]
    res=[]
    
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
        content="영화제목 : "+str(titleAll[i])+" (평점 "+str(scoreAll[i]+")")
        res.append(content)
    return res

def Top10MovieContent():
    html=urlopen("https://movie.naver.com/movie/running/current.nhn")
    bs=BeautifulSoup(html, "html.parser")
    i=0
    print("상위 10개의 영화 줄거리 입니다.\n")
    for a in bs.select("div div div ul li div a"):
        b=a.get('href')
        if b.find('/movie/bi/mi/basic')!=-1:
            furl="https://movie.naver.com"+str(b)
            html=urlopen(furl)
            content=BeautifulSoup(html, "html.parser")
            a=content.body.find('h3', {"class":"h_movie"}).text
            title=a.split()
            print("영화제목 - ", end='')
            for j in range(0, len(title)):
                if title[j].find('상영')!=-1:
                    break;
                print(title[j]+" ", end='')
            print('\n\n'+(content.body.find('p', {"class":"con_tx"}).text)+"\n\n")
            i=i+1
            if i==10:
                break

#영화 조회
title=CurrentRunningMovie()
i=1 #앞에 번호 생성
for r in title:
    print("[",i,"]", r)
    i=i+1

#상위 영화10개 줄거리 조회 (수정)-> 사용자가 N개 선택가능하도록 OR 특정 영화 선택조회
content=Top10MovieContent()




    



