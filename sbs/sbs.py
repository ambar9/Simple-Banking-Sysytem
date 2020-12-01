from tkinter import *
from tkinter import messagebox
from time import gmtime, strftime
from PIL import ImageTk,Image


def is_number(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0
    
def check_acc_number(num):
    try:
        fpin=open(num+'.txt','r')
    except FileNotFoundError:
        messagebox.showinfo("Error",'INvalid credentials!\n try again')
        return 0
    fpin.close()
    return

def home_return(master):
    master.destroy()  
    main_menu()

def write(master,name,oc,pin):
    if ((is_number(name)) or (is_number(oc)==0) or (is_number(pin)==0)or name==''):
        messagebox.showinfo('error','Invalid Credentials')
        master.destroy()
        return
    
    f1=open('Account_Record.txt','r')
    accnt_no=int(f1.readline())
    accnt_no+=1
    f1.close()
    
    f1=open('Account_Record.txt','w')
    f1.write(str(accnt_no))
    f1.close()
    
    fdata=open(str(accnt_no)+'.txt','w')
    fdata.write(pin +'\n')
    fdata.write(oc +'\n')
    fdata.write(str(accnt_no) +'\n')
    fdata.write(name)
    fdata.close()
    
    frec=open(str(accnt_no)+'-rec.txt','w')
    frec.write('DATE                        Credit       Debit        Balance\n')
    frec.write(str(strftime('[%y-%m-%d] [%H:%M:%S] ',gmtime()))+"      "+oc+'                       '+oc+'\n')
    frec.close()
    messagebox.showinfo('Details','Your Account number is : '+str(accnt_no))
    master.destroy()
    return

def crdt_write(master,amt,accnt_no,name):

	if(is_number(amt)==0):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

	fdata=open(accnt_no+".txt",'r')
	pin=fdata.readline()
	camt=int(fdata.readline())
	fdata.close()
	amti=int(amt)
	cb=amti+camt
	fdata=open(accnt_no+".txt",'w')
	fdata.write(pin)
	fdata.write(str(cb)+"\n")
	fdata.write(accnt_no+"\n")
	fdata.write(name+"\n")
	fdata.close()
	frec=open(str(accnt_no)+"-rec.txt",'a+')
	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+str(amti)+"              "+str(cb)+"\n")
	frec.close()
	messagebox.showinfo("Operation Successfull!!","Amount Credited Successfully!!")
	master.destroy()
	return

def debit_write(master,amt,accnt_no,name):

	if(is_number(amt)==0):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 
			
	fdata=open(accnt_no+".txt",'r')
	pin=fdata.readline()
	camt=int(fdata.readline())
	fdata.close()
	if(int(amt)>camt):
		messagebox.showinfo("Error!!","You dont have that amount left in your account\nPlease try again.")
	else:
		amti=int(amt)
		cb=camt-amti
		fdata=open(accnt_no+".txt",'w')
		fdata.write(pin)
		fdata.write(str(cb)+"\n")
		fdata.write(accnt_no+"\n")
		fdata.write(name+"\n")
		fdata.close()
		frec=open(str(accnt_no)+"-rec.txt",'a+')
		frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+"              "+str(amti)+"              "+str(cb)+"\n")
		frec.close()
		messagebox.showinfo("Operation Successfull!!","Amount Debited Successfully!!")
		master.destroy()
		return

def check_log_in(master,name,accnt_no,pin):
    if(check_acc_number(accnt_no)==0):
        master.destroy()
        main_menu()
        return
    
    if (is_number(name) or is_number(pin)==0):
        messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
        master.destroy()
        main_menu()
    else:
        master.destroy()
        log_in_menu(accnt_no,name)
     
def Cr_Amt(accnt_no,name):
	root=Tk()
	root.geometry("600x300")
	root.title("Credit Amount")
	root.configure(bg="orange")
	#fr1=tk.Frame(creditwn,bg="blue")
	l_title=Message(root,text="UNITED BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
	l1=Label(root,relief="raised",text="Enter Amount to be credited: ")
	e1=Entry(root,relief="raised")
	l1.pack(side="top")
	e1.pack(side="top")
	b=Button(root,text="Credit",relief="raised",command=lambda:crdt_write(root,e1.get(),accnt_no,name))
	b.pack(side="top")
	root.bind("<Return>",lambda x:crdt_write(root,e1.get(),accnt_no,name))   
 
def De_Amt(accnt_no,name):
	root=Tk()
	root.geometry("600x300")
	root.title("Debit Amount")	
	root.configure(bg="orange")
	#fr1=tk.Frame(debitwn,bg="blue")
	l_title=Message(root,text="UNITED BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
	l1=Label(root,relief="raised",text="Enter Amount to be debited: ")
	e1=Entry(root,relief="raised")
	l1.pack(side="top")
	e1.pack(side="top")
	b=Button(root,text="Debit",relief="raised",command=lambda:debit_write(root,e1.get(),accnt_no,name))
	b.pack(side="top")
	root.bind("<Return>",lambda x:debit_write(root,e1.get(),accnt_no,name))
 
def disp_bal(accnt_no):
    fdata=open(accnt_no+".txt",'r')
    fdata.readline()
    bal=fdata.readline()
    fdata.close()
    messagebox.showinfo("Balance",bal)
 
def disp_tr_hist(accnt_no):
	root=Tk()
	root.geometry("900x600")
	root.title("Transaction History")
	root.configure(bg="orange")
	#fr1=tk.Frame(disp_wn,bg="blue")
	l_title=Message(root,text="UNITED BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
	fr1=Frame(root)
	fr1.pack(side="top")
	l1=Message(root,text="Your Transaction History:",padx=100,pady=20,width=1000,bg="blue",fg="orange",relief="raised")
	l1.pack(side="top")
	fr2=Frame(root)
	fr2.pack(side="top")
	frec=open(accnt_no+"-rec.txt",'r')
	for line in frec:
		l=Message(root,anchor="w",text=line,relief="raised",width=2000)
		l.pack(side="top")
	b=Button(root,text="Quit",relief="raised",command=root.destroy)
	b.pack(side="top")
	frec.close()
    
 
def log_in_menu(accnt_no,name):
    root=Tk()
    root.title('UNIVERSE BANK ' +name)
    root.iconbitmap('bicon.ico')
    root.geometry('1600x500')
    root.configure(bg='orange')
    fr=Frame(root)
    fr.pack(side=TOP)
    l1_title=Message(root,text='UNIVERSE BANK',bg='black',fg='white',relief=RAISED,justify='center',anchor='center',padx=600,pady=0,width=2000)
    l1_title.config(font=('Consolas','40','bold'))
    l1_title.pack(side='top')
    
    l1=Label(root,text='Logged in as '+name,relief=RAISED,fg='white',bg='black',justify='center',anchor='center')
    l1.pack(side='top')
    img2=PhotoImage(file="credit.gif")
    myimg2=img2.subsample(2,2)
    b2=Button(image=myimg2,command=lambda : Cr_Amt(accnt_no,name))
    b2.image=myimg2
    b2.place(x=100,y=150)
    
    img3=PhotoImage(file="debit.gif")
    myimg3=img3.subsample(2,2)
    b3=Button(image=myimg3,command=lambda: De_Amt(accnt_no,name))
    b3.image=myimg3
    b3.place(x=100,y=220)
    
    img4=PhotoImage(file="balance1.gif")
    myimg4=img4.subsample(2,2)
    b4=Button(image=myimg4,command=lambda: disp_bal(accnt_no))
    b4.image=myimg4
    b4.place(x=900,y=150)
    
    img5=PhotoImage(file="transaction.gif")
    myimg5=img5.subsample(2,2)
    b5=Button(image=myimg5,command=lambda: disp_tr_hist(accnt_no))
    b5.image=myimg5
    b5.place(x=900,y=220)
    
    
    img6=PhotoImage(file="logout.gif")
    myimg6=img6.subsample(2,2)
    b6=Button(image=myimg6,relief="raised",command=lambda: logout(root))
    b6.image=myimg6
    b6.place(x=500,y=400)
    
    root.mainloop()
   
def logout(master):
    messagebox.showinfo("Logged Out","You have been Logged Out Successfully.")
    master.destroy()
    main_menu()
    

         
def log_in(master):
    master.destroy()
    root=Tk()
    root.title('Log In')
    root.geometry('600x300')
    root.iconbitmap('E:/Ambar/Vs python/sbs/bicon.ico')
    root.configure(bg="orange")
    l1_title=Message(root,text='UNIVERSE BANK',relief=RAISED,fg='white',bg='black',anchor='center',width=2000,padx=600,pady=0,justify='center')
    l1_title.config(font=('Consolas',40,'bold'))
    l1_title.config(cursor='star')
    l1_title.pack(side=TOP)
    l1=Label(root,text='Enter your Name : ')
    l1.pack(side=TOP)
    e1=Entry(root)
    e1.pack(side=TOP)
    l2=Label(root,text='Enter your Account Number : ')
    l2.pack(side=TOP)
    e2=Entry(root)
    e2.pack(side=TOP)
    l3=Label(root,text='Enter your Pin : ')
    l3.pack(side=TOP)
    e3=Entry(root,show='*')
    e3.pack(side=TOP)
    b=Button(root,text="Submit",command=lambda: check_log_in(root,e1.get().strip(),e2.get().strip(),e3.get().strip()))
    b.pack(side=TOP)
    b2=Button(root,text="Home",relief=RAISED,fg='white',bg='black',command=lambda:home_return(root))
    b2.pack(side=TOP)
    root.bind("<Return>",lambda x:check_log_in(root,e1.get().strip(),e2.get().strip(),e3.get().strip()))
    root.mainloop()
    
    
def Create():
    root=Tk()
    root.title('Create Account')
    root.geometry('600x400')
    root.iconbitmap('E:/Ambar/Vs python/sbs/bicon.ico')
    root.configure(bg='orange')
    fr=Frame(root)
    fr.pack(side=TOP)
    l_title=Message(root,text='UNIVERSE BANK',relief=RAISED,width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
    l_title.config(font=('Consolas',40,'bold'))
    l_title.config(cursor='star')
    l_title.pack(side=TOP)
    l1=Label(root,text="Enter your name: ")
    l1.pack(side=TOP)
    e1=Entry(root)
    e1.pack(side=TOP)
    l2=Label(root,text="Enter Opening Credit: ")
    l2.pack(side=TOP)
    e2=Entry(root)
    e2.pack(side=TOP)
    l3=Label(root,text="Enter Desired Pin: ")
    l3.pack(side=TOP)
    e3=Entry(root,show='*')
    e3.pack(side=TOP)
    b=Button(root,text='Submit',command=lambda :write(root, e1.get().strip(),e2.get().strip(),e3.get().strip()))
    b.pack(side=TOP)
    root.bind("<Return>",lambda x:write(root,e1.get().strip(),e2.get().strip(),e3.get().strip()))
    return
	
    
def main_menu():
    root=Tk()
    root.title('UNIVERSE BANK')
    root.geometry('1200x600')
    root.iconbitmap('E:/Ambar/Vs python/sbs/bicon.ico')
    root.configure(background='orange')
    fr=Frame(root)
    fr.pack(side=TOP)
    bg=Image.open('main1.jpg')
    resized=bg.resize((1200,600),Image.ANTIALIAS)
    bg_image=ImageTk.PhotoImage(resized)
    x=Label(image=bg_image)
    
    l_title=Message(root,text='SIMPLE BANKING\n SYSTEM',relief=RAISED,width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
    l_title.config(font=('Consolas',40,'bold'))
    l_title.config(cursor='star')
    l_title.pack(side=TOP)
    
    
    
    
    img1=PhotoImage(file="new.gif")
    myimg1=img1.subsample(2,2)
    b1=Button(image=myimg1,command=Create)
    b1.image=myimg1
    b1.place(x=450,y=350)
    
    img2=PhotoImage(file="login.gif")
    myimg2=img2.subsample(2,2)
    b2=Button(image=myimg2,command=lambda: log_in(root))
    b2.image=myimg2
    b2.place(x=450,y=275)
    
    img3=PhotoImage(file="quit.gif")
    myimg3=img3.subsample(2,2)
    b3=Button(image=myimg3,command=root.destroy)
    b3.image=myimg3
    b3.place(x=563,y=415)
    # new_account_btn=PhotoImage(file='new.gif')
    # new_account_btn1=PhotoImage(file='login.gif')
    #mg_label=Label(image=new_account_btn)
    #Img_label.pack()
    # imgc1=ImageTk.PhotoImage(file="new.gif")
    # imglo=ImageTk.PhotoImage(file="login.gif")
    # imgc=imgc1.subsample(2,2)
    # imglog=imglo.subsample(2,2)

    # b1=Button(root,image=new_account_btn,borderwidth=0,command=Create)
    # #b1.image=imgc1
    # b2=Button(root,image=new_account_btn1,command=lambda: log_in(root))
    # #b2.image=imglo
    # img6=ImageTk.PhotoImage(file="quit.gif")
    # #myimg6=img6.subsample(2,2)

    # b6=Button(image=img6,command=root.destroy,borderwidth=0)
    # b6.image=img6
    # b1.place(x=300,y=300)
    # b2.place(x=300,y=200)	
    # b6.place(x=520,y=400)

    
    x.pack()
    

    root.mainloop()
main_menu()