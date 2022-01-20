#匯入tkinter模組並取一個名字叫做tk
import tkinter as tk
import tkinter.messagebox

#跳出訊息函式
def clickMe():
    tkinter.messagebox.showinfo(title='oops',message='HII!')

#宣告一個叫做window的視窗
window = tk.Tk()
#設定視窗標題
window.title('GUI')
#設定視窗大小
window.geometry('300x300')

label = tk.Label(window,text="NNNNNNNNN",bg='#0055AB',fg='#55FFCA')
label.pack()

entry = tk.Entry(window,width = 20)
entry.pack()

button = tk.Button(window,text="download",command=clickMe)
button.pack()

#執行
window.mainloop()