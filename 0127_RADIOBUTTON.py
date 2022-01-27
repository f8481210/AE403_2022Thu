import tkinter as tk
window = tk.Tk()
window.title('RADIOBUTTON')
window.geometry("500x500")

def selection():
    label.config(text='I like ' + string.get())

#宣告一個RB存值的變數
string = tk.StringVar()

label = tk.Label(window,bg='#F00',text='NULL')
label.pack()

radio1 = tk.Radiobutton(window,text = 'Minecraft',
                        variable = string,
                        value = 'Minecraft',
                        command = selection)
radio1.pack()


window.mainloop()