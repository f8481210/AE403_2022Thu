#0224_clock
import turtle #匯入turtle模組
tur = turtle.Turtle()   #宣告第一隻烏龜

def number(i):
    tur.forward(100) #往前走100步
    tur.write(i) #寫下i
    tur.back(100) #退後100步
    tur.right(30) #右轉30度 360/12 = 30

tur.penup() #舉起筆
tur.left(60) #左轉60
for i in range(1,13): #起點1，終點12+1
    number(i)


turtle.done()
turtle.exitonclick()