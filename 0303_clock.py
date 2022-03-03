#0303_clock
#匯入模組
import turtle , time , datetime
tur = turtle.Turtle()   #宣告第一隻烏龜
tur.speed(10)
#step1 時鐘刻度
def number(i):
    tur.forward(250) #往前走250步
    tur.write(i) #寫下i
    tur.back(250) #退後250步
    tur.right(30) #右轉30度 360/12 = 30

tur.penup() #舉起筆
tur.left(60) #左轉60
for i in range(1,13): #起點1，終點12+1
    number(i)
tur.goto(260,-150)
tur.pendown()
tur.circle(300)
    
#step2 時針、分針、秒針
#控制時針分針
update = True
#控制秒針
updateSecond = True
#取得現在時間
while True:
    now = datetime.datetime.now()
    h = now.hour % 12
    m = now.minute
    s = now.second
    
    if update:
        #畫時針
        hour = turtle.Turtle()
        hour.color('#f00')
        #指針朝上
        hour.seth(90)
        #一圈12小時(30度/小時)
        #分鐘也會影響時針，每60分鐘影響30度(0.5度/分鐘)
        hour.right(h*30+m*0.5)
        hour.forward(140)
        
        #畫分針
        minute = turtle.Turtle()
        minute.color('#0f0')
        minute.seth(90) #指針朝上
        #360/60 = 6度/分鐘
        minute.right(m*6)
        minute.forward(200)
        #時針分針更新完畢
        update = False
        
    if updateSecond:
        #畫秒針
        second = turtle.Turtle()
        second.color('#00f')
        second.seth(90) #指針朝上
        #6度/秒鐘
        second.right(s*6)
        second.forward(220)
        #秒針更新完畢
        updateSecond = False

    #step3 讓秒針一直轉，指針會依據現在時間移動到正確位置
    time.sleep(1) #讓程式睡一秒
    now = datetime.datetime.now()
    #取得新的分鐘
    mnew = now.minute
    #比對現在是不是同一時間
    if mnew != m :
        update = True
        hour.clear() #清除
        hour.reset() #重畫
        minute.clear() #清除
        minute.reset() #重畫
    
    updateSecond = True
    second.clear() #清除
    second.reset() #重畫

turtle.done()
turtle.exitonclick()