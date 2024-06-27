import time
from tkinter import *


def clock(a):
    #getting all the values
    hour=time.strftime('%I')
    minute=time.strftime('%M')
    second=time.strftime('%S')
    am_pm=time.strftime('%p')
    day=time.strftime('%A')
    date=time.strftime('%d')
    month=time.strftime('%m')
    year=time.strftime('%Y')

    #creating the labels
    label_time=Label(a,text=hour+':'+minute+' '+am_pm,bg='grey',fg='white',font=('elephant',16,'bold'))
    label_date=Label(a,text=date+'-'+month+'-'+year+', '+day,bg='grey',fg='white',font=('elephant',16,'bold'))

    #placing the labels
    label_time.place(relx=0,rely=0,relwidth=0.15,relheight=0.55)
    label_date.place(relx=0.78,rely=0,relwidth=0.225,relheight=0.55)

    #calling the function again after one second
    label_time.after(60000,lambda:clock(a))
    label_date.after(60000,lambda:clock(a))


