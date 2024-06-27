from tkinter import *
from tkinter import ttk
from tkinter.font import nametofont

def polo(t):
    global tree,search_entry,val,count
    root=Tk()
    root.geometry('800x700')
    root.title('Book Info')
    root.configure(background='black')

    val=t

    #creating of frame,labels and buttons
    heading_frame=Frame(root,bg="#FFBB00",bd=5)
    heading_frame.place(relx=0.15,rely=0.025,relwidth=0.7,relheight=0.15)

    headingLabel=Label(heading_frame, text='Issued Books', bg='black', fg='white', font=('elephant',25,'bold'))
    headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

    #button_info=Button(root,text='Info',bg='grey',fg='black',font=('elephant',20),command=issued_books_info)
    button_exit=Button(root,text='Exit',bg='grey',fg='black',font=('elephant',20),command=root.destroy)

    #button_info.place(relx=0.1,rely=0.85,relwidth=0.3,relheight=0.09)
    button_exit.place(relx=0.6,rely=0.885,relwidth=0.3,relheight=0.09)

    #creating the search bar
    search_entry=Entry(root,width=35,borderwidth=2,bg='white',font=('courier',17,'bold'))

    #creating the search button
    search_button=Button(root,text='Submit',bg='grey',fg='black',font=('elephant',14),command=search)

    search_entry.place(relx=0.2,rely=0.2,relwidth=0.525,relheight=0.075)
    search_button.place(relx=0.725,rely=0.2,relwidth=0.1,relheight=0.075)

    #create tree
    style=ttk.Style()

    style.theme_use("clam")

    style.configure("Treeview",
                    background="silver",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="silver"
                    )

    style.map('Treeview',
             background=[('selected','blue')])

    nametofont("TkHeadingFont").configure(size=16)

    tree_frame=Frame(root,bg='black')
    tree_frame.place(relx=0.1,rely=0.295,relwidth=0.8,relheight=0.58)

    scroll=Scrollbar(tree_frame)
    scroll.pack(side=RIGHT,fill=Y)

    tree=ttk.Treeview(tree_frame,yscrollcommand=scroll.set)

    tree.pack(expand=True,fill='both')

    scroll.config(command=tree.yview)


    #define column
    tree['columns']=('Book ID','Member ID','Date Borrowed')

    #format columns
    tree.column("#0",width=0,stretch=NO)
    tree.column("Book ID",anchor=W,width=200)
    tree.column("Member ID",anchor=CENTER,width=200)
    tree.column("Date Borrowed",anchor=W,width=200)

    #Creating Headings
    tree.heading("#0",text="",anchor=W)
    tree.heading("Book ID",text="Book ID",anchor=W)
    tree.heading("Member ID",text="Member ID",anchor=CENTER)
    tree.heading("Date Borrowed",text='Date Borrowed',anchor=W)


    #adding the striped colour
    tree.tag_configure('odd',background='white')
    tree.tag_configure('even',background='aqua')
    
    #add data
    count=0    
    for i in t:
        #adding the striped color
        if count%2==0:
            tree.insert(parent='',index='end',iid=count,text='',values=(i[0],i[1],i[2]),tags=('even',))

        else:
            tree.insert(parent='',index='end',iid=count,text='',values=(i[0],i[1],i[2]),tags=('odd',))
            
        count+=1
                

    tree.pack(pady=20)

    root.mainloop()

'''
def issued_books_info():
    global q

    selected=tree.selection()

    values=tree.item(selected,'values')

    try:
        if q.state()=='normal':
            pass

    except Exception:
        q=Tk()
        q.title('Issued Book')
        q.geometry('800x600')
        q.config(bg='black')

        #creating the labels
        main_heading = Frame(q,bg="#FFBB00",bd=5) 
        main_label = Label(main_heading, text="Book Info", bg='black', fg='white', font=('elephant',25,'bold'))

        #placing the labels
        main_heading.place(relx=0.15,rely=0.1,relwidth=0.7,relheight=0.18)
        main_label.place(relx=0,rely=0,relwidth=1,relheight=1)

'''



def search():
    global count
    #getting the values
    search_value=search_entry.get()
    
    #deleting the values
    search_entry.delete(0,END)


    #getting the new values
    lst=[]


    if len(search_value)==1:
        if search_value.upper()=='B' or search_value.upper()=='M':
            #deleting all the records
            for x in tree.get_children():
                tree.delete(x)
                
            for i in t:
                #adding the striped color
                if count%2==0:
                    tree.insert(parent='',index='end',iid=count,text='',values=(i[0],i[1],i[2]),tags=('even',))

                else:
                    tree.insert(parent='',index='end',iid=count,text='',values=(i[0],i[1],i[2]),tags=('odd',))
            
                count+=1

        else:
            pass

    elif search_value[0].upper()=='B' and search_value[1:].isnumeric()==True:

        #deleting all the records
        for x in tree.get_children():
                tree.delete(x)
                
        for i in val:
            if search_value[1:]==i[0][1:]:
                lst.append(i)

        if len(lst)==0:
            tree.insert(parent='',index='end',iid=count,text='',values=('No Record Found','',''),tags=('even',))

            count+=1
        else:
            for i in lst:
                #adding the striped color
                if count%2==0:
                    tree.insert(parent='',index='end',iid=count,text='',values=(i[0],i[1],i[2]),tags=('even',))

                else:
                    tree.insert(parent='',index='end',iid=count,text='',values=(i[0],i[1],i[2]),tags=('odd',))
                
                count+=1

        lst=[]

    elif search_value[0].upper()=='M' and search_value[1:].isnumeric()==True:

        #deleting all the records
        for x in tree.get_children():
                tree.delete(x)
                
        for i in val:
            if search_value[1:]==i[1][1:]:
                lst.append(i)

        if len(lst)==0:
            tree.insert(parent='',index='end',iid=count,text='',values=('No Record Found','',''),tags=('even',))

            count+=1

        else:            
            for i in lst:
                #adding the striped color
                if count%2==0:
                    tree.insert(parent='',index='end',iid=count,text='',values=(i[0],i[1],i[2]),tags=('even',))

                else:
                    tree.insert(parent='',index='end',iid=count,text='',values=(i[0],i[1],i[2]),tags=('odd',))
                
                count+=1

        lst=[]

    elif search_value.isnumeric()==True or len(search_value.split('/'))==1:

        #deleting all the records
        for x in tree.get_children():
                tree.delete(x)

        for i in val:
            if search_value in str(i[2]):
                lst.append(i)

        if len(lst)==0:
            tree.insert(parent='',index='end',iid=count,text='',values=('No Record Found','',''),tags=('even',))

            count+=1

        else:            
            for i in lst:
                #adding the striped color
                if count%2==0:
                    tree.insert(parent='',index='end',iid=count,text='',values=(i[0],i[1],i[2]),tags=('even',))

                else:
                    tree.insert(parent='',index='end',iid=count,text='',values=(i[0],i[1],i[2]),tags=('odd',))
                
                count+=1

        lst=[]

        
        


                


        

    

            
            
            
    

        
    
