import json

# 字典保存结果
result = {}

def json_analysis():
    '''Json analysis'''

    json_str = ''
    with open(r'.\tb(2020-02-17).json', encoding='utf-8') as f:
        json_str = f.read()
    
    # print(json_str)
    data = json.loads(json_str)

    print('\n')

    # 基本参数
    # print(30 * '=',  "基本配置", 30 * '=')
    base_cfg(data)
    
    # MQTT 配置
    # print(30 * '=',  "MQTT配置", 30 * '=')
    mqtt_cfg(data['mqtt'])

    # RS485 配置
    # print(30 * '=',  "RS485配置", 30 * '=')
    rs485_cfg(data)

    # Mudbus 配置
    # print(30 * '=',  "Mudbus配置", 30 * '=')
    mudbus_cfg(data['modbusReadPara'])
    
    with open('.\\json_result.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(result, indent=4, ensure_ascii=False))

    print('\n')
    pass


def base_cfg(data:dict):
    '''基本参数'''
    # print('参数版本: ', data['param_ver'])
    # print('每分钟最大串口流量(Byte): ', data['flow'])
    # print('串口分帧超时(ms): ', data['uartReadTime'])
    # print('网络分帧超时(ms): ', data['netReadTime'])
    # print('是否启用自动更新: ', data['fota'])
    # print('配置密码: ', data['password'])
    # preset = data['preset']
    # print('远程更新参数和固件')
    # print('\t白名单号: ', preset['number'])
    # print('\t振铃延时: ', preset['delay'])
    # print('\t短信字段: ', preset['smsword'])
    base_data = {}
    result['base_cfg'] = base_data
    base_data['param_ver'] = data['param_ver']
    base_data['flow'] = data['flow']
    base_data['uartReadTime'] = data['uartReadTime']
    base_data['netReadTime'] = data['netReadTime']
    base_data['fota'] = data['fota']
    base_data['password'] = data['password']
    base_data['preset'] = data['preset']


def mqtt_cfg(data:dict):
    '''MQTT 配置'''
    mqtt_info = ['心跳包间隔', '地址/域名', '服务端口号', \
                '登陆账号', '登陆密码', '保存会话标志位', \
                'QOS级别', 'Publish参数retain', 'Transport', \
                '遗嘱']
    
    mqtt_data = {}
    result['mqtt_cfg'] = mqtt_data

    it = iter(data)
    for info in mqtt_info:
        value = next(it)
        # print(info, ': ', value)
        mqtt_data[info] = value
    
    pass


def rs485_cfg(data:dict):
    '''RS485 配置'''

    serialport_info = ['波特率', '数据位', '校验位', '停止位']

    modbuspollreport = ['Delay between Poll(ms)', 'Response Timeout(ms)', 'Polling Interval(s)', \
                        'Report Interval(s)', 'Change Report Mode']

    serialport_data = {}
    result['serialport_cfg'] = serialport_data

    serialport_cfg = data['uconf']
    it = iter(serialport_cfg)

    for info in serialport_info:
        value = next(it)
        # print(info, ': ', next(it))
        serialport_data[info] = value
    
    modbus_poll_report = data['modbusPollReport']
    # print('modbusPollReport: ')
    # for item in modbus_poll_report:
        # print('\t', item)
    
    mpr = {}
    result['modbusPollReport'] = mpr
    itr = iter(modbus_poll_report)
    for item in modbuspollreport:
        mpr[item] = next(itr)

    pass


def mudbus_cfg(data:list):
    '''Mudbus 配置'''

    variable_info = ['变量的功能码', '变量的起始地址', '变量的名称', \
                    '变量的数据类型', '变量的采样低值', '变量的采样高值', \
                    '变量的工程低值', '变量的工程高值', '变量的阈值', \
                    '变量的低报值', '变量的高报值']
    
    mudbus_data = {}
    result['mudbus_cfg'] = mudbus_data

    device_count = data[0]
    # print('设备数量', ' : ', device_count)
    mudbus_data['device_count'] = device_count

    data.pop(0)
    # print(mudbus_read_para)

    device_info = []
    mudbus_data['devices'] = device_info

    it = iter(data)
    device_index = 0
    while True:
        device_index += 1

        value = next(it, None)
        if None == value:
            break
        
        dev = {}
        device_info.append(dev)
        dev['index'] = device_index

        # print()
        # print(30 * '*', f' 设备：【{device_index}】 ', 30 * '*')
        # print('设备名称: ', value)
        dev['name'] = value

        value = next(it, None)
        # print('设备地址: ', value)
        dev['address'] = value

        value = next(it, None)
        # print('变量个数: ', value)
        dev['variable_count'] = value

        variables = []
        dev['variables'] = variables
        for i in range(1, value + 1):
            # print(30 * '-', '变量：[{}]'.format(i), 30 * '-')
            var = {}
            variables.append(var)
            var['index'] = i
            for info in variable_info:
                # print(info, ': ', next(it))
                var[info] = next(it)

    pass


if __name__ == "__main__":
    json_analysis()
    print(json.dumps(result, indent=4, ensure_ascii=False))

