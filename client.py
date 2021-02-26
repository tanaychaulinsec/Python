import socket
def client():
    host='localhost'
    port=23456
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.connect((host,port))
    while 1:
        data=raw_input(">>>")
        if not data: break
        s.send(data)
        data=s.recv(1024)
        if not data: break
        print(data)
    s.close()
client()