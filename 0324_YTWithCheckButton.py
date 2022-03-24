#0324
#匯入套件


#定義全域變數，儲存目前下載進度
progress = 0     

#定義進度條函式    
def showProgress(stream,chunk,bytes_remaining):
    size = stream.filesize
        
    global progress
    preProgress = progress
        
    currentProgress = (size - bytes_remaining)*100 // size
    progress = currentProgress
        
    if preProgress != progress:
            scale.set(progress)
            window.update()
            print("目前進度： " + str(progress) + "%")
    if progress == 100: 
            print("下載完成！")

#定義下載影片的函式
def onClick():
    
    #定義全域變數
    global var
    #將var的值設成entry中的內容
    
    #點擊之後將button反灰(不能點選)
    
     #例外處理
    try:
        #取得網址及下載
        
        
        #確認是否要下載音樂

        #下載
        
        
    #發生例外
    except:
        print("下載失敗")
        
    #按鈕恢復正常

        
#定義thread函式，執行onClick


"""建立基本視窗"""


#視窗固定，使用者不能拉大小


#創建label元件


#建立var變數來存取entry的內容


#創建entry元件


#建立onlyMusic變數來存check的內容


#創建Checkbutton元件


#創建button元件


#創建scale元件


#開始運行視窗程式




