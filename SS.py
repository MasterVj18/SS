from tkinter import *
from tkinter import messagebox
import cx_Oracle
#cx_Oracle.init_oracle_client(lib_dir=r"C:\InstantClient\instantclient_21_6")
try:
    con = cx_Oracle.connect('system/vijay777@localhost:1521/XEPDB1')
except Exception as error:
    print("Database not Connected!! Try again!!\nError: ", error)
else:
    print('Database Connected Sucessfully!!')

#Why this try
#try:
            #Cur = con.cursor()
            #Cur.execute("select * from AFS")
            #for Mem_id, First_name, Last_name, DateofBirth, Gender, Address, Mobile_no, Amount_paid, Amnt_to_be_paid,Interest_amnt in Cur:
             #   print("menber id :",Mem_id)
           
#except Exception as error:
 #           print('Error while executing',error)
#else:
 #           print('Execution Completed!!')
  #          con.commit()

def insert_tab():
    ins=Tk()
    tit=Label(ins,text="INSERTION" ,font="grey")
    tit.place(x=300,y=10)
    lbl1=Label( ins,text='Member ID')
    lbl2=Label( ins,text='First Name')
    lbl3=Label(ins, text='Last Name')
    lbl4=Label(ins, text='Date Of Birth')
    lbl5=Label(ins, text='Gender')
    lbl6=Label(ins, text='Address')
    lbl7=Label(ins, text='Mobile Number')
    lbl8=Label(ins, text='Amount Paid')
    lbl9=Label(ins, text='Amount to be Paid')
    lbl10=Label(ins, text='Interest Amount')
   
   
   
   
    idi=Entry(ins,bd=3)
    fname=Entry(ins,bd=3)
    lname=Entry(ins,bd=3)
    dt=Entry(ins,bd=3)
    gndr=Entry(ins,bd=3)
    addrs=Entry(ins,bd=3)
    mob=Entry(ins,bd=3)
    amntpd=Entry(ins,bd=3)
    amnttobepd=Entry(ins,bd=3)
    intamt=Entry(ins,bd=3)
   
   
   
    lbl1.place(x=100, y=50)
    idi.place(x=360, y=50)
    lbl2.place(x=100, y=100)
    fname.place(x=360, y=100)
    lbl3.place(x=100, y=150)
    lname.place(x=360, y=150)
    lbl4.place(x=100, y=200)
    dt.place(x=360, y=200)
    lbl5.place(x=100, y=250)
    gndr.place(x=360, y=250)
    lbl6.place(x=100, y=300)
    addrs.place(x=360, y=300)
    lbl7.place(x=100, y=350)
    mob.place(x=360, y=350)
    lbl8.place(x=100, y=400)
    amntpd.place(x=360, y=400)
    lbl9.place(x=100, y=450)
    amnttobepd.place(x=360, y=450)
    lbl10.place(x=100, y=500)
    intamt.place(x=360, y=500)
   
   
    ins.title('Association Finance System')
    ins.geometry("800x600+10+10")
    ins.configure(bg='orange')

    bt1=Button(ins,text="INSERT",command=lambda: [f()])
   
    bt1.place(x=600,y=350)
    bte=Button(ins,text="CLOSE",command=ins.destroy)
    bte.place(x=250,y=550)
    #end=Label(  ins ,text="ELEMENTS INSERTED",)
    #end.place(x=500,y=500)
   


    def f():
        i=idi.get()
        fn=fname.get()
        ln=lname.get()
        d=dt.get()
        g=gndr.get()
        ad=addrs.get()
        m=mob.get()
        ap=amntpd.get()
        atp=amnttobepd.get()
        ia=intamt.get()
        print (i)
        print (fn)
        print (ln)
        print (d)
        print (g)
        print (ad)
        print (m)
        print (ap)
        print (atp)
        print (ia)
        try:
                Cur = con.cursor()
                Cur.execute("insert into AFS (Mem_id,First_name,Last_name,DateofBirth,Gender,Address,Mobile_no,Amount_paid,Amnt_to_be_paid,Interest_amnt) values(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)",[i,fn,ln,d,g,ad,m,ap,atp,ia])
                con.commit()
                Cur.execute("insert into FundCollection (Mem_id,last_Date) values(:1,:2)",[i,d])
                con.commit()

        except Exception as error:
                print('Error while executing insertion',error)
        else:
               
                print('insert Completed')
                con.commit()
   
    ins.mainloop()
   
   
   

       
       



               
def delete_tab():
    dle=Tk()
    tit=Label(dle,text="DELETION" ,font="grey")
    tit.place(x=300,y=50)
    lbl1=Label(dle,text='Enter the Member ID to be delete :')
    lbl1.place(x=100, y=200)
    id=Entry(dle,bd=3)
    id.place(x=360, y=200)
   
    bt1=Button(dle,text="DELETE",command=lambda: [delete()])
    bt1.place(x=300,y=250)
    bte=Button(dle,text="CLOSE",command=dle.destroy)
    bte.place(x=300,y=350)
    def delete():        
           
            i1=id.get()
            print (i1)
            try:
                    Cur = con.cursor()
                    Cur.execute("delete from AFS where Mem_id = :1",[i1])
                   
            except Exception as error:
                    print('Error while executing deletion',error)
            else:
                    print('Deletion Completed!!')
                    con.commit()
    dle.title('Association Finance System')
    dle.geometry("800x600+10+10")
    dle.configure(bg='orange')
    dle.mainloop()



def update_tab():
    up=Tk()
    tit=Label(up,text="UPDATION" ,font="grey")
    tit.place(x=300,y=10)
    lbl1=Label( up,text='Enter the Member ID you want to update :')
    lbl2=Label( up,text='First Name')
    lbl3=Label(up, text='Last Name')
    lbl4=Label(up, text='Date Of Birth')
    lbl5=Label(up, text='Gender')
    lbl6=Label(up, text='Address')
    lbl7=Label(up, text='Mobile Number')
    #lbl8=Label(up, text='Amount Paid')
    #lbl9=Label(up, text='Amount to be Paid')
    #lbl10=Label(up, text='Interest Amount')
   
    idi=Entry(up,bd=3)
    fname=Entry(up,bd=3)
    lname=Entry(up,bd=3)
    dt=Entry(up,bd=3)
    gndr=Entry(up,bd=3)
    addrs=Entry(up,bd=3)
    mob=Entry(up,bd=3)
    #amntpd=Entry(up,bd=3)
    #amnttobepd=Entry(up,bd=3)
    #intamt=Entry(up,bd=3)
   
    lbl1.place(x=100, y=100)
    idi.place(x=360, y=100)
    lbl2.place(x=100, y=150)
    fname.place(x=360, y=150)
    lbl3.place(x=100, y=200)
    lname.place(x=360, y=200)
    lbl4.place(x=100, y=250)
    dt.place(x=360, y=250)
    lbl5.place(x=100, y=300)
    gndr.place(x=360, y=300)
    lbl6.place(x=100, y=350)
    addrs.place(x=360, y=350)
    lbl7.place(x=100, y=400)
    mob.place(x=360, y=400)
    #lbl8.place(x=100, y=400)
    #amntpd.place(x=360, y=400)
    #lbl9.place(x=100, y=450)
    #amnttobepd.place(x=360, y=450)
    #lbl10.place(x=100, y=500)
    #intamt.place(x=360, y=500)
   
   
    up.title('Association Finance System')
    up.geometry("800x600+10+10")
    up.configure(bg='orange')

    bt1=Button(up,text="update fname",command=lambda: [updatefn()])
    bt1.place(x=600,y=150)
    bt2=Button(up,text="update lname",command=lambda: [updateln()])
    bt2.place(x=600,y=200)
    bt3=Button(up,text="update Date of Birth",command=lambda: [updated()])
    bt3.place(x=600,y=250)
    bt4=Button(up,text="update Gender",command=lambda: [updateg()])
    bt4.place(x=600,y=300)
    bt5=Button(up,text="update Address",command=lambda: [updatead()])
    bt5.place(x=600,y=350)
    bt6=Button(up,text="update Mobile number",command=lambda: [updatem()])
    bt6.place(x=600,y=400)
    #bt7=Button(up,text="update Amount paid",command=lambda: [updateap()])
   # bt7.place(x=600,y=400)
    #bt8=Button(up,text="update Amount to be paid",command=lambda: [updateatp()])
    #bt8.place(x=600,y=450)
    #bt9=Button(up,text="update Interest Amount",command=lambda: [updateia()])
    #bt9.place(x=600,y=500)
   
   
    bte=Button(up,text="CLOSE",command=up.destroy)
    bte.place(x=250,y=500)
   
    def updatefn():
        i=idi.get()
        fn=fname.get()
        print (i)
        print (fn)
        try:
                Cur = con.cursor()
                Cur.execute("update AFS set first_name=:1 where Mem_id=:2",[fn,i])
               
        except Exception as error:
                print('Error while executing insertion',error)
        else:
               
                print('First name Updated')
                con.commit()
               
    def updateln():
        i=idi.get()
        ln=lname.get()
        print (i)
        print (ln)
        try:
                Cur = con.cursor()
                Cur.execute("update AFS set last_name=:1 where Mem_id=:2",[ln,i])

        except Exception as error:
                print('Error while executing insertion',error)
        else:
               
                print('Last name Updated')
                con.commit()
               
    def updated():
        i=idi.get()
        d=dt.get()
        print (i)
        print (d)
        try:
                Cur = con.cursor()
                Cur.execute("update AFS set DateofBirth=:1 where Mem_id=:2",[d,i])

        except Exception as error:
                print('Error while executing insertion',error)
        else:
               
                print('Date of Birth Updated')
                con.commit()
   
   
    def updateg():
           i=idi.get()
           g=gndr.get()
           print (i)
           print (g)
           try:
                   Cur = con.cursor()
                   Cur.execute("update AFS set Gender=:1 where Mem_id=:2",[g,i])
   
           except Exception as error:
                   print('Error while executing insertion',error)
           else:
                 
                   print('Gender Updated')
                   con.commit()
             
   
   
    def updatead():
          i=idi.get()
          ad=addrs.get()
          print (i)
          print (ad)
          try:
                  Cur = con.cursor()
                  Cur.execute("update AFS set Address=:1 where Mem_id=:2",[ad,i])
   
          except Exception as error:
                  print('Error while executing insertion',error)
          else:
                 
                  print('Address Updated')
                  con.commit()
   
    def updatem():
         i=idi.get()
         m=mob.get()
         print (i)
         print (mob)
         try:
                 Cur = con.cursor()
                 Cur.execute("update AFS set Mobile_no=:1 where Mem_id=:2",[mob,i])
 
         except Exception as error:
                 print('Error while executing insertion',error)
         else:
               
                 print('Mobile number Updated')
                 con.commit()
   
   
   
    up.mainloop()
   

def main():
    main=Tk()
    l1=Label(main,text="Association Finance System" ,font="grey")
    l1.place(x=270,y=10)
    b1=Button( main,text='INSERT',font="grey",command=lambda: [insert_tab()])
    b1.place(x=360, y=200)
    b2=Button(main, text='DELETE',font="grey", command=lambda: [delete_tab()])
    b2.place(x=360, y=300)
    b3=Button( main,text='UPDATE',font="grey",command=lambda: [update_tab()] )
    b3.place(x=360, y=400)
    b4=Button(main, text='CLOSE',font="red", command=main.destroy)
    b4.place(x=360, y=500)
   
    main.title('Association Finance System')
    main.geometry("800x600+10+10")
    main.configure(bg='orange')
    main.mainloop()
 
def loan():
    loan=Tk()
    tit=Label(loan,text="LOAN DISTRIBUTION" ,font="grey")
    tit.place(x=300,y=50)
    lbl1=Label( loan,text='Loaner ID')
    lbl2=Label( loan,text='Member ID')
    lbl3=Label( loan,text='Loan Amount')
    lbl5=Label(loan, text='Loaner Address')
    lbl6=Label(loan, text='Mobile Number')
   
   
    loanid=Entry(loan,bd=3)
    idi=Entry(loan,bd=3)
    la=Entry(loan,bd=3)
    addrs=Entry(loan,bd=3)
    mob=Entry(loan,bd=3)
   
   
   
    lbl1.place(x=100, y=100)
    loanid.place(x=360, y=100)
    lbl2.place(x=100, y=150)
    idi.place(x=360, y=150)
    lbl3.place(x=100, y=200)
    la.place(x=360, y=200)
    lbl5.place(x=100, y=250)
    addrs.place(x=360, y=250)
    lbl6.place(x=100, y=300)
    mob.place(x=360, y=300)
   
   
   

    bt1=Button(loan,text="SUBMIT",command=lambda: [ld()])
   
    bt1.place(x=250,y=400)
    bte=Button(loan,text="CLOSE",command=loan.destroy)
    bte.place(x=250,y=550)
    #end=Label(  ins ,text="ELEMENTS INSERTED",)
    #end.place(x=500,y=500)
    #loan.mainloop()

   
    def ld():
        li=loanid.get()
        mi=idi.get()
        a=la.get()
        ad=addrs.get()
        m=mob.get()
       
       
       
        try:
                Cur = con.cursor()
                Cur.execute("insert into Loaner (Mem_id,Loaner_ID,Loan_amount,Loaner_address,Loaner_Mobile) values (:1,:2,:3,:4,:5)",[mi,li,a,ad,m])
                Cur.execute("update AFS set Amnt_to_be_paid = Amnt_to_be_paid+:1 where Mem_id=:2",[a,mi])
                Cur.execute("insert into  EMI (Mem_id,Loaner_ID,EMI_amnt,interest) values (:1,:2,:3/5,(:4/100)*2)",[mi,li,a,a])
                Cur.execute("update treasury set amount=amount-:1 where company = 'AFS'",[a])
                

        except Exception as error:
                print('Error while executing insertion',error)
        else:
               
                print('insert Completed')
                con.commit()
   
    loan.title('Association Finance System')
    loan.geometry("800x600+10+10")
    loan.configure(bg='orange')
    loan.mainloop()
   
   


def FundCollection_tab():

    fund=Tk()

    tit=Label(fund,text="FUND COLLECTION" ,font="grey")

    tit.place(x=300,y=10)

    lbl1=Label(fund,text='Member ID')

    lbl2=Label(fund,text='Have you paid the fund? (y/n)')

   

    idi=Entry(fund,bd=3)

    yn=Entry(fund,bd=3)

   

    lbl1.place(x=100, y=200)

    lbl2.place(x=100, y=350)

    idi.place(x=360, y=200)

    yn.place(x=360, y=350)

    y=yn.get()
   
    b5=Button(fund, text='SUBMIT',font="red", command=lambda:[click() ])
    b5.place(x=360, y=400)
    b4=Button(fund, text='CLOSE',font="red", command=fund.destroy)
    b4.place(x=360, y=500)
    def click():
        i=idi.get()
        y=yn.get()
        if(y=='y'):

            messagebox.showinfo("Message","Fund Paid!!")

            try:

                    Cur = con.cursor()
                    Cur.execute("update FundCollection set last_Date=sysdate where Mem_id=:1",[i])
                    con.commit()
                    
                    Cur.execute("update Treasury set amount=amount+1000 where company = 'AFS'")
                    Cur.execute("select * from treasury")
                    row=Cur.fetchall()
                    print(row)
                    con.commit

                   

            except Exception as error:

                    print('Error while executing updation',error)

            else:

                   

                    print('Date Updated')

                    con.commit()

           

            try:
                       
                    Cur = con.cursor()

                    Cur.execute("update FundCollection set No_of_months=No_of_months+1 where Mem_id=:1",[i])

                   

            except Exception as error:

                    print('Error while executing updation',error)

            else:

                   

                    print('No of months Updated')

                    con.commit()

                   

            try:

                    Cur = con.cursor()
                    Cur.execute("update AFS set Amount_paid = Amount_paid+1000 where Mem_id=:1",[i])
                    Cur.execute("update FundCollection set Fund = Fund+1000 where Mem_id=:1",[i])
                    #Cur.execute("update AFS set Amnt_to_be_paid = Fund+1000 where Mem_id=:1",[i])
                   

            except Exception as error:

                    print('Error while executing updation',error)

            else:


                    print('Amount paid Updated')

                    con.commit()

           

        if(y=='n'):

            messagebox.showinfo("Message","Fund not Paid!!")

   
    fund.title('Association Finance System')
    fund.geometry("800x600+10+10")
    fund.configure(bg='orange')
    fund.mainloop()
    #fund.mainloop()
   
def EMI():
    EMI=Tk()
    tit=Label(EMI,text="EMI COLLECTION" ,font="grey")
    tit.place(x=300,y=50)
    lbl0=Label(EMI,text='Member ID')
    lbl1=Label(EMI,text='Loaner ID')

    lbl2=Label(EMI,text='Have you paid intrest or both intrest and EMI? (i/e)')

   
    idm=Entry(EMI,bd=3)
    idi=Entry(EMI,bd=3)

    yn=Entry(EMI,bd=3)

   
    lbl0.place(x=100, y=100)
    lbl1.place(x=100, y=200)

    lbl2.place(x=100, y=350)
    idi.place(x=360, y=200)
    idm.place(x=360, y=100)

    yn.place(x=400, y=350)

    y=yn.get()
   
    b5=Button(EMI, text='SUBMIT',font="red", command=lambda:[click() ])
    b5.place(x=360, y=400)
    b4=Button(EMI, text='CLOSE',font="red", command=EMI.destroy)
    b4.place(x=360, y=500)
    def click():
        m=idm.get()
        i=idi.get()
        y=yn.get()
        amnt=0
        inst=0
        if(y=='i'):

            messagebox.showinfo("Message","Interest Paid!!")

            try:
                    
                    Cur = con.cursor()
                    Cur.execute("select interest from EMI where loaner_id=:1",[i])
                    for interest in Cur:
                        print(interest)
                        inst=interest[0]
                    Cur.execute("update AFS set Amount_paid=Amount_paid+:1  where Mem_id=:2",[inst,m])
                    Cur.execute("update AFS set Interest_amnt=Interest_amnt+:1  where Mem_id=:2",[inst,m])
                    Cur.execute("update treasury set amount=amount+:1 where com_id = 1",[inst])

                   

            except Exception as error:

                    print('Error while executing updation',error)

            else:

                   

                    print('Date Updated')

                    con.commit()


           

        if(y=='e'):

            messagebox.showinfo("Message","EMI and Interest Paid!!")
            try:
                    Cur = con.cursor()
                    Cur.execute("select interest,EMI_amnt from EMI where loaner_id=:1",[i])
                    for interest,EMI_amnt in Cur:
                        print(interest)
                        print(EMI_amnt)
                        inst=interest
                        amnt=EMI_amnt
                    Cur.execute("update AFS set Amount_paid=Amount_paid+:1+:2  where Mem_id=:2",[inst,amnt,m])
                    Cur.execute("update AFS set Interest_amnt=Interest_amnt+:1  where Mem_id=:2",[inst,m])
                    
                    Cur.execute("update EMI set no_months=no_months+1 where Loaner_ID=:1",[i])
                    Cur.execute("update treasury set amount=amount+:1+:2 where company = 'AFS'",[inst,amnt])

            except Exception as error:
                    print('Error while executing updation',error)

            else:
                    print('No of months Updated')
                    con.commit()
    
    EMI.title('Association Finance System')
    EMI.geometry("800x600+10+10")
    EMI.configure(bg='orange')
    EMI.mainloop()
    
def association():
    association=Tk()
    l1=Label(association,text="Association Finance System" ,font="grey")
    l1.place(x=290,y=10)
    b1=Button(association, text='Fund Collection',font="grey",command=lambda:[FundCollection_tab() ])
    b1.place(x=340, y=200)
    b2=Button(association, text='Loan Distribution',font="grey", command=lambda:[loan()])
    b2.place(x=340, y=300)
    b3=Button(association, text='EMI Collection',font="grey", command=lambda:[EMI()])
    b3.place(x=340, y=400)
    b4=Button( association,text='CLOSE',font="red", command=association.destroy)
    b4.place(x=360, y=500)
   
    association.title('Association Finance System')
    association.geometry("800x600+10+10")
    association.configure(bg='orange')
    association.mainloop()

def home():
     home=Tk()
     l1=Label(home,text="Association Finance System" ,font="grey")
     l1.place(x=270,y=10)
     b1=Button(home, text='Association Operation',font="grey",command=lambda: [association()])
     b1.place(x=320, y=200)
     b2=Button( home,text='DML Operation',font="grey", command=lambda: [main()])
     b2.place(x=340, y=350)
     b4=Button(home, text='CLOSE',font="red", command=home.destroy)
     b4.place(x=360, y=500)
   
     home.title('Association Finance System')
     home.geometry("800x600+10+10")
     home.configure(bg='orange')
     home.mainloop()
home()
