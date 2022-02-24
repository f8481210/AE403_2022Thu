#circle(半徑,角度,幾步完成(n邊形))
#shape('') arrow, blank, circle, classic, square, triangle, turtle
#stamp()蓋印章
#color('')畫筆顏色

import turtle
tur = turtle.Turtle()
tur.color('#019858')
tur.shape('turtle')

tur.penup()                # 提筆
for i in range(5, 60, 2):    # 迴圈：從 5 開始，每次跳 2 步，直到 60
    tur.stamp()            # 蓋章
    tur.forward(i)      # 向前 step 步
    tur.right(24)          # 右轉 24 度
    
turtle.done()
turtle.exitonclick()