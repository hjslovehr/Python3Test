import socket
import threading

def server_start():
    ip = '127.0.0.1'
    port = 6000

    # 创建 Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定监听地址和端口
    s.bind((ip, port))

    # 开始监听端口
    s.listen(100)

    print('Server start [{}:{}]'.format(ip, port))
    while True:
        print('Wait a client connetion...')
        # 接收一个新的连接
        sock, addr  = s.accept()
        t = threading.Thread(target=receive, args=(sock, addr))
        t.start()
    pass


def receive(sock, addr):
    print("Accept new connection from %s:%s" % addr)

    # 向客户端发送欢迎消息
    sock.send(b"Server: Welcome!\n")

    while True:
        data = sock.recv(2048)
        
        print('Receive: ', data.decode())

        # 如果客户端发送 exit 过来请求退出，结束循环
        if data == b"exit":
            sock.send(b"Server: Good bye!\n")
            break

        sock.send(b"Server: Hello %s !" % data)
    
    sock.close()
    print("Connection from %s:%s is closed" % addr)
    pass


if __name__ == "__main__":
    server_start()


