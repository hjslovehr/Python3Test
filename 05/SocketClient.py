import socket
import threading
import os

def client_start(ip:str, port:str):

    port = int(port)

    # 创建 socket 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # 连接服务端
        s.connect((ip, port))

        # 启用新线程接收数据
        receiveThread = threading.Thread(target=receive, args=(s,))
        receiveThread.start()

        try:
            while True:
                cmd = input('请选择要发送命令（1 字符串；2 文件；“exit” 退出）: ')

                if cmd == 'exit':
                    break

                if '1' == cmd:
                    s.send(input('输入发送内容: ').encode())
                elif '2' == cmd:
                    file_name = input('请输入文件绝对路径: ')
                    if os.path.exists(file_name):
                        file_content = ''
                        with open(file=file_name, mode='r',encoding='utf-8') as f:
                            file_content = f.read()
                        s.send(file_content.encode())
                    else:
                        print(f'{file_name} 文件不存在！')
                else:
                    print('输入命令不正确，请重新选择。')
            
        except Exception as ex:
            print(ex)
            pass
            
        s.close()
        pass
    except Exception as ex:
        print(ex)


def receive(sock):
    while True:
        try:
            data = sock.recv(2048)
            if 0 == len(data):
                return
            print('Receive server data: {}'.format(data.decode()))
        except Exception:
            break
    pass


if __name__ == "__main__":
    client_start(input('请输入服务端IP: '), input('请输入端口: '))

    print()
    print('==================== Press "Enter" key to exit... ====================')
    input()

