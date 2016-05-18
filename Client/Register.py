from Tkinter import *
from ttk import *
import tkMessageBox
import tkFileDialog
import shutil
import ctypes
import os

class Register:

    def regwindow(self):
        self.root = Tk()
        self.frame = Frame(self.root, width=350, height=340)
        self.frame.pack()

        self.label0 = Label(self.root, text="Register", font=("Segoe UI", 24))
        self.label0.place(x=13, y=13)

        self.label1 = Label(self.root, text="Name: ")
        self.label1.place(x=61, y=69)
        self.txtName = Entry(self.root)
        self.txtName.place(x=105, y=70, width=206, height=20)

        self.label2 = Label(self.root, text="Age: ")
        self.label2.place(x=70, y=99)
        self.txtAge = Entry(self.root)
        self.txtAge.place(x=105, y=100, width=206, height=20)

        self.label3 = Label(self.root, text="Gender: ")
        self.label3.place(x=54, y=129)
        self.gender = ("Male", "Female", "Undefined")
        self.cbGender = Combobox(self.root, values=self.gender,state="readonly")
        self.cbGender.current(0)
        self.cbGender.place(x=105, y=130, width=206, height=20)

        self.label4 = Label(self.root, text="Username: ")
        self.label4.place(x=41, y=159)
        self.txtUsername = Entry(self.root)
        self.txtUsername.place(x=105, y=160, width=206, height=20)

        self.label5 = Label(self.root, text="Password: ")
        self.label5.place(x=41, y=189)
        self.txtPassword = Entry(self.root, show="*")
        self.txtPassword.place(x=105, y=190, width=206, height=20)

        self.label6 = Label(self.root, text="Confirm Password: ")
        self.label6.place(x=5, y=219)
        self.txtConfirmPassword = Entry(self.root, show="*")
        self.txtConfirmPassword.place(x=105, y=220, width=206, height=20)

        self.label7 = Label(self.root, text="Image:")
        self.label7.place(x=60, y=252)
        self.btnImage = Button(self.root, text="Select Image", command=self.openfilez)
        self.btnImage.place(x=105, y=246, width=100, height=25)

        self.btnRegister = Button(self.root, text="Register", command=self.reg)
        self.btnRegister.place(x=53, y=285, width=100, height=25)

        self.btnCancel = Button(self.root, text="Cancel", command=self.root.destroy)
        self.btnCancel.place(x=177, y=285, width=100, height=25)

        self.root.wm_title("Register")
        self.root.resizable(width=FALSE, height=FALSE)
        self.root.mainloop()

    def reg(self):
        chktrigger = False
        global usernamepicked
        usernamepicked = self.txtUsername.get().strip()
        chktrigger = self.chkacc()

        if chktrigger != False:
            accfile = open("files/acclist.txt", "a")
            container = self.txtUsername.get().strip() + "," + self.txtPassword.get().strip() + "," + self.txtName.get().strip() + "," + self.txtAge.get().strip() + "," + self.cbGender.get() + " \n"
            accfile.write(container)
            accfile.close()
            atfile = open("files/accattempt.txt", "a")
            container = self.txtUsername.get().strip() + ",0 \n"
            atfile.write(container)
            atfile.close()
            print "Done writing to text file"
            print "Now attempting to save an image..."
            try:
                shutil.copy2(self.imagefile, "files/profilephotos/" + self.txtUsername.get().strip() + ".jpg")
            except IOError as e:
                print "Photo save error! Please Check! " + e.message
            tkMessageBox.showinfo( "Success!", "Account Successfully Created!")
            self.quitme()


    def chkacc(chk):
        usrl = 0
        username = []
        accfile = ""
        newfileswitch = False

        try:
            accfile = open("files/acclist.txt", "r")
        except:
            accfile = open("files/acclist.txt", "w+")
            newfileswitch = True

        if not newfileswitch:
            try:
                acc = accfile.read()
                loop = 0
                counts = (acc.count("\n"))
                acc = acc.replace(" \n", ",")
                acc = acc.split(",", counts*5)
                while (loop < (counts*5)):
                    username.append(acc[usrl])
                    usrl = usrl + 5
                    loop = loop + 5

                print usernamepicked
                accindex = username.index(usernamepicked)
                if accindex is not None:
                    print "Account Existed!", accindex
                    chk = False
                    tkMessageBox.showerror("Username taken!", "Apparently, that username was already taken")
                    return False
                else:
                    print "throwed to else 1"
                    print "This account doesn't exist"
                    chk = True
                    return True

            except:
                print "throwed an exception"
                print "This account doesn't exist"
                chk = True
                return True

        else:
            print "throwed to else 2"
            print "New File created"
            chk = True
            return True


    def openfilez(self):
        self.imagefile = tkFileDialog.askopenfilename(filetypes=(("JPG", "*.jpg"), ("All Files", "*")))
        print self.imagefile
        self.selectedimage = True


    def quitme(self):
        self.root.destroy()