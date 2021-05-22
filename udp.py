import socket

ip='0.0.0.0'
port = 8001

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((ip,port))

print("udp server started")
while True:
    data,addr = sock.recvfrom(1024)
    print("received message",data.decode('utf-8'), "from",addr)
    currentTime = " " + time.ctime(time.time())+"\r\n"
    data = data+currentTime.encode('ascii')
    sock.sendto(data,addr)
print("asd??????")
