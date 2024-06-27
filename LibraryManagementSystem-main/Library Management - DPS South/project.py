from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector as n
from PIL import ImageTk,Image
import time
from datetime import datetime,date


#primary windows
#1.first page
def firstpg():
    global a
    
    a=Tk()
    a.title('library') #setting title
    a.geometry('1000x667') #setting size of window  
    a.config(cursor="pirate")
    
    #setting background image
    my_pic=Image.open('images/bg.jpg')
    resized=my_pic.resize((1000,667),Image.ANTIALIAS)
    new=ImageTk.PhotoImage(resized)
    label=Label(a,image=new)
    label.pack()
    
    #creating and placing frames
    hf = Frame(a,bg="#FFBB00",bd=5)
    hf.place(relx=0.15,rely=0.1,relwidth=0.7,relheight=0.18)
    b = Frame(a,bg="#FFBB00",bd=5)
    b.place(relx=0.15,rely=0.5,relwidth=0.25,relheight=0.15)
    c = Frame(a,bg="#FFBB00",bd=5)
    c.place(relx=0.6,rely=0.5,relwidth=0.25,relheight=0.15)
    d = Frame(a,bg="#FFBB00",bd=5)
    d.place(relx=0.38,rely=0.75,relwidth=0.25,relheight=0.15)

    #creating and placing heading label
    headingLabel = Label(hf, text="Welcome to DPS South Library", bg='black', fg='white', font=('elephant',25,'bold'))
    headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

    #creating buttons
    button_sign=Button(b,text='Sign In',bg='black',fg='white',font=('elephant',20),command=lambda:[hf.destroy(),b.destroy(),c.destroy(),d.destroy(),signin()])
    button_log=Button(c,text='Log In',bg='black',fg='white',font=('elephant',20),command=lambda:[hf.destroy(),b.destroy(),c.destroy(),d.destroy(),login()])
    button_exitt=Button(d,text='Exit',bg='black',fg='white',font=('elephant',20),command=quit)
    
    #placing buttons on screen
    button_sign.place(relx=0,rely=0,relwidth=1,relheight=1)
    button_log.place(relx=0,rely=0,relwidth=1,relheight=1)
    button_exitt.place(relx=0,rely=0,relwidth=1,relheight=1)
    a.mainloop()
    
#2.log in window
'''function login() is the window the user encounters when he/she has to log into
the library management system'''
def login():
    global entry_username,entry_passwd,entry_passwd,a,button_show_passwd
    
    a.title('Login')  #creating a title for the tk window
    a.geometry('1000x667')  #setting the tk window
    
    #creating the main heading frame
    main_heading = Frame(a,bg="#FFBB00",bd=5) 
    main_label = Label(main_heading, text="Log-in", bg='black', fg='white', font=('elephant',25,'bold')) #main label to go in the main frame

    #creating the labels to go on the screen
    label_username=Label(a,text='Enter Username:', bg='black', fg='white',font=('elephant',22)) 
    label_passwd=Label(a,text='Enter Password:', bg='black', fg='white',font=('elephant',22))

    #creeating the entry widgets
    entry_username=Entry(a,font=('courier',25),width=35,borderwidth=5,bg='white')
    entry_passwd=Entry(a,font=('courier',25),show='*',width=35,borderwidth=5,bg='white')

    #creating the buttons for the window
    button_submit=Button(a,text='Submit',bg='black',fg='white',font=('elephant',20),command=lambda:loading_progress(True))
    button_exit=Button(a,text='Exit',bg='black',fg='white',font=('elephant',20),command=lambda:[a.destroy(),firstpg()])
    button_show_passwd=Button(a,text='Show',bg='black',fg='white',font=('elephant',20),command=lambda:show_passwd('log-in'))

    #binding the keyboard key 'Enter' to perform a function
    a.bind("<Return>",loading_progress)

    #placing the labels on the window
    main_heading.place(relx=0.15,rely=0.1,relwidth=0.7,relheight=0.18)
    main_label.place(relx=0,rely=0,relwidth=1,relheight=1)

    label_username.place(relx=0.07,rely=0.4,relwidth=0.3,relheight=0.1)
    label_passwd.place(relx=0.07,rely=0.65,relwidth=0.3,relheight=0.1)

    entry_username.place(relx=0.5,rely=0.4,relwidth=0.45,relheight=0.1)
    entry_passwd.place(relx=0.5,rely=0.65,relwidth=0.35,relheight=0.1)

    button_submit.place(relx=0.2,rely=0.85,relwidth=0.2,relheight=0.1)
    button_exit.place(relx=0.6,rely=0.85,relwidth=0.2,relheight=0.1)
    button_show_passwd.place(relx=0.85,rely=0.65,relwidth=0.1,relheight=0.1)

    a.mainloop()

'''function for the login page;
to show the password'''
def show_passwd(n):
    global truth_password_login,truth_password_signin_1,truth_password_signin_2
    
    if n=='log-in':
        if truth_password_login==False:
            #getting the password
            e_passwd=entry_passwd.get()
            entry_passwd.delete(0,END)

            #getting the show to show the password
            entry_passwd.config(show='')
            entry_passwd.insert(0,e_passwd)

            #configure the button to change to hide button
            button_show_passwd.config(text='Hide')
            a.update()

            #setting the counter value to True
            truth_password_login=True

        elif truth_password_login==True:
            #getting the password
            e_passwd=entry_passwd.get()
            entry_passwd.delete(0,END)

            #getting the show to show the password
            entry_passwd.config(show='*')
            entry_passwd.insert(0,e_passwd)

            #configure the button to change to hide button
            button_show_passwd.config(text='Show')
            a.update()

            #setting the counter value to False
            truth_password_login=False

    elif n=='sign-in1':

        #condition to show and hide password
        if truth_password_signin_1==2:
            #getting the password
            e_passwd=entry_passwd.get()
            entry_passwd.delete(0,END)

            #getting the show to show the password
            entry_passwd.config(show='')
            entry_passwd.insert(0,e_passwd)

            #configure the button to change to hide button
            button_show_password_1.config(text='Hide')
            a.update()

            #setting the counter value to True
            truth_password_signin_1=3


        elif truth_password_signin_1==3:
            #getting the password
            e_passwd=entry_passwd.get()
            entry_passwd.delete(0,END)

            #getting the show to show the password
            entry_passwd.config(show='*')
            entry_passwd.insert(0,e_passwd)

            #configure the button to change to hide button
            button_show_password_1.config(text='Show')
            a.update()

            #setting the counter value to True
            truth_password_signin_1=2            

    elif n=='sign-in2':

        if truth_password_signin_2==4:
            #getting the password
            e_passwd=entry_passwd_confirm.get()
            entry_passwd_confirm.delete(0,END)

            #getting the show to show the password
            entry_passwd_confirm.config(show='')
            entry_passwd_confirm.insert(0,e_passwd)

            #configure the button to change to hide button
            button_show_password_2.config(text='Hide')
            a.update()

            #setting the counter value to True
            truth_password_signin_2=5

        elif truth_password_signin_2==5:
            #getting the password
            e_passwd=entry_passwd_confirm.get()
            entry_passwd_confirm.delete(0,END)

            #getting the show to show the password
            entry_passwd_confirm.config(show='*')
            entry_passwd_confirm.insert(0,e_passwd)

            #configure the button to change to hide button
            button_show_password_2.config(text='Show')
            a.update()

            #setting the counter value to True
            truth_password_signin_2=4 
        

#loading window
'''creating the loading bar
for the login window'''
def loading_progress(event):
    global progress_bar,d
    d=Tk()
    d.title('LOADING')
    d.geometry('500x200')
    d.configure(background='white')

    #creating the progress bar
    progress_bar=ttk.Progressbar(d,orient=HORIZONTAL,length=400,mode='determinate')
    label=Label(d,text='Please wait\nfor a few seconds..',bg='white',fg='black',font=('Courier',16))

    #placing the progress bar
    progress_bar.place(relx=0.1,rely=0.6)
    label.place(relx=0.25,rely=0.2)

    step_add()

#step up 
'''function that gets the data from login() function
and helps in using the progress bar'''
def step_add():
    global e_username,e_password

    #getting the data from the entry widgets
    e_username=entry_username.get()
    e_password=entry_passwd.get()

    #deleting the data in teh entry widget
    entry_username.delete(0,END)
    entry_passwd.delete(0,END)

    #incrementing the progress bar to increase
    for i in range(5):
        progress_bar['value']+=20
        d.update()
        time.sleep(1)

    d.destroy()
    submit_log_in()

#submit_log_in
'''function to check for the correct password and username
and have a counter of 3 incorrect attempts to kill the program'''
def submit_log_in():
    global incorrect_passwd_count
    
    if incorrect_passwd_count>=3:
        quit()
    
    #checking if the username and password is same or not    
    elif [e_username,e_password] not in list_username_passwd:
        incorrect_passwd_count+=1
        error_unmatched_passwordorusername()

    elif [e_username,e_password] in list_username_passwd:
        a.destroy()
        mainpg()
    

#3.Sign in  Window
'''function signin() is used to for the user to
enter a new password and username'''
def signin():
    global entry_username,entry_passwd,entry_passwd_confirm,button_show_password_1,button_show_password_2  #making these variables global
    
    a.title('Signup')   #creating a title for the tk window
    a.geometry('1000x667') #setting the tk window

    #creating the main heading frame
    main_heading = Frame(a,bg="#FFBB00",bd=5) 
    main_label = Label(main_heading, text="Sign-Up", bg='black', fg='white', font=('elephant',25,'bold')) #main label to go in the main frame

    #creating labels for on screen information
    label_username=Label(a,text='Enter Username:', bg='black', fg='white',font=('elephant',22)) 
    label_passwd=Label(a,text='Enter Password:', bg='black', fg='white',font=('elephant',22))
    label_confirm_passwd=Label(a,text='Enter Password Again:', bg='black', fg='white',font=('elephant',22))

    #creating entry widgets to get the required data    
    entry_username=Entry(a,width=35,borderwidth=5,bg='white',font=('courier',17))
    entry_passwd=Entry(a,show='*',width=35,borderwidth=5,bg='white',font=('courier',17))
    entry_passwd_confirm=Entry(a,show='*',width=35,borderwidth=5,bg='white',font=('courier',17))

    #creating the button widgets to perform certain functions
    button_submit=Button(a,text='Submit',bg='black',fg='white',font=('elephant',20),command=lambda:submit_sign_in(True))
    button_exit=Button(a,text='Exit',bg='black',fg='white',font=('elephant',20),command=lambda:[a.destroy(),firstpg()])
    button_show_password_1=Button(a,text='Show',bg='black',fg='white',font=('elephant',20),command=lambda:show_passwd('sign-in1'))
    button_show_password_2=Button(a,text='Show',bg='black',fg='white',font=('elephant',20),command=lambda:show_passwd('sign-in2'))

    a.bind("<Return>",submit_sign_in)

    #palcing all the widgets that have been created
    main_heading.place(relx=0.15,rely=0.1,relwidth=0.7,relheight=0.18)
    main_label.place(relx=0,rely=0,relwidth=1,relheight=1)

    label_username.place(relx=0.07,rely=0.35,relwidth=0.3,relheight=0.1)
    label_passwd.place(relx=0.07,rely=0.5,relwidth=0.3,relheight=0.1)
    label_confirm_passwd.place(relx=0.07,rely=0.65,relwidth=0.4,relheight=0.1)

    entry_username.place(relx=0.5,rely=0.35,relwidth=0.45,relheight=0.1)
    entry_passwd.place(relx=0.5,rely=0.5,relwidth=0.35,relheight=0.1)
    entry_passwd_confirm.place(relx=0.5,rely=0.65,relwidth=0.35,relheight=0.1)

    button_exit.place(relx=0.6,rely=0.85,relwidth=0.2,relheight=0.1)
    button_submit.place(relx=0.2,rely=0.85,relwidth=0.2,relheight=0.1)
    button_show_password_1.place(relx=0.85,rely=0.5,relwidth=0.1,relheight=0.1)
    button_show_password_2.place(relx=0.85,rely=0.65,relwidth=0.1,relheight=0.1)
    
    a.mainloop() #making the loop run infinitely

'''function to get the information from the entry widgets from sign in window
and to check if the password and confirmed password is same'''
def submit_sign_in(event):
    #getting the data from entry widget
    e_username=entry_username.get()
    e_passwd=entry_passwd.get()
    e_passwd_confirm=entry_passwd_confirm.get()

    #deleting the data in the entry widgets
    entry_username.delete(0,END)
    entry_passwd.delete(0,END)
    entry_passwd_confirm.delete(0,END)

    if len(e_username)<4 or len(e_passwd)<6 or len(e_passwd_confirm)<6:
        error_passwd_short()
    if len(e_passwd)>=6 and len(e_passwd_confirm)>=6:
        #checking if the passwords are same
        if e_passwd!=e_passwd_confirm:
            not_correct_passwd()
            
        #appending password and username to a text file if they match
        elif e_passwd==e_passwd_confirm:
            x=open('passwords.txt','a')
            
            x.write(str(e_username))
            x.write(' ')
            x.write(str(e_passwd))
            x.write('\n')

            list_username_passwd.append([e_username,e_passwd])
            x.close()
            username_added_confirmation()

#4.Main Window
def mainpg():
    global y,count
    
    y=Tk() 
    y.title('library') #setting title for the window
    y.geometry('1000x667') #setting size of the window

    #setting background image
    my_pic=Image.open('images/bg3.jpg')
    resized=my_pic.resize((1000,667),Image.ANTIALIAS)
    new=ImageTk.PhotoImage(resized)
    label=Label(y,image=new)
    label.pack()
        
    #creating and placing frames
    hf = Frame(y,bg="#FFBB00",bd=5)
    hf.place(relx=0.15,rely=0.1,relwidth=0.7,relheight=0.18)
    time_frame=Frame(y,bg='grey',bd=5)
    time_frame.place(relx=0,rely=0.95,relwidth=1,relheight=0.1)
    button_frame=Frame(y,bg='black',bd=5)
    button_frame.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.51)
    headingLabel = Label(hf, text="DPS South Library", bg='black', fg='white', font=('elephant',27))
    headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

    import clock
    clock.clock(time_frame)

    '''creation of the menu bar widgets'''
    #1.main task bar
    mainpg_menu=Menu(y,tearoff=False)
    y.config(menu=mainpg_menu)

    #2.file menu
    file_menu=Menu(mainpg_menu)
    mainpg_menu.add_cascade(label='File_',menu=file_menu)
    file_menu.add_command(label='Logout',command=lambda:[y.destroy(),firstpg()])
    file_menu.add_separator()
    file_menu.add_command(label='Quit',command=y.destroy)

    #3.Member menu
    member_menu=Menu(mainpg_menu)
    mainpg_menu.add_cascade(label="Member_",menu=member_menu)
    member_menu.add_command(label='Add Member',command=lambda:[y.destroy(),add_member()])
    member_menu.add_command(label='Delete Member',command=lambda:[y.destroy(),delete_member()])

    #3.search menu
    search_menu=Menu(mainpg_menu)
    mainpg_menu.add_cascade(label="Search_",menu=search_menu)
    search_menu.add_command(label='Book list         Ctrl+B',command=lambda:[disp_book(True)])
    search_menu.add_command(label='Member list       Ctrl+M',command=lambda:[disp_member(True)])
    search_menu.add_command(label='Issued Books',command=lambda:[y.destroy(),disp_member_books()])

    #binding the keys
    y.bind("<Control-Key-B>",disp_book)
    y.bind("<Control-Key-M>",disp_member)
    
    #creating buttons
    button_add=Button(button_frame,text='Add Book',bg='black',fg='white',font=('elephant',20),command=lambda:[hf.destroy(),button_frame.destroy(),add()])
    button_delete=Button(button_frame,text='Delete Book',bg='black',fg='white',font=('elephant',20),command=lambda:[hf.destroy(),button_frame.destroy(),delete()])
    button_update=Button(button_frame,text='Update Book',bg='black',fg='white',font=('elephant',20),command=lambda:[hf.destroy(),button_frame.destroy(),update()])
    button_issue=Button(button_frame,text='Issue Book',bg='black',fg='white',font=('elephant',20),command=lambda:[hf.destroy(),button_frame.destroy(),issue()])
    button_return=Button(button_frame,text='Return Book',bg='black',fg='white',font=('elephant',20),command=lambda:[hf.destroy(),button_frame.destroy(),returnn()])
    button_quit=Button(button_frame,text='Exit',bg='black',fg='white',font=('elephant',20),command=y.destroy)

    #placing buttons
    button_add.place(relx=0,rely=0,relwidth=1,relheight=0.2)
    button_delete.place(relx=0,rely=0.2,relwidth=1,relheight=0.2)
    button_update.place(relx=0,rely=0.4,relwidth=1,relheight=0.2)
    button_issue.place(relx=0,rely=0.6,relwidth=1,relheight=0.2)
    button_return.place(relx=0,rely=0.8,relwidth=1,relheight=0.2)


    y.mainloop()

'''function to let the user enter the new members to the system'''
def add_member():
    global clicked1,clicked2,name,frame,x,clicked1,clicked2

    x=Tk()
    x.title('Add Member') #setting title for window
    x.geometry('1000x667')#setting size for window

    #background image
    my_pic=Image.open('images/member.jpg')
    resized=my_pic.resize((1000,667),Image.ANTIALIAS)
    new=ImageTk.PhotoImage(resized)
    label=Label(x,image=new)
    label.pack()

    
    #creating frames
    frame=Frame(x,bg='black',bd=5)
    headingFram=Frame(x,bg="#FFBB00",bd=5)

    #creating quit and submit buttons
    button_quit=Button(x,text='Exit',bg='black',fg='white',font=('elephant',15),command=lambda:[x.destroy(),mainpg()])
    button_submit=Button(x,text='Submit',bg='black',fg='white',font=('elephant',14),command=lambda:addmember_submit())

    #creating labels
    label=Label(headingFram,text='Add Member',bg='black',fg='white',font=('elephant',25))
    label1=Label(frame,text='Name:',bg='black',fg='white',font=('elephant',17))
    label2=Label(frame,text='Class:',bg='black',fg='white',font=('elephant',17))
    label3=Label(frame,text='Section:',bg='black',fg='white',font=('elephant',17))

    name=Entry(frame,font=('courier',17),width=35,borderwidth=3,bg='white')

    #creating dropdown menu options list
    class_options=['VIII','IX','X','XI','XII']
    section_options=['A','B','C','D','E','F','G','H']

    #creating tkinter variables
    clicked1=StringVar()
    clicked1.set('select')   
    clicked2=StringVar()
    clicked2.set('select')

    #creating dropdown menus
    classs=OptionMenu(frame,clicked1,*class_options)
    section=OptionMenu(frame,clicked2,*section_options)      

    #placing frames and buttons
    frame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    headingFram.place(relx=0.2,rely=0.02,relwidth=0.6,relheight=0.16)
    label.place(relx=0,rely=0,relwidth=1,relheight=1)
    label1.place(relx=0.03,rely=0.29,relwidth=0.2,relheight=0.1)
    label2.place(relx=0.03,rely=0.55,relwidth=0.2,relheight=0.1)
    label3.place(relx=0.03,rely=0.81,relwidth=0.2,relheight=0.1)
   
    name.place(relx=0.48,rely=0.29,relwidth=0.5,relheight=0.12)
    classs.place(relx=0.48,rely=0.55,relwidth=0.3,relheight=0.1)
    section.place(relx=0.48,rely=0.81,relwidth=0.3,relheight=0.1)
    
    
    button_quit.place(relx=0.6,rely=0.85,relwidth=0.2,relheight=0.1)
    button_submit.place(relx=0.20,rely=0.85,relwidth=0.2,relheight=0.1)
    y.mainloop()

'''function to get the entries of the new member from the user'''
def addmember_submit():
    
    #fetching values from add_member
    name_member=name.get()
    clas=clicked1.get()
    section=clicked2.get()    
    Maxlen=max(lst_memberid)

    #resetting values
    name.delete(0,END)
    clicked1.set('Select')
    clicked2.set('Select')

    for i in range(1,len(lst_memberid)+1):
        if i==int(Maxlen[1:]):
            member_id='M'+str(i+1)
            break
        
        elif i!=int(lst_memberid[i-1][1:]):
            print(int(lst_memberid[i-1][1:]))
            member_id='M'+str(i)
            break
        
    #adding information to database
    c_addmember=con.cursor()
    st='insert into members values("%s","%s","%s","%s")'%(member_id,name_member,clas,section)
    c_addmember.execute(st)
    lst_memberid.append(member_id)
    
    con.commit()

    confirm_memberadded()


'''function that allows the user to delete members'''
def delete_member():
    global delete_entry,x
    x=Tk()
    x.title('Delete Member') #setting title for the window
    x.geometry('1000x667') #setting size of the window

    #background image
    my_pic=Image.open('images/image.jpg')
    resized=my_pic.resize((1000,667),Image.ANTIALIAS)
    new=ImageTk.PhotoImage(resized)
    label=Label(x,image=new)
    label.pack()

    #creating frames
    frame=Frame(x,bg='black',bd=5)
    headingFram=Frame(x,bg="#FFBB00",bd=5)

    #creating the submit and quit button
    button_quit=Button(x,text='Exit',bg='black',fg='white',font=('elephant',15),command=lambda:[x.destroy(),mainpg()])
    button_submit=Button(x,text='Submit',bg='black',fg='white',font=('elephant',14),command=lambda:deletemember_submit())

    #creating labels
    label=Label(headingFram,text='Delete Member',bg='black',fg='white',font=('elephant',25))
    label1=Label(frame,text='Member id:',bg='black',fg='white',font=('elephant',20))

    #entry widget
    delete_entry=Entry(frame,width=35,borderwidth=3,bg='white',font=('courier',17))

    #placing frames and labels
    frame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    headingFram.place(relx=0.2,rely=0.02,relwidth=0.6,relheight=0.16)
    label.place(relx=0,rely=0,relwidth=1,relheight=1)
    label1.place(relx=0,rely=0.4,relwidth=0.35,relheight=0.2)
    delete_entry.place(relx=0.44,rely=0.4,relwidth=0.5,relheight=0.15)
    
    button_quit.place(relx=0.6,rely=0.85,relwidth=0.2,relheight=0.1)
    button_submit.place(relx=0.20,rely=0.85,relwidth=0.2,relheight=0.1)
    
    x.mainloop()

'''function to delete the member IDs'''
def deletemember_submit():
    #getting data
    e=delete_entry.get()
    print(e)
    #resetting variables
    delete_entry.delete(0,END)

    print(lst_memberid)
    #displaying error window
    if e not in lst_memberid:
        error_nomemberid()

    elif e in lst_memberid:

        for i in range(len(lst_issued_book)):
            

            if e==lst_issued_book[i][1]:
               
                error_memberhas_book()

            elif e!=lst_issued_book[i][1]:
                c_delete=con.cursor()
                
                #sql query to delete the member
                st='delete from members where member_id="%s"'%(e)
                c_delete.execute(st)

                #removing the book id from the lst
                lst_memberid.remove(e)
                con.commit()

                confirm_deletedmember()

        else:
                c_delete=con.cursor()
                
                #sql query to delete the member
                st='delete from members where member_id="%s"'%(e)
                c_delete.execute(st)

                #removing the book id from the lst
                lst_memberid.remove(e)
        
                con.commit()

                confirm_deletedmember()


'''function that allows us to see a list of books'''
def disp_book(e):
    global listb,search_entry
    y.destroy()
    
    w=Tk()
    w.title('Book list')
    w.geometry('600x667')

    frme=Frame(w,bg='black',bd=5)
    label=Label(frme,text='Book List',bg='black',fg='white',font=('elephant',25))
    frme.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.2)
    label.place(relx=0,rely=0,relwidth=1,relheight=1)

    frame=Frame(w)
    scroll=Scrollbar(frame,orient=VERTICAL)

    listb=Listbox(frame,font=('elephant',20),width=60,yscrollcommand=scroll.set)

    scroll.config(command=listb.yview)
    scroll.pack(ipady=100,side=RIGHT,fill=Y)
    frame.place(relx=0,rely=0.4,relwidth=1,relheight=0.4)

    listb.pack(ipadx=50,ipady=100)

    c_search=con.cursor()
    st='select book_id, book_name from books'
    c_search.execute(st)
    variable=c_search.fetchall()
    for i in variable:
        x=str(i[0])+'-'+str(i[1])
        listb.insert(END,x)

    button_moreinfo=Button(w,text='info',bg='black',fg='white',font=('elephant',20),command=lambda:[moreinfo_books(True)])
    button_cancel=Button(w,text='exit',bg='black',fg='white',font=('elephant',20),command=lambda:[w.destroy(),mainpg()])
    search_entry=Entry(w,font=('courier',25),width=35,borderwidth=3,bg='white')
    search_button=Button(w,text="Search",bg='white',font=('courier',12),command=lambda:[search('book')])

    listb.bind('<Double-1>',moreinfo_books)    
        
    button_moreinfo.place(relx=0.1,rely=0.85,relwidth=0.3,relheight=0.1)
    button_cancel.place(relx=0.6,rely=0.85,relwidth=0.3,relheight=0.1)
    search_entry.place(relx=0.15,rely=0.3,relwidth=0.6 ,relheight=0.06)
    search_button.place(relx=0.75,rely=0.3,relwidth=0.1,relheight=0.06)

    w.mainloop()

def search(m):

    if m=='book':
        e=search_entry.get()
        search_entry.delete(0,END)
        listb.delete(0,END)
        
        c_search=con.cursor()
        st='select book_id, book_name from books where book_name like "%{e1}%"'.format(e1=e)
        c_search.execute(st)
        variable=c_search.fetchall()
        for i in variable:
            x=str(i[0])+'-'+str(i[1])
            listb.insert(END,x)
           
        con.commit()

    elif m=='member':
        e=search_entry_member.get()
        search_entry_member.delete(0,END)
        listb.delete(0,END)

        c_search=con.cursor()
        st='select member_id, member_name from members where member_name like "%{e1}%"'.format(e1=e)
        c_search.execute(st)
        variable=c_search.fetchall()
        for i in variable:
            x=str(i[0])+'-'+str(i[1])
            listb.insert(END,x)
            
def moreinfo_books(event):
    global q
    
    try:
        if q.state()=='normal':
            pass
            
            #info_window_open()

    except Exception:
        q=Tk()
        q.title('Book Info')
        q.geometry('600x600')
        q.config(bg='black')
                
        e1=listb.get(ANCHOR)
        e1=e1.split('-')
        
        #getting a  list of all the book_ids
        c_search_book=con.cursor()
        st='select * from books where book_id="%s"'%(e1[0])
        c_search_book.execute(st)

        tupl=c_search_book.fetchall()
        list_search_book=list(tupl)
        
        for j in range(len(list_search_book)):
            if list_search_book[j][0]==e1[0]:
                Book_index=j
            else:
                continue

        #getting the list of members who have borrowed the book
        c_memberborrowbook=con.cursor()
        st='select m.member_id,m.member_name from members m,issued_books i where m.member_id=i.member_id and i.book_id="%s"'%(e1[0])
        c_memberborrowbook.execute(st)

        tuple_memberborrowed=c_memberborrowbook.fetchall()
        list_memberborrowed=[]

        #converting the list into a tuple
        for k in tuple_memberborrowed:
                list_memberborrowed.append(list(k))           

        list_memberborrowed.sort()
        
        #creating of the list box as well as the scrollbar
        frame_book=Frame(q)
        scroll=Scrollbar(frame_book,orient=VERTICAL)

        list_book=Listbox(frame_book,font=('elephant',16),width=60,yscrollcommand=scroll.set)

        scroll.config(command=listb.yview)
        scroll.pack(ipady=100,side=RIGHT,fill=Y)
        frame_book.place(relx=0.08,rely=0.65,relwidth=0.4,relheight=0.3)

        list_book.pack(ipadx=50,ipady=100)
        
        #checking if any one has borrowed the book
        if list_memberborrowed==[]:
            list_book.insert(END,'No borrowers!!')

        else:
            for i in list_memberborrowed:
                st=i[0]+'-'+i[1]
                list_book.insert(END,st)
                

        #getting a count of the books in the issued_books table
        c_search_bookcount=con.cursor()
        st='select count(book_id) from issued_books where book_id="%s"'%(e1[0])
        c_search_bookcount.execute(st)
        count_tuple=c_search_bookcount.fetchall()
        count=[]
        for i in count_tuple:
            count.append(i[0])

        frame_bookid=Frame(q,bg='#FFD700',bd=5)
        frame_bookname=Frame(q,bg='black',bd=5)
        frame_authorname=Frame(q,bg='black',bd=5)
        frame_borrowed_number=Frame(q,bg='black',bd=5)
        
        #creating all the labels for the more info page
        label_bookid=Label(frame_bookid,text=list_search_book[Book_index][0],bg='black',fg='yellow',font=('elephant',40,'bold'))
        label_book_name=Label(frame_bookname,text="Book Name:",bg='black',fg='yellow',font=('elephant',20,'bold'))
        label_bookname=Label(frame_bookname,text=list_search_book[Book_index][1],bg='black',fg='white',font=('elephant',18,'bold'))
        label_book_author=Label(frame_authorname,text="Book Author:",bg='black',fg='yellow',font=('elephant',20,'bold'))
        label_bookauthor=Label(frame_authorname,text=list_search_book[Book_index][2],bg='black',fg='white',font=('elephant',16,'bold'))
        label_number_books=Label(frame_borrowed_number,text="Number of books\n left:",bg='black',fg='yellow',font=('elephant',20,'bold'))
        label_numberbooks_left=Label(frame_borrowed_number,text=str(list_search_book[Book_index][3]-count[0])+' Books',bg='black',fg='white',font=('elephant',16,'bold'))
        label_borrowed_by=Label(q,text='Borrowed by:',bg='black',fg='yellow',font=('elephant',20,'bold'))
        
        frame_bookid.place(relx=0.1,rely=0.015,relwidth=0.8,relheight=0.2)
        frame_bookname.place(relx=0.08,rely=0.245,relwidth=0.4,relheight=0.3)
        frame_authorname.place(relx=0.52,rely=0.245,relwidth=0.4,relheight=0.3)
        frame_borrowed_number.place(relx=0.52,rely=0.55,relwidth=0.4,relheight=0.3)
        label_bookid.place(relx=0,rely=0,relwidth=1,relheight=1)
        label_book_name.place(relx=0,rely=0.2,relwidth=1,relheight=0.25)
        label_book_author.place(relx=0,rely=0.2,relwidth=1,relheight=0.25)
        label_borrowed_by.place(relx=0.08,rely=0.55,relwidth=0.4,relheight=0.1)
        label_number_books.place(relx=0,rely=0.1,relwidth=1,relheight=0.33)
        
        label_bookname.place(relx=0,rely=0.6,relwidth=1,relheight=0.2)
        label_bookauthor.place(relx=0,rely=0.6,relwidth=1,relheight=0.2)
        label_numberbooks_left.place(relx=0,rely=0.5,relwidth=1,relheight=0.33)

        button_exit=Button(q,text='Exit',command=q.destroy)

        button_exit.place(relx=0.7,rely=0.85,relwidth=0.15,relheight=0.1)
        
        q.mainloop()

'''function that allows us to see a list of members'''
def disp_member(e):
    global listb,search_entry_member
    y.destroy()
    
    w=Tk()
    w.title('Member list')
    w.geometry('600x667')

    frme=Frame(w,bg='black',bd=5)
    label=Label(frme,text='Member List',bg='black',fg='white',font=('elephant',25))
    frme.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.2)
    label.place(relx=0,rely=0,relwidth=1,relheight=1)

    frame=Frame(w)
    scroll=Scrollbar(frame,orient=VERTICAL)

    listb=Listbox(frame,font=('elephant',20),width=60,yscrollcommand=scroll.set)

    scroll.config(command=listb.yview)
    scroll.pack(ipady=100,side=RIGHT,fill=Y)
    frame.place(relx=0,rely=0.4,relwidth=1,relheight=0.4)

    listb.pack(ipadx=50,ipady=100)

    c_search=con.cursor()
    st='select member_id,member_name from members'
    c_search.execute(st)
    variable=c_search.fetchall()
    for i in variable:
        x=str(i[0])+'-'+str(i[1])
        listb.insert(END,x)

    button_moreinfo=Button(w,text='info',bg='black',fg='white',font=('elephant',20),command=lambda:[moreinfo_members(True)])
    button_cancel=Button(w,text='exit',bg='black',fg='white',font=('elephant',20),command=lambda:[w.destroy(),mainpg()])
    search_entry_member=Entry(w,font=('courier',25),width=35,borderwidth=3,bg='white')
    search_button=Button(w,text="Search",bg='white',font=('courier',12),command=lambda:[search('member')])

    listb.bind('<Double-1>',moreinfo_members)    
        
    button_moreinfo.place(relx=0.1,rely=0.85,relwidth=0.3,relheight=0.1)
    button_cancel.place(relx=0.6,rely=0.85,relwidth=0.3,relheight=0.1)
    search_entry_member.place(relx=0.15,rely=0.3,relwidth=0.6 ,relheight=0.06)
    search_button.place(relx=0.75,rely=0.3,relwidth=0.1,relheight=0.06)
    
    w.mainloop()

def moreinfo_members(event):
    global q
    
    try:
        if q.state()=='normal':
            pass

    except Exception:
        q=Tk()
        q.title('Book Info')
        q.geometry('600x600')
        q.config(bg='black')
                
        e1=listb.get(ANCHOR)
        e1=e1.split('-')

        #getting a  list of all the book_ids
        c_search_member=con.cursor()
        st='select * from members where member_id="%s"'%(e1[0])
        c_search_member.execute(st)

        tupl=c_search_member.fetchall()
        list_search_member=list(tupl)
        
        for j in range(len(list_search_member)):
            if list_search_member[j][0]==e1[0]:
                Member_index=j
            else:
                continue

        #getting the list of members who have borrowed the book
        c_bookborrowed=con.cursor()
        st='select i.book_id,b.book_name from issued_books i,books b where i.book_id=b.book_id and i.member_id="%s"'%(e1[0])
        c_bookborrowed.execute(st)

        tuple_bookborrowed=c_bookborrowed.fetchall()
        list_bookborrowed=[]

        #converting the list into a tuple
        for k in tuple_bookborrowed:
                list_bookborrowed.append(list(k))           

        list_bookborrowed.sort()
        
        #creating of the list box as well as the scrollbar
        frame_book=Frame(q)
        scroll=Scrollbar(frame_book,orient=VERTICAL)

        list_book=Listbox(frame_book,font=('elephant',16),width=60,yscrollcommand=scroll.set)

        scroll.config(command=listb.yview)
        scroll.pack(ipady=100,side=RIGHT,fill=Y)
        frame_book.place(relx=0.08,rely=0.65,relwidth=0.4,relheight=0.3)

        list_book.pack(ipadx=50,ipady=100)
        
        #checking if any one has borrowed the book
        if list_bookborrowed==[]:
            list_book.insert(END,'No books\n borrowed!!')

        else:
            for i in list_bookborrowed:
                st=i[0]+'-'+i[1]
                list_book.insert(END,st)

        main_frame=Frame(q,bg='#FFD700',bd=5)
        frame_memberid=Frame(q,bg='black',bd=5)
        frame_membername=Frame(q,bg='black',bd=5)
        frame_section=Frame(q,bg='black',bd=5)
        
        #creating all the labels for the more info page
        main_label=Label(main_frame,text='Member Info',bg='black',fg='yellow',font=('elephant',25,'bold'))
        label_member_id=Label(frame_memberid,text='Member ID:',bg='black',fg='yellow',font=('elephant',20,'bold'))
        label_member_name=Label(frame_membername,text='Member Name:',bg='black',fg='yellow',font=('elephant',20,'bold'))
        label_section_head=Label(frame_section,text='Member Section:',bg='black',fg='yellow',font=('elephant',20,'bold'))
        label_borrowed=Label(q,text='Books Borrowed:',bg='black',fg='yellow',font=('elephant',20,'bold'))

        label_memberid=Label(frame_memberid,text=list_search_member[Member_index][0],bg='black',fg='white',font=('elephant',17,'bold'))
        label_membername=Label(frame_membername,text=list_search_member[Member_index][1],bg='black',fg='white',font=('elephant',17,'bold'))
        label_section=Label(frame_section,text=str(list_search_member[Member_index][2]+'-'+list_search_member[Member_index][3]),bg='black',fg='white',font=('elephant',17,'bold'))

        main_frame.place(relx=0.1,rely=0.015,relwidth=0.8,relheight=0.2)
        frame_memberid.place(relx=0.08,rely=0.245,relwidth=0.4,relheight=0.3)
        frame_membername.place(relx=0.52,rely=0.245,relwidth=0.4,relheight=0.3)
        frame_section.place(relx=0.52,rely=0.55,relwidth=0.4,relheight=0.3)
        
        main_label.place(relx=0,rely=0,relwidth=1,relheight=1)
        label_member_id.place(relx=0,rely=0.2,relwidth=1,relheight=0.25)
        label_member_name.place(relx=0,rely=0.2,relwidth=1,relheight=0.25)
        label_borrowed.place(relx=0.08,rely=0.55,relwidth=0.4,relheight=0.1)
        label_section_head.place(relx=0,rely=0.001,relwidth=1,relheight=0.33)

        label_memberid.place(relx=0,rely=0.6,relwidth=1,relheight=0.2)
        label_membername.place(relx=0,rely=0.6,relwidth=1,relheight=0.2)
        label_section.place(relx=0,rely=0.401,relwidth=1,relheight=0.33)

        button_exit=Button(q,text='Exit',command=q.destroy)

        button_exit.place(relx=0.7,rely=0.85,relwidth=0.15,relheight=0.1)        
               
        q.mainloop()
        


'''function that allows us to see a list of issued books'''
def disp_member_books():
    import tree
    cursor=con.cursor()
    st='select * from issued_books'
    cursor.execute(st)
    data=cursor.fetchall()

    tree.polo(data)

    mainpg()


#secondaty window
#1.Add window
def add():
    global entry_add1,entry_add2,entry_add3,entry_add4
    
    y.title('Add book')#setting title
    y.geometry('1000x667') #setting size of window

    #setting background image
    my_pic=Image.open('images/bg3.jpg')
    resized=my_pic.resize((1000,667),Image.ANTIALIAS)
    new=ImageTk.PhotoImage(resized)
    label=Label(y,image=new)
    label.pack()

    #creating frames
    frame=Frame(y,bg='black',bd=5)
    topfram = Frame(y,bg="#FFBB00",bd=5)

    label=Label(topfram,text='Add Book',bg='black',fg='white',font=('elephant',25))
    label1=Label(frame,text="Book's Name:",bg='black',fg='white',font=('elephant',20))
    label2=Label(frame,text="Book's Author:",bg='black',fg='white',font=('elephant',20))
    label3=Label(frame,text='Number of books:',bg='black',fg='white',font=('elephant',20))

    #creating entry widgets
    entry_add1=Entry(frame,font=('courier',17),width=35,borderwidth=3,bg='white')
    entry_add2=Entry(frame,font=('courier',17),width=35,borderwidth=3,bg='white')
    entry_add3=Entry(frame,font=('courier',17),width=35,borderwidth=3,bg='white')

    #placing all widgets
    frame.place(relx=0.1,rely=0.27,relwidth=0.8,relheight=0.5)
    topfram.place(relx=0.2,rely=0.02,relwidth=0.6,relheight=0.16)
    label.place(relx=0,rely=0,relwidth=1,relheight=1)

    label1.place(relx=0.03,rely=0.2,relwidth=0.23,relheight=0.1)
    label2.place(relx=0.03,rely=0.45,relwidth=0.26,relheight=0.1)
    label3.place(relx=0.03,rely=0.7,relwidth=0.3,relheight=0.1)
        
    entry_add1.place(relx=0.45,rely=0.2,relwidth=0.5,relheight=0.12)
    entry_add2.place(relx=0.45,rely=0.45,relwidth=0.5,relheight=0.12)
    entry_add3.place(relx=0.45,rely=0.7,relwidth=0.5,relheight=0.12)

    #creating exit and submit buttons
    button_quit=Button(y,text='Exit',bg='black',fg='white',font=('elephant',14),command=lambda:[y.destroy(),mainpg()])
    button_submit=Button(y,text='Submit',bg='black',fg='white',font=('elephant',14),command=add_submit) 

    #placing buttons
    button_quit.place(relx=0.6,rely=0.85,relwidth=0.2,relheight=0.1)
    button_submit.place(relx=0.2,rely=0.85,relwidth=0.2,relheight=0.1)

    y.mainloop()

#submit for add button    
def add_submit(): 
    '''string values which are entered'''
    e1=entry_add1.get()
    e2=entry_add2.get()
    e3=entry_add3.get()

    #resetting values
    entry_add1.delete(0,END)
    entry_add2.delete(0,END)
    entry_add3.delete(0,END)
    Max_bookid = ''

    if (len(lst_bookid) == 0):
        book_id = 'B1'

    else:
        Max_bookid=max(lst_bookid)
    
    for i in range(1,len(lst_bookid)+1):
        if i==int(Max_bookid[1:]):
            book_id='B'+str(i+1)
            break
        
        elif i!=int(lst_bookid[i-1][1:]):
            book_id='B'+str(i)
            break
        
    print(book_id)
    lst_bookid.append(book_id)

    #adding information to database
    c_add=con.cursor()
    st='insert into books values("%s","%s","%s",%s)'%(book_id,e1,e2,e3)
    c_add.execute(st)
       
    con.commit()
    confirm_book_added()
    
    
#2.Delete window
def delete():
    global entry_delete1
    
    y.title('Delete book')#setting title
    y.geometry('1000x667')#setting size of window

    #setting background
    my_pic=Image.open('images/bg3.jpg')
    resized=my_pic.resize((1000,667),Image.ANTIALIAS)
    new=ImageTk.PhotoImage(resized)
    label=Label(y,image=new)
    label.pack()

    #creating main frames
    frame=Frame(y,bg='black',bd=5)
    topfram = Frame(y,bg="#FFBB00",bd=5)
    
    #creating exit and submit buttons
    button_quit=Button(y,text='Exit',bg='black',fg='white',font=('elephant',15),command=lambda:[y.destroy(),mainpg()])
    button_submit=Button(y,text='Submit',bg='black',fg='white',font=('elephant',14),command=delete_submit)

    #creating labels
    label=Label(topfram,text='Delete book',bg='black',fg='white',font=('elephant',25))
    label1=Label(frame,text='Enter Book ID:',bg='black',fg='white',font=('elephant',17))

    entry_delete1=Entry(frame,width=35,borderwidth=3,bg='white',font=('courier',17))

    #placing widgets
    frame.place(relx=0.1,rely=0.25,relwidth=0.8,relheight=0.5)
    topfram.place(relx=0.2,rely=0.02,relwidth=0.6,relheight=0.16)
    label.place(relx=0,rely=0,relwidth=1,relheight=1)
    label1.place(relx=0,rely=0.4,relwidth=0.35,relheight=0.2)
    entry_delete1.place(relx=0.44,rely=0.4,relwidth=0.5,relheight=0.15)

    button_quit.place(relx=0.6,rely=0.85,relwidth=0.2,relheight=0.1)
    button_submit.place(relx=0.20,rely=0.85,relwidth=0.2,relheight=0.1)
    y.mainloop()

'''function to delete books'''
def delete_submit():
    #getting data
    e1=entry_delete1.get()

    #list of all the books issued
    lat_bookissued=[]
    
    #resetting variables
    entry_delete1.delete(0,END)

    #displaying error window
    if e1 not in lst_bookid:
        error_nobookid()

    elif e1 in lst_bookid:

        for i in range(len(lst_issued_book)):
            

            if e1==lst_issued_book[i][0]:
                print('Not possible')
                error_book_isissued()

            elif e1!=lst_issued_book[i][0]:
                c_delete=con.cursor()
                
                #sql query to delete the books
                st='delete from books where book_id="%s"'%(e1)
                c_delete.execute(st)

                #removing the book id from the lst
                lst_bookid.remove(e1)
                con.commit()

                confirm_deletebook()

        else:
                c_delete=con.cursor()
                
                #sql query to delete the books
                st='delete from books where book_id="%s"'%(e1)
                c_delete.execute(st)

                #removing the book id from the lst
                lst_bookid.remove(e1)
                con.commit()

                confirm_deletebook()
            

#3.Update window
def update():
    global entry_update1,entry_update2
    
    y.title('Update Book')#setting title
    y.geometry('1000x667')#setting size of window

    #setting background image
    my_pic=Image.open('images/bg3.jpg')
    resized=my_pic.resize((1000,667),Image.ANTIALIAS)
    new=ImageTk.PhotoImage(resized)
    label=Label(y,image=new)
    label.pack()

    #creating frames
    frame=Frame(y,bg='black',bd=5)
    topfram = Frame(y,bg="#FFBB00",bd=5)

    #creating exit and submit buttons
    button_quit=Button(y,text='Exit',bg='black',fg='white',font=('elephant',15),command=lambda:[y.destroy(),mainpg()])
    button_submit=Button(y,text='Submit',bg='black',fg='white',font=('elephant',15),command=update_submit)

    #creating labels
    label=Label(topfram,text='Update number of books',bg='black',fg='white',font=('elephant',24))
    label1=Label(frame,text='Book ID:',bg='black',fg='white',font=('elephant',17))
    label2=Label(frame,text='New Number of Books:',bg='black',fg='white',font=('elephant',18))

    #creating entry widget
    entry_update1=Entry(frame,width=35,borderwidth=3,bg='white',font=('courier',17))
    entry_update2=Entry(frame,width=35,borderwidth=3,bg='white',font=('courier',17))

    #placing widgets
    frame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    topfram.place(relx=0.2,rely=0.02,relwidth=0.6,relheight=0.16)
    label.place(relx=0,rely=0,relwidth=1,relheight=1)
    label1.place(relx=0.03,rely=0.32,relwidth=0.2,relheight=0.1)
    label2.place(relx=0.041,rely=0.56,relwidth=0.36,relheight=0.25)

    entry_update1.place(relx=0.48,rely=0.29,relwidth=0.5,relheight=0.12)
    entry_update2.place(relx=0.48,rely=0.62,relwidth=0.5,relheight=0.12)

    button_quit.place(relx=0.6,rely=0.85,relwidth=0.2,relheight=0.1)
    button_submit.place(relx=0.20,rely=0.85,relwidth=0.2,relheight=0.1)
    y.mainloop()
    
def update_submit():
    
    #getting values
    e1=entry_update1.get()
    e2=entry_update2.get()
    
    #resetting variables
    entry_update1.delete(0,END)
    entry_update2.delete(0,END)

    if e1 not in lst_bookid:
        error_nobookid()
        
    elif e1 in lst_bookid:
        #adding information to database
        c_update=con.cursor()
        st='update books set no_of_books=%s where book_id="%s"'%(e2,e1)
        c_update.execute(st)

        con.commit()
        
    
#4.Issue window
def issue():
    global entry_issue1,entry_issue2,y
    
    y.title('Issue book')#setting title
    y.geometry('1000x667')#setting size of window
    
    #setting background image
    my_pic=Image.open('images/bg3.jpg')
    resized=my_pic.resize((1000,667),Image.ANTIALIAS)
    new=ImageTk.PhotoImage(resized)
    label=Label(y,image=new)
    label.pack()

    #creating frames
    frame=Frame(y,bg='black',bd=5)
    topfram = Frame(y,bg="#FFBB00",bd=5)

    #creating buttons
    button_quit=Button(y,text='Exit',bg='black',fg='white',font=('elephant',15),command=lambda:[y.destroy(),mainpg()])
    button_submit=Button(y,text='Submit',bg='black',fg='white',font=('elephant',14),command=issue_submit)

    #creating labels
    label=Label(topfram,text='Issue book',bg='black',fg='white',font=('elephant',25))
    label1=Label(frame,text='Book ID:',bg='black',fg='white',font=('elephant',17))
    label2=Label(frame,text='Member ID:',bg='black',fg='white',font=('elephant',17))

    #creating entry widgets
    entry_issue1=Entry(frame,width=35,borderwidth=3,bg='white',font=('courier',17))
    entry_issue2=Entry(frame,width=35,borderwidth=3,bg='white',font=('courier',17))

    #placing all widgets
    frame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    topfram.place(relx=0.2,rely=0.02,relwidth=0.6,relheight=0.16)
    label.place(relx=0,rely=0,relwidth=1,relheight=1)
    label1.place(relx=0.03,rely=0.29,relwidth=0.2,relheight=0.1)
    label2.place(relx=0.06,rely=0.62,relwidth=0.18,relheight=0.1)

    entry_issue1.place(relx=0.48,rely=0.29,relwidth=0.5,relheight=0.12)
    entry_issue2.place(relx=0.48,rely=0.62,relwidth=0.5,relheight=0.12)
    
    button_quit.place(relx=0.6,rely=0.85,relwidth=0.2,relheight=0.1)
    button_submit.place(relx=0.20,rely=0.85,relwidth=0.2,relheight=0.1)
    y.mainloop()

'''function to enter the issued books data into the table issued_books'''    
def issue_submit():
    # Textual month, day and year	
    #d2 = today.strftime("%B %d, %Y")
    
    e1=entry_issue1.get()
    e2=entry_issue2.get()
    Date=datetime.now()
    D=Date.strftime("%Y/%m/%d")

    entry_issue1.delete(0,END)
    entry_issue2.delete(0,END)

    if [e1,e2] in lst_issued_book:
        error_issuedbook_exists()

    elif [e1,e2] not in lst_issued_book:
        if e1 not in lst_bookid or e2 not in lst_memberid:
            no_book_member_exist()
        else:
            c_issue=con.cursor()
            c='insert into issued_books values("%s","%s","%s")'%(e1,e2,D)
            c_issue.execute(c)
            con.commit()
            lst_issued_book.append([e1,e2])

            confirm_book_issued()
                 
        
#returnn window
def returnn():
    global entry1,entry2,y
    
    y.title('Return book')#setting title
    y.geometry('1000x667')#setting size of window

    #setting background
    my_pic=Image.open('images/bg3.jpg')
    resized=my_pic.resize((1000,667),Image.ANTIALIAS)
    new=ImageTk.PhotoImage(resized)
    label=Label(y,image=new)
    label.pack()

    #creating frames
    frame=Frame(y,bg='black',bd=5)
    headingFram = Frame(y,bg="#FFBB00",bd=5)

    #creating exit and submit buttons
    button_quit=Button(y,text='Exit',bg='black',fg='white',font=('elephant',15),command=lambda:[y.destroy(),mainpg()])
    button_submit=Button(y,text='Submit',bg='black',fg='white',font=('elephant',14),command=lambda:return_submit())

    #creating labels
    label=Label(headingFram,text='Return book',bg='black',fg='white',font=('elephant',25))
    label1=Label(frame,text='Book ID:',bg='black',fg='white',font=('elephant',17))
    label2=Label(frame,text='Member ID:',bg='black',fg='white',font=('elephant',17))

    #creating entry widgets
    entry1=Entry(frame,width=35,borderwidth=3,bg='white',font=('courier',17))
    entry2=Entry(frame,width=35,borderwidth=3,bg='white',font=('courier',17))

    #placing widgets
    frame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    headingFram.place(relx=0.2,rely=0.02,relwidth=0.6,relheight=0.16)
    label.place(relx=0,rely=0,relwidth=1,relheight=1)
    label1.place(relx=0.03,rely=0.29,relwidth=0.2,relheight=0.1)
    label2.place(relx=0.06,rely=0.62,relwidth=0.18,relheight=0.1)

    entry1.place(relx=0.48,rely=0.29,relwidth=0.5,relheight=0.12)
    entry2.place(relx=0.48,rely=0.62,relwidth=0.5,relheight=0.12)

    button_quit.place(relx=0.6,rely=0.85,relwidth=0.2,relheight=0.1)
    button_submit.place(relx=0.20,rely=0.85,relwidth=0.2,relheight=0.1)
    y.mainloop()

    

def return_submit():
    global e1,e2
    
    e1=entry1.get()
    e2=entry2.get()

    entry1.delete(0,END)
    entry2.delete(0,END)

    if [e1,e2] not in lst_issued_book:
        error_no_borrow()

    elif [e1,e2] in lst_issued_book:
        
        lst_issued_book.remove([e1,e2])

        confirm_book_delete()

def quitt():
    return

#errors and confirmations
'''messagebox shows the password entered is less than
6 characters'''
def error_passwd_short():
    error_passwd_small=messagebox.askretrycancel('ERROR!!!','Username or Password must be 6 characters minimum!!')
    
'''messagebox that shows the error if the passwords dont match'''
def not_correct_passwd():
    error_notmatching=messagebox.askretrycancel('ERROR!!','Passwords dont match!!')

    if error_notmatching:
        return
    else:
        a.destroy()
        firstpg()

'''confirmation messagebox to show that the username and password have been added'''
def username_added_confirmation():
    confirm_added=messagebox.showinfo('CONFIRMED!!!!','Username and password have been added')

    if confirm_added:
        a.destroy()
        firstpg()

    else:
        a.destroy()
        firstpg()
        
'''messagebox to show the confirmation of correct username
and password'''
def error_unmatched_passwordorusername():
    error_incorrect_username_or_password=messagebox.askretrycancel('ERROR!!','Username or Password is \nincorrect!!')

def confirm_book_added():
    confirm_addbook=messagebox.showinfo('CONFIRMED!!!!','Book has been added')

    if confirm_addbook:
        y.destroy()
        mainpg()

def error_nobookid():
    error=messagebox.askretrycancel('ERROR!!','Book ID doesnt exist!!')

    if error:
        pass
    else:
        y.destroy()
        mainpg()
    

def confirm_deletebook():
    confirm_addbook=messagebox.showinfo('CONFIRMED!!!!','Book has been deleted')

    if confirm_addbook:
        y.destroy()
        mainpg()


def confirm_memberadded():
    c_memberadded=messagebox.showinfo('CONFIRMED!!!','The member ID has been created')
    x.destroy()
    mainpg()

def error_nomemberid():
    error=messagebox.askretrycancel('ERROR!!','Member ID doesnt exist!!')

    if error:
        pass
    else:
        x.destroy()
        mainpg()
        
    

def confirm_deletedmember():
    c_memberdeleted=messagebox.showinfo('CONFIRMED!!!','The member ID has been deleted')
    x.destroy()
    mainpg()

def error_issuedbook_exists():
    error=messagebox.askretrycancel("ERROR!!!",'A book is already issued to this member')

    if error:
        pass
    else:
        y.destroy()
        mainpg()

def confirm_book_issued():
    confirm=messagebox.showinfo("CONFIRMED!!!",'The book has been issued')

    if confirm:
        y.destroy()
        mainpg()

def error_book_isissued():
    error=messagebox.askretrycancel('ERROR!!','Book issued to a member!!')

    if error:
        pass
    else:
        y.destroy()
        mainpg()

def error_memberhas_book():
    error=messagebox.askretrycancel('ERROR!!','member has a book issued!!')
    
    if error:
        pass
    else:
        x.destroy()
        mainpg()

def error_no_borrow():
    error=messagebox.askretrycancel('Error!!!','Book has either not been borrowed or not been borrowed by this member..')

    if error:
        pass
    else:
        y.destroy()
        mainpg()

def no_book_member_exist():
    error=messagebox.askretrycancel('Error!!!','The following Book ID or Member ID does not exist')

def info_window_open():
    info=messagebox.info('Attention!!!','The window is already opened and more than one cannot be open')

    
def confirm_book_delete():

    c=con.cursor()
    st='select time_issued from issued_books where book_id="{}" and member_id="{}"'.format(e1,e2)
    c.execute(st)

    data=c.fetchall()
    
    lit=str(data[0][0]).split('-')
    date_issued=int(lit[2])
    month_issued=int(lit[1])
    year_issued=int(lit[0])

    fulldate_issued=str(date_issued)+'-'+str(month_issued)+'-'+str(year_issued)

    today_day=datetime.now()
    today_year=int(today_day.year)
    today_month=int(today_day.month)
    today_date=int(today_day.day)

    today=date.today()
    today=today.strftime('%d-%m-%Y')
    
    if data==():
        error_no_borrow()
        
    if (today_year-year_issued>=1) or (today_year-year_issued==0 and today_month-month_issued>=1) or (today_year-year_issued==0 and today_month-month_issued==0 and  today_date-date_issued>7):
        latesubmit=messagebox.showinfo('BOOK LATE!!!','The book is has been taken for more than 7 days\n Date of Issue: '+fulldate_issued+'\n'+'Date of Return: '+today)
        c_return=con.cursor()
        st='delete from issued_books where book_id="%s" and member_id="%s"'%(e1,e2)
        c_return.execute(st)

        con.commit()
        
    else:
        confirm=messagebox.showinfo('SUCCESS!!!','The book has been successfully returned..')
        c_return=con.cursor()
        st='delete from issued_books where book_id="%s" and member_id="%s"'%(e1,e2)
        c_return.execute(st)

        con.commit()

    y.destroy()
    mainpg()

        
#main
''' Commands to create the mysql tables:
1.Creating the table books:
    create table books(
    book_id varchar(6),
    book_name varchar(50),
    book_author varchar(50),
    no_of_books int,
    primary key(book_id)
    );

2.Creating the Members table:
    create table members(
    member_id varchar(15),
    member_name varchar(30),
    class varchar(5),
    section varchar(5),
    primary key(member_id)
    )

3.Creating the Issued books table:
    create table issued_books(
    book_id varchar(15),
    member_id varchar(15),
    time_issued date,
    foreign key(book_id) REFERENCES books(book_id),
    foreign key(member_id) REFERENCES members(member_id))'''


incorrect_passwd_count=0
we=True
truth_password_login=False
truth_password_signin_1=2
truth_password_signin_2=4

#database connector
con=n.connect(host='localhost',user='root',passwd='root123',database='project')

#to get a list of all the books
cursor_books=con.cursor()
q_books='select book_id from books'
cursor_books.execute(q_books)
tuple_books=cursor_books.fetchall()
lst_bookid=[]

for i in tuple_books:
    #list of all the book id
    lst_bookid.append(i[0])
    
#to get a list of all the members
cursor_members=con.cursor()
q_members='select member_id from members'
cursor_members.execute(q_members)
tuple_members=cursor_members.fetchall()
lst_memberid=[]

for i in tuple_members:
    #list of all the member ids
    lst_memberid.append(i[0])

cursor_issued_book=con.cursor()
q_issued_book='select * from issued_books'
cursor_issued_book.execute(q_issued_book)
tuple_issued_book=cursor_issued_book.fetchall()
lst_issued_book=[]


for i in tuple_issued_book:
    #list of all the member ids
    lst_issued_book.append(list(i[0:2]))
    
#passwords=open('passwords.txt','w')----->for text file
file=open('passwords.txt','r')
list_username_passwd=[]
for i in file:
    lst=i.split()
    list_username_passwd.append(lst)

file.close()

firstpg()
#mainpg()


    
    


    
