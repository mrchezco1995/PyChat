from socket import *
import time

'#Put IP here...'
'#Put Socket here...'
host = ""
port = 12345

clients = []
clientnames = []

s = socket(AF_INET, SOCK_DGRAM)
s.bind((host, port))

'#Set Blocking to 0 so it will accept basically everything'
s.setblocking(0)

quitting = False
print "server started....."

while not quitting:
    try:
        '#Receive 1024 bytes of data... Its basically 1KB :P '
        data, addr = s.recvfrom(1024)
        if str(data).count("<clntadr>") >= 1:
            clientname = str(data).replace("<clntadr>", "")
            try:
                clientindex = clientnames.index(clientname)
                clientnames[clientindex] = clientname
                print "A Client has joined back to the Chat!"
                print clients
                print clientnames
                for clientlist in clientnames:
                    for client in clients:
                        s.sendto("<client>" + clientlist, client)
            except:
                clientnames.append(clientname)
                print "New Clients have been added to the list! :D"
                print clients
                print clientnames
                for clientlist in clientnames:
                    for client in clients:
                        s.sendto("<client>" + clientlist, client)
        else:
            if "Quit" in str(data):
                '#Quit if a specified string was detected...'
                quitting = True
            if addr not in clients:
                '#If a new client was found, add them to the clients list'
                clients.append(addr)


            print time.ctime(time.time()) + str(addr) + ": :" + str(data)
            for client in clients:
                '#Send the data to all clients... This is a groupchat afterall :3'
                s.sendto(data, client)

    except:
        '#Try again if something goes wrong.....' '#There is something wrong, like literally LOL. Pass and re-run the thread XD'
        pass

    '#Add a delay of .2 seconds to prevent the CPU from overloading... '
    time.sleep(0.2)

'#Close the connection when out of the loop'
s.close()