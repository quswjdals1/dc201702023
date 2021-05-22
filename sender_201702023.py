import sys
import socket
import os
import math
import time

def pcheck(argv):
    if len(argv)!=2:
        sys.exit()

def sender_send(file_name):
    s.sendto("valid list command.".encode('utf-8'),caddr)
    
    if(os.path.isfile(file_name)):
        s.sendto("file exists!".encode('utf-8'),caddr)
    else:
        s.close()
        sys.exit()
    size = os.stat(file_name).st_size
    print("file size "+str(size)+"bytes")
    
    check = math.ceil(size/4096)
    s.sendto(str(check).encode('utf-8'), caddr)
    
    f = open(file_name,"rb")
    count=1
    data,addr=s.recvfrom(4096)
    
    if (data.decode('utf-8'))=="ready":
        while check!=0:
            c_file = f.read(4096)
            s.sendto(c_file,caddr)
            check-=1
            print ("packet number "+str(count))
            count+=1
            time.sleep(0.005)
    f.close()
    print("file closed")

if __name__ == "__main__":
    
    pcheck(sys.argv)
    
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(("",int(sys.argv[1])))
    while True:
        data, caddr = s.recvfrom(4096)

        text = data.decode('utf8')
        handler = text.split()

        if(handler[0])=='receive':
            sender_send(handler[1])
        elif handler[0]=='exit':
            s.close()
            sys.exit()
