class student:
    person=0
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print("Initialize name:{:s} age:{:d}".format(self.name, self.age))
    def hi(self):
        print("Hi, my name is {:s}".format(self.name))

class score(student):
    def __init__(self, name, age, score):
        student.__init__(self, name, age)
        self.score=score
        print("Initiallize score:{:d}".format(self.score))
    def introduce(self):
        student.hi(self)
        print('My score is {:d}...'.format(self.score))

s=[]
s.append(score('wonjae', 25, 95))
s.append(score('sangbin', 25, 100))
for i in s: i.introduce()


