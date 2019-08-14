#画wifi万能钥匙logo
import turtle as t

def border_bar(): # 边框栏
    t.up()
    t.goto(76*2, -116*2)
    t.pd()
    t.pencolor('blue')
    t.pensize(12)
    for i in range(4):
        t.circle(40*2, 90)
        t.fd(152*2)


def  signal_intensity(): #信号强度（即那四个圆弧）
    t.up()
    t.goto(-70.7,  100)
    t.pd()
    t.pencolor('blue')
    t.pensize(28)
    t.lt(225)
    t.circle(100, 90)
    t.up()
    t.circle(100, 90)
    t.pd()
    t.circle(100, 90)
    t.up()
    t.goto(-99, 130)
    t.lt(90)
    t.pd()
    t.circle(140, 90)
    t.up()
    t.circle(140, 90)
    t.pd()
    t.circle(140, 90)


def key(): # 中间部分
    t.up()
    t.goto(-5, 60)
    t.left(135)
    t.pd()
    t.pensize(40)
    t.fd(107)
    
    t.up()
    t.goto(32, 30)
    t.pd()
    t.fd(30)

    t.up()
    t.goto(43, -90)
    t.pd()
    t.left(90)
    t.pensize(25)
    t.pencolor('blue')
    t.lt(90)
    a=1.2
    for i in range(120):
        if 0<=i<30 or 60<=i<90:
            a=a+0.07
            t.lt(3) #向左转3度
            t.fd(a) #向前走a的步长
        else:
            a=a-0.07
            t.lt(3)
            t.fd(a)


def main():
    border_bar()
    signal_intensity()
    key()
    t.ht()
    t.done()
    

main()
