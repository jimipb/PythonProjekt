import tkinter as tk

window = tk.Tk()

gewichtung=[4,2]
rowcnt = 0
entries = {} 
for i in range(2):
    i = tk.Entry(window)
    i.grid(row=rowcnt)
    entries[rowcnt] = i
    rowcnt += 1

label = tk.Label(window, text = "")
label.grid(row=2)

def callback(event):
    zahl=0
    for i in range(2):
        zahl += gewichtung[i]*int(entries[i].get())
    text = str(zahl/6)
    label.configure(text=text)

entries[1].bind("<Return>",callback)

tk.mainloop()
