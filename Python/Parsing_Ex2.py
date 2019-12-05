# -*- coding: utf-8 -*-
import string
from urllib.request import urlopen
from bs4 import BeautifulSoup
import string

array={1,2,3,4}
for i in range(0, 2):
    if array[0]==1:
        return;
print(array)

html=urlopen('https://movie.naver.com/movie/bi/mi/basic.nhn?code=167651')
bs=BeautifulSoup(html, "html.parser")
a=(bs.body.find('h3', {"class":"h_movie"}).text)
array_c=a.split()
print(array_c)

html=urlopen('https://movie.naver.com/movie/bi/mi/basic.nhn?code=171725')
bs=BeautifulSoup(html, "html.parser")
a=(bs.body.find('h3', {"class":"h_movie"}).text)
array_c=a.split()
print(array_c)

html=urlopen('https://movie.naver.com/movie/bi/mi/basic.nhn?code=167651')
bs=BeautifulSoup(html, "html.parser")
print((bs.body.find('p', {"class":"con_tx"}).text))
