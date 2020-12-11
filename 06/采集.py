import socket
import threading
import json

RECEIVE_MAX_SIZE = 1024 * 1024 * 10

def server_start():
    server_ip = input('请输入IP：')
    server_port = int(input('请输入端口：'))

    # 创建 Socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定监听地址和端口
    server.bind((server_ip, server_port))

    # 开始监听端口
    server.listen(1000)

    print('Server start [{}:{}]'.format(server_ip, server_port))

    while True:
        try:
            print('Wait a client connetion...')
            # 接收一个新的连接
            sock, addr  = server.accept()
            t = threading.Thread(target=receive, args=(sock, addr))
            t.start()
        except:
            break
    pass


def receive(sock, addr):
    print("Accept new connection from %s:%s" % addr)
    
    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_RCVBUF,
        RECEIVE_MAX_SIZE
    )

    while True:
        try:
            data = sock.recv(RECEIVE_MAX_SIZE)
            if 0 == len(data):
                break
            data_process(data.decode())
        except Exception as ex:
            print(ex)
            break
    
    sock.close()
    print("Connection from %s:%s is closed" % addr)
    pass


def data_process(data:str):
    http = http_analysis(data)
    if None == http:
        return
    
    # 保存接收内容
    with open('receive_data.txt', mode='a', encoding='utf-8') as target:
        target.write(data + '\r\n') # windows 换行符是 \r\n, 类 Unix 平台时 \n

    if '/LAPI/V1.0/System/Event/Notification/PersonVerification' != http['Head']['Url']:
        print('不是采集数据，自动丢弃')
        return
    
    json_object = json.loads(http['Body'])

    faceInfo = json_object['FaceInfoList'][0]
    cardInfo = json_object['CardInfoList'][0]
    
    person = {}
    person['Name'] = cardInfo['Name']
    person['Gender'] = cardInfo['Gender']
    person['Birthday'] = cardInfo['Birthday']
    person['IdentityNo'] = cardInfo['IdentityNo']
    person['ResidentialAddress'] = cardInfo['ResidentialAddress']
    person['IDImage'] = cardInfo['IDImage']['Data']
    person['FaceImage'] = faceInfo['FaceImage']['Data']

    print(json.dumps(person, ensure_ascii=False, indent=4))

    with open('result.txt', mode='a', encoding='utf-8') as target:
        target.write(json.dumps(person, ensure_ascii=False, indent=4))
    
    pass


def http_analysis(data:str):
    try:
        http_response = {}

        '''HTTP 协议规定 heads 和 body 之间有个空号'''
        white_line_size = len('\n\n')
        whitespace_line_pose = data.find('\n\n')
        if -1 == whitespace_line_pose:
            white_line_size = len('\r\n\r\n')
            whitespace_line_pose = data.find('\r\n\r\n')
        
        if -1 == whitespace_line_pose:
            print('数据不满足 http 协议')
            return None
        
        head_str = data[0:whitespace_line_pose]
        heads = head_str.split('\n')

        heads_dic = {}
        first_line = heads[0].split(' ')
        heads_dic['Method'] = first_line[0]
        heads_dic['Url'] = first_line[1]
        heads_dic['Verson'] = first_line[2]

        for i in range(1, len(heads)):
            temp = heads[i].split(':')
            heads_dic[temp[0]] = temp[1]
        
        http_response['Head'] = heads_dic

        body_start_pos = whitespace_line_pose + white_line_size
        body_end_pos = whitespace_line_pose + white_line_size + int(heads_dic['Content-Length']) - 1
        body_str = data[body_start_pos:body_end_pos]

        http_response['Body'] = body_str

        return http_response

    except Exception as ex:
        print(ex)
        return None


if __name__ == "__main__":
    server_start()
    pass


