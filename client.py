#Will ask for a username. A seperate thread will handle the incoming messages.
import time
import socket
import threading

tLock = threading.Lock()
shutdown = False

def receiving (name, sock):
    while not shutdown:
        try:
            tLock.acquire()
            while True:
                data, addr = sock.recfrom(1024)
                print (str(data))
        except:
            pass
        finally:
            tLock.release()

host = "127.0.0.10"
port = 0

server = ("127.0.0.10", 2222)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

rT = threading.Thread(target = receiving, args= ("RecvThread", s))
rT.start()

alias = raw_input("Name: ")
message = raw_input(alias + ">>>")

while message != 'q':
    if message != " ":
        s.sendto(alias + ": " + message, server)
    tLock.acquire()
    message = raw_input(alias + ">>>")
    tLock.release()
    time.sleep(0.1)

shutdown = True
rT.join()
s.close()