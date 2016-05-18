from Tkinter import *
from ttk import *
import tkMessageBox
import shutil
import tkFileDialog

class UpdateAcc(object):

    def __init__(self, user):
        self.user = user
        self.namelist = []
        self.agelist = []
        self.usernamelist = []
        self.pwlist = []
        self.genderlist = []

        self.usrl = 0
        self.pwl = 1
        self.nml = 2
        self.agl = 3
        self.gndl = 4

        accfile = open("files/acclist.txt", "r")
        acc = accfile.read()
        self.counts = acc.count("\n")
        acc = acc.replace(" \n", ",")
        acc = acc.split(",", self.counts*5)
        loop = 0

        while (loop < (self.counts*5)):
            self.usernamelist.append(acc[self.usrl])
            self.pwlist.append(acc[self.pwl])
            self.namelist.append(acc[self.nml])
            self.agelist.append(acc[self.agl])
            self.genderlist.append(acc[self.gndl])

            self.usrl = self.usrl + 5
            self.pwl = self.pwl + 5
            self.nml = self.nml + 5
            self.agl = self.agl + 5
            self.gndl = self.gndl + 5
            loop = loop + 5

        self.accindex = self.usernamelist.index(self.user)
        print self.user
        print self.accindex


        self.update()



    def update(self):
        self.root = Tk()
        self.frame = Frame(self.root, width=350, height=340)
        self.frame.pack()

        self.label0 = Label(self.root, text="Update Info", font=("Segoe UI", 24))
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

        self.btnRegister = Button(self.root, text="Update", command=self.saveme)
        self.btnRegister.place(x=53, y=285, width=100, height=25)

        self.btnCancel = Button(self.root, text="Cancel", command=self.root.destroy)
        self.btnCancel.place(x=177, y=285, width=100, height=25)
        self.root.wm_title("Update")
        self.root.resizable(width=FALSE, height=FALSE)

        self.txtName.insert(0, self.namelist[self.accindex])
        self.txtAge.insert(0, self.agelist[self.accindex])
        self.cbGender.current(self.accindex)
        self.txtUsername.insert(0, self.usernamelist[self.accindex])
        self.txtPassword.insert(0, self.pwlist[self.accindex])
        self.txtConfirmPassword.insert(0, self.pwlist[self.accindex])
        self.root.mainloop()


    def saveme(self):
        if self.txtPassword.get() == self.txtConfirmPassword.get():
            self.usernamelist[self.accindex] = self.txtUsername.get().strip()
            self.pwlist[self.accindex] = self.txtPassword.get()
            self.namelist[self.accindex] = self.txtName.get().strip()
            self.agelist[self.accindex] = self.txtAge.get().strip()
            self.genderlist[self.accindex] = self.cbGender.get()

            f = open("files/acclist.txt", "w+")
            sel = 0
            loop = 0

            while (loop < (self.counts*5)):
                container = self.usernamelist[sel] + "," + self.pwlist[sel] + "," + self.namelist[sel] + "," + self.agelist[sel] + "," + self.genderlist[sel] + " \n"
                f.write(container)

                sel = sel + 1
                loop = loop + 5

            f.close()

            try:
                shutil.copy2(self.imagefile, "files/profilephotos/" + self.txtUsername.get().strip() + ".jpg")
            except IOError as e:
                print "Photo save error! Please Check! " + e.message

            tkMessageBox.showinfo("Success!", "Account Information Successfully updated!")
            self.root.destroy()

        else:
            tkMessageBox.showerror("Error!", "Password not the same! No changes are made")


    def openfilez(self):
        self.imagefile = tkFileDialog.askopenfilename(filetypes=(("JPG", "*.jpg"), ("All Files", "*")))
        print self.imagefile
        self.selectedimage = True



    def quitme(self):
        self.root.destroy()