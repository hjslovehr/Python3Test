import os

def test():
    while True:
        file_path = input('请输入文件全路径：')
        if not os.path.exists(file_path):
            print(f'{file_path} 不存在')
            continue
        
        file_content = ''
        with open(file_path, mode='r', encoding='utf-8') as f:
            file_content = f.read()
        
        print(file_content)

        http = http_analysis(file_content)


        head = http['Head']
        body = http['Body']

        print('Method', ':', head['Method'])
        print('Url', ':', head['Url'])
        print('Body', ':', body)
    pass


def http_analysis(data:str):
    http_response = {}

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


if __name__ == "__main__":
    test()
    pass


