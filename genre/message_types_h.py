message_types_h_header = """// Auto generated file, do not edit directly

#ifndef _CANLIB_MESSAGE_TYPES_H
#define _CANLIB_MESSAGE_TYPES_H

// Message Priority
typedef enum {
    PRIO_HIGHEST = 0x0,
    PRIO_HIGH = 0x1,
    PRIO_MEDIUM = 0x2,
    PRIO_LOW = 0x3,
} can_msg_prio_t;
"""

message_types_h_board_inst_generic = """// Board Instance IDs
typedef enum {
    BOARD_INST_ID_ANY = 0x00,
    BOARD_INST_ID_GENERIC = 0x01,
} can_board_inst_id_t;
"""

def gen_message_types_h(rocketcan):
    print(message_types_h_header)

    print('// Message Types')
    print('typedef enum {')
    for msg in rocketcan['messages']:
        print("    MSG_" + msg['name'].data + ' = 0x' + '{:03X}'.format(msg['id'].data) + ',')
    print('} can_msg_type_t;\n')

    print('// Board Type IDs')
    print('typedef enum {')
    for board in rocketcan['boards']:
        print('    BOARD_TYPE_ID_' + board['name'].data + ' = 0x' + '{:02X}'.format(board['id'].data) + ',')
    print('} can_board_type_id_t;\n')

    print(message_types_h_board_inst_generic)

    inst_id = 2
    for board in rocketcan['boards']:
        if "inst" in board:
            print('typedef enum {')
            for inst in board['inst']:
                print('    BOARD_INST_ID_' + board['name'].data + '_' + inst['name'].data + ' = 0x' + '{:02X}'.format(inst_id) + ',')
                inst_id += 1
            print('} can_board_inst_id_' + board['name'].data.lower() + '_t;\n')

    for enum in rocketcan['enums']:
        first = True
        print('typedef enum {')
        for val in enum['value']:
            if 'value' in val:
                print('    ' + enum['prefix'].data + '_' + val['name'].data + ' = 0x' + '{:02X}'.format(val['value'].data) + ',')
            else:
                if(first):
                    print('    ' + enum['prefix'].data + '_' + val['name'].data + ' = 0,')
                else:
                    print('    ' + enum['prefix'].data + '_' + val['name'].data + ',')
            first = False
        print('} can_' + enum['name'].data + '_t;\n')

    print('#endif')
