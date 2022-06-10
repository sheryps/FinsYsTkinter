import tkinter as tk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter import StringVar, ttk
import mysql.connector
from tkinter import *
mydata=mysql.connector.connect(host='localhost', user='root', password='', database='finsys_tkinter1')
cur=mydata.cursor()
def salescreditnote():  
    estwin=tk.Tk()
    estwin.title('Sales Records')
    estwin.geometry('1500x1000')
    estwin['bg'] = '#2f516f'
    cid=2
    mycanvas=tk.Canvas(estwin,width=1800,height=1200)
    mycanvas.place(relx=0,rely=0,relwidth=1,relheight=1)
    yscrollbar =ttk.Scrollbar(estwin,orient='vertical',command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT,fill=Y)
    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))
    frame=tk.Frame(mycanvas)
    frame['bg']='#2f516f'
    mycanvas.create_window((0,0),window=frame,anchor='nw',width=1500,height=1500)
    hf1=tk.Frame(frame,bg='#243e54')
    tk.Label(hf1,text='CREDIT NOTE',font=('Times New Roman',30),bg='#243e54').place(relx=0.4,rely=0.1)
    hf1.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.1)
    hf2=tk.Frame(frame,bg='#243e54')
            #customer
    tk.Label(hf2,text='Fin sYs',font=('Times New Roman',30),bg='#243e54').place(relx=0.4,rely=0.02)      
    tk.Label(hf2,text='Customer',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.11) 
    def estimatecusinput():
        try:
                cur.execute("SELECT firstname,lastname FROM customer")
                val=cur.fetchall()         
                for row in val:
                    tm.append(row[0]+row[1])   
        except:
            pass              
    tm=['Select Customer']
    estimatecusinput()     
    estcus=ttk.Combobox(hf2,values=tm)
    estcus.current(0)  
    estcus.place(relx=0.05,rely=0.15,relwidth=0.2,relheight=0.03)
    tk.Button(hf2,text='+',font=(14)).place(relx=0.26,rely=0.15,relwidth=0.025,relheight=0.03)
    tk.Label(hf2,text='Email',font=('times new roman', 14),bg='#2f516f').place(relx=0.30,rely=0.11)
    email=tk.Entry(hf2)
    email.place(relx=0.3,rely=0.15,relwidth=0.2,relheight=0.03)
    tk.Label(hf2,text='Billing Address',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.2) 
    bill=tk.Entry(hf2)
    bill.place(relx=0.05,rely=0.24,relwidth=0.2,relheight=0.12)
    tk.Label(hf2,text='Estimate Date',font=('times new roman', 14),bg='#2f516f').place(relx=0.3,rely=0.2)
    estdate=tk.Entry(hf2)
    estdate.place(relx=0.3,rely=0.24,relwidth=0.2,relheight=0.03) 
    tk.Label(hf2,text='Expiration Date',font=('times new roman', 14),bg='#2f516f').place(relx=0.55,rely=0.2) 
    expdate=DateEntry(hf2)
    expdate.place(relx=0.55,rely=0.24,relwidth=0.2,relheight=0.03)
    tk.Label(hf2,text='Place of Supply',font=('times new roman', 14),bg='#2f516f').place(relx=0.3,rely=0.29)
    estplace=tk.Entry(hf2)
    estplace.place(relx=0.3,rely=0.33,relwidth=0.2,relheight=0.03) 
    tk.Label(hf2,text='#',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.38)
    tk.Label(hf2,text='PRODUCT/SERVICES',font=('times new roman', 14),bg='#2f516f').place(relx=0.1,rely=0.38)
    tk.Label(hf2,text='DESCRIPTION',font=('times new roman', 14),bg='#2f516f').place(relx=0.28,rely=0.38)
    tk.Label(hf2,text='QTY',font=('times new roman', 14),bg='#2f516f').place(relx=0.41,rely=0.38,relwidth=0.1)
    tk.Label(hf2,text='RATE',font=('times new roman', 14),bg='#2f516f').place(relx=0.53,rely=0.38,relwidth=0.1)
    tk.Label(hf2,text='TOTAL',font=('times new roman', 14),bg='#2f516f').place(relx=0.66,rely=0.38,relwidth=0.1)
    tk.Label(hf2,text='TAX',font=('times new roman', 14),bg='#2f516f').place(relx=0.78,rely=0.38,relwidth=0.1)
   #row1
    pro=['Select Product']
    try:
                cur.execute("SELECT name FROM inventory WHERE cid =%s",([cid]))
                vall=cur.fetchall()         
                for row in vall:
                        pro.append(row[0])     
                cur.execute("SELECT name FROM noninventory WHERE cid =%s",([cid]))
                valll=cur.fetchall()         
                for row in valll:
                    pro.append(row[0])   
                cur.execute("SELECT name FROM bundle WHERE cid =%s",([cid]))
                vall1=cur.fetchall()         
                for row in vall1:
                    pro.append(row[0])         
    except:
                pass
    tk.Label(hf2,text='1',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.43)     
    prod=ttk.Combobox(hf2,values=pro)
    prod.bind('<<ComboboxSelected>>',)
    prod.place(relx=0.1,rely=0.43,relwidth=0.16,relheight=0.03)
    desc=tk.Entry(hf2)
    desc.place(relx=0.28,rely=0.43,relwidth=0.11,relheight=0.03)
    quan1=IntVar()  
    qty=tk.Spinbox(hf2,from_=0,to=2147483647,textvariable=quan1,font=(8))
    qty.bind('<FocusIn>',)
    qty.place(relx=0.41,rely=0.43,relwidth=0.1,relheight=0.03)
    rate1=IntVar()
    rate=tk.Spinbox(hf2,textvariable=rate1,from_=0,to=2147483647,font=(8))
    rate.bind('<FocusIn>',)
    rate.place(relx=0.53,rely=0.43,relwidth=0.1,relheight=0.03)
    total=tk.Entry(hf2,font=(8))
    total.place(relx=0.66,rely=0.43,relwidth=0.1,relheight=0.03)
    taxval=['28.0% GST(28%)','18.0% GST(18%)','12.0% GST(12%)','06.0% GST(06%)','05.0% GST(05%)','03.0% GST(03%)',
                                                    '0.25% GST(0.25%)','0.0% GST(0%)','Exempt GST(0%)','Out of Scope(0%)']                                           
    tax=ttk.Combobox(hf2,values=taxval)
    tax.bind('<<ComboboxSelected>>',)
    tax.place(relx=0.78,rely=0.43,relwidth=0.1,relheight=0.03)

    #row22
    tk.Label(hf2,text='2',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.48)   
    prod1=ttk.Combobox(hf2,values=pro)
    prod1.bind('<<ComboboxSelected>>',)
    prod1.place(relx=0.1,rely=0.48,relwidth=0.16,relheight=0.03)
    desc1=tk.Entry(hf2)
    desc1.place(relx=0.28,rely=0.48,relwidth=0.11,relheight=0.03)
    quan2=IntVar()  
    qty1=tk.Spinbox(hf2,from_=0,to=2147483647,textvariable=quan1,font=(8))
    qty1.bind('<FocusIn>',)
    qty1.place(relx=0.41,rely=0.48,relwidth=0.1,relheight=0.03)
    rate22=IntVar()
    rate1=tk.Spinbox(hf2,textvariable=rate1,from_=0,to=2147483647,font=(8))
    rate1.bind('<FocusIn>',)
    rate1.place(relx=0.53,rely=0.48,relwidth=0.1,relheight=0.03)
    total1=tk.Entry(hf2,font=(8))
    total1.place(relx=0.66,rely=0.48,relwidth=0.1,relheight=0.03)
    tax1=ttk.Combobox(hf2,values=taxval)
    tax1.bind('<<ComboboxSelected>>',)
    tax1.place(relx=0.78,rely=0.48,relwidth=0.1,relheight=0.03)
    #third row
    tk.Label(hf2,text='3',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.53)   
    prod2=ttk.Combobox(hf2,values=pro)
    prod2.bind('<<ComboboxSelected>>',)
    prod2.place(relx=0.1,rely=0.53,relwidth=0.16,relheight=0.03)
    desc2=tk.Entry(hf2)
    desc2.place(relx=0.28,rely=0.53,relwidth=0.11,relheight=0.03)
    quan2=IntVar()  
    qty2=tk.Spinbox(hf2,from_=0,to=2147483647,textvariable=quan1,font=(8))
    qty2.bind('<FocusIn>',)
    qty2.place(relx=0.41,rely=0.53,relwidth=0.1,relheight=0.03)
    rate33=IntVar()
    rate2=tk.Spinbox(hf2,textvariable=rate1,from_=0,to=2147483647,font=(8))
    rate2.bind('<FocusIn>',)
    rate2.place(relx=0.53,rely=0.53,relwidth=0.1,relheight=0.03)
    total2=tk.Entry(hf2,font=(8))
    total2.place(relx=0.66,rely=0.53,relwidth=0.1,relheight=0.03)
    tax2=ttk.Combobox(hf2,values=taxval)
    tax2.bind('<<ComboboxSelected>>',)
    tax2.place(relx=0.78,rely=0.53,relwidth=0.1,relheight=0.03)
    #forth row
    tk.Label(hf2,text='4',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.58)   
    prod3=ttk.Combobox(hf2,values=pro)
    prod3.bind('<<ComboboxSelected>>',)
    prod3.place(relx=0.1,rely=0.58,relwidth=0.16,relheight=0.03)
    desc3=tk.Entry(hf2)
    desc3.place(relx=0.28,rely=0.58,relwidth=0.11,relheight=0.03)
    quan3=IntVar()  
    qty3=tk.Spinbox(hf2,from_=0,to=2147483647,textvariable=quan1,font=(8))
    qty3.bind('<FocusIn>',)
    qty3.place(relx=0.41,rely=0.58,relwidth=0.1,relheight=0.03)
    rate44=IntVar()
    rate3=tk.Spinbox(hf2,textvariable=rate1,from_=0,to=2147483647,font=(8))
    rate3.bind('<FocusIn>',)
    rate3.place(relx=0.53,rely=0.58,relwidth=0.1,relheight=0.03)
    total3=tk.Entry(hf2,font=(8))
    total3.place(relx=0.66,rely=0.58,relwidth=0.1,relheight=0.03)
    tax3=ttk.Combobox(hf2,values=taxval)
    tax3.bind('<<ComboboxSelected>>',)
    tax3.place(relx=0.78,rely=0.58,relwidth=0.1,relheight=0.03)

    #total
    tk.Label(hf2,text='Sub Total',font=('times new roman', 16),bg='#2f516f').place(relx=0.7,rely=0.65,relwidth=0.1,relheight=0.04)
    sub=tk.Entry(hf2,font=('times new roman', 16))
    sub.place(relx=0.82,rely=0.65,relheight=0.04,relwidth=0.12)
    tk.Label(hf2,text='Tax Amount',font=('times new roman', 16),bg='#2f516f').place(relx=0.7,rely=0.71,relwidth=0.1,relheight=0.04)
    taxamount=tk.Entry(hf2,font=('times new roman', 16))
    taxamount.place(relx=0.82,rely=0.71,relheight=0.04,relwidth=0.12)
    tk.Label(hf2,text='Grand Total',font=('times new roman', 16),bg='#2f516f').place(relx=0.7,rely=0.77,relwidth=0.1,relheight=0.04)
    totalamount=tk.Entry(hf2,font=('times new roman', 16))
    totalamount.place(relx=0.82,rely=0.77,relheight=0.04,relwidth=0.12)
    tk.Button(hf2,text='Save',font=('times new roman', 16),bg='#2f516f').place(relx=0.8,rely=0.85,relwidth=0.1,relheight=0.04)
    hf2.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.7)
    estwin.mainloop()   
salescreditnote()