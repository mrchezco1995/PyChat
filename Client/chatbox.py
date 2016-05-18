from Tkinter import *
from socket import *
from threading import Thread, Lock
import tkFileDialog
import profanity_filter
import appearance
import UpdateAcc
import tkMessageBox
import Login
#import emoji
import time
import winsound
import win32gui
import Profile
import about

'#Connect to Server'
tLock = Lock()
shutdown = False

'#Put the server IP address here'
'#127.0.0.1 means localhost...'

host = "127.0.0.1"
port = 0
clientnames = []
server = (host, 12345)

s = socket(AF_INET, SOCK_DGRAM)
s.connect((host, port))
s.setblocking(0)

'#Load configurations...'
windowcolorfile = open("files/config/wcolor.txt", "r")
windowcolor = windowcolorfile.read()
print "Set Window color to: " + windowcolor
fontfile = open("files/config/wfont.txt", "r")
font = fontfile.read()
print "Set Font to: " + font
fontcolorfile = open("files/config/wfontcolor.txt", "r")
fontcolor = fontcolorfile.read()
print "Set Font color to: " + fontcolor
fontsizefile = open("files/config/wfontsize.txt", "r")
fontsize = int(fontsizefile.read())
print "Set Font size to: " + str(fontsize)

'#Load previous chat'
chathistory = open("files/chathistory.txt", "r")
chath = chathistory.read()

class Chatbox(object):

    def __init__(self, alias):

        self.alias = alias
        self.windowname = "PyChat - Logged In as " + self.alias
        self.playsound = True
        self.recvthread = Thread(target=self.recvmsg, args=("RecvThread", s))
        self.recvthread.start()
        #Thread(target=updateclient, args=("ClientListThread", s)).start()
        self.root = Toplevel()
        '#Create a window'
        self.frame = Frame(self.root, width=600, height=450, bg=windowcolor)
        self.frame.pack()

        '#Create a Menu'
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)

        self.accMenu = Menu(self.menu)
        self.menu.add_cascade(label="Account", menu=self.accMenu)
        self.accMenu.add_command(label="Update Account", command=self.updateacc)
        self.accMenu.add_separator()
        self.accMenu.add_command(label="Logout", command=self.quitme)
        self.accMenu.add_command(label="Exit", command=self.root.destroy)

        self.chatMenu = Menu(self.menu)
        self.menu.add_cascade(label="Chat", menu=self.chatMenu)
        self.chatMenu.add_command(label="Backup Conversation", command=self.saveconversation)
        self.chatMenu.add_command(label="Delete Conversation", command=self.clearconversation)

        self.thmMenu = Menu(self.menu)
        self.menu.add_cascade(label="Appearance", menu=self.thmMenu)
        self.thmMenu.add_command(label="Themes", command=appearance.Appearance().appwindow)

        self.abtMenu = Menu(self.menu)
        self.menu.add_cascade(label="About", menu=self.abtMenu)
        self.abtMenu.add_command(label="About this Project", command=about.About().aboutus)

        '#Create a chat log'
        self.chatLog = Text(self.root, font=(font, fontsize), fg=fontcolor)
        self.chatLog.insert(END, "Connecting..... \n")
        self.chatLog.config(state=DISABLED)
        self.scrollbar1 = Scrollbar(self.root, command=self.chatLog.yview, cursor="heart")
        self.chatLog["yscrollcommand"] = self.scrollbar1.set
        self.scrollbar1.place(x=415, y=13, height=325)
        self.chatLog.place(x=13, y=13, width=405, height=325)


        '#Create list of friends online'
        self.label2 = Label(self.root, text="Online: ", font=(font, 20), fg="White", bg=windowcolor)
        self.label2.place(x=445, y=11)
        self.friendsList = Listbox(self.root, font=(font, fontsize), fg=fontcolor)
        #self.friendsList.config(state=DISABLED)
        self.friendsList.bind("<Double-Button-1>", self.fetchme)
        self.scrollbar2 = Scrollbar(self.root, command=self.friendsList.yview, cursor="heart")
        self.friendsList["yscrollcommand"] = self.scrollbar2.set
        self.friendsList.place(x=445, y=49, width=142, height=293)

        '#Create a scrollbar'

        '#Create an entry where you can enter your message'
        self.chatEntry = Text(self.root, font=(font, fontsize), fg=fontcolor)
        self.chatEntry.bind("<Return>", self.sendmsg)
        self.chatEntry.place(x=13, y=349, width=425, height=85)



        '#Create a send button'
        self.btnLogin = Button(self.root, text="SEND", command=self.sendmsg)
        self.btnLogin.bind("<Return>", self.sendmsg)
        self.btnLogin.place(x=445, y=349, width=142, height=85)

        '#Set it fixed, not resizable......'
        self.root.resizable(width=FALSE, height=FALSE)
        self.root.wm_title(self.windowname)
        self.chatLog.config(state=NORMAL)
        self.chatLog.insert(END, chath)
        self.chatLog.see(END)
        self.chatLog.config(state=DISABLED)
        self.root.mainloop()


    def sendmsg(self, *args):
        if self.chatEntry.get("0.0", END).strip() != "":
            self.playsound = False
            msg = self.alias + " : " + self.chatEntry.get("0.0", END).strip() + "\n"
            '#Filter Message before sending it...'
            f = profanity_filter.Filter(msg, clean_word="[*****]")
            cleanmsg = f.clean()

            #msg = emoji.emojize(chatEntry.get("0.0", END).strip() + " \n") '#Experimental Emjoi support, but this doesn't easily work on Python 2.7 so no go :( '

            #chatLog.config(state=NORMAL)
            #chatLog.insert(END, msg)
            self.chatEntry.delete(1.0, END)
            #chatLog.config(state=DISABLED)
            s.sendto(cleanmsg, server)
        else:
            print "Empty textbox... No Message was sent"

    def recvmsg(self, name, sock):
        s.sendto(self.alias + " Is connected \n", server)
        s.sendto("<clntadr>" + self.alias, server)
        while not shutdown:
            try:
                data = sock.recv(1024)
                if data.count("<client>") >= 1:
                    print "A new user joined the chat"
                    dtr = data.replace("<client>", "")
                    print "and that's " + dtr
                    try:
                        clientindex = clientnames.index(dtr)
                        clientnames[clientindex] = dtr
                        print clientnames[clientindex] + " rejoined the conversation"
                    except:
                        clientnames.append(dtr)
                        print dtr + " joined the conversation"

                   # self.friendsList.config(state=NORMAL)
                    self.friendsList.delete(0, END)
                    for users in clientnames:
                        self.friendsList.insert(END, users)
                        print "adding user: " + users
                    #self.friendsList.config(state=DISABLED)
                else:
                    if data != "":
                        self.chatLog.config(state=NORMAL)
                        self.chatLog.insert(END, str(data))
                        self.chatLog.see(END)
                        self.chatLog.config(state=DISABLED)
                        try:
                            self.chathfile = open("files/chathistory.txt", "a")
                            self.chathfile.write(str(data))
                            self.chathfile.close()
                        except:
                            print "Cannot save chat to file for some reasons...."
                        if self.playsound is True:
                            try:
                                print "Playing Notification....."
                                winsound.PlaySound("files/notif.wav", winsound.SND_FILENAME)
                            except:
                                print "File not found... Cannot play notification sound"
                            try:
                                flashwin = win32gui.FindWindow(None, self.windowname)
                                win32gui.FlashWindow(flashwin, True)
                            except:
                                print "Something went wrong... Cannot flash window..."
                        else:
                            self.playsound = True
                        print str(data)
            except:
                pass

            time.sleep(0.2)


    def updateclient(self, sock):
        while not shutdown:
            try:
                data = sock.recv(1024)
                if data.count("<client>") >= 1:
                    data = data.replace("<client>", "")
                    try:
                        clientindex = clientnames.index(data)
                        clientnames[clientindex] = data
                    except:
                        clientnames.append(data)
                    self.friendsList.config(state=NORMAL)
                    self.friendsList.delete("1.0", END)
                    for users in clientnames:
                        self.friendsList.insert(END, users + "\n")
                    self.friendsList.config(state=DISABLED)
            except:
                pass


    def fetchme(self, *args):
        selection = self.friendsList.curselection()
        print "Opening Profile for " + self.friendsList.get(selection)
        Profile.Profile(self.friendsList.get(selection))


    def saveconversation(self):
        f = tkFileDialog.asksaveasfile(mode="w", defaultextension=".txt")
        if f is None:
            return
        text2save = self.chatLog.get("1.0", END)
        f.write(text2save)
        f.close()
        tkMessageBox.showinfo("Success", "Conversation successfully saved!")

    def clearconversation(self):
        result = tkMessageBox.askquestion("Delete Conversation", "You are about to delete your conversation history. Are you sure you want to do this?", icon="warning")
        if result == "yes":
            f = open("files/chathistory.txt", "w+")
            f.close()
            self.chatLog.config(state=NORMAL)
            self.chatLog.delete(0.0, END)
            self.chatLog.config(state=DISABLED)
            tkMessageBox.showinfo("Success", "Chat History successfully deleted!")
        else:
            return


    def updateacc(self):
        UpdateAcc.UpdateAcc(self.alias)



    def quitme(self):
        shutdown = True
        time.sleep(1)
        s.close()
        time.sleep(1)
        self.root.destroy()
        Login.Login().loginwindow()



#root = Tk()
#b = Chatbox(root)
#root.resizable(width=FALSE, height=FALSE)
#root.protocol("WM_DELETE_WINDOW", Chatbox.quit)
#root.wm_title("Chat - Underchat")
#root.mainloop()
#s.close()