from tkinter import *

root = Tk()
root.title("윈도우")
root.geometry("800x200+500+1500")

btn = Button(root, text="버튼클릭")
btn.pack()

txt = Text(root, width=100, height=5)
txt.pack()

root.mainloop()