import time
import socket


host = "127.0.0.10"
port = 2222

clients = []

#going to use the UDP communication

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

quitting = False
print ("Server Active!")

while not quitting:
    try:
        data, addr = s.recvfrom(1024)
        if "Quit" in str(data):
            quitting = True

        if addr not in clients:
            clients.append(addr)

        print (time.ctime(time.time()) + str(addr) + ": :" + str(data))

    except:
        pass
for client in clients:
    s.sendto(data,client)
s.close()
