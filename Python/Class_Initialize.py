# _*_coding: utf-8 _*_

class Point:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

p=Point(1,2)
print (p)
print (p.x)

r=Point()
print (r)
print (r.x)

class Person:
    def __init__(self, language=""):
        self.language=language

p1=Person()
p1.language="korean"
p1.age="13"
print(p1.age)
