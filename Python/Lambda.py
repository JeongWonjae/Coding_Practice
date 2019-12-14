#-*- coding:utf-8 -*-
from functools import reduce

def sum(x, y):
    return x+y

print (sum(1,2))

print ((lambda x,y: x+y)(1,2))

###

def squared(x):
    lst=[0,0,0,0,0]
    for idx in x:
        lst[idx]=idx**2
    return lst
print (squared((range(5))))

print ( list(map(lambda x: x**2, range(5))) )

###

print ( reduce(lambda x,y:x+y, [0,1,2,3,4]) )
print ( reduce(lambda x,y:y+x, 'abcde') )
''' sequence
1.b+a
2.c+ba
3.d+cba
4.e+dcba

'''
print ( reduce(lambda x,y:x+y, 'abcde') ) 

print ( list(filter(lambda x:x<5, range(10))) ) #return true values

print ( list(filter(lambda x:x%2!=0, range(10))) )

###

plusTen=lambda x:x+10
print (plusTen(23))
print ( list(map(lambda x:x+10, range(10))))

###
