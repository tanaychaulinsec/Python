import socket
def server():
    host='localhost'
    port=23456
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(5)
    while 1:
        print ("waiting for connection")
        conn,addr=s.accept()
        print("connected from",addr)
        print(conn)
        while 1:
            data=conn.recv(1024)
            if not data: break
            data1=raw_input(">>>")
            if not data1: break
            conn.send(data1)
        conn.close()
    conn.close()
server()