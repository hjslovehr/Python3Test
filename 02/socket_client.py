import socket
import threading

def client_start():
    ip = '127.0.0.1'
    port = 6000

    # 创建 socket 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接服务端
    s.connect((ip, port))
    
    # 打印服务端接收的数据
    print(s.recv(2048).decode())

    # 启用新线程接收数据
    t = threading.Thread(target=receive, args=(s,))
    t.start()

    while True:
        data = input('Please input something: ')
        s.send(data.encode())
        if data == 'exit':
            break
    s.close()
    pass


def receive(sock):
    while True:
        data = sock.recv(2048)
        print('Receive server data: {}'.format(data.decode()))
    pass


if __name__ == "__main__":
    client_start()


