message_types_py_header = """# Auto generated file, do not edit directly

msg_prio = {
    'HIGHEST': 0x0,
    'HIGH':    0x1,
    'MEDIUM':  0x2,
    'LOW':     0x3
}
"""

message_type_py_board_inst_header = """board_inst_id = {
    'ANY':         0x00,
    'GENERIC':     0x01,"""

def gen_message_types_py(rocketcan):
    print(message_types_py_header)
    print('msg_type = {')
    for msg in rocketcan['messages']:
        print('    \'' + msg['name'].data + '\':' + ' ' * (21 - len(msg['name'].data)) + '0x' + '{:03X}'.format(msg['id'].data) + ',')
    print('}\n')

    print('board_type_id = {')
    for board in rocketcan['boards']:
        print('    \'' + board['name'].data + '\':' + ' ' * (21 - len(board['name'].data)) + '0x' + '{:02X}'.format(board['id'].data) + ',')
    print('}\n')

    print(message_type_py_board_inst_header)
    inst_id = 2
    for board in rocketcan['boards']:
        if "inst" in board:
            for inst in board['inst']:
                print('    \'' + inst['name'].data + '\':' + ' ' * (12 - len(inst['name'].data)) + '0x' + '{:02X}'.format(inst_id) + ',')
                inst_id += 1
    print('}\n')
    
    for enum in rocketcan['enums']:
        print(enum['name'].data + ' = {')
        enum_val_count = 0
        for val in enum['value']:
            val_real_name = enum['prefix'].data + '_' + val['name'].data
            if 'value' in val:
                enum_val_count = val['value'].data
            print('    \'' + val_real_name + '\':' + ' ' * (30 - len(val_real_name)) + '0x' + '{:02X}'.format(enum_val_count) + ',')
            enum_val_count += 1
        print('}\n')
