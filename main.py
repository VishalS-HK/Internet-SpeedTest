import tkinter as tk
from tkinter import *
from tkinter.ttk import Labelframe
from turtle import bgcolor
from click import command
from numpy import pad
from math import *
import speedtest


win=Tk()
win.title('Internet Speed Test')
win.geometry('600x650')
win.config(bg='Black')


##FUNCTION TO CHECK THE DATA-CONVERSION SPEEDS
def thespeed(choice1):
    sp=speedtest.Speedtest()
    sp.get_servers()
    if choice1=='Kbps':
        down=str(round(sp.download()/(10**3),2))+' Kbps'
        up=str(round(sp.upload()/(10**3),2))+' Kbps'
        downloadspeed.config(text=down,fg='green')
        uploadspeed.config(text=up,fg='green')
    elif choice1=="Mbps":
        down=str(round(sp.download()/(pow(10,6)),2))+' Mbps'
        up=str(round(sp.upload()/(pow(10,6)),2))+' Mbps'
        downloadspeed.config(text=down,fg='green')
        uploadspeed.config(text=up,fg='green')
    elif choice1=='Gbps':
        down=str(round(sp.download()/(pow(10,9)),2))+' Gbps'
        up=str(round(sp.upload()/(pow(10,9)),2))+' Gbps'
        downloadspeed.config(text=down,fg='green')
        uploadspeed.config(text=up,fg='green')
        
def chosen():
    global choice
    choice=speedunit.get()
    return thespeed(choice)
    
##WIDGETS
heading=Label(win,text='INTERNET SPEED TEST',font=("Times New Roman",35,'bold',UNDERLINE),fg='White',bg='Black')
heading.place(x=100,y=50)

download=Label(win,text='\nDownload Speed',font=('Consolas',25,'bold',UNDERLINE),bg='Black',fg='#00ffff')
download.place(x=200,y=100)

downloaddrop_options=['Kbps','Mbps','Gbps']
speedunit=StringVar()
speedunit.set(downloaddrop_options[2])

downloaddrop=OptionMenu(win,speedunit,*downloaddrop_options)
downloaddrop.config(bg='Black')
downloaddrop.place(x=270,y=200)

downloadspeed=Label(win,text='\n00',font=('Consolas',25),bg='Black',fg='White')
downloadspeed.place(x=270,y=250)

upload=Label(win,text='Upload Speed',font=('Consolas',25,'bold',UNDERLINE),bg='Black',fg='#00ffff')
upload.place(x=215,y=350)

uploadspeed=Label(win,text='\n00',font=('Consolas',25),bg='Black',fg='White')
uploadspeed.place(x=270,y=400)

runbutton=Button(win,text="CHECK SPEED NOW!!",font=('Times New Roman',30,'bold',UNDERLINE),fg='red',command=chosen)
runbutton.place(x=130,y=500)

win.mainloop()
