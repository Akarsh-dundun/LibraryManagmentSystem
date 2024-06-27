from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector as n
import time

#main windows
#1.password window
def passwd():
    global z,top_bar,entry_passwd1,entry_passwd2,incorrect_count
    
    z=Tk()
    z.title('Library')
    z.geometry('700x450')
    z.configure(background='black')    
    label=Label(z,text='Login',bg='yellow',fg='black',font=('Courier',26))
    frame=Frame(z,bg='black')
    login_menu=Menu(z)
    
    z.config(menu=login_menu)

    sign_up_menu=Menu(login_menu)
    
    label_passwd1=Label(frame,text='Enter username:',bg='black',fg='white',font=('Courier',18))
    label_passwd2=Label(frame,text='Enter password:',bg='black',fg='white',font=('Courier',18))
    
    entry_passwd1=Entry(frame,width=35,borderwidth=5,bg='white')
    entry_passwd2=Entry(frame,show="*",width=35,borderwidth=5,bg='white')

    frame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.4)
    
    label.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    label_passwd1.place(relx=0.07,rely=0.35,relwidth=0.39,relheight=0.1)
    label_passwd2.place(relx=0.07,rely=0.75,relwidth=0.39,relheight=0.1)
    entry_passwd1.place(relx=0.5,rely=0.3,relwidth=0.4,relheight=0.2)
    entry_passwd2.place(relx=0.5,rely=0.7,relwidth=0.4,relheight=0.2)

    login_menu.add_cascade(label="Sign-up",menu=sign_up_menu)
    sign_up_menu.add_command(label='Add Member',command=add_member)
    sign_up_menu.add_command(label='Delete Member',command=delete_member)
    
    cursor_passwd=con.cursor()
    st='select * from password'
    cursor_passwd.execute(st)
    username_passwd=cursor_passwd.fetchall()

    for i in username_passwd:
        if list(i) in lst_passwd:
            pass
        else:
            lst_passwd.append(list(i))
    
    button_quit=Button(z,text='Exit',bg='white',fg='black',font=('Courier',18),command=lambda:[dest(True)])
    button_submit=Button(z,text='Login',bg='white',fg='black',font=('Courier',18),command=lambda:[login(True)])           

    z.bind("<Return>",login)
    z.bind("<Escape>",dest)
    
    button_quit.place(relx=0.6,rely=0.85,relwidth=0.2,relheight=0.1)
    button_submit.place(relx=0.20,rely=0.85,relwidth=0.2,relheight=0.1)

    #dropdown()
    con.commit()
    z.mainloop()

#2.library window
def main_window():
    global x
    
    if m==True:
        x=Tk()
        x.title('Library')
        x.geometry('700x650')

        my_pic=Image.open('images/background.jpg')
        resized=my_pic.resize((700,690),Image.ANTIALIAS)
        new_pic=ImageTk.PhotoImage(resized)
        label=Label(x,image=new_pic)
        label.pack()

        headingFrame = Frame(x,bg="#FFBB00",bd=5)
        top_bar_main=Frame(x,bg='grey',bd=5)
        headingFrame.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
        headingLabel = Label(headingFrame, text="Welcome to \n DPS South Library", bg='black', fg='white', font=('Courier',15))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

        button_add=Button(x,text='Add Book',bg='black',fg='white',font=('Courier',14),command=add)
        button_delete=Button(x,text='Delete Book',bg='black',fg='white',font=('Courier',14),command=delete)
        button_book_no=Button(x,text='Update Book number',bg='black',fg='white',font=('Courier',14),command=num)
        button_issue=Button(x,text='Issue Book',bg='black',fg='white',font=('Courier',14),command=issue)
        button_return=Button(x,text='Return Book',bg='black',fg='white',font=('Courier',14),command=retur)
        button_book_list=Button(x,text='Show Book List',bg='black',fg='white',font=('Courier',14),command=lis)
        button_log_out=Button(top_bar_main,text='Logout',bg='white',fg='black',font=('Courier',14),command=log_out)

        top_bar_main.place(relx=0,rely=0,relwidth=1,relheight=0.05)
        button_add.place(relx=0.32,rely=0.4,relwidth=0.38,relheight=0.08)
        button_delete.place(relx=0.32,rely=0.48,relwidth=0.38,relheight=0.08)
        button_book_no.place(relx=0.32,rely=0.56,relwidth=0.38,relheight=0.08)
        button_issue.place(relx=0.32,rely=0.64,relwidth=0.38,relheight=0.08)
        button_return.place(relx=0.32,rely=0.72,relwidth=0.38,relheight=0.08)
        button_book_list.place(relx=0.32,rely=0.8,relwidth=0.38,relheight=0.08)
        button_log_out.place(relx=0.85,rely=0,relwidth=0.15,relheight=1)

        x.mainloop()

    elif m==False:
        quit()


def login(event):
    global m
    
    e1=entry_passwd1.get()
    e2=entry_passwd2.get()

    entry_passwd1.delete(0,END)
    entry_passwd2.delete(0,END)

    if [e1,e2] in lst_passwd:
        m=True
        z.destroy()
        main_window()
        
    else:
        m=False
        error_incorrect_logindetails()
        

def dropdown():
    global clicked
    
    title_heading1='Sign-Up'
    options=['Add Member',
             'Delete Member']

    clicked=StringVar()
    clicked.set(title_heading1)

    drop=OptionMenu(top_bar,clicked,*options,command=selected)
    drop.place(relx=0,rely=0,relwidth=0.12,relheight=0.95)
    
def selected(event):
    select=clicked.get()
    
    if select=='Add Member':
        if len(lst_passwd)>=3:
            z.destroy()
            display_maximum_users()
            passwd()
            
        elif len(lst_passwd)<3:
            z.destroy()
            add_member()
            passwd()

    if select=='Delete Member':
        if len(lst_passwd)>1:
            z.destroy()
            delete_member()
            passwd()
            
        elif len(lst_passwd)<=1:
            z.destroy()
            minimum_users_info()
            passwd()

def loading_progress(det):
    global progress_bar,d
    d=Tk()
    d.title('LOADING')
    d.geometry('500x200')
    d.configure(background='white')

    progress_bar=ttk.Progressbar(d,orient=HORIZONTAL,length=400,mode='determinate')
    label=Label(d,text='Please wait\nfor a few seconds..',bg='white',fg='black',font=('Courier',16))

    progress_bar.place(relx=0.1,rely=0.6)
    label.place(relx=0.25,rely=0.2)

    if det=='add':
        step_add()
    elif det=='delete':
        step_delete()

def step_add():
    for i in range(5):
        progress_bar['value']+=20
        d.update()
        time.sleep(1)

    d.destroy()
    new_member()

def step_delete():
    for i in range(5):
        progress_bar['value']+=20
        d.update()
        time.sleep(1)

    d.destroy()
    remove_member()

#after windows
#1.incorrect login details
def error_incorrect_logindetails():
        global incorrect_count,error_box
        
        if incorrect_count==3:
            z.destroy()
            quit()
            
        error_box=messagebox.askretrycancel('ERROR!!','Incorrect Username or Password!!')
        print(error_box)   
        if error_box:
            incorrect_count+=1
            z.destroy()
            passwd()
        else:
            z.destroy()
    

#2.adding the username and password
def confirmation_correct_info():
        w=Tk()
        w.title('CONFIRMED')
        w.geometry('300x150')
        w.configure(background='black')

        label=Label(w,text='The username and passwd\n have been stored\nclick on OK to continue!!',bg='black',fg='white',font=('Courier',12))
        button_okay=Button(w,text='OK',bg='white',fg='black',font=('Courier',14),command=lambda:[w.destroy(),p.destroy()])

        label.place(relx=0.01,rely=0.2,relwidth=0.96,relheight=0.5)
        button_okay.place(relx=0.7,rely=0.8,relwidth=0.2,relheight=0.15)

        w.mainloop()

#3.username and password deletion
def confirmation_deleted_info():
        w=Tk()
        w.title('CONFIRMED')
        w.geometry('300x150')
        w.configure(background='black')

        label=Label(w,text='The username and passwd\n have been deleted\nclick on OK to continue!!',bg='black',fg='white',font=('Courier',12))
        button_okay=Button(w,text='OK',bg='white',fg='black',font=('Courier',14),command=lambda:[w.destroy(),l.destroy()])

        label.place(relx=0.01,rely=0.2,relwidth=0.96,relheight=0.5)
        button_okay.place(relx=0.7,rely=0.8,relwidth=0.2,relheight=0.15)

        w.mainloop()

#4.showing maximum number of users reached
def display_maximum_users():
        w=Tk()
        w.title('ERROR!!')
        w.geometry('300x150')
        w.configure(background='black')

        label=Label(w,text='Maximum number of users are there!\nclick on delete to remove some\n or OK to continue',bg='black',fg='white',font=('Courier',10))
        button_okay=Button(w,text='OK',bg='white',fg='black',font=('Courier',14),command=w.destroy)
        button_delete=Button(w,text='Delete',bg='white',fg='black',font=('Courier',14),command=delete_member)
        
        label.place(relx=0.01,rely=0.2,relwidth=0.96,relheight=0.5)
        button_okay.place(relx=0.65,rely=0.8,relwidth=0.3,relheight=0.15)
        button_delete.place(relx=0.15,rely=0.8,relwidth=0.3,relheight=0.15)

        w.mainloop()
        
#5.username and password doesnt exist
def error_deleted_info():
        w=Tk()
        w.title('ERROR!!')
        w.geometry('300x150')
        w.configure(background='black')

        label=Label(w,text='The following\nusername and password\ndont exist!!',bg='black',fg='white',font=('Courier',12))
        button_okay=Button(w,text='OK',bg='white',fg='black',font=('Courier',14),command=lambda:[l.destroy(),w.destroy(),delete_member()])

        label.place(relx=0.01,rely=0.2,relwidth=0.96,relheight=0.5)
        button_okay.place(relx=0.7,rely=0.8,relwidth=0.2,relheight=0.15)

        w.mainloop()

#6.only one usernam is left and cannot be deleted
def minimum_users_info():
        w=Tk()
        w.title('ERROR!!')
        w.geometry('300x150')
        w.configure(background='black')

        label=Label(w,text='Cannot delete as\nminimum 1 password is required',bg='black',fg='white',font=('Courier',10))
        button_okay=Button(w,text='OK',bg='white',fg='black',font=('Courier',14),command=lambda:w.destroy())

        label.place(relx=0.01,rely=0.2,relwidth=0.96,relheight=0.5)
        button_okay.place(relx=0.7,rely=0.8,relwidth=0.2,relheight=0.15)

        w.mainloop()

#7.when a duplicate username is being entered
def error_username_exist():
        w=Tk()
        w.title('ERROR!!')
        w.geometry('300x150')
        w.configure(background='black')

        label=Label(w,text='The following\n username already\n exists!!',bg='black',fg='white',font=('Courier',12))
        button_okay=Button(w,text='OK',bg='white',fg='black',font=('Courier',14),command=lambda:[w.destroy(),p.destroy()])

        label.place(relx=0.01,rely=0.2,relwidth=0.96,relheight=0.5)
        button_okay.place(relx=0.7,rely=0.8,relwidth=0.2,relheight=0.15)

        w.mainloop()

               
def add_member():
    global entry_add_member1,entry_add_member2,p
    z.destroy()
    det='add'
    p=Tk()
    p.title('Library')
    p.geometry('700x450')
    p.configure(background='black')
    label=Label(p,text='Add Member',bg='yellow',fg='black',font=('Courier',26))
    frame=Frame(p,bg='black')
    
    label_add_member1=Label(frame,text='Enter username:',bg='black',fg='white',font=('Courier',18))
    label_add_member2=Label(frame,text='Enter password:',bg='black',fg='white',font=('Courier',18))

    entry_add_member1=Entry(frame,width=35,borderwidth=5,bg='white')
    entry_add_member2=Entry(frame,width=35,borderwidth=5,bg='white')

    frame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.4)

    label.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    label_add_member1.place(relx=0.07,rely=0.35,relwidth=0.39,relheight=0.1)
    label_add_member2.place(relx=0.07,rely=0.75,relwidth=0.39,relheight=0.1)
    entry_add_member1.place(relx=0.5,rely=0.3,relwidth=0.4,relheight=0.2)
    entry_add_member2.place(relx=0.5,rely=0.7,relwidth=0.4,relheight=0.2)

    button_quit=Button(p,text='Exit',bg='white',fg='black',font=('Courier',18),command=lambda:[p.destroy(),passwd()])
    button_submit=Button(p,text='Add',bg='white',fg='black',font=('Courier',18),command=lambda:[loading_progress(det)])

    button_quit.place(relx=0.6,rely=0.85,relwidth=0.2,relheight=0.1)
    button_submit.place(relx=0.20,rely=0.85,relwidth=0.2,relheight=0.1)

    p.mainloop()

def delete_member():
    global entry_delete_member1,entry_delete_member2,l
    z.destroy()
    det='delete'
    l=Tk()
    l.title('Library')
    l.geometry('700x450')
    l.configure(background='black')
    label=Label(l,text='Delete Member',bg='yellow',fg='black',font=('Courier',26))
    frame=Frame(l,bg='black')
    
    label_delete_member1=Label(frame,text='Enter username:',bg='black',fg='white',font=('Courier',18))
    label_delete_member2=Label(frame,text='Enter password:',bg='black',fg='white',font=('Courier',18))

    entry_delete_member1=Entry(frame,width=35,borderwidth=5,bg='white')
    entry_delete_member2=Entry(frame,width=35,borderwidth=5,bg='white')

    frame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.4)

    label.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    label_delete_member1.place(relx=0.07,rely=0.35,relwidth=0.39,relheight=0.1)
    label_delete_member2.place(relx=0.07,rely=0.75,relwidth=0.39,relheight=0.1)
    entry_delete_member1.place(relx=0.5,rely=0.3,relwidth=0.4,relheight=0.2)
    entry_delete_member2.place(relx=0.5,rely=0.7,relwidth=0.4,relheight=0.2)

    button_quit=Button(l,text='Exit',bg='white',fg='black',font=('Courier',18),command=lambda:[l.destroy(),passwd()])
    button_submit=Button(l,text='Delete',bg='white',fg='black',font=('Courier',18),command=lambda:[loading_progress(det)])
    
    button_quit.place(relx=0.6,rely=0.85,relwidth=0.2,relheight=0.1)
    button_submit.place(relx=0.20,rely=0.85,relwidth=0.2,relheight=0.1)

    l.mainloop()

def dest(event):
    global m
    m=False
    z.destroy()

def new_member():
    lst_username=[]
    
    e1=entry_add_member1.get()
    e2=entry_add_member2.get()

    entry_add_member1.delete(0,END)
    entry_add_member2.delete(0,END)

    cursor=con.cursor()
    st='insert into password values("%s","%s")'%(e1,e2)

    for i in range(len(lst_passwd)):
        lst_username.append(lst_passwd[i][0])
    
    if e1 in lst_username:
        error_username_exist()        
    if e1 not in lst_username:
        cursor.execute(st)
        confirmation_correct_info()

    con.commit()   

def remove_member():
    global lst_passwd
    
    e1=entry_delete_member1.get()
    e2=entry_delete_member2.get()

    entry_delete_member1.delete(0,END)
    entry_delete_member2.delete(0,END)

    cursor=con.cursor()
    st='select * from password where USERNAME="%s"'%(e1)
    cursor.execute(st)
    
    corresponding_passwd=cursor.fetchone()
    

    if corresponding_passwd==None:
        error_deleted_info()      

    elif corresponding_passwd[1]==e2:
        cursor_delete_member=con.cursor()
        st='delete from password where USERNAME="%s"'%(e1)
        cursor_delete_member.execute(st)
        con.commit()

        lst_passwd.remove([e1,e2])
                
    confirmation_deleted_info()         
                
def add():
    global entry_add1,entry_add2,entry_add3,entry_add4
    y=Tk()
    y.title('Add book')
    y.geometry('700x550')
    y.configure(background='cyan')
    frame=Frame(y,bg='black',bd=5)
    topfram = Frame(y,bg="#FFBB00",bd=5)   

    label=Label(topfram,text='Add Book',bg='black',fg='white',font=('Courier',14))
    label1=Label(frame,text='Book ID:',bg='black',fg='white',font=('Courier',12))
    label2=Label(frame,text="Book's Name:",bg='black',fg='white',font=('Courier',12))
    label3=Label(frame,text="Book's Author:",bg='black',fg='white',font=('Courier',12))
    label4=Label(frame,text='Number of books:',bg='black',fg='white',font=('Courier',12))
    
    entry_add1=Entry(frame,width=35,borderwidth=5,bg='white')
    entry_add2=Entry(frame,width=35,borderwidth=5,bg='white')
    entry_add3=Entry(frame,width=35,borderwidth=5,bg='white')
    entry_add4=Entry(frame,width=35,borderwidth=5,bg='white')

    
    frame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    topfram.place(relx=0.2,rely=0.02,relwidth=0.6,relheight=0.16)
    label.place(relx=0,rely=0,relwidth=1,relheight=1)

    label1.place(relx=0.05,rely=0.11,relwidth=0.15,relheight=0.1)
    label2.place(relx=0.05,rely=0.34,relwidth=0.23,relheight=0.1)
    label3.place(relx=0.05,rely=0.57,relwidth=0.27,relheight=0.1)
    label4.place(relx=0.05,rely=0.8,relwidth=0.3,relheight=0.1)

    entry_add1.place(relx=0.45,rely=0.11,relwidth=0.5,relheight=0.1)
    entry_add2.place(relx=0.45,rely=0.34,relwidth=0.5,relheight=0.1)
    entry_add3.place(relx=0.45,rely=0.57,relwidth=0.5,relheight=0.1)
    entry_add4.place(relx=0.45,rely=0.8,relwidth=0.5,relheight=0.1)
    
    button_quit=Button(y,text='QUIT',bg='black',fg='white',font=('Courier',14),command=y.destroy)
    button_submit=Button(y,text='Submit',bg='black',fg='white',font=('Courier',14),command=submit) 

    button_quit.place(relx=0.6,rely=0.85,relwidth=0.2,relheight=0.1)
    button_submit.place(relx=0.20,rely=0.85,relwidth=0.2,relheight=0.1)

    y.mainloop()
    
def delete():
    global entry_delete1
    y=Tk()
    y.title('Delete book')
    y.geometry('700x550')
    y.configure(background='cyan')
    frame=Frame(y,bg='black',bd=5)
    topfram = Frame(y,bg="#FFBB00",bd=5)

    button_quit=Button(y,text='QUIT',bg='black',fg='white',font=('Courier',14),command=y.destroy)
    button_submit=Button(y,text='Submit',bg='black',fg='white',font=('Courier',14),command=delete_book)
    
    label=Label(topfram,text='Delete book',bg='black',fg='white',font=('Courier',14))
    label1=Label(frame,text='Enter Book ID:',bg='black',fg='white',font=('Courier',12))

    entry_delete1=Entry(frame,width=35,borderwidth=5,bg='white')
    
    frame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    topfram.place(relx=0.2,rely=0.02,relwidth=0.6,relheight=0.16)
    label.place(relx=0,rely=0,relwidth=1,relheight=1)
    label1.place(relx=0.08,rely=0.4,relwidth=0.25,relheight=0.1)
    entry_delete1.place(relx=0.48,rely=0.4,relwidth=0.5,relheight=0.1)

    button_quit.place(relx=0.6,rely=0.85,relwidth=0.2,relheight=0.1)
    button_submit.place(relx=0.20,rely=0.85,relwidth=0.2,relheight=0.1)

    y.mainloop()

def num():
    global entry_update1,entry_update2
    y=Tk()
    y.title('List of Book')
    y.geometry('700x550')
    y.configure(background='cyan')
    frame=Frame(y,bg='black',bd=5)
    topfram = Frame(y,bg="#FFBB00",bd=5)

    button_quit=Button(y,text='QUIT',bg='black',fg='white',font=('Courier',14),command=y.destroy)
    button_submit=Button(y,text='Submit',bg='black',fg='white',font=('Courier',14),command=change_no_of_books)
    
    label=Label(topfram,text='Update number of books',bg='black',fg='white',font=('Courier',14))
    label1=Label(frame,text='Book ID:',bg='black',fg='white',font=('Courier',12))
    label2=Label(frame,text='New Number of Books:',bg='black',fg='white',font=('Courier',12))

    entry_update1=Entry(frame,width=35,borderwidth=5,bg='white')
    entry_update2=Entry(frame,width=35,borderwidth=5,bg='white')

    frame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    topfram.place(relx=0.2,rely=0.02,relwidth=0.6,relheight=0.16)
    label.place(relx=0,rely=0,relwidth=1,relheight=1)
    label1.place(relx=0.03,rely=0.29,relwidth=0.2,relheight=0.1)
    label2.place(relx=0.06,rely=0.62,relwidth=0.36,relheight=0.1)

    entry_update1.place(relx=0.48,rely=0.29,relwidth=0.5,relheight=0.1)
    entry_update2.place(relx=0.48,rely=0.62,relwidth=0.5,relheight=0.1)

    button_quit.place(relx=0.6,rely=0.85,relwidth=0.2,relheight=0.1)
    button_submit.place(relx=0.20,rely=0.85,relwidth=0.2,relheight=0.1)

    y.mainloop()
    
def issue():
    y=Tk()
    y.title('Issue book')
    y.geometry('700x550')
    y.configure(background='cyan')
    frame=Frame(y,bg='black',bd=5)
    topfram = Frame(y,bg="#FFBB00",bd=5)

    button_quit=Button(y,text='QUIT',bg='black',fg='white',font=('Courier',14),command=y.destroy)
    button_submit=Button(y,text='Submit',bg='black',fg='white',font=('Courier',14),command=lambda:submit())

    label=Label(topfram,text='Issue book',bg='black',fg='white',font=('Courier',14))
    label1=Label(frame,text='Book ID:',bg='black',fg='white',font=('Courier',12))
    label2=Label(frame,text='Member ID:',bg='black',fg='white',font=('Courier',12))

    entry1=Entry(frame,width=35,borderwidth=5,bg='white')
    entry2=Entry(frame,width=35,borderwidth=5,bg='white')
    
    frame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    topfram.place(relx=0.2,rely=0.02,relwidth=0.6,relheight=0.16)
    label.place(relx=0,rely=0,relwidth=1,relheight=1)
    label1.place(relx=0.03,rely=0.29,relwidth=0.2,relheight=0.1)
    label2.place(relx=0.06,rely=0.62,relwidth=0.18,relheight=0.1)

    entry1.place(relx=0.48,rely=0.29,relwidth=0.5,relheight=0.1)
    entry2.place(relx=0.48,rely=0.62,relwidth=0.5,relheight=0.1)
    
    button_quit.place(relx=0.6,rely=0.85,relwidth=0.2,relheight=0.1)
    button_submit.place(relx=0.20,rely=0.85,relwidth=0.2,relheight=0.1)

def retur():
    y=Tk()
    y.title('Return book')
    y.geometry('700x550')
    y.configure(background='cyan')
    frame=Frame(y,bg='black',bd=5)
    headingFram = Frame(y,bg="#FFBB00",bd=5)

    button_quit=Button(y,text='QUIT',bg='black',fg='white',font=('Courier',14),command=y.destroy)
    button_submit=Button(y,text='Submit',bg='black',fg='white',font=('Courier',14),command=lambda:submit())

    label=Label(headingFram,text='Return book',bg='black',fg='white',font=('Courier',14))
    label1=Label(frame,text='Book ID:',bg='black',fg='white',font=('Courier',12))
    label2=Label(frame,text='Member ID:',bg='black',fg='white',font=('Courier',12))

    entry1=Entry(frame,width=35,borderwidth=5,bg='white')
    entry2=Entry(frame,width=35,borderwidth=5,bg='white')

    frame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    headingFram.place(relx=0.2,rely=0.02,relwidth=0.6,relheight=0.16)
    label.place(relx=0,rely=0,relwidth=1,relheight=1)
    label1.place(relx=0.03,rely=0.29,relwidth=0.2,relheight=0.1)
    label2.place(relx=0.06,rely=0.62,relwidth=0.18,relheight=0.1)

    entry1.place(relx=0.48,rely=0.29,relwidth=0.5,relheight=0.1)
    entry2.place(relx=0.48,rely=0.62,relwidth=0.5,relheight=0.1)

    button_quit.place(relx=0.6,rely=0.85,relwidth=0.2,relheight=0.1)
    button_submit.place(relx=0.20,rely=0.85,relwidth=0.2,relheight=0.1)

    y.mainloop()

def lis():
    global y

    y=Tk()
    y.title('List of Book')
    y.geometry('700x550')
    y.configure(background='black')
    scroll()

    frame=Frame(y_2,bg='black',bd=5)
    headingFram = Frame(y_2,bg="#FFBB00",bd=5)

    button_quit=Button(y_2,text='QUIT',bg='black',fg='white',font=('Courier',14),command=y.destroy)

    label=Label(headingFram,text='List of Book',bg='black',fg='white',font=('Courier',14))
    
    frame.grid(column=4,row=1,columnspan=3)
    headingFram.grid(column=5,row=1,columnspan=3)
    label.grid(column=4,row=1,ipadx=50,ipady=40)

    s=1
    for i in range(4):
        label_space=Label(y_2,text='    ',bg='black',fg='white')
        label_space.grid(column=1,row=s)
        s+=1
        
    r=4
    for i in range(100):
        label_book=Label(y_2,text=' This is line no:'+str(i),bg='black',fg='white')
        label_book.grid(column=1,row=r)
        label_space.grid(column=1,row=r+1)
        
        r+=3
    

def submit():
    e1=(entry_add1.get()).capitalize()
    e2=(entry_add2.get()).capitalize()
    e3=(entry_add3.get()).capitalize()
    e4=(entry_add4.get()).capitalize()

    entry_add1.delete(0,END)
    entry_add2.delete(0,END)
    entry_add3.delete(0,END)
    entry_add4.delete(0,END)
    
    cursor=con.cursor()
    st='insert into books values("%s","%s","%s",%s,%s)'%(e1,e2,e3,e4,e4)
    cursor.execute(st)

    con.commit()

def delete_book():
    e1=entry_delete1.get()

    entry_delete1.delete(0,END)

    cursor=con.cursor()
    st='delete from books where book_id="%s"'%(e1)
    cursor.execute(st)

    con.commit()

def change_no_of_books():
    e1=entry_update1.get()
    e2=entry_update2.get()

    entry_update1.delete(0,END)
    entry_update2.delete(0,END)

    cursor=con.cursor()
    st='update books set total_number_of_books=%s where book_id="%s"'%(e2,e1)
    #st1='update books set current_number_of_books=%s where book_id="%s"'%(e2,e1)
    cursor.execute(st)
    #cursor.execute(st1)
    
    con.commit()

def scroll():
    global y_2
    #creation of scroll bar
    #create a main fream
    y_new=Frame(y,bg='black')
    y_new.place(relx=0,rely=0,relwidth=1,relheight=1)

    #create a canvas
    canvas=Canvas(y_new,bg='black')
    canvas.pack(side=LEFT,fill=BOTH,expand=1)

    #add a scrollbar to the canvas
    scroll_bar=ttk.Scrollbar(y_new,orient=VERTICAL,command=canvas.yview)
    scroll_bar.pack(side=RIGHT,fill=Y)

    #configure the canvas
    canvas.configure(yscrollcommand=scroll_bar.set)
    canvas.bind('<Configure>',lambda e:canvas.configure(scrollregion=canvas.bbox("all")))  

    #create ANOTHER frame inside the canvas
    y_2=Frame(y_new,bg='black')

    #add that new frame to a windwo in the canvas
    canvas.create_window((0,0),window=y_2)

def log_out():
    x.destroy()
    m=False
    passwd()
    
#main
lst_passwd=[]
incorrect_count=0
m=True
con=n.connect(host='localhost',user='root',passwd='root123',database='project')

#passwd()
main_window()
con.commit()
