from Tkinter import *
from PIL import ImageTk, Image

class About:
    def aboutus(self):
        self.root = Toplevel()
        self.frame = Frame(self.root, width=330, height=470)
        self.frame.pack()

        self.imagelogo = ImageTk.PhotoImage(Image.open("images/logo.png"))
        self.imagelabel = Label(self.root, image=self.imagelogo)
        self.imagelabel.place(x=13, y=13)

        self.label0 = Label(self.root, text="PyChat By:", font=("Segoe UI", 14), fg="Black")
        self.label0.place(x=9, y=116)

        self.label1 = Label(self.root, text="Renz Hernandez (mrchezco1995)", font=("Segoe UI", 12), fg="Black")
        self.label1.place(x=13, y=152)

        self.label2 = Label(self.root, text="Follow me on Twitter: @TechKidPH", font=("Segoe UI", 12), fg="Black")
        self.label2.place(x=13, y=182)

        self.label3 = Label(self.root, text="Follow me on FB: fb.com/MrChezco1995r2", font=("Segoe UI", 12), fg="Black")
        self.label3.place(x=13, y=212)

        self.label4 = Label(self.root, text="Sub to my YouTube Channels down below:", font=("Segoe UI", 12), fg="Black")
        self.label4.place(x=13, y=242)

        self.label5 = Label(self.root, text="youtube.com/user/mrchezco1995", font=("Segoe UI", 12), fg="Black")
        self.label5.place(x=13, y=272)

        self.label6 = Label(self.root, text="youtube.com/user/TechKidPH", font=("Segoe UI", 12), fg="Black")
        self.label6.place(x=13, y=302)

        self.label6 = Label(self.root, text="HAIL HYDRA!!!", font=("Segoe UI", 12), fg="Black")
        self.label6.place(x=13, y=332)

        self.label7 = Label(self.root, text="jk XD ", font=("Segoe UI", 12), fg="Black")
        self.label7.place(x=13, y=362)

        self.btnOkay = Button(self.root, text="Okay", command=self.root.destroy)
        self.btnOkay.place(x=110, y=422, width=100, height=25)

        self.root.wm_title("About PyChat")
        self.root.resizable(width=FALSE, height=FALSE)
        self.root.mainloop()






