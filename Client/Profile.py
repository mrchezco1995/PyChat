from Tkinter import *
from PIL import Image, ImageTk


class Profile(object):

    def __init__(self, profname):
        self.profname = profname
        self.user = []
        self.name = []
        self.age = []
        self.gender = []

        self.usrl = 0
        self.nml = 2
        self.agl = 3
        self.gndl = 4
        loop =  0

        fetchfile = open("files/acclist.txt", "r")
        fetcher = fetchfile.read()
        counter = fetcher.count("\n")
        fetcher = fetcher.replace(" \n", ",")
        fetcher = fetcher.split(",", counter*5)
        while (loop < (counter*5)):
            self.user.append(fetcher[self.usrl])
            self.name.append(fetcher[self.nml])
            self.age.append(fetcher[self.agl])
            self.gender.append(fetcher[self.gndl])
            self.usrl = self.usrl + 5
            self.nml = self.nml + 5
            self.agl =  self.agl + 5
            self.gndl = self.gndl + 5
            loop = loop + 5

        self.proindex = self.user.index(self.profname)

        self.proname = self.name[self.proindex]
        self.proage = self.age[self.proindex]
        self.progender = self.gender[self.proindex]

        self.drawprofile()


    def drawprofile(self):
        self.root = Toplevel()
        self.frame = Frame(self.root, width=450, height=300)
        self.frame.pack()

        self.label0 = Label(self.root, text="Profile", font=("Segoe UI", 24))
        self.label0.place(x=12, y=9)

        self.label1 = Label(self.root, text="Name: ")
        self.label1.place(x=195, y=72)
        self.lblName = Label(self.root, text=self.proname)
        self.lblName.place(x=244, y=72)

        self.label2 = Label(self.root, text="Age: ")
        self.label2.place(x=195, y=112)
        self.lblAge = Label(self.root, text=self.proage)
        self.lblAge.place(x=244, y=112)

        self.label3 = Label(self.root, text="Gender: ")
        self.label3.place(x=195, y=152)
        self.lblGender = Label(self.root, text=self.progender)
        self.lblGender.place(x=244, y=152)

        self.btnClose = Button(self.root, text="Close", command=self.quitme)
        self.btnClose.place(x=36, y=212, width=100, height=25)

        self.originalphoto = Image.open("files/profilephotos/" + self.profname + ".jpg")
        self.resizedphoto = self.originalphoto.resize((140, 140), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.resizedphoto)
        self.profilephoto = Label(self.root, image=self.image)
        self.profilephoto.place(x=18, y=55)

        self.root.wm_title(self.profname + "'s Profile")
        self.root.resizable(width=FALSE, height=FALSE)
        self.root.mainloop()

    def quitme(self):
        self.root.destroy()