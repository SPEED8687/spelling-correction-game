from tkinter import *
from textblob import TextBlob
import textblob
def clearTheWord():
    word1.delete(0,END)
    word2.delete(0,END)
def correctTheWord():
    inputword=word1.get()
    blobobj=TextBlob(inputword)
    correctedword=str(blobobj.correct())
    word2.delete(0,END)
    word2.insert(10,correctedword)
if __name__=='__main__':
    root=Tk()
    root.configure(background='lightgreen')
    root.geometry('400x150')
    root.title('spelling correction app')
    header=Label(root,text='Welcome to the Spelling Correction App',fg='black',bg='red')
    header.grid(row=0,column=1)
    label1=Label(root,text='input word',fg='black',bg='dark green')
    label1.grid(row=1,column=0)
    label2=Label(root,text='corrected word',fg='black',bg='dark green')
    label2.grid(row=3,column=0)
    word1=Entry()
    word2=Entry()
    word1.grid(row=1,column=1)
    word2.grid(row=3,column=1)
    button1=Button(root,text='correction',bg='red',fg='black',command=correctTheWord)
    button1.grid(row=2,column=1)
    button2=Button(root,text='clear',bg='red',fg='black',command=clearTheWord)
    button2.grid(row=4,column=1)
    root.mainloop()