import tkinter as tk
window = tk.Tk()
window.title('RADIOBUTTON')
window.geometry("500x500")

def selection():
    label.config(text='I am a '+ string2.get() + ' I like ' + string.get())

#宣告一個RB存值的變數
string = tk.StringVar()
string2 = tk.StringVar()

label = tk.Label(window,bg='#F00',text='NULL')
label.pack()

radio1 = tk.Radiobutton(window,text = 'Minecraft',
                        variable = string,
                        value = 'Minecraft',
                        command = selection)
radio1.pack()

radio2 = tk.Radiobutton(window,text = "pygame",
                        variable = string,
                        value = "pygame",
                        command = selection)
radio2.pack()
radio3 = tk.Radiobutton(window,text = "tkinter",
                        variable = string,
                        value = "tkinter",
                        command = selection)
radio3.pack()

r4 = tk.Radiobutton(window,text = "boy",
                    variable = string2,
                    value = 'boy',command = selection)
r4.pack()

r5 = tk.Radiobutton(window,text = "girl",
                    variable = string2,
                    value = 'girl',command = selection)
r5.pack()

window.mainloop()