#0310_ytdownloader
#匯入pytube模組內的YouTube
from pytube import YouTube

#定義全域變數，儲存目前下載進度
progress = 0

def showProgress(chunk, file_handle, bytes_remaining):
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
    
#建立YouTube物件，並指定on_progress_callback函式
yt = YouTube("影片網址",
             on_progress_callback=showProgress)
#從yt內的所有串流中，篩選出只有音樂的串流，並從此串流抓出第一個串流
stream = yt.streams.filter(res="720p").first()
#下載串流，括號內設定下載位置及檔案名稱
stream.download()

