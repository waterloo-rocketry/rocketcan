def gen_message_types_py(rocketcan):
    print('msg_type = {')
    for msg in rocketcan['messages']:
        print('    \'' + msg['name'].data + '\':' + hex(msg['id'].data) + ',')
    print('}')

    print('board_id = {')
    for board in rocketcan['boards']:
        print('    \'' + board['name'].data + '\':' + hex(board['id'].data) + ',')
    print('}')

    for enum in rocketcan['enums']:
        print(enum['name'].data + ' = {')
        enum_val_count = 0
        for val in enum['value']:
            print('    \'' + val['name'].data + '\':' + hex(enum_val_count) + ',')
            enum_val_count += 1
        print('}')
