import tkinter as tk
def myfunc():
    lbl['text']= str(int(lbl['text']) + 1) 
Window=tk.Tk()
Window.title('counter')
Window.geometry('600x400')
lbl =tk.Label(text='0',font=('Arial Bold',50))
btn =tk.Button(text='Click me',font=('Arial Bold',50),command=myfunc)
btn.pack()
lbl.pack()
Window.mainloop()