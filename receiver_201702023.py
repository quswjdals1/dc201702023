import socket
import os
import sys

def pcheck(argv):
    if len(argv)!=3:
        sys.exit()
        return False
    else:
        return True



if __name__ == "__main__":

    pcheck(sys.argv)
    print("asdasd")
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.setblocking(0)
    s.settimeout(15)
    
    while True:
        a=input("enter a command: \n1. receive [file_name]\n2. exit\n")
        s.sendto(a.encode('utf-8'),((sys.argv[1]),int(sys.argv[2])))
    
        a1=a.split()
        if a1[0]=="receive":
            data,addr =s.recvfrom(4096)
            print(data.decode('utf-8'))
        elif a1[0]=="exit":
            s.close()
            sys.exit()
        data,addr = s.recvfrom(4096)
        print(data.decode('utf-8'))
        if(data.decode('utf-8')!="file exists!"):
            s.close()
            sys.exit()
        f = open(a1[1],"wb")

        data,addr = s.recvfrom(4096)
        num =int (data.decode('utf-8'))
        print(str(num)+" times recieve")

        check =  num
        count = 1
        s.sendto("ready".encode('utf-8'),addr)
        while check!=0:
            data,addr=s.recvfrom(4096)
            f.write(data)
            check-=1
            print("received packet number "+str(count))
            count+=1
        f.close()
        print("file closed")
