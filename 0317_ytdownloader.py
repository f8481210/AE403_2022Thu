#0317_ytdownloader
#匯入pytube模組內的YouTube
from pytube import YouTube
#匯入tkinter模組取名叫做tk
import tkinter as tk

"""建立基本視窗"""
window = tk.Tk()
window.title("YouTube下載器")
window.geometry("500x150")

#定義全域變數，儲存目前下載進度
progress = 0

def showProgress(stream,chunk,bytes_remaining):
    #總檔案大小
    size = stream.filesize
    
    global progress
    preProgress = progress
    #目前下載進度(總大小-剩餘大小)除總大小 = 已下載百分比
    #全部大小 - 剩餘大小 = 已經下載多少 *100/總大小
    #去掉小數點 1.強制轉換成int 2.//
    progress = (size - bytes_remaining)*100//size
    
    if progress == 100:
        print("FINISH!")
        return
    elif progress != preProgress:
        print("目前進度:" +str(progress)+"%")

#建立var變數來存取entry的內容
var = tk.StringVar()
def onClick():
    #定義全域變數，設定成entry中的文字內容
    global var
    var.set(entry.get())
    
    #例外處理，如果取得網址及下載錯誤，則發生例外
    try:
        #建立YouTube物件，並指定on_progress_callback函式
        #var.get() 取出要下載的網址
        yt = YouTube(var.get(),on_progress_callback=showProgress)
        stream = yt.streams.first()
        stream.download()
    except:
        print("下載失敗")

#創建label元件
label = tk.Label(window,text = "請輸入YouTube影片網址")
label.pack()
#創建entry元件
entry = tk.Entry(window, width = 50)
entry.pack()
#創建button元件
button = tk.Button(window, text = "下載",command = onClick)
button.pack()
#創建scale元件
scale = tk.Scale(window, label='進度條',from_=0, to=100,
                 orient=tk.HORIZONTAL,length=200,
                 showvalue=True)
scale.pack()

#開始運行視窗程式
window.mainloop()