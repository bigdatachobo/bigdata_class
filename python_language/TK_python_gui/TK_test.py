# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 11:32:53 2019

@author: sundooedu
"""
# Ui = 유저창(User interface Window) : 메인창(TK) >>> 그림 요소=위젯
# GUi 프로그램 

from tkinter import *
root = Tk()
root.mainloop()

from tkinter import *
root = Tk()
 
lbl = Label(root, text="이름")
lbl.pack()
 
txt = Entry(root)
txt.pack()
 
btn = Button(root, text="OK")
btn.pack()

btn2 = Button(root,text="CANCEL")
btn2.pack()
 
root.mainloop()

from tkinter import *
root = Tk()
root.geometry("400x200") # 창너비와 높이 변경 가능 
lbl = Label(root, text="이름")
lbl.grid(row=0, column=0)
txt = Entry(root)
txt.grid(row=0, column=1)
btn = Button(root, text="OK", width=15)
btn.grid(row=1, column=0)
btn2 = Button(root, text="CANCEL", width=15)
btn2.grid(row=1, column=1)
 
root.mainloop()

from tkinter import *
from tkinter import messagebox
 
root = Tk()
 
# 버튼 클릭 이벤트 핸들러
def okClick(e): # 이벤트받자
    name = txt.get()
    messagebox.showinfo("이름", name)
 
lbl = Label(root, text="이름")
lbl.grid(row=0, column=0)
txt = Entry(root)
txt.grid(row=0, column=1)
 
# 버튼 클릭 이벤트와 핸들러 정의
#btn = Button(root, text="OK", command=okClick)

btn = Button(root, text="OK",background='blue')
btn.bind("<Button-1>",okClick )
txt.bind("<Return>",okClick)
btn.grid(row=1, column=1)
 
root.mainloop()
#%%

from tkinter import * # '*' >>> '모든'을 의미함
from tkinter import simpledialog # 입력창
from tkinter import messagebox # 메세지 박스

root = Tk()
root.title('마이창')
root.geometry('300x200')
name = simpledialog.askstring('회원정보','이름')
#print(name)
messagebox.showinfo('이름',name)

root.mainloop








