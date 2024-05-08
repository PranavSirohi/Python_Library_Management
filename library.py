import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

#=======================variables========================
        self.member_var=tk.StringVar()
        self.prn_var=tk.StringVar()
        self.id_var=tk.StringVar()
        self.firstname_var=tk.StringVar()
        self.lastname_var=tk.StringVar()
        self.address_var=tk.StringVar()
        self.mobile_var=tk.StringVar()
        self.bookid_var=tk.StringVar()
        self.bookname_var=tk.StringVar()
        self.dateborrowed_var=tk.StringVar()
        self.datedue_var=tk.StringVar()
        self.latereturnfine_var=tk.StringVar()
        self.actualprice_var=tk.StringVar()



        lbtitle = tk.Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="green", bd=20, relief=tk.RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbtitle.pack(side=tk.TOP, fill=tk.X)

        frame = tk.Frame(self.root, bd=12, relief=tk.RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1360, height=400)
        
        # =======DATA FRAME LEFT=======
        DataFrameLeft = tk.LabelFrame(frame, text="Library Membership Information", bg="powder blue", fg="green", bd=8, relief=tk.RIDGE, font=("times new roman", 10, "bold"))
        DataFrameLeft.place(x=0, y=5, width=850, height=350)

        lblMember = tk.Label(DataFrameLeft, bg="powder blue",  text="Member Type", font=("times new roman", 15, "bold"))
        lblMember.grid(row=0, column=0, sticky=tk.W, padx=2, pady=6)

        comMember = ttk.Combobox(DataFrameLeft,textvariable=self.member_var, font=("times new roman", 15, "bold"), width=27, state="readonly")
        comMember["values"] = ("Admin Staff", "Student", "Lecturer")
        comMember.grid(row=0, column=1)

        lblPRN_No = tk.Label(DataFrameLeft, bg="powder blue", text="PRN No.", font=("arial", 12, "bold"))
        lblPRN_No.grid(row=1, column=0, sticky=tk.W, padx=2, pady=6)
        txtPRN_NO = tk.Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.prn_var,width=29)
        txtPRN_NO.grid(row=1, column=1, padx=2, pady=6)

        lblID_No = tk.Label(DataFrameLeft, bg="powder blue", text="ID No.", font=("arial", 12, "bold"))
        lblID_No.grid(row=3, column=0, sticky=tk.W, padx=2, pady=6)
        txtID_NO = tk.Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.id_var,width=29)
        txtID_NO.grid(row=3, column=1, padx=2, pady=6)

        lblFIRST_NAME = tk.Label(DataFrameLeft, bg="powder blue", text="First Name", font=("arial", 12, "bold"))
        lblFIRST_NAME.grid(row=4, column=0, sticky=tk.W, padx=2, pady=6)
        txtFIRST_NAME = tk.Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.firstname_var,width=29)
        txtFIRST_NAME.grid(row=4, column=1, padx=2, pady=6)

        lblLAST_NAME = tk.Label(DataFrameLeft, bg="powder blue", text="Last Name", font=("arial", 12, "bold"))
        lblLAST_NAME.grid(row=5, column=0, sticky=tk.W, padx=2, pady=6)
        txtLAST_NAME = tk.Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable= self.lastname_var,width=29)
        txtLAST_NAME.grid(row=5, column=1, padx=2, pady=6)

        lblADDRESS = tk.Label(DataFrameLeft, bg="powder blue", text="Address", font=("arial", 12, "bold"))
        lblADDRESS.grid(row=6, column=0, sticky=tk.W, padx=2, pady=6)
        txtADDRESS = tk.Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.address_var,width=29)
        txtADDRESS.grid(row=6, column=1, padx=2, pady=6)

        lblMOBILE = tk.Label(DataFrameLeft, bg="powder blue", text="Mobile No.", font=("arial", 12, "bold"))
        lblMOBILE.grid(row=7, column=0, sticky=tk.W, padx=2, pady=6)
        txtMOBILE = tk.Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable= self.mobile_var,width=29)
        txtMOBILE.grid(row=7, column=1, padx=2, pady=6)

        lblBOOK_ID = tk.Label(DataFrameLeft, bg="powder blue", text="Book ID", font=("arial", 12, "bold"))
        lblBOOK_ID.grid(row=0, column=2, sticky=tk.W, padx=2, pady=6)
        txtBOOK_ID = tk.Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.bookid_var,width=29)
        txtBOOK_ID.grid(row=0, column=3, padx=2, pady=6)

        lblBOOK_NAME = tk.Label(DataFrameLeft, bg="powder blue", text="Book Name", font=("arial", 12, "bold"))
        lblBOOK_NAME.grid(row=1, column=2, sticky=tk.W, padx=2, pady=6)
        txtBOOK_NAME = tk.Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.bookname_var,width=29)
        txtBOOK_NAME.grid(row=1, column=3, padx=2, pady=6)

        lblDATE_BORROWED = tk.Label(DataFrameLeft, bg="powder blue", text="Date Borrowed", font=("arial", 12, "bold"))
        lblDATE_BORROWED.grid(row=2, column=2, sticky=tk.W, padx=2, pady=6)
        txtDATE_BORROWED = tk.Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable= self.dateborrowed_var,width=29)
        txtDATE_BORROWED.grid(row=2, column=3, padx=2, pady=6)

        lblDATE_DUE = tk.Label(DataFrameLeft, bg="powder blue", text="Date Due", font=("arial", 12, "bold"))
        lblDATE_DUE.grid(row=3, column=2, sticky=tk.W, padx=2, pady=6)
        txtDATE_DUE = tk.Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.datedue_var,width=29)
        txtDATE_DUE.grid(row=3, column=3, padx=2, pady=6)

        lblFINE = tk.Label(DataFrameLeft, bg="powder blue", text="Late Return Fine:", font=("arial", 12, "bold"))
        lblFINE.grid(row=4, column=2, sticky=tk.W, padx=2, pady=6)
        txtFINE = tk.Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.latereturnfine_var,width=29)
        txtFINE.grid(row=4, column=3, padx=2, pady=6)

        lblACTUAL_PRICE = tk.Label(DataFrameLeft, bg="powder blue", text="Actual Price", font=("arial", 12, "bold"))
        lblACTUAL_PRICE.grid(row=5, column=2, sticky=tk.W, padx=2, pady=6)
        txtACTUAL_PRICE = tk.Entry(DataFrameLeft, font=("arial", 12, "bold"),textvariable=self.actualprice_var,width=29)
        txtACTUAL_PRICE.grid(row=5, column=3, padx=2, pady=6)



        
        
        # =======DATA FRAME RIGHT========
        DataFrameRight = tk.LabelFrame(frame, text="Book Details", bg="powder blue", fg="green", bd=8, relief=tk.RIDGE, font=("times new roman", 10, "bold"))
        DataFrameRight.place(x=860, y=5, width=450, height=350)
        self.txtBox=tk.Text(DataFrameRight, font=("arial", 12, "bold"),width=26,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=tk.Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Automate the Boring Stuff with Python','Fluent Python','Python Cookbook',
                 'The C++ Programming Language','C++ Primer','C++ Concurrency in Action',
                 'Modern C++ Design: Generic Programming and Design Patterns Applied']
        
        def SelectBook(event=""):
            value=str(listbox.get(listbox.curselection()))
            x=value
            if(x=="Automate the Boring Stuff with Python"):
                self.bookid_var.set("BKID5454")
                self.bookname_var.set("Automate the Boring Stuff with Python")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.actualprice_var.set("Rs.775")

            elif(x=="Fluent Python"):
                self.bookid_var.set("BKID5455")
                self.bookname_var.set("Fluent Python")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.actualprice_var.set("Rs.1005") 

            elif(x=="Python Cookbook"):
                self.bookid_var.set("BKID5600")
                self.bookname_var.set("Python Cookbook")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.actualprice_var.set("Rs.500")  

            elif(x=="The C++ Programming Language "):
                self.bookid_var.set("BKID5601")
                self.bookname_var.set("The C++ Programming Language")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.actualprice_var.set("Rs.650") 

            elif(x=="C++ Primer"):
                self.bookid_var.set("BKID5751")
                self.bookname_var.set("C++ Primer")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.actualprice_var.set("Rs.800") 

            elif(x=="C++ Concurrency in Action"):
                self.bookid_var.set("BKID5740")
                self.bookname_var.set("C++ Concurrency in Action")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.actualprice_var.set("Rs.1000")  

            elif(x=="Modern C++ Design: Generic Programming and Design Patterns Applied"):
                self.bookid_var.set("BKID5115")
                self.bookname_var.set("Modern C++ Design: Generic Programming and Design Patterns Applied")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.latereturnfine_var.set("Rs.50")
                self.actualprice_var.set("Rs.1200")                   
        
        listbox=tk.Listbox(DataFrameRight,font=("arial", 12, "bold"),width=20,height=16)
        listbox.bind("<<ListboxSelect>>",SelectBook)
        listbox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listbox.yview)

        #for loop to take the list of books in the listbox which have the scrollbar
        for item in listBooks:
           listbox.insert(tk.END,item)
        

        # =======BUTTONS FRAME========
        Framebutton = tk.Frame(self.root, bd=12, relief=tk.RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=530, width=1360, height=70)

        btnAddData=tk.Button(Framebutton,command=self.add_data,text="Add Data",font=("arial", 12, "bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)
        btnAddData=tk.Button(Framebutton,command=self.ShowData,text="Show Data",font=("arial", 12, "bold"),width=21,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)
        btnAddData=tk.Button(Framebutton,command=self.update,text="Update",font=("arial", 12, "bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)
        btnAddData=tk.Button(Framebutton,command=self.delete,text="Delete",font=("arial", 12, "bold"),width=21,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)
        btnAddData=tk.Button(Framebutton,command=self.reset,text="Reset",font=("arial", 12, "bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)
        btnAddData=tk.Button(Framebutton,command=self.iExit, text="Exit",font=("arial", 12, "bold"),width=21,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)

        # =======INFORMATION FRAME========
        FrameDetails = tk.Frame(self.root, bd=12, relief=tk.RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=600, width=1360, height=100)

        Table_Frame = tk.Frame(FrameDetails, bd=6, relief=tk.RIDGE, bg="powder blue")
        Table_Frame.place(x=0, y=2, width=1290, height=80)

        xscroll=ttk.Scrollbar(Table_Frame,orient="horizontal")
        yscroll=ttk.Scrollbar(Table_Frame,orient="vertical")


        self.library_table=ttk.Treeview(Table_Frame,column=("membertype","PRN No.","idno","firstname","lastname","address",
                                                            "mobile","bookid","bookname","dateborrowed","datedue",
                                                            "latereturnfine","actualprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side="bottom",fill="x")
        yscroll.pack(side="right",fill="y")

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)



        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("PRN No.",text="PRN No.")
        self.library_table.heading("idno",text="ID No.")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address",text="Address")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("bookname",text="Book Namw")
        self.library_table.heading("dateborrowed",text="Date of Borrowed")
        self.library_table.heading("datedue",text="Data Due")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("actualprice",text="Actual Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill="both",expand=1) 

        self.library_table.column("membertype",width=70)
        self.library_table.column("PRN No.", width=70)
        self.library_table.column("idno",  width=70)
        self.library_table.column("firstname", width=70)
        self.library_table.column("lastname", width=70)
        self.library_table.column("address", width=70)
        self.library_table.column("mobile",  width=70)
        self.library_table.column("bookid",  width=70)
        self.library_table.column("bookname",  width=70)
        self.library_table.column("dateborrowed", width=70)
        self.library_table.column("datedue", width=70)
        self.library_table.column("latereturnfine", width=70)
        self.library_table.column("actualprice", width=70)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)


    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="W7301@jqir#",database="library_management")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                          self.member_var.get(),
                                                          self.prn_var.get(),
                                                          self.id_var.get(),
                                                          self.firstname_var.get(),
                                                          self.lastname_var.get(),
                                                          self.address_var.get(),
                                                          self.mobile_var.get(),
                                                          self.bookid_var.get(),
                                                          self.bookname_var.get(),
                                                          self.dateborrowed_var.get(),
                                                          self.datedue_var.get(),
                                                          self.latereturnfine_var.get(),
                                                          self.actualprice_var.get()
                                                          ))    
        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Success","Member Has been inserted successfully")

    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="W7301@jqir#",database="library_management")
        my_cursor=conn.cursor()
        my_cursor.execute("UPDATE library SET MemberType=%s, IDNo=%s, FirstName=%s, LastName=%s, ADDRESS=%s, MobileNumber=%s, BookID=%s, BookName=%s, DateBorrowed=%s, DateDue=%s, LateReturnFine=%s, ActualPrice=%s WHERE PRNNo=%s", (
                                  self.member_var.get(),
                                  self.id_var.get(),
                                  self.firstname_var.get(),
                                  self.lastname_var.get(),
                                  self.address_var.get(),
                                  self.mobile_var.get(),
                                  self.bookid_var.get(),
                                  self.bookname_var.get(),
                                  self.dateborrowed_var.get(),
                                  self.datedue_var.get(),
                                  self.latereturnfine_var.get(),
                                  self.actualprice_var.get(),
                                  self.prn_var.get()  # prn_no. is at last as we update according to it
        ))

        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member has been updated") # this is the small square message box that is show when any update has been done by clicking update button on horizontal bar


    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="W7301@jqir#",database="library_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",tk.END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
       cursor_row = self.library_table.focus()
       content = self.library_table.item(cursor_row)
       row = content['values']


       self.member_var.set(row[0])
       self.prn_var.set(row[1])
       self.id_var.set(row[2])
       self.firstname_var.set(row[3])
       self.lastname_var.set(row[4])
       self.address_var.set(row[5])
       self.mobile_var.set(row[6])
       self.bookid_var.set(row[7])
       self.bookname_var.set(row[8])
       self.dateborrowed_var.set(row[9])
       self.datedue_var.set(row[10])
       self.latereturnfine_var.set(row[11])
       self.actualprice_var.set(row[12])
    
    #to show dtat after click on show data horizontal tab in right most box
    def ShowData(self):
        self.txtBox.insert(tk.END,"Member Type\t\t"+self.member_var.get() + "\n")   
        self.txtBox.insert(tk.END,"PRN No.\t\t"+self.prn_var.get() + "\n")   
        self.txtBox.insert(tk.END,"ID No\t\t"+self.id_var.get() + "\n")   
        self.txtBox.insert(tk.END,"First Name\t\t"+self.firstname_var.get() + "\n")   
        self.txtBox.insert(tk.END,"Last Name\t\t"+self.lastname_var.get() + "\n")   
        self.txtBox.insert(tk.END,"Address\t\t"+self.address_var.get() + "\n")   
        self.txtBox.insert(tk.END,"Mobile No.\t\t"+self.mobile_var.get() + "\n")   
        self.txtBox.insert(tk.END,"Book ID\t\t"+self.bookid_var.get() + "\n")   
        self.txtBox.insert(tk.END,"Book Name\t\t"+self.bookname_var.get() + "\n")   
        self.txtBox.insert(tk.END,"Data Borrowed\t\t"+self.dateborrowed_var.get() + "\n")   
        self.txtBox.insert(tk.END,"Data Due\t\t"+self.datedue_var.get() + "\n")   
        self.txtBox.insert(tk.END,"Late Return Fine\t\t"+self.latereturnfine_var.get() + "\n")   
        self.txtBox.insert(tk.END,"Actual Price\t\t"+self.actualprice_var.get() + "\n")   

    def reset(self):
     self.member_var.set("")
     self.prn_var.set("")
     self.id_var.set("")
     self.firstname_var.set("")
     self.lastname_var.set("")
     self.address_var.set("")
     self.mobile_var.set("")
     self.bookid_var.set("")
     self.bookname_var.set("")
     self.dateborrowed_var.set("")
     self.datedue_var.set("")
     self.latereturnfine_var.set("")
     self.actualprice_var.set("")
     self.txtBox.delete("1.0", tk.END)  # Corrected attribute name


    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return   


    def delete(self):
        if self.prn_var.get()==""  or self.id_var.get()=="":
            messagebox.showerror("Error","First Select the Member")  # if data is not present in the entry field than show error
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="W7301@jqir#",database="library_management")
            my_cursor=conn.cursor()
            query="delete from library where PRNNo=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been Deleted")


               






if __name__ == "__main__":
    root = tk.Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
