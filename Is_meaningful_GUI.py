import os

import tkinter

import tkinter.messagebox

from tkinter import StringVar

import pandas as pd

data=pd.read_csv('word_list.csv')


column=[]

index=0




# 创建tkinter应用程序窗口

root = tkinter.Tk()

# 设置窗口大小和位置

root.geometry('430x650+40+30')

# 不允许改变窗口大小

root.resizable(False, False)

# 设置窗口标题

root.title('Is_meaningful')

status=0

text=StringVar()

text.set(data.iloc[index][1])

def change(flag):
    
    global column,index,status
    
    column.append(flag)
    
    if status==1:
        index+=1
        text.set(data.iloc[index][1])
        status=0


# “yes”按钮

def yesButton():
    global status
    status=1
    change('y')

btnPre = tkinter.Button(root, text='YES', command=yesButton)

btnPre.place(x=100, y=20, width=80, height=30)



# “no”按钮

def noButton():
    global status
    status=1
    change('n')

btnNext = tkinter.Button(root, text='NO', command=noButton)

btnNext.place(x=230, y=20, width=80, height=30)


def saveButton():
    
    global column
    
    print(column)
    
    dataframe=pd.DataFrame({'Is_meaningful(y for yes,n for no)':column})
    dataframe.to_csv("result.csv",index=False,sep=',')

svButton=tkinter.Button(root,text='SAVE',command=saveButton)

svButton.place(x=175,y=600,width=80,height=30)


# 用来显示词汇的Label组件

textLabel = tkinter.Label(root,textvariable=text)


textLabel.place(x=10, y=50, width=400, height=300)


# 启动消息主循环

root.mainloop()
