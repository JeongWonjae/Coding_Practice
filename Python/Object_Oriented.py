class car:
    #클래스 변수
    call=0
    #자동으로 호출되는 init
    def __init__(self, color, type):
        #객체 변수, 각각의 객체마다 독립적으로 접근
        self.color=color
        self.type=type
        car.call+=1
        print("[INIT] (Initializing {:s} {:s})".format(self.color, self.type))
    #self는 아래에서 객체 선언시 자기 자신을 말함
    def start_up(self):
        print(f"[INFO] Start up this {self.color} {self.type} car!")

    #클래스메소드 데코레이터는 다음에 나오는 함수는 클래스 전체에 속해있는 어떤 값들, 기능들을 다루는 메소드가 됨
    @classmethod
    #cls는 클래스를 참조
    def how_many_calls(cls):
        print("[COUNT] This class have {:d} cars.".format(cls.call))

    def turn_off(self):
        print("[INFO] Turn off This {} {} car".format(self.color, self.type))
        car.call-=1
        if car.call==0: print("[COUNT] Don't have car...")
        elif car.call==1: print("[COUNT] Have {} car".format(car.call))
        else: print("[COUNT] Have {} cars".format(car.call))

c=car('black', 'sport') #INIT
c.start_up() #STARTUP
c.how_many_calls() #COUNT CARS

d=car('yellow', 'mini')
d.start_up()
d.how_many_calls()

a=car('blue', 'truck')
a.start_up()
a.how_many_calls()

print("\n")

c.turn_off() #TURNOFF
#c.how_many_calls()
d.turn_off()
#d.how_many_calls()
a.turn_off()