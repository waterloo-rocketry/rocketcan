messages_types_ts_header = """// Auto generated file, do not edit directly

import { z } from 'zod'

// ============================================================
// Message Priority
// ============================================================

export const msg_prio = {
    HIGHEST: 0,
    HIGH: 1,
    MEDIUM: 2,
    LOW: 3,
} as const

export const msg_prio_schema = z.nativeEnum(msg_prio)
export type msg_prio = z.infer<typeof msg_prio_schema>"""

message_type_ts_board_inst_header = """// ============================================================
// Board Instance ID
// ============================================================

export const board_inst_id = {
    ANY: 0x00,
    GROUND: 0x01,
    ROCKET: 0x02,"""

def convert_to_title_case(snake_str):
    components = snake_str.split('_')
    return ' '.join(x.title() for x in components[:])

def gen_message_types_ts(rocketcan):
    print(messages_types_ts_header)

    print('\n// ============================================================\n// Message Type\n// ============================================================\n')
    print('export const msg_type = {')
    for msg in rocketcan['messages']:
        print('    ' + msg['name'].data + ': 0x' + '{:02X}'.format(msg['id'].data) + ',')
    print('} as const\n')
    print('export const msg_type_schema = z.nativeEnum(msg_type)')
    print('export type msg_type = z.infer<typeof msg_type_schema>\n')

    print('// ============================================================\n// Board Type ID\n// ============================================================\n')
    print('export const board_type_id = {')
    for board in rocketcan['boards']:
        print('    ' + board['name'].data + ': 0x' + '{:02X}'.format(board['id'].data) + ',')
    print('} as const\n')
    print('export const board_type_id_schema = z.nativeEnum(board_type_id)')
    print('export type board_type_id = z.infer<typeof board_type_id_schema>\n')

    print(message_type_ts_board_inst_header)
    inst_id = 3
    for board in rocketcan['boards']:
        if "inst" in board:
            for inst in board['inst']:
                print('    ' + inst['name'].data + ': 0x' + '{:02X}'.format(inst_id) + ',')
                inst_id += 1
    print('} as const\n')
    print('export const board_inst_id_schema = z.nativeEnum(board_inst_id)')
    print('export type board_inst_id = z.infer<typeof board_inst_id_schema>\n')

    for enum in rocketcan['enums']: # start of numbering errors
        print('// ============================================================\n// ' + convert_to_title_case(enum['name'].data) + '\n// ============================================================\n')
        print('export const ' + enum['name'].data + ' = {')
        enum_val_count = 0
        for val in enum['value']:
            val_real_name = enum['prefix'].data + '_' + val['name'].data
            if 'value' in val:
                enum_val_count = val['value'].data
            print('    ' + val_real_name + ': 0x' + '{:02X}'.format(enum_val_count) + ',')
            enum_val_count += 1
        print('} as const\n')
        print('export const ' + enum['name'].data + '_schema = z.nativeEnum(' + enum['name'].data + ')')
        print('export type ' + enum['name'].data + ' = z.infer<typeof ' + enum['name'].data + '_schema>\n')

    for bitfield in rocketcan['bitfields']:
        print('// ============================================================\n// ' + convert_to_title_case(bitfield['name'].data) + ' Offset (bitfield positions)\n// ============================================================\n')
        print('export const ' + bitfield['name'].data + '_offset = {')
        bit_count = 0
        for bit in bitfield['bits']:
            bit_real_name = bitfield['prefix'].data + '_' + bit['name'].data
            print('    ' + bit_real_name + ': 0x' + '{:02X}'.format(bit_count) + ',')
            bit_count += 1
        print('} as const\n')
        print('export const ' + bitfield['name'].data + '_offset_schema = z.nativeEnum(' + bitfield['name'].data + '_offset)')
        print('export type ' + bitfield['name'].data + '_offset = z.infer<typeof ' + bitfield['name'].data + '_offset_schema>\n')