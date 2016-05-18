from Tkinter import *
from ttk import *
import tkMessageBox


class Appearance():

    def appwindow(self):
        self.root = Tk()

        self.frame = Frame(self.root, width=310, height=300)
        self.frame.pack()

        self.label0 = Label(self.root, text="Appearance", font=("Segoe UI", 24))
        self.label0.place(x=13, y=13)

        self.label1 = Label(self.root, text="Window Color: ")
        self.label1.place(x=12, y=71)
        self.wincolor = ("Black", "White", "Blue", "Red", "Green", "Pink", "Purple", "Violet")
        self.cbWincolor = Combobox(self.root, values=self.wincolor, state="readonly")
        self.cbWincolor.current(0)
        self.cbWincolor.place(x=94, y=68, width=190, height=21)

        self.label2 = Label(self.root, text="Font: ")
        self.label2.place(x=57, y=106)
        self.winfont = ("Arial", "Times New Roman", "Papyrus", "Comic Sans MS", "Segoe UI", "Calibri", "Consolas", "Lucida Sans")
        self.cbWinfont = Combobox(self.root, values=self.winfont, state="readonly")
        self.cbWinfont.current(0)
        self.cbWinfont.place(x=94, y=103, width=190, height=21)

        self.label3 = Label(self.root, text="Font Size: ")
        self.label3.place(x=34, y=141)
        self.winfontsize = ("10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20")
        self.cbWinfontsize = Combobox(self.root, values=self.winfontsize, state="readonly")
        self.cbWinfontsize.current(0)
        self.cbWinfontsize.place(x=94, y=138, width=190, height=21)

        self.label4 = Label(self.root, text="Font Color: ")
        self.label4.place(x=30, y=176)
        self.winfontcolor = ("Black", "White", "Blue", "Red", "Green", "Pink", "Purple", "Violet")
        self.cbWinfontcolor = Combobox(self.root, values=self.winfontcolor, state="readonly")
        self.cbWinfontcolor.current(0)
        self.cbWinfontcolor.place(x=94, y=173, width=190, height=21)

        self.btnSave = Button(self.root, text="Save", command=self.save)
        self.btnSave.place(x=43, y=217, width=100, height=25)

        self.btnCancel = Button(self.root, text="Cancel", command=self.quit)
        self.btnCancel.place(x=149, y=217, width=100, height=25)

        self.root.wm_title("Appearance")
        self.root.resizable(width=FALSE, height=FALSE)

        self.root.mainloop()

    def save(self):
        try:
            self.wcolorfile = open("files/config/wcolor.txt", "w+")
            self.wcolorfile.write(self.cbWincolor.get())
            self.wcolorfile.close()

            self.wfontfile = open("files/config/wfont.txt", "w+")
            self.wfontfile.write(self.cbWinfont.get())
            self.wfontfile.close()

            self.wfontcolor = open("files/config/wfontcolor.txt", "w+")
            self.wfontcolor.write(self.cbWinfontcolor.get())
            self.wfontcolor.close()

            self.wfontsize = open("files/config/wfontsize.txt", "w+")
            self.wfontsize.write(self.cbWinfontsize.get())
            self.wfontsize.close()

            tkMessageBox.showinfo("Success!", "Changes successfully saved! You may need to restart the program to see changes...")
            self.quit()

        except IOError as e:
            tkMessageBox.showerror("IOError!", "There's something went wrong... \n" + e.message)

    def quit(self):
        self.root.destroy()