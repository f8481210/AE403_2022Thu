import tkinter as tk
window = tk.Tk()
window.title('MENU')
window.geometry("500x500")

#創選單列 一個視窗一個
menubar = tk.Menu(window)

#建立第一個選單
filemenu = tk.Menu(menubar,tearoff = False)

#新增選項 add_command
filemenu.add_command(label='NEW')
filemenu.add_command(label='OPEN')

#新增分隔線
filemenu.add_separator()

filemenu.add_command(label='EXIT')

#選單 > 選單列
menubar.add_cascade(label='FILE',menu=filemenu)

#第二層選單
subMenu = tk.Menu(menubar,tearoff=False)
subMenu.add_command(label="遊戲優化Max")
subMenu.add_command(label="攻擊所有敵人")

#第一層 加入 第二層
filemenu.add_cascade(label='sub',menu = subMenu)

#打包
window.config(menu = menubar)

window.mainloop()



