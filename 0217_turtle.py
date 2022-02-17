#匯入turtle模組
import turtle

#宣告第一隻turtle
t1 = turtle.Turtle()
#設定畫布大小
turtle.setup(500,500)
#把筆舉起來
t1.penup()
#移動至指定座標
t1.goto(-200,200)
#筆放下
t1.pendown()
#設定顏色
t1.fillcolor('#00F')
#開始上色
t1.begin_fill()

for i in range(4):
    #往前走
    t1.forward(100)
    #右轉
    t1.right(90)
    
#結束上色
t1.end_fill()






#告訴turtle程式結束
turtle.done()

#離開畫面
turtle.exitonclick()
