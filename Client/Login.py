from Tkinter import *
from PIL import ImageTk, Image
import tkMessageBox
import chatbox
import sys
import os

import Register



class Login(object):

    def loginwindow(self):
        self.root = Tk()
        '#Create a frame with a width of 330 and height of 250..... :) '
        self.frame = Frame(self.root, width=330, height=250)
        self.frame.pack()

        '#Load a logo from Pythons PIL Library'
        self.logo = ImageTk.PhotoImage(Image.open("images/logo.png"))
        '#Set that image as a label in Tkinter... '
        self.label0 = Label(self.root, image=self.logo)
        '#Exact Coordinate...... '
        '#Syempre, may offset rin ng konti :P '
        self.label0.place(x=12, y=8)

        '#Create a Label named, Login, with the exact location...'
        self.label1 = Label(self.root, text="Login: ")
        self.label1.place(x=51, y=134)

        '#Self Explanatory na...'
        self.label2 = Label(self.root, text="Password: ")
        self.label2.place(x=31, y=165)

        '#Create a textbox, set the exact location and exact width and height niya... '
        self.txtUser = Entry(self.root)
        self.txtUser.place(x=93, y=131, width=164, height=20)

        '#Self Explanatory na eto......'
        self.txtPass = Entry(self.root, show="*")
        self.txtPass.place(x=93, y=162, width=164, height=20)

        '#Create a button.....'
        self.btnLogin = Button(self.root, text="Login", command=self.login)
        self.btnLogin.place(x=128, y=188, width=75, height=23)

        self.btnRegister = Button(self.root, text="Register", command=Register.Register().regwindow)
        self.btnRegister.place(x=128, y=217, width=75, height=23)

        '#Set Window Name.... I called it, PyChat'
        self.root.wm_title("PyChat")
        '#Now set it to not resizable... Maximize Button should be disabled too with this... '
        self.root.resizable(width=FALSE, height=FALSE)
        self.root.mainloop()


    def login(self):
        acc = ""
        usrl = 0
        pwl = 1
        nml = 2

        username = []
        password = []
        name = []

        try:
            acc = open("files/acclist.txt", "r")
            accfile = acc.read()
            counts = (accfile.count("\n"))
            accfile = accfile.replace(" \n", ",")
            accfile = accfile.split(",", counts*5)
            loop = 0
            while (loop < (counts*5)):
                username.append(accfile[usrl])
                password.append(accfile[pwl])
                name.append(accfile[nml])

                usrl = usrl + 5
                pwl = pwl + 5
                nml = nml + 5
                loop = loop + 5

            accountindex = username.index(self.txtUser.get().strip())
            atfile = open("files/accattempt.txt", "r")
            atf = atfile.read()
            counter = atf.count("\n")
            atf = atf.replace(" \n", ",")
            atf = atf.split(",", counter*2)

            userat = []
            attempt = []
            usrl = 0
            atl = 1
            loop = 0
            while (loop < (counter*2)):
                userat.append(atf[usrl])
                attempt.append(atf[atl])
                usrl = usrl + 2
                atl = atl + 2
                loop = loop + 2

            if(int(attempt[userat.index(self.txtUser.get().strip())]) >= 3):
                tkMessageBox.showerror("Account Disabled!", "Account disabled! Maximum number of Login attempts has been reached! Please contact an Administrator to reset your account!")
            else:

                if (self.txtPass.get() == password[accountindex]):
                    print "Welcome, " + name[accountindex] + "!"
                    self.resetattempt()
                    tkMessageBox.showinfo("Login Success!", "Welcome, " + name[accountindex] + "!")
                    self.root.withdraw()
                    chatbox.Chatbox(username[accountindex])

                else:
                    print "Wrong Password! BOOOO :( "
                    self.writeattempt()
                    tkMessageBox.showerror("Wrong Password!", "Sorry, that was a wrong password!")


        except IOError as e:
            tkMessageBox.showerror("IOError!", "There was something wrong. Please Check the error below: \n" + e.message)
        except ValueError:
            tkMessageBox.showerror("Input Error!!", "An Input Error was found! Are you sure that account already exists?")
        except:
            #tkMessageBox.showerror("Unexpected Error!", "An Unexpected Error was encountered! Check!")
            print "Something went wrong.... Please go check it!"
            sys.exit()

    def writeattempt(self):
        usrl = 0
        atl = 1
        username = []
        attempts = []
        try:
            attemptfile = open("files/accattempt.txt", "r")
            try:
                atf = attemptfile.read()
                counts = atf.count("\n")
                atf = atf.replace(" \n", ",")
                atf = atf.split(",", counts*2)
                loop = 0
                while(loop < (counts*2)):
                    username.append(atf[usrl])
                    attempts.append(atf[atl])
                    usrl = usrl + 2
                    atl = atl + 2
                    loop = loop + 2

                attempts[username.index(self.txtUser.get().strip())] = str(int(attempts[username.index(self.txtUser.get().strip())]) + 1)

                usrl = 0
                loop = 0

                attemptfile = open("files/accattempt.txt", "w+")

                while (loop < (counts*2)):
                    container = username[usrl] + "," + attempts[usrl] + " \n"
                    attemptfile.write(container)
                    usrl = usrl + 1
                    loop = loop + 2

                attemptfile.close()

            except IOError as e:
                print "There was an IOError problem, please see details: \n" +  e.message
            except:
                print "There was a problem....."

        except IOError as e:
             print "There was an IOError problem, please see details: \n" +  e.message
        except:
            print "There was a problem....."

    def resetattempt(self):
        usrl = 0
        atl = 1
        username = []
        attempts = []
        try:
            attemptfile = open("files/accattempt.txt", "r")
            try:
                atf = attemptfile.read()
                counts = atf.count("\n")
                atf = atf.replace(" \n", ",")
                atf = atf.split(",", counts*2)
                loop = 0
                while(loop < (counts*2)):
                    username.append(atf[usrl])
                    attempts.append(atf[atl])
                    usrl = usrl + 2
                    atl = atl + 2
                    loop = loop + 2

                attempts[username.index(self.txtUser.get().strip())] = "0"

                usrl = 0
                loop = 0

                attemptfile = open("files/accattempt.txt", "w+")

                while (loop < (counts*2)):
                    container = username[usrl] + "," + attempts[usrl] + " \n"
                    attemptfile.write(container)
                    usrl = usrl + 1
                    loop = loop + 2

                attemptfile.close()

            except IOError as e:
                print "There was an IOError problem, please see details: \n" +  e.message
            except:
                print "There was a problem....."

        except IOError as e:
             print "There was an IOError problem, please see details: \n" +  e.message
        except:
            print "There was a problem....."



    def reg(self):
        regroot = Tk()
        b = Register.Register(regroot)
        #btnCancel = Button(regroot, text="Cancel", command=regroot.destroy)
        #btnCancel.place(x=177, y=270, width=100, height=25)
        regroot.wm_title("Register")
        regroot.resizable(width=FALSE, height=FALSE)
        regroot.mainloop()

    def quit(self):
        self.root.destroy()



