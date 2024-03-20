from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter
import random
import time
import datetime
import mysql.connector
from main import Face_Recognition_System

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1660x790+0+0")
        self.root.title("Login")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Afroj Ansari\OneDrive\Desktop\college_images\back.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\Afroj Ansari\OneDrive\Desktop\college_images\afroj.jpg")
        img1=img1.resize((100,100),Image.AFFINE)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        # label
        username=lbl=Label(frame,text="Username*",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password*",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #======Icon Images=====
        img2=Image.open(r"C:\Users\Afroj Ansari\OneDrive\Desktop\college_images\LoginIconAppl.png")
        img2=img2.resize((25,25),Image.AFFINE)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"C:\Users\Afroj Ansari\OneDrive\Desktop\college_images\lock-512.png")
        img3=img3.resize((25,25),Image.AFFINE)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=393,width=25,height=25)

        # LoginButton
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),border=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        # RegistereButton
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        # forgetpassbtn
        registerbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=10,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)    

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field are required")
        elif self.txtuser.get()=="Afroj" and self.txtpass.get()=="ansari":
             messagebox.showinfo("Success!","Welcome to code with Afroj channel please support me")    
        else:
             conn=mysql.connector.connect(host="localhost",username="root",password="Afroj@2000",database="mydata")
             my_cursor=conn.cursor()
             my_cursor.execute("select * from register where email=%s and password=%s", (
                                                self.txtuser.get(),
                                                self.txtpass.get()
                                                ))

             row=my_cursor.fetchone()
             #print (row)
             if row==None:
                 messagebox.showerror("Error","Invalid username & password")
             else:
                 open_main=messagebox.askyesno("YesNo","Access only admin")
                 if open_main>0:
                     self.new_window=Toplevel(self.root)
                     self.app=Face_Recognition_System(self.new_window)
                 else:
                     if not open_main:
                         return
             conn.commit()
             conn.close()

    #========reset password========
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.roo2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.roo2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.roo2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Afroj@2000",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct Answer",parent=self.roo2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value) 

                conn.commit()
                conn.close() 
                messagebox.showinfo("Info","Your password has been reset, please login new password",parent=self.roo2)
                self.roo2.destroy()  
            

        
    #========forget pass window========         
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","please enter the email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Afroj@2000",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
             # print(row)

            if row==None:
                messagebox.showerror("My error","Please enter the valid username")
            else:
                conn.close()
                self.roo2=Toplevel()
                self.roo2.title("Forget Password")
                self.roo2.geometry("340x450+610+170")

                l=Label(self.roo2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.roo2,text="Select Security Questions",font=('times new roman',15,'bold'),bg='white',fg='black')
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.roo2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your birth place","Your gf name","Your friend name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0) 

                security_A=Label(self.roo2,text="Security Answer",font=('times new roman',15,'bold'),bg='white',fg='black')
                security_A.place(x=50,y=150) 

                self.txt_security=ttk.Entry(self.roo2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.roo2,text="New Password",font=('times new roman',15,'bold'),bg='white',fg='black')
                new_password.place(x=50,y=220) 

                self.txt_new_password=ttk.Entry(self.roo2,font=("times new roman",15,"bold"))
                self.txt_new_password.place(x=50,y=250,width=250)

                btn=Button(self.roo2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=135,y=300)


        
class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x790+0+0")
        self.root.title("Register")


        #========variable=======
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confPass=StringVar()

        #====bg image====
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Afroj Ansari\OneDrive\Desktop\college_images\hiiiii.png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #====left image====
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\Afroj Ansari\OneDrive\Desktop\college_images\thought-good-morning-messages-LoveSove.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

        #=======main frame=====
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=('times new roman',20,'bold'),background='white',foreground='darkgreen')
        register_lbl.place(x=20,y=20)

        #=====label and entry====

        #------row1
        fname=Label(frame,text="First Name",font=('times new roman',15,'bold'),background='white')
        fname.place(x=50,y=100)

        frame_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        frame_entry.place(x=50,y=130,width=250) 

        l_name=Label(frame,text="Last Name",font=('times new roman',15,'bold'),bg='white')
        l_name.place(x=370,y=100) 

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #------row2
        contact=Label(frame,text="Contact No:",font=('times new roman',15,'bold'),bg='white',fg='black')
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email*",font=('times new roman',15,'bold'),bg='white',fg='black')
        email.place(x=370,y=170) 

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)


        #------row3
        security_Q=Label(frame,text="Select Security Questions",font=('times new roman',15,'bold'),bg='white',fg='black')
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your birth place","Your gf name","Your friend name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0) 

        security_A=Label(frame,text="Security Answer",font=('times new roman',15,'bold'),bg='white',fg='black')
        security_A.place(x=370,y=240) 

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        #------row4
        pswd=Label(frame,text="Password*",font=('times new roman',15,'bold'),bg='white',fg='black')
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password*",font=('times new roman',15,'bold'),bg='white',fg='black')
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confPass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #=======checkbutton========
        self.var_check=IntVar()
        checkbutton=Checkbutton(frame,variable=self.var_check,text="I agree the terms & conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbutton.place(x=50,y=380)

        #=====buttons=======
        img = Image.open(r"C:\Users\Afroj Ansari\OneDrive\Desktop\college_images\register-now-button1.jpg")
        img = img.resize((200, 55), Image.AFFINE)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0, cursor="hand2", font=('times new roman', 15, 'bold'), bg='white', fg='black')
        b1.place(x=10, y=420, width=200)

        img1 = Image.open(r"C:\Users\Afroj Ansari\OneDrive\Desktop\college_images\loginpng.png")
        img1 = img1.resize((200, 45), Image.AFFINE)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1,command=self.reset_login,borderwidth=0, cursor="hand2", font=('times new roman', 15, 'bold'), bg='white', fg='black')
        b1.place(x=330, y=420, width=200)

    #======function declaration=====
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
           messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confPass.get():
           messagebox.showerror("Error", "Password and confirm password must be the same")
        elif self.var_check.get() == 0:
           messagebox.showerror("Error", "Please agree to the terms and conditions")
        else:
    
              conn=mysql.connector.connect(host="localhost",username="root",password="Afroj@2000",database="mydata")
              my_cursor=conn.cursor()
              query=("Select * from register where email=%s")
              value=(self.var_email.get(),)
              my_cursor.execute(query,value)
              row=my_cursor.fetchone()
              if row!=None:
                  messagebox.showerror("Error","User already exist, please try another email")
              else:
                  my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s,%s)", (

                                                                                         self.var_fname.get(),
                                                                                         self.var_lname.get(),
                                                                                         self.var_contact.get(),
                                                                                         self.var_email.get(),
                                                                                         self.var_securityQ.get(),
                                                                                         self.var_securityA.get(),
                                                                                         self.var_pass.get()
         
                                                                                       ))
              conn.commit()
              conn.close()
              messagebox.showinfo("Success","Register Successfully")

    def reset_login(self):
        self.root.destroy()          

if __name__ == "__main__":
    main()