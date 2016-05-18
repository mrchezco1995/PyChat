# PyChat
A Python-based Messenger

## What is PyChat? 
PyChat is a messenger written in Python 2.7 and utilizes TKinter for its GUI. This uses User Data Protocol or UDP as its connection method. It's intended to be multiplatform but since this some libs that only works for Windows (pywin32), this works only on Windows for now (you can remove pywin32 stuffs and replace it with other libs or remove it completely from the code to make it work on other platforms thou...).

##Features
PyChat has the following features:
- User Data Protocol (UDP) as its connection method 
- Group chat 
- Shows online members/clients 
- Profanity Filter (Because swearing is bad :( ) 
- Notification sounds (SQUEE!!! XD ) 
- Window Alert (Yellow flashing thingy on taskbar? Anyone?) 

## Prerequesites
PyChat requires the following libs: 
- Python 2.7
- pywin32
- Python Image Library (PIL)

## How to start PyChat?
You can start PyChat's client side by just running the file "start.py". In localhost situation this should run fine even if the server isn't running but when you are not running it as localhost, you need to start the server first, configure client's connection parameters to connect to the server's address, and run it... Not doing so will crash the script.

## How to configure the connection?
You can configure the connection by editing "chatbox.py" to connect it to the server's IP address... Just edit host and that's it... No need to configure the default port, which is 12345, unless you need to...

You can also configure "chatbox-server.py" connection settings too if you want... 

##Bugs
PyChat had some minor bugs like online clients doesn't refresh when a user disconnect, which make you think a user in question is online but its not... It also had some minor bugs when configuring user settings or account settings too... You'll see... That's all of the bugs I know so far for this code XD 

##SNEK
Yeah... Sneks.... SNEK!!!!!!!!!!!! XD 


- PyChat
