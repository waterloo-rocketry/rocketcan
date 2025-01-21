def gen_message_types_h(rocketcan):
    print('// Auto generated file, do not edit directly\n')

    print('#ifndef _CANLIB_MESSAGE_TYPES_H\n#define _CANLIB_MESSAGE_TYPES_H\n')

    print('enum MSG_TYPE_ID {')
    for msg in rocketcan['messages']:
        print("    MSG_" + msg['name'].data + " = " + hex(msg['id'].data) + ',')
    print('}\n')

    print('enum BOARD_TYPE_ID {')
    for board in rocketcan['boards']:
        print('    BOARD_TYPE_ID_' + board['name'].data + ' = ' + hex(board['id'].data) + ',')
    print('}\n')

    for board in rocketcan['boards']:
        if "inst" in board:
            inst_id = 1
            print('enum BOARD_INST_ID_' + board['name'].data + ' {')
            for inst in board['inst']:
                print('    BOARD_INST_ID_' + board['name'].data + '_' + inst['name'].data + ' = ' + hex(inst_id) + ',')
                inst_id += 1
            print('}\n')

    for enum in rocketcan['enums']:
        first = True
        print('enum ' + enum['name'].data + ' {')
        for val in enum['value']:
            if(first):
                print('   ' + val['name'].data + ' = 0,')
            else:
                print('   ' + val['name'].data + ',')
                first = False
        print('};\n')

    print('#endif')
