from tkinter import *
import datetime
def motion(event):
    x, y = event.x, event.y
    # print('{}, {}'.format(x, y))
    root.destroy()
def update_time():
    t = datetime.datetime.now().strftime('%H:%M')
    v.set(t)
    root.after(1000, update_time)
    # print(t)
root = Tk()
root.attributes('-fullscreen', True)
v = StringVar()
w = Label(root, textvariable=v, font=("Arial", 550, 'bold'))
w.pack(expand='true')
root.bind('<Escape>', motion)
root.configure(background='black')
w.configure(background='black', fg='green')
update_time()
root.mainloop()
