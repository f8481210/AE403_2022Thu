import turtle
tur = turtle.Turtle()

#設置畫面大小
turtle.setup(650,650)

#定義畫矩形&著色函式
def rectangle():
    tur.begin_fill()
    tur.forward(600)
    tur.right(90)
    tur.forward(200)
    tur.right(90)
    tur.forward(600)
    tur.right(90)
    tur.forward(200)
    tur.right(90)
    tur.end_fill()

def myGoto(x,y):
    tur.penup()
    tur.goto(x,y)
    tur.pendown()

#上面黑色部分
myGoto(-300,300)
tur.fillcolor('#000')
rectangle()

#中間紅色部分
myGoto(-300,100)
tur.fillcolor('#F00')
rectangle()


#下面黃色部分
myGoto(-300,-100)
tur.fillcolor('#FF0')
rectangle()

#完成程式
turtle.done()
turtle.exitonclick()

