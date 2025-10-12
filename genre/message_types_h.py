message_types_h_header = """// Auto generated file, do not edit directly

#ifndef CANLIB_MESSAGE_TYPES_H
#define CANLIB_MESSAGE_TYPES_H

// Message Priority
typedef enum {
\tPRIO_HIGHEST = 0x0,
\tPRIO_HIGH = 0x1,
\tPRIO_MEDIUM = 0x2,
\tPRIO_LOW = 0x3
} can_msg_prio_t;
"""

message_types_h_board_inst_generic = """// Board Instance IDs
typedef enum {
\tBOARD_INST_ID_ANY = 0x00,
\tBOARD_INST_ID_GROUND = 0x01,
\tBOARD_INST_ID_ROCKET = 0x02,
\tBOARD_INST_ID_PAYLOAD = 0x03
} can_board_inst_id_t;
"""

def gen_message_types_h(rocketcan):
    print(message_types_h_header)

    message_id_max = 0
    print('// Message Types')
    print('typedef enum {')
    for msg in rocketcan['messages']:
        print('\tMSG_' + msg['name'].data + ' = 0x' + '{:03X}'.format(msg['id'].data) + ',')
        if(msg['id'].data > message_id_max):
            message_id_max = msg['id'].data
    print('\tMSG_ID_ENUM_MAX = 0x' + '{:03X}'.format(message_id_max + 1))
    print('} can_msg_type_t;\n')

    board_type_id_max = 0
    print('// Board Type IDs')
    print('typedef enum {')
    for board in rocketcan['boards']:
        print('\tBOARD_TYPE_ID_' + board['name'].data + ' = 0x' + '{:02X}'.format(board['id'].data) + ',')
        if(board['id'].data > board_type_id_max):
            board_type_id_max = board['id'].data
    print('\tBOARD_TYPE_ID_ENUM_MAX = 0x' + '{:02X}'.format(board_type_id_max + 1))
    print('} can_board_type_id_t;\n')

    print(message_types_h_board_inst_generic)

    inst_id = 4
    for board in rocketcan['boards']:
        if 'inst' in board:
            print('typedef enum {')
            for inst in board['inst']:
                print('\tBOARD_INST_ID_' + board['name'].data + '_' + inst['name'].data + ' = 0x' + '{:02X}'.format(inst_id) + ',')
                inst_id += 1
            print('\tBOARD_INST_ID_' + board['name'].data + '_ENUM_MAX = 0x' + '{:02X}'.format(inst_id))
            print('} can_board_inst_id_' + board['name'].data.lower() + '_t;\n')

    for enum in rocketcan['enums']:
        index = 0
        pure_index = True
        print('typedef enum {')
        for val in enum['value']:
            if 'value' in val:
                print('\t' + enum['prefix'].data + '_' + val['name'].data + ' = 0x' + '{:02X}'.format(val['value'].data) + ',')
                pure_index = False
            else:
                print('\t' + enum['prefix'].data + '_' + val['name'].data + ' = 0x' + '{:02X}'.format(index) + ',')
                index += 1
        if(pure_index):
            print('\t' + enum['prefix'].data + '_ENUM_MAX = 0x' + '{:02X}'.format(index))
        print('} can_' + enum['name'].data + '_t;\n')

    for bitfields in rocketcan['bitfields']:
        index = 0
        print('typedef enum {')
        for bit in bitfields['bits']:
            print('\t' + bitfields['prefix'].data + '_' + bit['name'].data + '_OFFSET = 0x' + '{:02X}'.format(index) + ',')
            index += 1
        print('\t' + bitfields['prefix'].data + '_' + bitfields['name'].data.upper() + '_OFFSET_MAX = 0x' + '{:02X}'.format(index))
        print('} can_' + bitfields['name'].data + '_offset_t;\n')
            
    print('#endif')
